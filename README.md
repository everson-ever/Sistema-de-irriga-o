# Sistema de irrigação automatizado

## Andamento atual do sistema
- Cadastro de agendamentos **OK**
- Deletar agendamentos **OK**
- Editar um agendamento **OK**
- Ativar e Desativar Válvula automaticamente de acordo com o agendamento **OK**
- Desativar um agendamento para não ser ativado no horário agendado **OK**
- Ativar e Desativar válvula manualmente **OK**
- Tempo padrão para desligar uma válvula acionada manualmente editável **OK**
- Gerar Log dos acionamentos **OK**
- Pesquisar nos logs (acionamentos do dia e entre datas) **OK**
- Visualizar válvulas ativas **OK**
- Agendar valvulas para serem ligadas apenas em determinado dia **Implementação futura**
- Capturar Ip do usuário que está acessando o sistema **Implementação futura**
- Pausar um acionamento automático e retornar quando deixar de ser pausado **Implementação futura**


## Desenvolvido com as tecnologias
- Raspberry pi 3
- Python - versão 3
- Javascript- es6
- Node js - 10.17.0
- Node Red - versão 1.0.2

### Raspberry pi 3
> Responsável por gerenciar o sistema

### Python3
> O python foi utilizado para desenvolver toda a lógica de funcionamento do sistema, desde
> cadastrar agendamentos a remover, até a ativação dos pinos dos raspberry.

### Javascript ,Node JS
> Javascript foi utlizado em funções do front para gerenciar o dados e node js foi instalado no
> raspberry para o funcionamento e gerenciamento do node red

### Node red
> Ferramenta utlizada para comunicar a interface do sistema de irrigação com os
> módulos do raspberry


# Imagens da aplicação
- Tela de cadastro de novo agendamento
<img src="https://github.com/EversonSilva9799/Sistema-de-irriga-o/blob/master/screenshot%20application/cadastro%20agendamentos.png" width="380">

- Tela de Agendamentos
<img src="https://github.com/EversonSilva9799/Sistema-de-irriga-o/blob/master/screenshot%20application/agendamentos.png" width="380">

- Tela de válvulas
<img src="https://github.com/EversonSilva9799/Sistema-de-irriga-o/blob/master/screenshot%20application/valvulas.png" width="380">

- Tela de tempo padrão
<img src="https://github.com/EversonSilva9799/Sistema-de-irriga-o/blob/master/screenshot%20application/tempo%20padrao.png" width="380">

- Tela de logs
<img src="https://github.com/EversonSilva9799/Sistema-de-irriga-o/blob/master/screenshot%20application/logs.png" width="380">


