from datetime import datetime
from BancoDados import BancoDados
import time

class PesquisaLog():

    def __init__(self):
        self.classHistorico = BancoDados('historico.json')
        self.classResultadoPesquisa = BancoDados('pesquisaHistoricoResultado.json')
       
        self.resultado = []


    def converterParaData(self, data):
        return datetime.strptime(data, '%Y-%m-%d')


    def armazenarResultado(self, resultados):
        historicosGravados = self.classResultadoPesquisa.dadosGravados()


        if len(historicosGravados) > 0:
            self.classResultadoPesquisa.limparArquivo()
         
        for resultado in resultados:
            
            resultado = self.classResultadoPesquisa.converterDadoJson(resultado)     
            self.classResultadoPesquisa.cadastrar(resultado)
            



    def historicoIntervalo(self, dataInicial, dataFinal):

        historicosGravados = self.classHistorico.dadosGravados()
     

        dataInicial = self.converterParaData(dataInicial)
        dataFinal = self.converterParaData(dataFinal)
    
        for historico in historicosGravados:
            
            historico = self.classHistorico.converterDadoDic(historico)
            dataHistorico = self.converterParaData(historico['data'])
            

            if dataHistorico >= dataInicial and dataHistorico <= dataFinal:
                self.resultado.append(historico)


        #joga os horarios dentro do arquivo json

        self.armazenarResultado(self.resultado)
        


    def historicosDia(self):
        dataHoje = datetime.now()
        dataHoje = dataHoje.strftime('%Y-%m-%d')
        dataHoje = self.converterParaData(dataHoje)

        historicosGravados = self.classHistorico.dadosGravados()
         
        for historico in historicosGravados:
            
            historico = self.classHistorico.converterDadoDic(historico)
            dataHistorico = self.converterParaData(historico['data'])

            if dataHistorico == dataHoje:
                self.resultado.append(historico)
                
        self.armazenarResultado(self.resultado)
        
        
        


        
