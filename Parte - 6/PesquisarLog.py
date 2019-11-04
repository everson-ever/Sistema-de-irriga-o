from datetime import datetime
from Horario import Horario
import time

class PesquisarLog():

    def __init__(self):
        self.classHistorico = Horario('historico.json')
        self.classResultadoPesquisa = Horario('pesquisaResultado.json')
       
        self.resultado = []


    def converterParaData(self, data):
        return datetime.strptime(data, '%Y-%m-%d')


    def armazenarResultado(self, resultados):
        for arquivo in resultados:
            
            arquivo = self.classResultadoPesquisa.converterHorarioJson(arquivo)
            
            self.classResultadoPesquisa.cadastrar(arquivo)
            



    def intervaloDatas(self, dataInicial, dataFinal):

        horariosGravados = self.classHistorico.horariosGravados()
     

        dataInicial = self.converterParaData(dataInicial)
        dataFinal = self.converterParaData(dataFinal)
    
        for historico in horariosGravados:
            
            historico = self.classHistorico.converterHorarioDic(historico)
            dataHistorico = self.converterParaData(historico['data'])
            

            if dataHistorico >= dataInicial and dataHistorico <= dataFinal:
                self.resultado.append(historico)


        #joga os horarios dentro do arquivo json
        self.armazenarResultado(self.resultado)
        


    def historicosDia(self):
        dataHoje = datetime.now()
        dataHoje = dataHoje.strftime('%Y-%m-%d')
        dataHoje = self.converterParaData(dataHoje)
         
        for historico in self.historico:
            dataHistorico = self.converterParaData(historico['data'])

            if dataHistorico == dataHoje:
                self.resultado.append(historico)
        for i in self.resultado:
            print(i)
        
        
        






pesquisarLog = PesquisarLog()

pesquisarLog.intervaloDatas("2019-09-1", "2019-09-25")
#pesquisarLog.historicosDia()

        
