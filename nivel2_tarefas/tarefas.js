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
    const maiorId = Math.max(0, ...tarefas.map((t) => t.id));

    const novaTarefa = {
        id: maiorId + 1,
        titulo: titulo,
        concluida: false
    };

    return [...tarefas, novaTarefa];
}

/** Devolve uma lista NOVA em que a tarefa com esse id está concluída. Id que não existe: lista igual. */
export function concluir(tarefas, id) {
    return tarefas.map((t) =>
        t.id === id
            ? { ...t, concluida: true }
            : t
    );
}

// ============================================================ MISSÃO 2.2 — Remover, filtrar e resumir
/** Lista NOVA sem a tarefa com esse id. */
export function remover(tarefas, id) {
    return tarefas.filter((t) => t.id !== id);
}

/** Só as tarefas que ainda não foram concluídas. */
export function pendentes(tarefas) {
    return tarefas.filter((t) => !t.concluida);
}

/** { total, concluidas, pendentes } — dica: reduce. */
export function resumo(tarefas) {
    return tarefas.reduce((acc, t) => ({
        total: acc.total + 1,
        concluidas: acc.concluidas + (t.concluida ? 1 : 0),
        pendentes: acc.pendentes + (!t.concluida ? 1 : 0)
    }), {
        total: 0,
        concluidas: 0,
        pendentes: 0
    });
}
// ============================================================ MISSÃO 2.3 — Desfazer e refazer
// Um histórico é { passado: [...estados], presente: estado, futuro: [...estados] }.

/** { passado: [], presente: estadoInicial, futuro: [] } */
export function criarHistorico(estadoInicial) {
    return {
        passado: [],
        presente: estadoInicial,
        futuro: []
    };
}

/** Novo histórico: o presente vai para o fim do passado, o novo presente é funcao(presente) e o futuro é esvaziado. */
export function aplicar(historico, funcao) {
    return {
        passado: [...historico.passado, historico.presente],
        presente: funcao(historico.presente),
        futuro: []
    };
}

/** Volta um passo: o último do passado vira presente e o presente antigo vai para o início do futuro.
 *  Sem passado: devolve o histórico como está. */
export function desfazer(historico) {
    if (historico.passado.length === 0) {
        return historico;
    }

    return {
        passado: historico.passado.slice(0, -1),
        presente: historico.passado.at(-1),
        futuro: [historico.presente, ...historico.futuro]
    };
}

/** O contrário de desfazer. Sem futuro: devolve o histórico como está. */
export function refazer(historico) {
    if (historico.futuro.length === 0) {
        return historico;
    }

    return {
        passado: [...historico.passado, historico.presente],
        presente: historico.futuro[0],
        futuro: historico.futuro.slice(1)
    };
}
