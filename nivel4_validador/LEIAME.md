# 🏔️ Nível 4 — Torre do Validador

> No topo da torre mora o formulário de cadastro. Para chegar lá, você forja **regras que lembram de si mesmas** e depois as junta como peças de Lego.

| | |
|---|---|
| **Linguagem** | Node: JavaScript (`validador.js`) ou TypeScript (`validador.ts`) |
| **Missões** | 3 (10 XP cada) + 10 XP de bônus |
| **Conceitos** | closures, funções de ordem superior e composição |

## 🧠 O conceito em 1 minuto

Pense numa loja que gera **cupons de desconto**: ao criar o cupom de 10%, o "10%" fica guardado dentro dele. Cada cupom lembra o seu percentual, sem variável global.

Uma **closure** é isso: uma função que "leva consigo" valores do lugar onde nasceu. Aqui, `minimo("Senha", 8)` devolve uma **nova função** que lembra o nome do campo e o tamanho mínimo. Depois você **compõe** essas funções para validar o formulário inteiro.

Um **validador** é uma função `(valor) => null` (tudo certo) ou `(valor) => "mensagem de erro"`.

## ▶️ Como jogar

- **JavaScript (padrão):** edite `validador.js`.
- **TypeScript:** `python quest.py escolher ts` e edite `validador.ts` (Node 22.18+).
- Teste com `python quest.py 4` (Mac/Linux: `python3 quest.py 4`).

---

## ⚔️ Missão 4.1 — Fábricas de regras (closures)

1. `obrigatorio(campo)`: devolve um validador. Vazio, só espaços, `null` ou `undefined` dão `"<campo> é obrigatório"`.
2. `minimo(campo, n)`: devolve um validador. Menos de `n` caracteres dão `"<campo> deve ter pelo menos <n> caracteres"`.
3. `padrao(campo, regex, descricao)`: se o texto não casa com a regex, `"<campo> deve <descricao>"`.

<details><summary>💡 Dica: a forma de uma fábrica</summary>

```js
export const minimo = (campo, n) => (valor) => /* devolve null ou a mensagem */;
```
A função de dentro enxerga `campo` e `n` mesmo depois que `minimo` terminou. Isso é a closure.
</details>

<details><summary>💡 Dica: texto ausente</summary>

`String(valor ?? "")` transforma `null`/`undefined` em texto vazio, e o resto do código fica simples.
</details>

## ⚔️ Missão 4.2 — Compondo regras

1. `todas(...validadores)`: devolve um validador que roda os validadores **em ordem** e devolve o **primeiro** erro (ou `null`).
2. `acumular(...validadores)`: devolve um validador que devolve a **lista de todos** os erros (`[]` se estiver tudo certo).

<details><summary>💡 Dica</summary>

Os parâmetros `...validadores` formam uma lista. Rode cada um com `map` e use `find` (primeiro erro) ou `filter` (todos os erros).
</details>

## ⚔️ Missão 4.3 — O formulário completo

`validarFormulario(regras, dados)`: `regras` é `{ campo: validador }` e `dados` é `{ campo: valor }`. Devolva `{ valido, erros }`, onde `erros` tem só os campos que falharam, cada um com a primeira mensagem.

1. `Object.entries(regras)` dá os pares `[campo, validador]`.
2. Rode cada validador com `dados[campo]`.
3. Fique só com os erros (`filter`) e monte o objeto com `Object.fromEntries`.
4. `valido` é verdadeiro quando não há nenhum erro.

<details><summary>💡 Dica</summary>

Campo ausente em `dados` vira `undefined`, e o seu `obrigatorio` já trata isso. Não altere `regras` nem `dados`!
</details>

---

## 🏆 Level clear

Três ✅ = nível limpo. `git add . && git commit -m "nivel 4: torre do validador concluida"`.
