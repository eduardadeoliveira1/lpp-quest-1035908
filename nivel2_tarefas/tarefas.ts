// NÍVEL 2 — Floresta das Tarefas (Node: TypeScript)
//
// Mesma missão do tarefas.js, agora com tipos. Para usar TypeScript, APAGUE o tarefas.js
// (se os dois existirem, o jogo usa o .js). Precisa de Node 22.18 ou mais novo.
// Rode:  python quest.py 2   (veja o LEIAME.md).
//
// Dica geral: use map, filter, reduce e o operador de espalhamento ( ...x ). Nada de push, splice, sort no original!

export type Tarefa = { id: number; titulo: string; concluida: boolean };
export type Historico<T> = { passado: T[]; presente: T; futuro: T[] };

// ============================================================ MISSÃO 2.1 — Adicionar e concluir sem mutar
/** Devolve uma lista NOVA com a tarefa nova no final. O id é o maior id existente + 1 (lista vazia: 1). */
export function adicionar(tarefas: Tarefa[], titulo: string): Tarefa[] {
  throw new Error("Missão 2.1 ainda não implementada: adicionar");
}

/** Devolve uma lista NOVA em que a tarefa com esse id está concluída. Id que não existe: lista igual. */
export function concluir(tarefas: Tarefa[], id: number): Tarefa[] {
  throw new Error("Missão 2.1 ainda não implementada: concluir");
}

// ============================================================ MISSÃO 2.2 — Remover, filtrar e resumir
/** Lista NOVA sem a tarefa com esse id. */
export function remover(tarefas: Tarefa[], id: number): Tarefa[] {
  throw new Error("Missão 2.2 ainda não implementada: remover");
}

/** Só as tarefas que ainda não foram concluídas. */
export function pendentes(tarefas: Tarefa[]): Tarefa[] {
  throw new Error("Missão 2.2 ainda não implementada: pendentes");
}

/** { total, concluidas, pendentes } — dica: reduce. */
export function resumo(tarefas: Tarefa[]): { total: number; concluidas: number; pendentes: number } {
  throw new Error("Missão 2.2 ainda não implementada: resumo");
}

// ============================================================ MISSÃO 2.3 — Desfazer e refazer
/** { passado: [], presente: estadoInicial, futuro: [] } */
export function criarHistorico<T>(estadoInicial: T): Historico<T> {
  throw new Error("Missão 2.3 ainda não implementada: criarHistorico");
}

/** Novo histórico: o presente vai para o fim do passado, o novo presente é funcao(presente) e o futuro é esvaziado. */
export function aplicar<T>(historico: Historico<T>, funcao: (estado: T) => T): Historico<T> {
  throw new Error("Missão 2.3 ainda não implementada: aplicar");
}

/** Volta um passo: o último do passado vira presente e o presente antigo vai para o início do futuro.
 *  Sem passado: devolve o histórico como está. */
export function desfazer<T>(historico: Historico<T>): Historico<T> {
  throw new Error("Missão 2.3 ainda não implementada: desfazer");
}

/** O contrário de desfazer. Sem futuro: devolve o histórico como está. */
export function refazer<T>(historico: Historico<T>): Historico<T> {
  throw new Error("Missão 2.3 ainda não implementada: refazer");
}
