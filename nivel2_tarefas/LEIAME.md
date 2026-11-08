# 🌲 Nível 2 — Floresta das Tarefas

> Na floresta, cada tarefa é uma árvore: **ninguém pode derrubar a que já existe**. Para "mudar" a floresta, você planta uma nova.

| | |
|---|---|
| **Linguagem** | Node: JavaScript (`tarefas.js`) ou TypeScript (`tarefas.ts`) |
| **Missões** | 3 (10 XP cada) + 10 XP de bônus |
| **Conceito** | imutabilidade (e um "desfazer" no estilo do Redux) |

## 🧠 O conceito em 1 minuto

**Imutabilidade** é tratar dados como o histórico do Git: você não apaga o commit anterior, cria um novo. Em código, isso significa não usar `push`, `splice`, `sort` ou `obj.campo = ...` no que recebeu, e sim **devolver uma cópia com a mudança**.

Nos testes deste nível as entradas vêm **congeladas** (`Object.freeze`): se a sua função tentar alterá-las, o teste mostra o erro na hora. É o jeito do jogo de te avisar. 😉

## ▶️ Como jogar

- **JavaScript (padrão):** edite `tarefas.js`.
- **TypeScript:** rode `python quest.py escolher ts` (apaga os `.js` iniciais) e edite `tarefas.ts`. Precisa de Node 22.18 ou mais novo.
- Teste com `python quest.py 2` (Mac/Linux: `python3 quest.py 2`).

Uma tarefa é `{ id: 1, titulo: "Estudar", concluida: false }`.

---

## ⚔️ Missão 2.1 — Adicionar e concluir sem mutar

1. `adicionar(tarefas, titulo)`: o novo `id` é o **maior id + 1** (lista vazia: `1`). Devolva `[...tarefas, novaTarefa]`.
2. `concluir(tarefas, id)`: use `map` e, na tarefa certa, devolva `{ ...t, concluida: true }`. As outras ficam como estão.
3. Id que não existe: a lista continua igual (e isso sai de graça com `map`).

<details><summary>💡 Dica: maior id</summary>

`Math.max(0, ...tarefas.map((t) => t.id))` já resolve a lista vazia.
</details>

## ⚔️ Missão 2.2 — Remover, filtrar e resumir

1. `remover`: `filter` com o id diferente.
2. `pendentes`: `filter` nas tarefas que **não** estão concluídas.
3. `resumo`: devolva `{ total, concluidas, pendentes }`. Use `reduce` com um objeto novo a cada passo.

<details><summary>💡 Dica: reduce</summary>

O valor inicial é `{ total: 0, concluidas: 0, pendentes: 0 }`. Em cada passo devolva um objeto **novo** com os contadores atualizados.
</details>

## ⚔️ Missão 2.3 — Desfazer e refazer

Um histórico é `{ passado: [...], presente: estado, futuro: [...] }`, como o "Ctrl+Z / Ctrl+Y" de um editor.

1. `criarHistorico(estado)`: passado e futuro vazios.
2. `aplicar(historico, funcao)`: o presente vai para o **fim** do passado, o novo presente é `funcao(presente)` e o futuro **zera**.
3. `desfazer`: o último do passado vira presente; o presente antigo vai para o **início** do futuro. Sem passado, devolva o histórico como está.
4. `refazer`: o contrário. Sem futuro, devolva como está.

<details><summary>💡 Dica: pegar o último e o resto</summary>

`historico.passado.at(-1)` é o último; `historico.passado.slice(0, -1)` é tudo menos o último.
</details>

---

## 🏆 Level clear

Três missões ✅ = nível limpo. Depois: `git add . && git commit -m "nivel 2: floresta das tarefas concluida"`.

Conquistas opcionais: **🔁 Zero laços** e **🧊 Mãos limpas** (sem `push`/`splice`/atribuição em objetos).
