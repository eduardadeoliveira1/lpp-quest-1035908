"""NÍVEL 1 — Vila do Boletim (Python)

Você é o(a) novo(a) monitor(a) da turma e vai montar o boletim usando funções PURAS.
Siga as missões na ordem e rode  python quest.py 1  a cada passo (veja o LEIAME.md).

Regra de ouro: uma função pura só usa o que recebe e só devolve um valor.
Não altere as listas recebidas e não use print dentro destas funções.
"""


# ============================================================ MISSÃO 1.1 — Funções puras
def media(notas):
    """Média aritmética da lista de notas, arredondada a 2 casas. Lista vazia: 0.0.

    media([8, 6, 10]) -> 8.0
    Dica: sum(...) e len(...) resolvem. Cuidado com a lista vazia!
    """
    raise NotImplementedError


def situacao(media_final):
    """"aprovado" (média >= 7), "recuperacao" (>= 5 e < 7) ou "reprovado" (< 5)."""
    raise NotImplementedError


# ============================================================ MISSÃO 1.2 — map: o boletim da turma
def boletim(alunos):
    """Recebe [{"nome": "Ana", "notas": [8, 9]}, ...] e devolve uma lista NOVA de
    {"nome": ..., "media": ..., "situacao": ...}, na mesma ordem.

    Dica: uma list comprehension (ou map) usando as funções da missão 1.1.
    A lista original não pode ser alterada!
    """
    raise NotImplementedError


# ============================================================ MISSÃO 1.3 — filter e reduce: aprovados e ranking
def aprovados(boletins):
    """Lista com os NOMES dos alunos aprovados, na ordem original. (filter)"""
    raise NotImplementedError


def media_da_turma(boletins):
    """Média das médias da turma, arredondada a 2 casas. Lista vazia: 0.0. (reduce ou sum)"""
    raise NotImplementedError


def ranking(boletins):
    """Lista de nomes ordenada pela média, da maior para a menor. Empate: ordem alfabética.

    Dica: sorted(..., key=lambda b: (-b["media"], b["nome"])) devolve uma lista NOVA.
    """
    raise NotImplementedError
