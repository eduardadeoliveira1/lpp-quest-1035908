# 🏜️ Nível 3 — Cânions dos Logs

> O servidor cuspiu um arquivo gigante de texto. Cada etapa da sua trilha recebe o que a anterior devolveu: um **pipeline**.

| | |
|---|---|
| **Linguagem** | Python |
| **Arquivo que você edita** | `logs.py` |
| **Missões** | 3 (10 XP cada) + 10 XP de bônus |
| **Conceito** | pipeline de transformações e composição |

## 🧠 O conceito em 1 minuto

Quem usa o terminal já conhece:

```
cat acessos.log | grep ERRO | wc -l
```

Cada comando faz **uma coisa** e passa o resultado adiante: ler, filtrar, contar. No código funcional é igual: funções pequenas e puras, ligadas em sequência. Neste nível você vai até construir o seu próprio `pipe`.

Uma linha de log: `"GET /home 200 120ms"` (método, rota, status, tempo).

## ▶️ Como jogar

Edite `logs.py` e teste com `python quest.py 3` (Mac/Linux: `python3 quest.py 3`).

---

## ⚔️ Missão 3.1 — Ler o log

1. `parsear_linha`: `linha.split()` separa em quatro pedaços. Converta `status` e `ms` para `int` (tire o `"ms"` do fim com `removesuffix`).
2. `parsear`: aplique `parsear_linha` a cada linha, **ignorando** as vazias e as que começam com `#`.

<details><summary>💡 Dica</summary>

Uma comprehension com `if`: `[parsear_linha(l) for l in linhas if l.strip() and not l.startswith("#")]`.
</details>

## ⚔️ Missão 3.2 — Filtrar e contar

1. `erros`: `filter` nos registros com `status >= 400`.
2. `contagem_por_rota`: `{rota: quantidade}`. Use `reduce` devolvendo um dicionário **novo** a cada passo (`{**acc, rota: acc.get(rota, 0) + 1}`). Nada de `acc[rota] += 1`!
3. `rotas_mais_acessadas(registros, n)`: use a contagem, ordene com `sorted` (quantidade maior primeiro; empate pela rota) e devolva `[rota, quantidade]` das `n` primeiras.

<details><summary>💡 Dica: ordenação por dois critérios</summary>

`sorted(contagem.items(), key=lambda par: (-par[1], par[0]))` ordena por quantidade decrescente e, no empate, por rota.
</details>

## ⚔️ Missão 3.3 — O pipeline final

1. `tempo_medio`: média do campo `ms` (2 casas; lista vazia → `0.0`).
2. `pipe(*funcoes)`: devolve uma função que aplica as funções da **esquerda para a direita**. `pipe(f, g)(x)` é `g(f(x))`. Sem funções, devolve o próprio `x`.
3. `relatorio(linhas)`: `parsear`, contar erros, calcular a taxa e o tempo médio e pegar o top 3 de rotas. Sem laços e sem variáveis que mudam.

<details><summary>💡 Dica: pipe</summary>

`def pipe(*funcoes): return lambda x: reduce(lambda acc, f: f(acc), funcoes, x)`. Entenda cada pedaço antes de usar!
</details>

---

## 🏆 Level clear

Três ✅ = nível limpo. `git add . && git commit -m "nivel 3: canions dos logs concluido"`.
