import unittest

from logs import (contagem_por_rota, erros, parsear, parsear_linha, pipe, relatorio,
                  rotas_mais_acessadas, tempo_medio)
from quest_utils import pura, sem_mutar

LINHAS = [
    "# acessos do servidor",
    "GET /home 200 120ms",
    "GET /home 200 80ms",
    "POST /login 401 200ms",
    "GET /produtos 200 300ms",
    "GET /produtos 500 900ms",
    "GET /produtos 200 100ms",
    "",
    "GET /sobre 404 50ms",
]
REGISTROS = [
    {"metodo": "GET", "rota": "/home", "status": 200, "ms": 120},
    {"metodo": "GET", "rota": "/home", "status": 200, "ms": 80},
    {"metodo": "POST", "rota": "/login", "status": 401, "ms": 200},
    {"metodo": "GET", "rota": "/produtos", "status": 200, "ms": 300},
    {"metodo": "GET", "rota": "/produtos", "status": 500, "ms": 900},
    {"metodo": "GET", "rota": "/produtos", "status": 200, "ms": 100},
    {"metodo": "GET", "rota": "/sobre", "status": 404, "ms": 50},
]


class Missao_3_1(unittest.TestCase):
    def test_parsear_linha(self):
        self.assertEqual(
            pura(self, parsear_linha, "GET /home 200 120ms"),
            {"metodo": "GET", "rota": "/home", "status": 200, "ms": 120},
        )

    def test_parsear_linha_converte_numeros(self):
        r = parsear_linha("POST /login 401 200ms")
        self.assertIsInstance(r["status"], int)
        self.assertIsInstance(r["ms"], int)

    def test_parsear_ignora_comentarios_e_linhas_vazias(self):
        self.assertEqual(pura(self, parsear, LINHAS), REGISTROS)

    def test_parsear_lista_vazia(self):
        self.assertEqual(parsear([]), [])


class Missao_3_2(unittest.TestCase):
    def test_erros(self):
        r = pura(self, erros, REGISTROS)
        self.assertEqual([x["status"] for x in r], [401, 500, 404])

    def test_erros_nenhum(self):
        self.assertEqual(erros([REGISTROS[0]]), [])

    def test_contagem_por_rota(self):
        self.assertEqual(
            pura(self, contagem_por_rota, REGISTROS),
            {"/home": 2, "/login": 1, "/produtos": 3, "/sobre": 1},
        )

    def test_contagem_vazia(self):
        self.assertEqual(contagem_por_rota([]), {})

    def test_rotas_mais_acessadas(self):
        self.assertEqual(
            pura(self, rotas_mais_acessadas, REGISTROS, 3),
            [["/produtos", 3], ["/home", 2], ["/login", 1]],
        )

    def test_rotas_mais_acessadas_n_maior_que_o_total(self):
        self.assertEqual(len(rotas_mais_acessadas(REGISTROS, 10)), 4)


class Missao_3_3(unittest.TestCase):
    def test_tempo_medio(self):
        self.assertEqual(pura(self, tempo_medio, REGISTROS), 250.0)

    def test_tempo_medio_vazio(self):
        self.assertEqual(tempo_medio([]), 0.0)

    def test_pipe_ordem_esquerda_para_direita(self):
        mais_um = lambda x: x + 1
        dobro = lambda x: x * 2
        self.assertEqual(pipe(mais_um, dobro)(3), 8)
        self.assertEqual(pipe(dobro, mais_um)(3), 7)

    def test_pipe_sem_funcoes_devolve_a_entrada(self):
        self.assertEqual(pipe()(42), 42)

    def test_relatorio(self):
        self.assertEqual(
            pura(self, relatorio, LINHAS),
            {"total": 7, "erros": 3, "taxa_erro": 0.43, "tempo_medio": 250.0,
             "top_rotas": [["/produtos", 3], ["/home", 2], ["/login", 1]]},
        )

    def test_relatorio_sem_registros(self):
        self.assertEqual(
            relatorio(["# nada aqui", ""]),
            {"total": 0, "erros": 0, "taxa_erro": 0.0, "tempo_medio": 0.0, "top_rotas": []},
        )

    def test_relatorio_nao_altera_as_linhas(self):
        sem_mutar(self, relatorio, LINHAS)
