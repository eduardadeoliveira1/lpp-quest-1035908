// NÍVEL 2 — Floresta das Tarefas (Node: JavaScript)
//
// Você vai construir o "estado" de um app de tarefas SEM nunca alterar o que recebe,
// no estilo do Redux. Siga as missões na ordem e rode:  python quest.py 2   (veja o LEIAME.md).
//
// Quer usar TypeScript? Apague este arquivo (tarefas.js) e implemente o tarefas.ts.
//
// Uma tarefa é { id: 1, titulo: "Estudar", concluida: false }.
// Dica geral: use map, filter, reduce e o operador de espalhamento ( ...x ). Nada de push, splice, sort no original!

// ============================================================ MISSÃO 2.1 — Adicionar e concluir sem mutar
/** Devolve uma lista NOVA com a tarefa nova no final. O id é o maior id existente + 1 (lista vazia: 1). */
export function adicionar(tarefas, titulo) {
  throw new Error("Missão 2.1 ainda não implementada: adicionar");
}

/** Devolve uma lista NOVA em que a tarefa com esse id está concluída. Id que não existe: lista igual. */
export function concluir(tarefas, id) {
  throw new Error("Missão 2.1 ainda não implementada: concluir");
}

// ============================================================ MISSÃO 2.2 — Remover, filtrar e resumir
/** Lista NOVA sem a tarefa com esse id. */
export function remover(tarefas, id) {
  throw new Error("Missão 2.2 ainda não implementada: remover");
}

/** Só as tarefas que ainda não foram concluídas. */
export function pendentes(tarefas) {
  throw new Error("Missão 2.2 ainda não implementada: pendentes");
}

/** { total, concluidas, pendentes } — dica: reduce. */
export function resumo(tarefas) {
  throw new Error("Missão 2.2 ainda não implementada: resumo");
}

// ============================================================ MISSÃO 2.3 — Desfazer e refazer
// Um histórico é { passado: [...estados], presente: estado, futuro: [...estados] }.

/** { passado: [], presente: estadoInicial, futuro: [] } */
export function criarHistorico(estadoInicial) {
  throw new Error("Missão 2.3 ainda não implementada: criarHistorico");
}

/** Novo histórico: o presente vai para o fim do passado, o novo presente é funcao(presente) e o futuro é esvaziado. */
export function aplicar(historico, funcao) {
  throw new Error("Missão 2.3 ainda não implementada: aplicar");
}

/** Volta um passo: o último do passado vira presente e o presente antigo vai para o início do futuro.
 *  Sem passado: devolve o histórico como está. */
export function desfazer(historico) {
  throw new Error("Missão 2.3 ainda não implementada: desfazer");
}

/** O contrário de desfazer. Sem futuro: devolve o histórico como está. */
export function refazer(historico) {
  throw new Error("Missão 2.3 ainda não implementada: refazer");
}
