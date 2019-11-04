from datetime import datetime
import time
import json

## Ainda apresenta alguns falhas de lógica
## * O método tempoOcioso() ainda não está calculando com exatidão o tempo a ficar ocioso do último horário
## * A lista temposMortos[] não está funcionando como deveria. Está aumentando o tamanho da lista a cada ciclo.

## O horário no arquivo JSON deve estar neste formato para funcionar corretamente:
## {"id": "1005", "horario": "10:40", "tempoLigado": "40"}

class Irrigar():

    def __init__(self):
        
        self.horariosLigar = []
        self.temposLigado = []
        self.temposMortos = []
        self._formatarHorarios()
        print("Sistema Iniciou")

    ## configurações para ligar o "led" devem ficar neste método
    def _ligar(self, hora, tempoLigado):
        
        print(f"O sistema Iniciou {hora} e vai passar {tempoLigado} m ligado")
        
    ## Configurações para desligar o "led" ativo devem ficar neste métodos
    def _desligar(self, hora, tempoLigado):
        
         print(f"O sistema do horário {hora} desligou e passou {tempoLigado} m ligado")
         print("")


    ## Pega os horários gravados
    def _pegarHorarios(self):
        horarios = open("horarios.json", 'r')
        return horarios.readlines()

    ## Método para pegar o json(horario) e separar horas a ligar e tempos ligado em duas lista
    ## em que a posição de um horário e seu tempo ligado será a mesma
    def _formatarHorarios(self):
        
        horarios = self._pegarHorarios()
        for horario in horarios:
            horario = json.loads(horario)
            self.horariosLigar.append(horario['horario'])
            self.temposLigado.append(int(horario['tempoLigado']))

        self.tempoOcioso()


    ## Calcula o tempo que o sistema fica ocioso entre um horário e outro, evitando que o
    ## sistema fique perguntando que horas são quando não há necessidade disso.     
    def tempoOcioso(self):
        
        formatDate = '%M:%S'
        for i in range(len(self.horariosLigar)):
            if self.horariosLigar[i] != self.horariosLigar[-1]:
                tempoMorto = (datetime.strptime(self.horariosLigar[i+1], formatDate) - datetime.strptime(self.horariosLigar[i], formatDate)).total_seconds()
                self.temposMortos.append(tempoMorto - self.temposLigado[i] )
            ## Erro aqui (Sistema ainda funciona)
            else:
                t = (datetime.strptime("24:00", formatDate) - datetime.strptime(self.horariosLigar[-1], formatDate)).total_seconds()
                t += (datetime.strptime("24:00", formatDate) - datetime.strptime(self.horariosLigar[0], formatDate)).total_seconds()

                self.temposMortos.append(t - self.temposLigado[-1])
    
    ## Método geral que iniciará o sitema
    def iniciar(self):
    
        while True:
            self._formatarHorarios()
            horaAtual = datetime.now()
            horaAtual = horaAtual.strftime('%H:%M')
            
            if horaAtual in self.horariosLigar:
                print("Horário encontrado")
   
                index = self.horariosLigar.index(horaAtual)
                #self.horariosLigar.remove(horaAtual)
                tempoLigado = self.temposLigado[index]
                #self.temposLigado.remove(tempoLigado)
                
                self._ligar(horaAtual, tempoLigado)
                
                time.sleep(tempoLigado * 60)
                self._desligar(horaAtual, tempoLigado)
                tempoMorto = self.temposMortos[index]
                self.temposMortos = []
                self._formatarHorarios()
                
                print(f"O while está dormindo {tempoMorto}")
                time.sleep(tempoMorto * 60)
                #self.temposMortos.remove(tempoMorto)
            else:
                print("Horário não encontrado")
                time.sleep(3)
                    
            




