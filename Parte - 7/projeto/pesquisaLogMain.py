from PesquisaLog import PesquisaLog
import sys

pesquisaLog = PesquisaLog()





dados = sys.argv[1]
dados = dados.split(',')

acao = dados[0]
dataInicial = dados[1]
dataFinal = dados[2]

if acao == 'historicoDia':
    pesquisaLog.historicosDia()

elif acao == 'historicoIntervalo':
    pesquisaLog.historicoIntervalo(dataInicial, dataFinal)
