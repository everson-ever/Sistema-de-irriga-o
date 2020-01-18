import json
import sys

from BancoDados import BancoDados

classAgendamentos = BancoDados('agendamentos.json')

dado = sys.argv[1]
dado = dado.split(',')

h = {}
h['id'] = "ID"
h['horario'] = dado[0]
h['tempoLigado'] = dado[1]
h['valvula'] = dado[2]
h['status'] = 0
h['ativado'] = 1


#dado = json.dumps(h)
dado = classAgendamentos.converterDadoJson(h)
classAgendamentos.cadastrar(dado)
