from Horario import Horario
import sys

horario = Horario('horarios.json')

horarioDeletar = sys.argv[1]

#if str(horarioDeletar).isdigit():
horario.deletar(int(horarioDeletar))

