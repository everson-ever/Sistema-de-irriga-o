import re


class ValidaDados():


    def regras():
        regrasDados = {
            "pureNumber": "[, ]",
            "timeFormat": "",
            
        }

    def isNumber(value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def validar(self, dados):
        for key in dados.keys():
            if key == "id":
                continue
            
            if len(str(dados[key])) == 0:
                return False

            dados[key] = re.sub('[, .]', '', str(dados[key]))

        return True
