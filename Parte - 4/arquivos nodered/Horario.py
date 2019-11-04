import json
import time


class Horario():

    def __init__(self):
        self._horariosGravados()
        self.ultimoHorario = 0


    ## Retorna os horários gravados no sistema
    def _horariosGravados(self):
        arq = open("horarios.json", 'r')
        return arq.readlines()


    ## Método responsável por calcular o id do novo horário
    ## params : {
    ##      ultimoId: Último id cadastrado no sistema
    ##      horario: horário a ser cadastrado - dicionário
    ##}
    def _adicionarId(self,ultimoId, horario):
        horario['id'] = str(int(ultimoId) + 1)
        return horario

    ## Pega o id de um horário
    ## params : {
    ##      horario: Um horario - formato: json
    ##}
    def _pegarIdHorario(self, horario):    
        horario = json.loads(self.ultimoHorario)    
        return horario['id']

    ## Converte um horário que está em formato json para dicionário python
    ## params : {
    ##      horario: Um horario - formato: json
    ##}
    def _converterHorarioDic(self, horario):
        horario = json.loads(horario)
        return horario

    ## Converte um horário que está em formato dic para json
    ## params : {
    ##      horario: Um horario - formato: dic
    ##}
    def _converterHorarioJson(self, horario):
        horario = json.dumps(horario)
        return horario

    ## Procura um horário no banco a partir de um id
    ## params : {
    ##      horrrios: Horários já cadastrados no sistema
    ##      horarioId: Um id de um horário
    ##}
    def _procurarHorarioBanco(self, horarios, horarioId):

        for index, horario in enumerate(horarios):
            horarioCadastrado = self._converterHorarioDic(horario)
            if int(horarioCadastrado['id']) == int(horarioId):
                return index
           
        return -1

    ## Cadastrar um novo horário
    ## params : {
    ##      novoHorario: Novo horário que será cadastrado - formato: json
    ##}
    def cadastrar(self, novoHorario):
        arq = open("horarios.json", 'a')

        ## Convertendo o horário passado para dicionário
        novoHorario = self._converterHorarioDic(novoHorario)

        
        ## Pegando todos horários cadastrados
        horarios = self._horariosGravados()

        if len(horarios) > 0:
            ## Adicionando um novo id para o novo horário
            self.ultimoHorario = horarios[-1]
            ultimoId = self._pegarIdHorario(self.ultimoHorario)
            novoHorario = self._adicionarId(ultimoId, novoHorario)
        else:
            ## Adicionando o primeiro horário ao sistema. id = 1
            ultimoId = 0
            novoHorario = self._adicionarId(ultimoId, novoHorario)

        # Cadastrando um novo horário
        try:
            arq.write("{0}{1}".format(json.dumps(novoHorario), '\n'))
            arq.close()
            return True
        except OSError as e:
            return False


    ## Deleta um horário do sistema
    ## params : {
    ##      horario: Lista de ID's de horários
    ##      ou
    ##      horario: Id do horário - number
    ##}
    def deletar(self, horario):
        if type(horario) == list:
            for h in horario:
                try:

                    ## Buscando o horário cadastrado no banco (arquivo)
                    horariosCadastrados = self._horariosGravados()
                    indexHorario = self._procurarHorarioBanco(horariosCadastrados, h)
                    

                    if indexHorario >= 0:
                    
                        del horariosCadastrados[indexHorario]
                        #print(horariosCadastrados)

                        arq = open("horarios.json", 'w')
                        arq.write('\n'.join(horariosCadastrados).replace('\n', '').replace('}', '}\n'))
                        arq.close()
                        #time.sleep(600)
                        #for h in horariosCadastrados:
                            #self.adicionarNaoExcluidos(h)
                        #return True
                    else:
                        return False
                    
                except IndexError:
                    return False
                except OSError:
                    return False
                              
        elif str(horario).isdigit():
            try:

                ## Buscando o horário cadastrado no banco (arquivo)
                horariosCadastrados = self._horariosGravados()
                indexHorario = self._procurarHorarioBanco(horariosCadastrados, horario)
                

                if indexHorario >= 0:
                
                    del horariosCadastrados[indexHorario]
                    #print(horariosCadastrados)

                    arq = open("horarios.json", 'w')
                    arq.write('\n'.join(horariosCadastrados).replace('\n', '').replace('}', '}\n'))
                    arq.close()
                    #time.sleep(600)
                    #for h in horariosCadastrados:
                        #self.adicionarNaoExcluidos(h)
                    return True
                else:
                    return False
                    
            except IndexError:
                return False


    
    def atualizar(self, horario):
        horariosCadastrados = self._horariosGravados()
        
        horario = self._converterHorarioDic(horario)
        horarioId = horario['id']

        indexHorario = self._procurarHorarioBanco(horariosCadastrados, horarioId)
        
        if indexHorario >= 0:
            horario = self._converterHorarioJson(horario)
            horariosCadastrados[indexHorario] = horario

            arq = open("horarios.json", 'w')
            arq.write('\n'.join(horariosCadastrados).replace('\n', '').replace('}', '}\n'))
            arq.close()
            return True
        return False






















        

