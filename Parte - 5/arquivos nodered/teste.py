from Horario import Horario


horario = Horario('pesquisaResultado.json')

horario.cadastrar('{"id": "13", "valvula": "Secao 1", "data": "2019-09-2", "inicio": "15:00", "fim": "15:02", "dia": "Quarta-feira", "modo": "Automatico"}')
#horario.atualizar('{"id": "4", "horario": "21:35", "tempoLigado": "200", "led": 11, "status": 0}')
#horario.deletar([9])
