from Horario import Horario
import sys
import json

classConfiguracoes = Horario('configuracoes.json')

tempo = sys.argv[1]
configuracoesDic = {}

configuracoesDic['id'] = 1
configuracoesDic['tempoPadrao'] = tempo

configuracoesJson = classConfiguracoes.converterHorarioJson(configuracoesDic)

classConfiguracoes.atualizar(configuracoesJson) 
