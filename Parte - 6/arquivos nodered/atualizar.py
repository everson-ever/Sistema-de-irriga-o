from BancoDados import BancoDados
import sys
import json

classAgendamentos = BancoDados('agendamentos.json')

dado = sys.argv[1]
dado = dado.split(',')

h = {}
h['id'] = dado[0]
h['horario'] = dado[1]
h['tempoLigado'] = dado[2]
h['valvula'] = dado[3]
h['status'] = 0

dado = json.dumps(h)



classAgendamentos.atualizar(dado)
