from BancoDados import BancoDados
import sys
import json

classConfiguracoes = BancoDados('configuracoes.json')

tempo = sys.argv[1]
configuracoesDic = {}

configuracoesDic['id'] = 1
configuracoesDic['tempoPadrao'] = tempo

configuracoesJson = classConfiguracoes.converterDadoJson(configuracoesDic)

classConfiguracoes.atualizar(configuracoesJson) 
