import json
import sys

from BancoDados import BancoDados

classAgendamentos = BancoDados('agendamentos.json')

dado = sys.argv[1]
dado = dado.split(',')

agendamento = classAgendamentos.pegarDadoBanco(dado[0])

h = {}
h['id'] = dado[0]
h['horario'] = dado[1]
h['tempoLigado'] = dado[2]
h['valvula'] = dado[3]
h['status'] = agendamento['status']
h['ativado'] = agendamento['ativado']

dado = json.dumps(h)



classAgendamentos.atualizar(dado)
