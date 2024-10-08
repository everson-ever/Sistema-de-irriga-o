import json
import time

from ValidaDados import ValidaDados


class BancoDados():

    def __init__(self, arquivo):
        self.validaDados = ValidaDados()
        self.arquivo = arquivo
        self.dadosGravados()


    ## Retorna os dados gravados no sistema - somente leitura
    def dadosGravados(self):
        arq = open(self.arquivo, 'r')
        return arq.readlines()


    ## Método responsável por calcular o id do novo dado
    ## params : {
    ##      ultimoId: Último id cadastrado no sistema
    ##      dado: dado a ser cadastrado - dicionário
    ##}
    def _adicionarId(self,ultimoId, dado):
        dado['id'] = str(int(ultimoId) + 1)
        return dado

    ## Pega o id de um dado
    ## params : {
    ##      dado: Um dado - formato: json
    ##}
    def _pegarIdDado(self, dado):    
        #dado = json.loads(dado)    
        dado = self.converterDadoDic(dado);
        return dado['id']

    ## Converte um dado que está em formato json para dicionário python
    ## params : {
    ##      dado: Um dado - formato: json
    ##}
    def converterDadoDic(self, dado):
        dado = json.loads(dado)
        return dado

    ## Converte um dado que está em formato dic para json
    ## params : {
    ##      dado: Um dado - formato: dic
    ##}
    def converterDadoJson(self, dado):
        dado = json.dumps(dado)
        return dado

    ## Procura um dado no banco a partir de um id
    ## params : {
    ##      dados: dados já cadastrados no sistema
    ##      dadoId: Um id de um dado
    ##}
    def _procurarDadoBanco(self, dados, dadoId):
        #dadosCadastrados = self.dadosGravados()

        for index, dado in enumerate(dados):
            dadoCadastrado = self.converterDadoDic(dado)
            if int(dadoCadastrado['id']) == int(dadoId):
                return index
    
    def pegarDadoBanco(self, idDadoPesquisar):
       
        dadosCadastrados = self.dadosGravados()

        for dado in dadosCadastrados:
            dado = self.converterDadoDic(dado)
            if dado['id'] == idDadoPesquisar:
                return dado
        return False

            
    def limparArquivo(self):
        arq = open(self.arquivo, 'w')
        arq.write('')
        arq.close()
           
        return -1

    def alterarStatus(self, index, status):
        dadoCadastrados = self.dadosGravados()
        dado = self.converterDadoDic(dadoCadastrados[index])
        dado['status'] = status

        dado = self.converterDadoJson(dado)

        self.atualizar(dado)

    def salvarArquivo(self, dadosCadastrados):
        arq = open(self.arquivo, 'w')
        arq.write('\n'.join(dadosCadastrados).replace('\n', '').replace('}', '}\n'))
        arq.close()

    ## Cadastrar um novo dado
    ## params : {
    ##      novoDado: Novo dado que será cadastrado - formato: json
    ##}
    def cadastrar(self, novoDado):
        arq = open(self.arquivo, 'a')

        ## Convertendo o dado passado para dicionário
        novoDado = self.converterDadoDic(novoDado)

        if(not self.validaDados.validar(novoDado)):
            return False

        
        ## Pegando todos os dados cadastrados
        dadosCadastrados = self.dadosGravados()

        if len(dadosCadastrados) > 0:
            ## Adicionando um novo id para o novo dado
            self.ultimoDado = dadosCadastrados[-1]
            ultimoId = self._pegarIdDado(self.ultimoDado)
            novoDado = self._adicionarId(ultimoId, novoDado)
        else:
            ## Adicionando o primeiro dado ao sistema. id = 1
            ultimoId = 0
            novoDado = self._adicionarId(ultimoId, novoDado)

        # Cadastrando um novo dado
        try:
            arq.write("{0}{1}".format(json.dumps(novoDado), '\n'))
            arq.close()
            return novoDado
        except OSError as e:
            return False


    ## Deleta um dado do sistema
    ## params : {
    ##      dado: ID's de dados - list
    ##      ou
    ##      dados: Id do dado - number
    ##}
    def deletar(self, dados):

        if str(dados).isdigit():
            dados = [dados]

            for dado in dados:
                try:

                    ## Buscando os dados cadastrados no banco 
                    dadosCadastrados = self.dadosGravados()
                    
                    indexDado = self._procurarDadoBanco(dadosCadastrados, dado)
                    
                    if indexDado == None:
                        indexDado = -1
                        continue
                    

                    if indexDado >= 0:
                    
                        del dadosCadastrados[indexDado]

                        self.salvarArquivo(dadosCadastrados)

                    else:
                        return False
                    
                except IndexError:
                    return False
                except OSError:
                    return False


    
    def atualizar(self, dado):
        dadosCadastrados = self.dadosGravados()
        
        dado = self.converterDadoDic(dado)
        dadoId = dado['id']

        if(not self.validaDados.validar(dado)):
            return False

        indexDado = self._procurarDadoBanco(dadosCadastrados, dadoId)

        if indexDado == None:
            return False
        
        if indexDado >= 0:
            dado = self.converterDadoJson(dado)
            dadosCadastrados[indexDado] = dado
            
            self.salvarArquivo(dadosCadastrados)
            
            return dado
        return False
