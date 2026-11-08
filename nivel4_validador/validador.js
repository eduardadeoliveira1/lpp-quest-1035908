// NÍVEL 4 — Torre do Validador (Node: JavaScript)
//
// Você vai montar o validador de um formulário de cadastro com FÁBRICAS de regras (closures)
// e depois COMPOR essas regras. Siga as missões na ordem e rode:  python quest.py 4   (veja o LEIAME.md).
//
// Quer usar TypeScript? Apague este arquivo (validador.js) e implemente o validador.ts.
//
// Um VALIDADOR é uma função (valor) => null   (se está tudo certo)
//                              ou (valor) => "mensagem de erro".
// Uma FÁBRICA é uma função que devolve um validador, "lembrando" os parâmetros que recebeu (closure).

// ============================================================ MISSÃO 4.1 — Fábricas de regras (closures)
/** obrigatorio("Nome") devolve um validador: valor vazio, só com espaços, null ou undefined
 *  => "Nome é obrigatório"; caso contrário null. */
export function obrigatorio(campo) {
  throw new Error("Missão 4.1 ainda não implementada: obrigatorio");
}

/** minimo("Senha", 8) devolve um validador: menos de 8 caracteres => "Senha deve ter pelo menos 8 caracteres". */
export function minimo(campo, n) {
  throw new Error("Missão 4.1 ainda não implementada: minimo");
}

/** padrao("E-mail", /@/, "conter @") devolve um validador: se o texto não casa com a regex => "E-mail deve conter @".
 *  Dica: regex.test(String(valor ?? "")) */
export function padrao(campo, regex, descricao) {
  throw new Error("Missão 4.1 ainda não implementada: padrao");
}

// ============================================================ MISSÃO 4.2 — Compondo regras
/** todas(v1, v2, ...) devolve um validador que roda os validadores em ordem e devolve o PRIMEIRO erro (ou null). */
export function todas(...validadores) {
  throw new Error("Missão 4.2 ainda não implementada: todas");
}

/** acumular(v1, v2, ...) devolve um validador que devolve a LISTA de todos os erros ([] se estiver tudo certo). */
export function acumular(...validadores) {
  throw new Error("Missão 4.2 ainda não implementada: acumular");
}

// ============================================================ MISSÃO 4.3 — O formulário completo
/** regras: { campo: validador }. dados: { campo: valor }.
 *  Devolve { valido: boolean, erros: { campo: "primeira mensagem" } } só com os campos que falharam.
 *  Dica: Object.entries, map, filter, Object.fromEntries. Não altere regras nem dados! */
export function validarFormulario(regras, dados) {
  throw new Error("Missão 4.3 ainda não implementada: validarFormulario");
}
