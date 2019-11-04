from datetime import date, datetime, timedelta
from Horario import Horario
from Log import Log
import time
import json

## O horário no arquivo JSON deve estar neste formato para funcionar corretamente:
## {"id": "1005", "horario": "10:40", "tempoLigado": "40"}

class Irrigacao():

    def __init__(self):
        
        self.classHorario = Horario('horarios.json')
        self.classLog = Log('historico.json')
        self.classValvulas = Horario('valvulas.json')
        self.leds = []
        self.ids = []
        self.horariosLigar = []
        self.horariosDesligar = []
        self.statusHorarios = []
        self.horariosPendentes = []
        self.pendentes = []
        self._formatarHorarios()
        self._iniciaListaItensPendentes()



    ## Pega os horários gravados
    def _pegarHorarios(self):
        horarios = open("horarios.json", 'r')
        return horarios.readlines()

    def _iniciaListaItensPendentes(self):
        horarios = self._pegarHorarios()
        
        for horario in horarios:
            horario = json.loads(horario)
            dadosHorario = {"id": horario['id'], "pendente": 1}
            self.horariosPendentes.append(dadosHorario)



    def _geraControleHorariosPendentes(self):
        horarios = self._pegarHorarios()

        
        for index, horario in enumerate(horarios):
            
            try:
                if not self.horariosPendentes[index]['id'] in self.ids:
                    del self.horariosPendentes[index]
                    #print("Horários pendentes")
                    #print(self.horariosPendentes)
                    #print()
                    #time.sleep(1)
                #else:
                    
                    #print()
                    #print("Pendente vai ser deletado")
                    #print(self.horariosPendentes)
                    #time.sleep(1)
                    
            except IndexError:
                print("Erro")

        for index, horario in enumerate(horarios):
            horario = json.loads(horario)

            try:
                if self.horariosPendentes[index]['pendente'] == 0 and self.statusHorarios[index] == 1:
                    #print(self.horariosPendentes)
                    #time.sleep(2)
                    self.horariosPendentes[index]['pendente'] == 0

            except IndexError:
                #print("Novo horário adicionado")
                #time.sleep(2)
                dadosHorario = {"id": horario['id'], "pendente": 1}
                self.horariosPendentes.append(dadosHorario)

       

    def calculaHoraDesligar(self, horarioLigar, minutosLigado):
        hora, minutos = horarioLigar.split(":")
        horarioDesligar = datetime(2000, 1, 1, int(hora), int(minutos), 0, 0)

        horarioDesligar = horarioDesligar + timedelta(minutes=minutosLigado)
        horarioDesligar = horarioDesligar.strftime('%H:%M')

        return horarioDesligar

    ## Método para pegar o json(horario) e separar horas a ligar e tempos ligado em duas lista
    ## em que a posição de um horário e seu tempo ligado será a mesma
    def _formatarHorarios(self):
        self.ids = []
        self.horariosLigar = []
        self.horariosDesligar = []
        self.statusHorarios = []
        self.leds = []
        
        horarios = self._pegarHorarios()
        for horario in horarios:
            horario = json.loads(horario)
            self.ids.append(horario['id'])
            self.horariosLigar.append(horario['horario'])
            self.horariosDesligar.append(self.calculaHoraDesligar(horario['horario'], int(horario['tempoLigado'])))
            self.statusHorarios.append(horario['status'])
            self.leds.append(horario['led'])
            

        if len(self.horariosPendentes) > 0:
            self._geraControleHorariosPendentes()
            


    
    ## Método geral que iniciará o sitema
    def iniciar(self):
        
        while True:
            self._formatarHorarios()
            
            horaAtual = datetime.now()
            horaAtual = horaAtual.strftime('%H:%M')

            print(self.horariosLigar)
            print(self.horariosDesligar )
            print(self.statusHorarios)
            print(self.horariosPendentes)
            print(self.leds)
            print()
            time.sleep(5)


            for index, horario in enumerate(self.horariosLigar):
                if horaAtual == horario and self.statusHorarios[index] == 0:

                    self.classHorario.alterarStatus(index,1)
                    self.horariosPendentes[index]['pendente'] = 0
                    self._formatarHorarios()

                    self.classLog.registrarLog("Secao 1", horaAtual, self.horariosDesligar[index], "Automatico")
                    #horarioDesligar = self.horariosDesligar[index]
                    #self._ligar(horaAtual, horarioDesligar)
                    print()
                    print("Ligar")
                    print("Index: ", index)
                    print("Horário: ", horario)
                    print("Desliga as: ", self.horariosDesligar[index])
                    print("led: ", self.leds[index])
                    print("Pendente: ", self.horariosPendentes[index]['pendente'])
                    print()
                    

                # Verifica se é hora de desligar
                if horaAtual >= self.horariosDesligar[index] and int(self.statusHorarios[index]) == 1:

                    self.classHorario.alterarStatus(index,0)
                    self.horariosPendentes[index]['pendente'] = 1
                    print()
                    print("Desligar")
                    print("Index: ", index)
                    print("Horário: ", horario)
                    print("Desligou as: ", self.horariosDesligar[index])
                    print("led: ", self.leds[index])
                    print("Pendente: ", self.horariosPendentes[index]['pendente'])
                    print()

                # O sistema retoma a sua execução depois de uma parada inesperada
                if horaAtual >= self.horariosLigar[index] and horaAtual < self.horariosDesligar[index] and int(self.statusHorarios[index]) == 1 and int(self.horariosPendentes[index]['pendente']) == 1:
                    self.horariosPendentes[index]['pendente'] = 0
                    #self._registrarLog("Seção 1", self.statusHorarios[index], self.horariosDesligar[index], "Automático")
                    self.classLog.registrarLog("Secao 1", horaAtual, self.horariosDesligar[index], "Automatico")
                    print("O Index é: ", index)
                    print()
                    print("Sistema Retomado")
                    print("Index: ", index)
                    print("Horário: ", horario)
                    print("Desliga as: ", self.horariosDesligar[index])
                    print("led: ", self.leds[index])
                    print("Pendente: ", self.horariosPendentes[index]['pendente'])
                    print()

                # Sistema inicia execução atrasado
                if horaAtual >= self.horariosLigar[index] and horaAtual < self.horariosDesligar[index] and int(self.statusHorarios[index]) == 0:
                    self.classHorario.alterarStatus(index, 1)
                    self.horariosPendentes[index]['pendente'] = 0
                    self.classLog.registrarLog("Secao 2", horaAtual, self.horariosDesligar[index], "Automatico")
                    print()
                    print("Sistema iniciado com atraso")
                    print("Index: ", index)
                    print("Horário: ", horario)
                    print("Desliga as: ", self.horariosDesligar[index])
                    print("led: ", self.leds[index])
                    print("Pendente: ", self.horariosPendentes[index]['pendente'])
                    print()
                if horaAtual < self.horariosLigar[index] and int(self.statusHorarios[index]) == 1:
                    self.classHorario.alterarStatus(index, 0)
                    self.horariosPendentes[index]['pendente'] = 1

                
                    
           

                        
      
                
            
                

            




