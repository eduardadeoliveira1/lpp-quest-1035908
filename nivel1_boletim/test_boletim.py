import unittest

from boletim import (aprovados, boletim, media, media_da_turma, ranking, situacao)
from quest_utils import pura, sem_mutar

ALUNOS = [
    {"nome": "Ana", "notas": [8, 9, 10]},
    {"nome": "Bruno", "notas": [5, 6, 7]},
    {"nome": "Carla", "notas": [3, 4, 5]},
    {"nome": "Davi", "notas": [7, 7, 7]},
]
BOLETINS = [
    {"nome": "Ana", "media": 9.0, "situacao": "aprovado"},
    {"nome": "Bruno", "media": 6.0, "situacao": "recuperacao"},
    {"nome": "Carla", "media": 4.0, "situacao": "reprovado"},
    {"nome": "Davi", "media": 7.0, "situacao": "aprovado"},
]


class Missao_1_1(unittest.TestCase):
    def test_media_simples(self):
        self.assertEqual(pura(self, media, [8, 6, 10]), 8.0)

    def test_media_arredonda_2_casas(self):
        self.assertEqual(pura(self, media, [7, 8, 8]), 7.67)

    def test_media_lista_vazia(self):
        self.assertEqual(media([]), 0.0)

    def test_situacao_aprovado(self):
        self.assertEqual(situacao(7), "aprovado")
        self.assertEqual(situacao(10), "aprovado")

    def test_situacao_recuperacao(self):
        self.assertEqual(situacao(6.99), "recuperacao")
        self.assertEqual(situacao(5), "recuperacao")

    def test_situacao_reprovado(self):
        self.assertEqual(situacao(4.99), "reprovado")
        self.assertEqual(situacao(0), "reprovado")


class Missao_1_2(unittest.TestCase):
    def test_monta_o_boletim(self):
        self.assertEqual(pura(self, boletim, ALUNOS), BOLETINS)

    def test_lista_vazia(self):
        self.assertEqual(boletim([]), [])

    def test_nao_altera_a_lista_original(self):
        sem_mutar(self, boletim, ALUNOS)

    def test_devolve_lista_nova(self):
        self.assertIsNot(boletim(ALUNOS), ALUNOS)


class Missao_1_3(unittest.TestCase):
    def test_aprovados(self):
        self.assertEqual(pura(self, aprovados, BOLETINS), ["Ana", "Davi"])

    def test_aprovados_ninguem(self):
        self.assertEqual(aprovados([BOLETINS[2]]), [])

    def test_media_da_turma(self):
        self.assertEqual(pura(self, media_da_turma, BOLETINS), 6.5)

    def test_media_da_turma_vazia(self):
        self.assertEqual(media_da_turma([]), 0.0)

    def test_ranking(self):
        self.assertEqual(pura(self, ranking, BOLETINS), ["Ana", "Davi", "Bruno", "Carla"])

    def test_ranking_empate_ordem_alfabetica(self):
        empate = [{"nome": "Zé", "media": 7.0, "situacao": "aprovado"},
                  {"nome": "Ana", "media": 7.0, "situacao": "aprovado"}]
        self.assertEqual(ranking(empate), ["Ana", "Zé"])

    def test_ranking_nao_altera_a_entrada(self):
        sem_mutar(self, ranking, BOLETINS)
