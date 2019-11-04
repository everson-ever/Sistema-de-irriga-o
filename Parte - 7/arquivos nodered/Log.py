from datetime import date

from BancoDados import BancoDados


class Log:

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.classLog = BancoDados(arquivo)






    def registrarLog(self, valvula, inicio, fim, modo):


        DIAS = [
        'Segunda-feira',
        'Terca-feira',
        'Quarta-feira',
        'Quinta-Feira',
        'Sexta-feira',
        'Sabado',
        'Domingo'
        ]
        data = date.today()
        indiceSemana = data.weekday()
        diaSemana = DIAS[indiceSemana]

        
        historico = {}
        historico['id'] = ''
        historico['valvula'] = valvula
        historico['data'] = str(data)
        historico['inicio'] = inicio
        historico['fim'] = fim
        historico['dia'] = diaSemana
        historico['modo'] = modo
        

        historico = self.classLog.converterDadoJson(historico)
        dadoCadastro = self.classLog.cadastrar(historico)

        return dadoCadastro
