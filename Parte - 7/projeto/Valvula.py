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

        for index, valvula in enumerate(valvulas):
            valvula = self.classDadosValvula.converterDadoDic(valvula)

            if int(valvula['valvula']) == int(valvulaLigar) and int(valvula['status']) == 0:

                valvula['status'] = 1

                valvula = self.classDadosValvula.converterDadoJson(valvula)
                self.classDadosValvula.atualizar(valvula)
        
                GPIO.output(int(valvulaLigar), 1)
                GPIO.output(self.bomba, 1)
                break

    def desligar(self, valvulaDesligar):

        valvulas = self.classDadosValvula.dadosGravados()


        for index, valvula in enumerate(valvulas):
            valvula = self.classDadosValvula.converterDadoDic(valvula)

            if int(valvula['valvula']) == int(valvulaDesligar) and int(valvula['status']) == 1:

                valvula['status'] = 0

                valvula = self.classDadosValvula.converterDadoJson(valvula)
                self.classDadosValvula.atualizar(valvula)

                GPIO.output(self.bomba, 0)
                GPIO.output(int(valvulaDesligar), 0)
                GPIO.cleanup()
                self.config()
                break
