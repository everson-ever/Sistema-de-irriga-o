from Horario import Horario
import sys

horario = Horario()

deletar = sys.argv[1]
print(type(deletar))
horario.deletar(int(deletar))

