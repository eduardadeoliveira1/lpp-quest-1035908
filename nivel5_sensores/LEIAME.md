# 🌋 Nível 5 — Vulcão dos Sensores

> Sensores de temperatura (IoT) monitoram o vulcão, mas alguns mandam lixo. Você vai percorrer as leituras **sem usar laços**, só com recursão, e montar o painel de alertas.

| | |
|---|---|
| **Linguagem** | Python |
| **Arquivo que você edita** | `sensores.py` |
| **Missões** | 3 (10 XP cada) + 10 XP de bônus |
| **Conceitos** | recursão e síntese de tudo que você aprendeu |

## 🧠 O conceito em 1 minuto

**Recursão** é como contar os arquivos de uma pasta: conte os da pasta e peça o mesmo para cada subpasta, até chegar numa pasta sem subpastas.

Toda função recursiva tem duas partes:

1. **Caso base**: a situação tão simples que dá para responder direto (uma lista vazia).
2. **Passo recursivo**: resolva o primeiro item e deixe o **resto** da lista para a própria função.

Leitura **válida** neste nível: um número entre `-40` e `85` (inclusive). `None` e valores fora disso são lixo.

## ▶️ Como jogar

Edite `sensores.py` e teste com `python quest.py 5` (Mac/Linux: `python3 quest.py 5`).

---

## ⚔️ Missão 5.1 — Recursão: o básico

1. `somar(valores)`: lista vazia → `0`; senão, `valores[0] + somar(valores[1:])`.
2. `contar(valores, predicado)`: quantos valores o `predicado` aceita. Lista vazia → `0`; senão, some `1` ou `0` para o primeiro e continue no resto.
3. `maximo(valores)`: lista vazia → `None`. Compare o primeiro com o máximo do resto (cuidado com o resto vazio!).

<details><summary>💡 Dica: o formato</summary>

```python
def somar(valores):
    if not valores:        # caso base
        return 0
    return valores[0] + somar(valores[1:])   # passo recursivo
```
Use esse molde nas três funções.
</details>

<details><summary>💡 Dica: maximo</summary>

Calcule `resto = maximo(valores[1:])`. Se `resto` for `None`, o primeiro é o máximo. Senão, devolva o maior dos dois.
</details>

## ⚔️ Missão 5.2 — Limpar e janelas

1. `limpar(leituras)`: lista nova só com as leituras válidas, na mesma ordem.
2. `media_movel(valores, janela)`: a média de cada grupo de `janela` valores seguidos, com 2 casas. `[1, 2, 3, 4]` com janela 2 dá `[1.5, 2.5, 3.5]`. Lista menor que a janela: `[]`.

<details><summary>💡 Dica: janelas</summary>

`valores[i:i + janela]` é a fatia que começa em `i`. Quantas janelas existem? `len(valores) - janela + 1`.
</details>

## ⚔️ Missão 5.3 — Alertas e o painel final

1. `detectar_alertas(leituras, limite)`: lista de `{"indice": i, "valor": v}` das leituras **válidas** acima do limite. O `indice` é o da lista **original**.
2. `resumo_sensores(sensores, limite)`: para cada sensor, devolva `{"validas": ..., "media": ..., "alertas": ...}`. Reaproveite `limpar`, `somar` e `detectar_alertas`.

<details><summary>💡 Dica: índices</summary>

`enumerate(leituras)` dá pares `(indice, valor)` e dentro de uma comprehension você pode filtrar com `if`.
</details>

<details><summary>💡 Dica: o painel</summary>

Uma *dict comprehension* monta o resultado: `{nome: resumir(leituras) for nome, leituras in sensores.items()}`.
</details>

---

## 🏆 Level clear

Três ✅ = nível limpo. `git add . && git commit -m "nivel 5: vulcao dos sensores concluido"`.

**Curiosidade:** o Python limita a recursão a cerca de mil chamadas. Para listas gigantes, `sum`, `map` e `reduce` são a opção prática, mas pensar de forma recursiva é um superpoder.
