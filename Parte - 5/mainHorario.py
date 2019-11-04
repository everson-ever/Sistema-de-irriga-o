from Horario import Horario


horario = Horario('horarios.json')

#horario.cadastrar('{"id": "", "horario": "15:00", "tempoLigado": "2", "led": 13, "status": 0 }')
#horario.atualizar('{"id": "4", "horario": "21:35", "tempoLigado": "200", "led": 11, "status": 0}')
horario.deletar([9])
