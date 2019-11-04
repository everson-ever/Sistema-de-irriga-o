from Led import Led
from datetime import datetime
import time
import json

## O horário no arquivo JSON deve estar neste formato para funcionar corretamente:
## {"id": "1005", "horario": "10:40", "tempoLigado": "40", "led": "11"}

class Irrigar():

    def __init__(self):
        
        self.horariosLigar = []
        self.temposLigado = []
        self.leds = []
        self._formatarHorarios()


    ## Pega os horários gravados
    def _pegarHorarios(self):
        horarios = open("horarios.json", 'r')
        return horarios.readlines()


    ## Método para pegar o json(horario) e separar horas a ligar e tempos ligado e leds em três listas.
    ## A posição de um horário, seu tempo ligado e led correspondem.
    def _formatarHorarios(self):
        
        horarios = self._pegarHorarios()
        for horario in horarios:
            horario = json.loads(horario)
            self.horariosLigar.append(horario['horario'])
            self.temposLigado.append(int(horario['tempoLigado']))
            self.leds.append(int(horario['led']))

    
    ## Método geral que iniciará o sitema
    def iniciar(self):
        led = Led()
    
        while True:
            self._formatarHorarios()
            horaAtual = datetime.now()
            horaAtual = horaAtual.strftime('%H:%M')
            time.sleep(2)
            if horaAtual in self.horariosLigar:
   
                index = self.horariosLigar.index(horaAtual)
                tempoLigado = self.temposLigado[index]
                
                ledAtual = self.leds[index]
                
                led.ligar(ledAtual)      
                time.sleep(tempoLigado * 60)
                
                led.desligar(ledAtual)
                
                self._formatarHorarios()

                    
            





