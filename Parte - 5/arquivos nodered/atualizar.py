from Horario import Horario
import sys
import json

horario = Horario('horarios.json')

atualizar = sys.argv[1]
atualizar = atualizar.split(',')

h = {}
h['id'] = atualizar[0]
h['horario'] = atualizar[1]
h['tempoLigado'] = atualizar[2]
h['valvula'] = atualizar[3]
h['status'] = 0

atualizar = json.dumps(h)



horario.atualizar(atualizar)
