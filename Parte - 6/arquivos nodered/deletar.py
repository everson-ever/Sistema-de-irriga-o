from BancoDados import BancoDados
import sys

classAgendamentos = BancoDados('agendamentos.json')

dado = sys.argv[1]

#if str(horarioDeletar).isdigit():
classAgendamentos.deletar(int(dado))

