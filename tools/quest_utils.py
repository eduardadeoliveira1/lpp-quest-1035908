"""Ajudantes dos testes em Python. Não precisa editar."""
import copy
import unittest


def sem_mutar(teste: unittest.TestCase, funcao, *args):
    """Chama funcao(*args) e confere que NENHUM argumento foi alterado. Devolve o resultado."""
    original = copy.deepcopy(args)
    resultado = funcao(*args)
    teste.assertEqual(
        args, original,
        "A função alterou um argumento recebido. Devolva valores novos em vez de mudar a entrada.",
    )
    return resultado


def pura(teste: unittest.TestCase, funcao, *args):
    """Chama duas vezes, sem mutar os argumentos, e confere que o resultado é o mesmo."""
    r1 = sem_mutar(teste, funcao, *copy.deepcopy(args))
    r2 = sem_mutar(teste, funcao, *copy.deepcopy(args))
    teste.assertEqual(r1, r2, "Mesma entrada, resultados diferentes: a função não é pura.")
    return r1
