"""Executa os testes de UM nível em Python e imprime o resultado em linhas @@QUEST@@ (uso interno do quest.py)."""
import json
import sys
import unittest

pasta_nivel, nome_modulo, pasta_tools = sys.argv[1:4]
sys.path.insert(0, pasta_tools)
sys.path.insert(0, pasta_nivel)


def resumo(erro):
    tipo, valor = erro[0], erro[1]
    if issubclass(tipo, AssertionError):
        texto = str(valor)
    elif issubclass(tipo, NotImplementedError):
        texto = "função ainda não implementada"
    else:
        texto = f"{tipo.__name__}: {valor}"
    return " ".join(texto.split())[:300]


class Resultado(unittest.TestResult):
    def __init__(self):
        super().__init__()
        self.eventos = []

    def _reg(self, teste, ok, msg=""):
        classe = type(teste).__name__
        nome = getattr(teste, "_testMethodName", "importação")
        self.eventos.append({"classe": classe, "teste": nome, "ok": ok, "msg": msg})

    def addSuccess(self, teste):
        super().addSuccess(teste)
        self._reg(teste, True)

    def addFailure(self, teste, erro):
        super().addFailure(teste, erro)
        self._reg(teste, False, resumo(erro))

    def addError(self, teste, erro):
        super().addError(teste, erro)
        self._reg(teste, False, resumo(erro))


resultado = Resultado()
unittest.defaultTestLoader.loadTestsFromName(nome_modulo).run(resultado)
for evento in resultado.eventos:
    print("@@QUEST@@ " + json.dumps(evento, ensure_ascii=False))
