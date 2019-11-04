from Log import Log
from Valvula import Valvula
from Horario import Horario
from datetime import datetime, timedelta
import time


class ControleManual():


    def __init__(self):
        self.classLog = Log('historico.json')
        self.classdadosValvula = Horario('valvulas.json')
        self.classConfiguracoes = Horario('configuracoes.json')
        self.valvula = Valvula()


    def ligar(self, valvulaLigar):


        valvulas = self.classdadosValvula.horariosGravados()

        horaAtual = datetime.now()
        horaAtual = horaAtual.strftime('%H:%M')
        
        for index, valvula in enumerate(valvulas):
            v = self.classdadosValvula.converterHorarioDic(valvula)

            if int(v['valvula']) == int(valvulaLigar) and int(v['status']) == 0:
                print("Ligado")
                self.valvula.ligar(int(valvulaLigar), int(valvulaLigar))

                valvula = {}
                valvula['id'] = v['id']
                valvula['valvula'] = v['valvula']
                valvula['status'] = 1
                valvula['secao'] = v['secao']
                valvula['desligadoManualmente'] = 0

                valvula = self.classdadosValvula.converterHorarioJson(valvula)

                configuracoes = self.classConfiguracoes.horariosGravados()
                configuracoes = self.classConfiguracoes.converterHorarioDic(configuracoes[0])
    
                tempoDesligamento = int(configuracoes['tempoPadrao'])


                horaDesligar = self.calculaHoraDesligar(horaAtual, tempoDesligamento)
                print(horaDesligar)
                
                self.classdadosValvula.atualizar(valvula)
                valvula = self.classdadosValvula.converterHorarioDic(valvula)
                self.classLog.registrarLog(v['secao'], horaAtual, horaDesligar, "Manual")

                
                valvulaLigada = True
                while valvulaLigada:
                    time.sleep(2)

                    valvulas = self.classdadosValvula.horariosGravados()

                    for index, valvula in enumerate(valvulas):
                        v = self.classdadosValvula.converterHorarioDic(valvula)

                        if int(v['valvula']) == int(valvulaLigar) and int(v['status']) == 0:
                            print("A válvula já foi desligada")
                            valvulaLigada = False
                            break
                    
                    horaAtual = datetime.now()
                    horaAtual = horaAtual.strftime('%H:%M')
                    

                    if horaAtual >= horaDesligar:
                        self.valvula.desligar(int(valvulaLigar), int(valvulaLigar))

                        valvula['status'] = 0
                        valvula = self.classdadosValvula.converterHorarioJson(valvula)
                        self.classdadosValvula.atualizar(valvula)
                        break

    def desligar(self, valvulaDesligar):
        valvulas = self.classdadosValvula.horariosGravados()

        horaAtual = datetime.now()
        horaAtual = horaAtual.strftime('%H:%M')

        for index, valvula in enumerate(valvulas):
            v = self.classdadosValvula.converterHorarioDic(valvula)

            if int(v['valvula']) == int(valvulaDesligar) and int(v['status']) == 1:
                
                self.valvula.desligar(int(valvulaDesligar), int(valvulaDesligar))
                
                valvula = {}
                valvula['id'] = v['id']
                valvula['valvula'] = v['valvula']
                valvula['status'] = 0
                valvula['secao'] = v['secao']
                valvula['desligadoManualmente'] = 1

                valvula = self.classdadosValvula.converterHorarioJson(valvula)

                
                self.classdadosValvula.atualizar(valvula)



                        

    def calculaHoraDesligar(self, horarioLigar, minutosLigado):
        hora, minutos = horarioLigar.split(":")
        horarioDesligar = datetime(2000, 1, 1, int(hora), int(minutos), 0, 0)

        horarioDesligar = horarioDesligar + timedelta(minutes=minutosLigado)
        horarioDesligar = horarioDesligar.strftime('%H:%M')

        return horarioDesligar
                


        


        
