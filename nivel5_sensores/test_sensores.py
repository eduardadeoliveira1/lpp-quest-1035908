import unittest

from quest_utils import pura, sem_mutar
from sensores import (contar, detectar_alertas, limpar, maximo, media_movel, resumo_sensores, somar)

LEITURAS = [22.5, None, 30.0, 90.0, -50.0, 41.0, 85.0, -40.0]
# válidas: 22.5, 30.0, 41.0, 85.0, -40.0


class Missao_5_1(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(pura(self, somar, [1, 2, 3, 4]), 10)

    def test_somar_vazia(self):
        self.assertEqual(somar([]), 0)

    def test_somar_lista_de_100_itens(self):
        self.assertEqual(somar(list(range(1, 101))), 5050)

    def test_contar(self):
        self.assertEqual(pura(self, contar, [1, 5, 9, 2], lambda x: x > 4), 2)

    def test_contar_vazia(self):
        self.assertEqual(contar([], lambda x: True), 0)

    def test_maximo(self):
        self.assertEqual(pura(self, maximo, [3, 9, 2, 7]), 9)
        self.assertEqual(maximo([-5, -2, -9]), -2)

    def test_maximo_vazia(self):
        self.assertIsNone(maximo([]))


class Missao_5_2(unittest.TestCase):
    def test_limpar(self):
        self.assertEqual(pura(self, limpar, LEITURAS), [22.5, 30.0, 41.0, 85.0, -40.0])

    def test_limpar_tudo_invalido(self):
        self.assertEqual(limpar([None, 100, -99]), [])

    def test_media_movel(self):
        self.assertEqual(pura(self, media_movel, [1, 2, 3, 4], 2), [1.5, 2.5, 3.5])

    def test_media_movel_janela_3(self):
        self.assertEqual(media_movel([10, 20, 30, 40, 50], 3), [20.0, 30.0, 40.0])

    def test_media_movel_arredonda(self):
        self.assertEqual(media_movel([1, 2, 2], 3), [1.67])

    def test_media_movel_lista_curta(self):
        self.assertEqual(media_movel([1, 2], 3), [])


class Missao_5_3(unittest.TestCase):
    def test_detectar_alertas(self):
        self.assertEqual(
            pura(self, detectar_alertas, LEITURAS, 40),
            [{"indice": 5, "valor": 41.0}, {"indice": 6, "valor": 85.0}],
        )

    def test_alerta_ignora_leituras_invalidas(self):
        self.assertEqual(detectar_alertas([None, 90.0, 200], 10), [])

    def test_resumo_sensores(self):
        sensores = {"s1": LEITURAS, "s2": [20.0, 24.0], "s3": [None, 999]}
        self.assertEqual(
            pura(self, resumo_sensores, sensores, 40),
            {
                "s1": {"validas": 5, "media": 27.7, "alertas": 2},
                "s2": {"validas": 2, "media": 22.0, "alertas": 0},
                "s3": {"validas": 0, "media": 0.0, "alertas": 0},
            },
        )

    def test_resumo_sem_sensores(self):
        self.assertEqual(resumo_sensores({}, 40), {})

    def test_resumo_nao_altera_a_entrada(self):
        sem_mutar(self, resumo_sensores, {"s1": LEITURAS}, 40)
