from BancoDados import BancoDados
import sys
import json

classAgendamentos = BancoDados('agendamentos.json')

dado = sys.argv[1]
dado = dado.split(',')

h = {}
h['id'] = "ID"
h['horario'] = dado[0]
h['tempoLigado'] = dado[1]
h['valvula'] = dado[2]
h['status'] = 0

dado = json.dumps(h)
classAgendamentos.cadastrar(dado)



