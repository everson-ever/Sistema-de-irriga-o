from Horario import Horario
import sys
import json

horario = Horario('horarios.json')

cadastrar = sys.argv[1]
cadastrar = cadastrar.split(',')

h = {}
h['id'] = "ID"
h['horario'] = cadastrar[0]
h['tempoLigado'] = cadastrar[1]
h['valvula'] = cadastrar[2]
h['status'] = 0

cadastrar = json.dumps(h)
horario.cadastrar(cadastrar)



