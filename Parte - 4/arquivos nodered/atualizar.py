from Horario import Horario
import sys
import json

horario = Horario()

atualizar = sys.argv[1]
atualizar = atualizar.split(',')

h = {}
h['id'] = atualizar[0]
h['horario'] = atualizar[1]
h['tempoLigado'] = atualizar[2]
h['led'] = atualizar[3]

atualizar = json.dumps(h)



horario.atualizar(atualizar)
