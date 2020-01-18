import time

from Irrigacao import Irrigacao

irrigacao = Irrigacao()


try:
    irrigacao.iniciar()

except Exception:
    time.sleep(5)
    irrigacao.iniciar()
