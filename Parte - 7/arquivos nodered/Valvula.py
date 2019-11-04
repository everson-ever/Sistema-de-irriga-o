import time
from datetime import datetime, timedelta

import RPi.GPIO as GPIO
from BancoDados import BancoDados


class Valvula:

    def __init__(self):
        self.bomba = 15
        self.classDadosValvula = BancoDados('valvulas.json')
        self.config()
        

    def config(self):
        vermelho = 11
        verde = 13

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(vermelho,GPIO.OUT)
        GPIO.setup(verde, GPIO.OUT)
        GPIO.setup(self.bomba, GPIO.OUT)


    def ligar(self, valvulaLigar):

        valvulas = self.classDadosValvula.dadosGravados()

        horaAtual = datetime.now()
        horaAtual = horaAtual.strftime('%H:%M')
        
        for index, valvula in enumerate(valvulas):
            v = self.classDadosValvula.converterDadoDic(valvula)

            if int(v['valvula']) == int(valvulaLigar) and int(v['status']) == 0:

                valvula = {}
                valvula['id'] = v['id']
                valvula['valvula'] = v['valvula']
                valvula['status'] = 1
                valvula['secao'] = v['secao']

                valvula = self.classDadosValvula.converterDadoJson(valvula)
                self.classDadosValvula.atualizar(valvula)
        
                GPIO.output(int(valvulaLigar), 1)
                GPIO.output(self.bomba, 1)

    def desligar(self, valvulaLigar):

        valvulas = self.classDadosValvula.dadosGravados()


        for index, valvula in enumerate(valvulas):
            v = self.classDadosValvula.converterDadoDic(valvula)

            if int(v['valvula']) == int(valvulaLigar) and int(v['status']) == 1:


                valvula = {}
                valvula['id'] = v['id']
                valvula['valvula'] = v['valvula']
                valvula['status'] = 0
                valvula['secao'] = v['secao']

                valvula = self.classDadosValvula.converterDadoJson(valvula)
                self.classDadosValvula.atualizar(valvula)

                GPIO.output(self.bomba, 0)
                GPIO.output(int(valvulaLigar), 0)
                GPIO.cleanup()
                self.config()
