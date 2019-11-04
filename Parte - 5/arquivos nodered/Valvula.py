from Horario import Horario
import RPi.GPIO as GPIO    
from datetime import datetime, timedelta
import time







class Valvula:

    def __init__(self):
        self.classDadosValvula = Horario('valvulas.json')
        self.config()

    def config(self):
        vermelho = 11
        verde = 13

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(vermelho,GPIO.OUT)
        GPIO.setup(verde, GPIO.OUT)


    def ligar(self, valvulaLigar, index):

        valvulas = self.classDadosValvula.horariosGravados()

        horaAtual = datetime.now()
        horaAtual = horaAtual.strftime('%H:%M')
        
        for index, valvula in enumerate(valvulas):
            v = self.classDadosValvula.converterHorarioDic(valvula)

            if int(v['valvula']) == int(valvulaLigar) and int(v['status']) == 0:
                print("Ligado")
                

                valvula = {}
                valvula['id'] = v['id']
                valvula['valvula'] = v['valvula']
                valvula['status'] = 1
                valvula['secao'] = v['secao']

                valvula = self.classDadosValvula.converterHorarioJson(valvula)
                self.classDadosValvula.atualizar(valvula)
        
                GPIO.output(int(valvulaLigar), 1)

    def desligar(self, valvulaLigar, index):

        valvulas = self.classDadosValvula.horariosGravados()


        for index, valvula in enumerate(valvulas):
            v = self.classDadosValvula.converterHorarioDic(valvula)

            if int(v['valvula']) == int(valvulaLigar) and int(v['status']) == 1:


                valvula = {}
                valvula['id'] = v['id']
                valvula['valvula'] = v['valvula']
                valvula['status'] = 0
                valvula['secao'] = v['secao']

                valvula = self.classDadosValvula.converterHorarioJson(valvula)
                self.classDadosValvula.atualizar(valvula)

                GPIO.output(int(valvulaLigar), 0)
                GPIO.cleanup()
                self.config()
