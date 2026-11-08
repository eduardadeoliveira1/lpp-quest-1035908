"""NÍVEL 3 — Cânions dos Logs (Python)

O servidor da empresa cuspiu um arquivo de log e você precisa transformar aquelas linhas num
relatório. Cada etapa recebe o resultado da anterior: é um PIPELINE.
Siga as missões na ordem e rode  python quest.py 3  a cada passo (veja o LEIAME.md).

Uma linha de log tem o formato:  "METODO ROTA STATUS TEMPOms"   ex.: "GET /home 200 120ms"
"""


# ============================================================ MISSÃO 3.1 — Ler o log
def parsear_linha(linha):
    """"GET /home 200 120ms" -> {"metodo": "GET", "rota": "/home", "status": 200, "ms": 120}

    Dica: linha.split() separa por espaços; int(...) converte; tire o "ms" do final do tempo.
    """
    partes = linha.split()

    return {
        "metodo": partes[0],
        "rota": partes[1],
        "status": int(partes[2]),
        "ms": int(partes[3].removesuffix("ms"))
    }


def parsear(linhas):
    """Lista NOVA de registros (dicionários) a partir das linhas de texto.
    Ignore linhas vazias e linhas de comentário (começam com "#"). Dica: comprehension com if.
    """
    return [
        parsear_linha(l.strip())
        for l in linhas
        if l.strip() and not l.strip().startswith("#")
    ]


# ============================================================ MISSÃO 3.2 — Filtrar e contar
def erros(registros):
    """Só os registros com status >= 400. (filter)"""
    return list(filter(lambda registro: registro["status"] >= 400, registros))


from functools import reduce

def contagem_por_rota(registros):
    """Dicionário {rota: quantidade de acessos}.

    Dica: reduce com um dicionário NOVO a cada passo:  {**acc, rota: acc.get(rota, 0) + 1}
    (nada de acc[rota] += 1, isso altera o dicionário!)
    """
    return reduce(
        lambda acc, registro: {
            **acc,
            registro["rota"]: acc.get(registro["rota"], 0) + 1
        },
        registros,
        {}
    )


def rotas_mais_acessadas(registros, n):
    """Lista de [rota, quantidade] das n rotas mais acessadas, da maior para a menor.
    Empate: ordem alfabética da rota. Dica: sorted(..., key=lambda par: (-par[1], par[0])).
    """
    contagens = contagem_por_rota(registros)

    ordenadas = sorted(
        contagens.items(),
        key=lambda item: (-item[1], item[0])
    )

    return [[rota, quantidade] for rota, quantidade in ordenadas[:n]]


# ============================================================ MISSÃO 3.3 — O pipeline final
def tempo_medio(registros):
    """Média do campo "ms", arredondada a 2 casas. Lista vazia: 0.0."""
    if len(registros) == 0:
        return 0.0

    soma = sum(registro["ms"] for registro in registros)
    return round(soma / len(registros), 2)

from functools import reduce

def pipe(*funcoes):
    """Compõe funções da ESQUERDA para a DIREITA: pipe(f, g)(x) == g(f(x)). pipe() não faz nada: devolve x.

    Dica: reduce(lambda acc, f: f(acc), funcoes, x) dentro de uma função que recebe x.
    """
    def executar(valor):
        return reduce(
            lambda resultado, funcao: funcao(resultado),
            funcoes,
            valor
        )

    return executar


def relatorio(linhas):
    """Monta o relatório a partir das linhas de texto (já com comentários e linhas vazias):

    {"total": nº de registros, "erros": nº de erros, "taxa_erro": erros/total (2 casas, 0.0 se total 0),
     "tempo_medio": ..., "top_rotas": as 3 rotas mais acessadas}

    Use as funções das missões anteriores. Sem laços e sem variáveis que mudam!
    """
    registros = parsear(linhas)
    lista_erros = erros(registros)

    return {
        "total": len(registros),
        "erros": len(lista_erros),
        "taxa_erro": round(
            len(lista_erros) / len(registros), 2
        ) if registros else 0.0,
        "tempo_medio": tempo_medio(registros),
        "top_rotas": rotas_mais_acessadas(registros, 3)
    }


