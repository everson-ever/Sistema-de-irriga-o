import json
import time
from datetime import datetime, timedelta

from BancoDados import BancoDados
from Log import Log
from Valvula import Valvula


class Irrigacao():

    def __init__(self):
        
        self.classAgendamentos = BancoDados('agendamentos.json')
        self.classLog = Log('historico.json')
        self.ids = []
        self.valvulas = []
        self.horariosLigar = []
        self.horariosDesligar = []
        self.statusHorarios = []
        self.statusAgendamentosAtivados = []
        self.horariosPendentes = []
        self.pendentes = []
        self._formatarHorarios()
        #self._iniciaListaItensPendentes()


    ## Pega os horários gravados
    def _pegarHorarios(self):
        horarios = open("agendamentos.json", 'r')
        return horarios.readlines()


    def _iniciaListaItensPendentes(self):
        horarios = self._pegarHorarios()
        self.horariosPendentes = []
        
        for horario in horarios:
            horario = json.loads(horario)
            dadosHorario = {"id": horario['id'], "pendente": 1}
            self.horariosPendentes.append(dadosHorario)


    def _geraControleHorariosPendentes(self):
        horarios = self._pegarHorarios()
               
        for index, horarioPendente in enumerate(self.horariosPendentes):
            try:

                #if self.horariosPendentes[i] == 0 and self.statusHorarios[i] == 1:
                if not (horarioPendente['id'] in self.ids):
                    del self.horariosPendentes[index]   
   
            except IndexError:
                print()

        for index, horario in enumerate(horarios):
            horario = json.loads(horario)

            try:
                if self.horariosPendentes[index]['pendente'] == 0 and self.statusHorarios[index] == 1:
                    self.horariosPendentes[index]['pendente'] == 0

            except IndexError:
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
        self.statusAgendamentosAtivados = []
        self.valvulas = []
        #self.horariosPendentes = []
        
        horarios = self._pegarHorarios()
        for horario in horarios:
            horario = json.loads(horario)
            self.ids.append(horario['id'])
            self.horariosLigar.append(horario['horario'])
            self.horariosDesligar.append(self.calculaHoraDesligar(horario['horario'], int(horario['tempoLigado'])))
            self.valvulas.append(horario['valvula'])
            self.statusHorarios.append(horario['status'])
            self.statusAgendamentosAtivados.append(horario['ativado'])

        if len(self.horariosPendentes) == 0:
            self._iniciaListaItensPendentes()
        

        if len(self.horariosPendentes) > 0:
            self._geraControleHorariosPendentes()
            
              
    ## Método geral que iniciará o sitema
    def iniciar(self):
        classValvula = Valvula()
        
        while True:
            self._formatarHorarios()
            
            horaAtual = datetime.now()
            horaAtual = horaAtual.strftime('%H:%M')


            for index, horario in enumerate(self.horariosLigar):
                valvulaAtual = int(self.valvulas[index])

                # Liga o hoário se estiver na hora de ligar e se estiver desligado
                if horaAtual == horario and self.statusHorarios[index] == 0:
                    # Verifica se o agendamento não foi desativado pelo usuário
                    if int(self.statusAgendamentosAtivados[index]) == 1: 
                        self.classAgendamentos.alterarStatus(index,1)
                        self.horariosPendentes[index]['pendente'] = 0
                        self._formatarHorarios()
                        self.classLog.registrarLog("Secao 1", horaAtual, self.horariosDesligar[index], "Automatico")                        
                        
                        classValvula.ligar(valvulaAtual)


                # Desliga a valvula quando estiver na hora
                if horaAtual >= self.horariosDesligar[index] and self.statusHorarios[index] == 1:
                    self.classAgendamentos.alterarStatus(index,0)
                    self.horariosPendentes[index]['pendente'] = 1
                    
                    classValvula.desligar(valvulaAtual)


                # O sistema retoma a sua execução depois de uma parada inesperada
                if horaAtual >= self.horariosLigar[index] and horaAtual < self.horariosDesligar[index] and int(self.statusHorarios[index]) == 1 and int(self.horariosPendentes[index]['pendente']) == 1:
                    if int(self.statusAgendamentosAtivados[index]) == 1:
                        self.horariosPendentes[index]['pendente'] = 0
                        self.classLog.registrarLog("Secao 1", horaAtual, self.horariosDesligar[index], "Reiniciado")
                        
                        classValvula.ligar(valvulaAtual)
                

                # Sistema inicia execução atrasado
                if horaAtual >= self.horariosLigar[index] and horaAtual < self.horariosDesligar[index] and int(self.statusHorarios[index]) == 0:
                    if int(self.statusAgendamentosAtivados[index]) == 1:
                        self.classAgendamentos.alterarStatus(index, 1)
                        self.horariosPendentes[index]['pendente'] = 0
                        self.classLog.registrarLog("Secao 2", horaAtual, self.horariosDesligar[index], "Automatico: Após o horário marcado")

                        classValvula.ligar(valvulaAtual)


                # OBS: Quando se inicia uma irrigação automática e logo depois desliga-se manualmente,
                # o sistema não volta a ligar naquele agendamento porque ainda estava ligado no modo automático,
                # ou seja, todos os valores das variáveis que controlam a execução ainda permanecem, portanto,
                # ainda tem um tempo de desligamento sendo verificado


                # Novo momento para desligar: Se é hora de desligar
