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
    if len(notas) == 0:
        return 0.0

    resultado = sum(notas) / len(notas)
    return round(resultado, 2)


def situacao(media_final):
    """"aprovado" (média >= 7), "recuperacao" (>= 5 e < 7) ou "reprovado" (< 5)."""
    if media_final >= 7:
        return "aprovado"
    elif media_final >= 5:
        return "recuperacao"
    else:
        return "reprovado"


# ============================================================ MISSÃO 1.2 — map: o boletim da turma
def boletim(alunos):
    """Recebe [{"nome": "Ana", "notas": [8, 9]}, ...] e devolve uma lista NOVA de
    {"nome": ..., "media": ..., "situacao": ...}, na mesma ordem.

    Dica: uma list comprehension (ou map) usando as funções da missão 1.1.
    A lista original não pode ser alterada!
    """
    def criar_boletim(aluno):
        nota_media = media(aluno["notas"])

        return {
            "nome": aluno["nome"],
            "media": nota_media,
            "situacao": situacao(nota_media)
        }

    return list(map(criar_boletim, alunos))


# ============================================================ MISSÃO 1.3 — filter e reduce: aprovados e ranking
def aprovados(boletins):
    """Lista com os NOMES dos alunos aprovados, na ordem original. (filter)"""
    return [
        aluno["nome"]
        for aluno in boletins
        if aluno["situacao"] == "aprovado"
    ]


def media_da_turma(boletins):
    """Média das médias da turma, arredondada a 2 casas. Lista vazia: 0.0. (reduce ou sum)"""
    if len(boletins) == 0:
        return 0.0

    soma = sum(aluno["media"] for aluno in boletins)
    return round(soma / len(boletins), 2)


def ranking(boletins):
    """Lista de nomes ordenada pela média, da maior para a menor. Empate: ordem alfabética.

    Dica: sorted(..., key=lambda b: (-b["media"], b["nome"])) devolve uma lista NOVA.
    """
    ordenados = sorted(
        boletins,
        key=lambda aluno: (-aluno["media"], aluno["nome"])
    )

    return [aluno["nome"] for aluno in ordenados]
