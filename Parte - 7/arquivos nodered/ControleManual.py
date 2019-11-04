import time
from datetime import datetime, timedelta

from BancoDados import BancoDados
from Log import Log
from Valvula import Valvula


class ControleManual():


    def __init__(self):
        self.classLog = Log('historico.json')
        self.classdadosValvula = BancoDados('valvulas.json')
        self.classConfiguracoes = BancoDados('configuracoes.json')
        self.valvula = Valvula()
        self.logCadastrado = ''


    def ligar(self, valvulaLigar):


        valvulas = self.classdadosValvula.dadosGravados()

        horaAtual = datetime.now()
        horaAtual = horaAtual.strftime('%H:%M')
        
        for index, valvula in enumerate(valvulas):
            valvulaCadastradaDic = self.classdadosValvula.converterDadoDic(valvula)

            if int(valvulaCadastradaDic['valvula']) == int(valvulaLigar) and int(valvulaCadastradaDic['status']) == 0:
                
                self.valvula.ligar(int(valvulaLigar))

                valvula = {}
                valvula['id'] = valvulaCadastradaDic['id']
                valvula['valvula'] = valvulaCadastradaDic['valvula']
                valvula['status'] = 1
                valvula['secao'] = valvulaCadastradaDic['secao']
                valvula['desligadoManualmente'] = 0

                valvula = self.classdadosValvula.converterDadoJson(valvula)

                configuracoes = self.classConfiguracoes.dadosGravados()
                configuracoes = self.classConfiguracoes.converterDadoDic(configuracoes[0])
    
                tempoDesligamento = int(configuracoes['tempoPadrao'])


                horaDesligar = self.calculaHoraDesligar(horaAtual, tempoDesligamento)
                
                
                self.classdadosValvula.atualizar(valvula)
                valvula = self.classdadosValvula.converterDadoDic(valvula)
                self.logCadastrado = self.classLog.registrarLog(valvulaCadastradaDic['secao'], horaAtual, horaDesligar, "Manual")
       

                
                valvulaLigada = True
                while valvulaLigada:
                    time.sleep(2)

                    valvulas = self.classdadosValvula.dadosGravados()

                    for index, valvula in enumerate(valvulas):
                        valvulaCadastradaDic = self.classdadosValvula.converterDadoDic(valvula)

                        if int(valvulaCadastradaDic['valvula']) == int(valvulaLigar) and int(valvulaCadastradaDic['status']) == 0:
                            
                            valvulaLigada = False
                            break
                    
                    horaAtual = datetime.now()
                    horaAtual = horaAtual.strftime('%H:%M')
                    

                    if horaAtual >= horaDesligar:
                        self.valvula.desligar(int(valvulaLigar))

                        valvula['status'] = 0
                        valvula = self.classdadosValvula.converterDadoJson(valvula)
                        self.classdadosValvula.atualizar(valvula)
                        break

    def desligar(self, valvulaDesligar):
        valvulas = self.classdadosValvula.dadosGravados()

        horaAtual = datetime.now()
        horaAtual = horaAtual.strftime('%H:%M')

        for index, valvula in enumerate(valvulas):
            valvulaCadastradaDic = self.classdadosValvula.converterDadoDic(valvula)

            if int(valvulaCadastradaDic['valvula']) == int(valvulaDesligar) and int(valvulaCadastradaDic['status']) == 1:
                
                self.valvula.desligar(int(valvulaDesligar))
                
                valvula = {}
                valvula['id'] = valvulaCadastradaDic['id']
                valvula['valvula'] = valvulaCadastradaDic['valvula']
                valvula['status'] = 0
                valvula['secao'] = valvulaCadastradaDic['secao']
                valvula['desligadoManualmente'] = 1

                valvula = self.classdadosValvula.converterDadoJson(valvula)

                
                self.classdadosValvula.atualizar(valvula)




    def calculaHoraDesligar(self, horarioLigar, minutosLigado):
        hora, minutos = horarioLigar.split(":")
        horarioDesligar = datetime(2000, 1, 1, int(hora), int(minutos), 0, 0)

        horarioDesligar = horarioDesligar + timedelta(minutes=minutosLigado)
        horarioDesligar = horarioDesligar.strftime('%H:%M')

        return horarioDesligar
