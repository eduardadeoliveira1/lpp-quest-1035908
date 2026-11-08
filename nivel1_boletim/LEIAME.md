# 🏡 Nível 1 — Vila do Boletim

> Você chegou à primeira vila. O monitor da turma precisa de ajuda para montar o boletim, e a regra do lugar é uma só: **funções puras**.

| | |
|---|---|
| **Linguagem** | Python |
| **Arquivo que você edita** | `boletim.py` |
| **Missões** | 3 (10 XP cada) + 10 XP de bônus se limpar o nível |
| **Conceitos** | função pura, `map`, `filter`, `reduce` |

## 🧠 O conceito em 1 minuto

Uma **função pura** é como a fórmula `=MÉDIA(A1:A3)` da planilha: com os mesmos números ela dá sempre o mesmo resultado e **não muda nada em outras células**. Se a sua função altera uma lista que recebeu, ou imprime na tela no meio do cálculo, ela deixou de ser pura.

`map` transforma cada item, `filter` mantém só alguns e `reduce` resume tudo em um valor. Em Python, a *list comprehension* costuma ser o jeito mais natural de escrever os dois primeiros.

## ▶️ Como jogar

1. Abra `boletim.py` no VS Code.
2. Troque `raise NotImplementedError` pela sua implementação, uma função de cada vez.
3. No terminal, rode `python quest.py 1` (Mac/Linux: `python3 quest.py 1`).
4. Leia as mensagens, corrija e repita. Quando uma missão ficar ✅, siga para a próxima.

---

## ⚔️ Missão 1.1 — Funções puras: média e situação

**Objetivo:** escrever `media(notas)` e `situacao(media_final)`.

1. Em `media`, some as notas (`sum`) e divida pela quantidade (`len`). Arredonde com `round(x, 2)`.
2. Trate a lista vazia: devolva `0.0` (dividir por zero dá erro!).
3. Em `situacao`, use `if / elif / else` com os limites 7 e 5.
4. Rode `python quest.py 1` e veja a missão 1.1 virar ✅.

<details><summary>💡 Dica: lista vazia</summary>

Uma expressão condicional resolve: `valor_se_tem_notas if notas else 0.0`.
</details>

<details><summary>💡 Dica: situação</summary>

`"aprovado" if media_final >= 7 else ...` pode ser encadeado, ou use `if/elif/else` dentro da função.
</details>

## ⚔️ Missão 1.2 — `map`: o boletim da turma

**Objetivo:** `boletim(alunos)` devolve uma lista **nova** com `nome`, `media` e `situacao` de cada aluno.

1. Para cada aluno, monte um dicionário novo `{"nome": ..., "media": ..., "situacao": ...}`.
2. Use as funções da missão anterior. Não escreva a conta de novo!
3. **Não altere** a lista `alunos` nem os dicionários dela. Os testes conferem.

<details><summary>💡 Dica: comprehension</summary>

```python
[{"nome": a["nome"], ...} for a in alunos]
```
Você pode calcular a média uma vez e reaproveitar. Se quiser, use `map` com uma função auxiliar.
</details>

## ⚔️ Missão 1.3 — `filter` e `reduce`: aprovados e ranking

**Objetivo:** `aprovados`, `media_da_turma` e `ranking`.

1. `aprovados`: filtre os boletins com situação `"aprovado"` e devolva só os nomes.
2. `media_da_turma`: some as médias e divida pela quantidade. Lista vazia devolve `0.0`.
3. `ranking`: ordene pela média, da maior para a menor, e devolva os nomes. Empate: ordem alfabética.

<details><summary>💡 Dica: ordenar sem mexer na lista</summary>

`sorted(...)` devolve uma lista nova (já `lista.sort()` altera a original). A chave pode ser uma tupla:
`key=lambda b: (-b["media"], b["nome"])`.
</details>

<details><summary>💡 Dica: reduce</summary>

`from functools import reduce` e `reduce(lambda acc, b: acc + b["media"], boletins, 0.0)`. O `0.0` final é o valor inicial.
</details>

---

## 🏆 Level clear

Quando as três missões estiverem ✅, o nível está limpo (+10 XP). Faça o commit:

```
git add .
git commit -m "nivel 1: vila do boletim concluida"
```

Conquistas opcionais deste nível: **🔁 Zero laços** (nenhum `for`/`while`) e **🧊 Mãos limpas** (nenhum `append`, `sort()` ou atribuição que altere dados).
