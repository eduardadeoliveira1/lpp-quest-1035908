# 🏰 Nível 6 — Castelo da Playlist (O CHEFÃO)

> O castelo é sua última parada. O rei só abre os portões para quem sabe filtrar, agrupar, ordenar e somar **sem alterar nenhuma lista**.

| | |
|---|---|
| **Linguagem** | Node: JavaScript (`playlist.js`) ou TypeScript (`playlist.ts`) |
| **Missões** | 3 (10 XP cada) + 10 XP de bônus |
| **Conceitos** | `filter`, `reduce`, agrupar e ordenar sem mutar |

## 🧠 O conceito em 1 minuto

Uma playlist é uma lista de músicas `{ titulo, artista, genero, duracao (segundos), plays }`. Relatórios como "quantas músicas por gênero?" ou "quem tem mais plays?" são o dia a dia de qualquer app de streaming.

Cuidado com um clássico: o `sort()` do JavaScript **altera o array original**! Em estilo funcional você ordena uma **cópia**: `[...lista].sort(...)`.

## ▶️ Como jogar

- **JavaScript (padrão):** edite `playlist.js`.
- **TypeScript:** `python quest.py escolher ts` e edite `playlist.ts` (Node 22.18+).
- Teste com `python quest.py 6` (Mac/Linux: `python3 quest.py 6`).

---

## ⚔️ Missão 6.1 — Filtrar e somar

1. `porGenero(musicas, genero)`: `filter`.
2. `duracaoTotal(musicas)`: soma dos segundos com `reduce`.
3. `formatarDuracao(segundos)`: `"m:ss"`. `65` → `"1:05"`, `3725` → `"62:05"`.

<details><summary>💡 Dica: formatar</summary>

Minutos: `Math.floor(segundos / 60)`. Segundos: `segundos % 60`, com zero à esquerda: `String(s).padStart(2, "0")`.
</details>

## ⚔️ Missão 6.2 — Agrupar

1. `agruparPor(lista, funcaoChave)`: devolve `{ chave: [itens...] }`, mantendo a ordem. Funciona com **qualquer** lista e qualquer função de chave!
2. `contarPor(lista, funcaoChave)`: `{ chave: quantidade }`. Reaproveite `agruparPor`.
3. `playsPorArtista(musicas)`: `{ artista: soma dos plays }`.

<details><summary>💡 Dica: reduce com objeto novo</summary>

```js
lista.reduce((acc, item) => {
  const k = funcaoChave(item);
  return { ...acc, [k]: [...(acc[k] ?? []), item] };
}, {});
```
Entenda o `[k]` (chave calculada) e o `?? []` (começa com lista vazia quando a chave ainda não existe).
</details>

## ⚔️ Missão 6.3 — Ordenar e o chefão

1. `ordenarPor(lista, funcaoChave, decrescente = false)`: devolve uma lista **nova**. Empate: mantém a ordem original (o `sort` do JavaScript já é estável).
2. `maisTocadas(musicas, n)`: títulos das `n` músicas com mais plays. Empate: ordem alfabética do título.
3. **O chefão:** `relatorioPlaylist(musicas)` devolve `{ totalMusicas, duracaoTotal: "m:ss", generos: {...}, topArtista, top3 }`. Playlist vazia: `topArtista: null`.

<details><summary>💡 Dica: comparador</summary>

O comparador de `sort` devolve um número negativo, zero ou positivo. Para texto, `a < b ? -1 : a > b ? 1 : 0`. Para decrescente, inverta o sinal.
</details>

<details><summary>💡 Dica: o chefão</summary>

Quase tudo já existe: `duracaoTotal`, `formatarDuracao`, `contarPor`, `playsPorArtista`, `maisTocadas`. O relatório só **junta** essas peças. Para o `topArtista`, ordene os pares de `Object.entries(playsPorArtista(...))`.
</details>

---

## 👑 Level clear

Três ✅ = nível limpo, e o **castelo se acende no mapa**. Faça o último commit e o push. 🎉

`git add . && git commit -m "nivel 6: castelo da playlist concluido"`
