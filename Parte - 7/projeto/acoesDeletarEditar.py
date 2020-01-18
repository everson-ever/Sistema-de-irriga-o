import sys

from BancoDados import BancoDados

classAgendamentos = BancoDados('agendamentos.json')

dados = sys.argv[1]
dados = dados.split(',')
print(dados)
acao = dados.pop(-1)



if acao == 'deletar':
    dado = dados[0]
    classAgendamentos.deletar(int(dado))

elif acao == 'editar':
    import json

    dado = dados

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

elif acao == 'situacao':
    dado = dados
    print(dado)
    agendamento = classAgendamentos.pegarDadoBanco(dado[0])

    agendamento['ativado'] = dados[1]

    agendamento = classAgendamentos.converterDadoJson(agendamento)

    classAgendamentos.atualizar(agendamento)
