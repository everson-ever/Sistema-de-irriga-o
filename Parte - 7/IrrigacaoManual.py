from Log import Log
from Valvula import Valvula
from Horario import Horario
from datetime import datetime, timedelta
import time


class IrrigacaoManual():


    def __init__(self):
        self.classLog = Log('historico.json')
        self.classdadosValvula = Horario('valvulas.json')
        self.valvula = Valvula()
        #self.classLed = Led()


    def irrigar(self, valvulaLigar):


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

                valvula = self.classdadosValvula.converterHorarioJson(valvula)

                horaDesligar = self.calculaHoraDesligar(horaAtual, 2)
                
                self.classdadosValvula.atualizar(valvula)
                valvula = self.classdadosValvula.converterHorarioDic(valvula)
                self.classLog.registrarLog(v['secao'], horaAtual, horaDesligar, "Manual")

                

                while True:
                    time.sleep(2)
                    
                    horaAtual = datetime.now()
                    horaAtual = horaAtual.strftime('%H:%M')
                    

                    if horaAtual >= horaDesligar:
                        self.valvula.desligar(int(valvulaLigar), int(valvulaLigar))

                        valvula['status'] = 0
                        valvula = self.self.classdadosValvula.converterHorarioJson(valvula)
                        self.classdadosValvula.atualizar(valvula)
                        print("Desligado automáticamente")
                        break




                        

    def calculaHoraDesligar(self, horarioLigar, minutosLigado):
        hora, minutos = horarioLigar.split(":")
        horarioDesligar = datetime(2000, 1, 1, int(hora), int(minutos), 0, 0)

        horarioDesligar = horarioDesligar + timedelta(minutes=minutosLigado)
        horarioDesligar = horarioDesligar.strftime('%H:%M')

        return horarioDesligar
                


        


        
