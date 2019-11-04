from BancoDados import BancoDados

bancoDados = BancoDados('agendamentos.json')

agendamento = '{"id": "2", "horario": "15:00", "tempoLigado": "2", "led": 13, "status": 0, "ativado": 1 }'

#bancoDados.cadastrar(agendamento)
#horario.atualizar('{"id": "4", "horario": "21:35", "tempoLigado": "200", "led": 11, "status": 0}')
#horario.deletar([9])

agendamento = bancoDados.converterDadoDic(agendamento)

agendamento = bancoDados.pegarDadoBanco(agendamento)

print(agendamento['id'])
