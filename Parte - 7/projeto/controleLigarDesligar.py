import sys

from ControleManual import ControleManual

controleManual = ControleManual()
logCadastrado = ''

dados = sys.argv[1]
dados = dados.split(',')

valvula = dados[0]
acao = dados[1]


if acao == 'ligar':
    controleManual.ligar(valvula)

elif acao == 'desligar':
    controleManual.desligar(valvula)
