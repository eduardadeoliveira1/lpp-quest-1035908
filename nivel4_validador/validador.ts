// NÍVEL 4 — Torre do Validador (Node: TypeScript)
//
// Mesma missão do validador.js, agora com tipos. Para usar TypeScript, APAGUE o validador.js
// (se os dois existirem, o jogo usa o .js). Precisa de Node 22.18 ou mais novo.
// Rode:  python quest.py 4   (veja o LEIAME.md).

/** (valor) => null se está tudo certo, ou a mensagem de erro. */
export type Validador = (valor: unknown) => string | null;

// ============================================================ MISSÃO 4.1 — Fábricas de regras (closures)
/** obrigatorio("Nome"): vazio, só espaços, null ou undefined => "Nome é obrigatório"; senão null. */
export function obrigatorio(campo: string): Validador {
  throw new Error("Missão 4.1 ainda não implementada: obrigatorio");
}

/** minimo("Senha", 8): menos de 8 caracteres => "Senha deve ter pelo menos 8 caracteres". */
export function minimo(campo: string, n: number): Validador {
  throw new Error("Missão 4.1 ainda não implementada: minimo");
}

/** padrao("E-mail", /@/, "conter @"): se não casa com a regex => "E-mail deve conter @". */
export function padrao(campo: string, regex: RegExp, descricao: string): Validador {
  throw new Error("Missão 4.1 ainda não implementada: padrao");
}

// ============================================================ MISSÃO 4.2 — Compondo regras
/** Roda os validadores em ordem e devolve o PRIMEIRO erro (ou null). */
export function todas(...validadores: Validador[]): Validador {
  throw new Error("Missão 4.2 ainda não implementada: todas");
}

/** Devolve a LISTA de todos os erros ([] se estiver tudo certo). */
export function acumular(...validadores: Validador[]): (valor: unknown) => string[] {
  throw new Error("Missão 4.2 ainda não implementada: acumular");
}

// ============================================================ MISSÃO 4.3 — O formulário completo
/** Devolve { valido, erros } com a primeira mensagem de cada campo que falhou. Não altere regras nem dados! */
export function validarFormulario(
  regras: Record<string, Validador>,
  dados: Record<string, unknown>,
): { valido: boolean; erros: Record<string, string> } {
  throw new Error("Missão 4.3 ainda não implementada: validarFormulario");
}
