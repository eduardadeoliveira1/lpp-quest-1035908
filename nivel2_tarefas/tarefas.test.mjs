import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { carregar, congelar, usar } from "../tools/carregar.mjs";

const lib = await carregar(import.meta.dirname, "tarefas");
const adicionar = usar(lib, "adicionar");
const concluir = usar(lib, "concluir");
const remover = usar(lib, "remover");
const pendentes = usar(lib, "pendentes");
const resumo = usar(lib, "resumo");
const criarHistorico = usar(lib, "criarHistorico");
const aplicar = usar(lib, "aplicar");
const desfazer = usar(lib, "desfazer");
const refazer = usar(lib, "refazer");

// Entradas CONGELADAS: se a sua função tentar alterá-las, o teste falha com um erro.
const base = () => congelar([
  { id: 1, titulo: "Estudar", concluida: false },
  { id: 2, titulo: "Treinar", concluida: true },
  { id: 5, titulo: "Revisar", concluida: false },
]);

describe("Missão 2.1 — Adicionar e concluir sem mutar", () => {
  it("adicionar põe a tarefa nova no final, com o próximo id", () => {
    const r = adicionar(base(), "Ler");
    assert.equal(r.length, 4);
    assert.deepEqual(r[3], { id: 6, titulo: "Ler", concluida: false });
    assert.deepEqual(r.slice(0, 3), base());
  });
  it("adicionar em lista vazia usa o id 1", () => {
    assert.deepEqual(adicionar(congelar([]), "Primeira"), [{ id: 1, titulo: "Primeira", concluida: false }]);
  });
  it("adicionar devolve uma lista nova", () => {
    const entrada = base();
    assert.notEqual(adicionar(entrada, "X"), entrada);
  });
  it("concluir marca só a tarefa pedida", () => {
    const r = concluir(base(), 1);
    assert.deepEqual(r[0], { id: 1, titulo: "Estudar", concluida: true });
    assert.deepEqual(r.slice(1), base().slice(1));
  });
  it("concluir com id inexistente devolve uma lista igual", () => {
    assert.deepEqual(concluir(base(), 99), base());
  });
});

describe("Missão 2.2 — Remover, filtrar e resumir", () => {
  it("remover tira a tarefa com o id", () => {
    assert.deepEqual(remover(base(), 2).map((t) => t.id), [1, 5]);
  });
  it("remover id inexistente mantém tudo", () => {
    assert.deepEqual(remover(base(), 99), base());
  });
  it("pendentes devolve só as não concluídas", () => {
    assert.deepEqual(pendentes(base()).map((t) => t.id), [1, 5]);
  });
  it("resumo conta total, concluídas e pendentes", () => {
    assert.deepEqual(resumo(base()), { total: 3, concluidas: 1, pendentes: 2 });
  });
  it("resumo de lista vazia", () => {
    assert.deepEqual(resumo(congelar([])), { total: 0, concluidas: 0, pendentes: 0 });
  });
});

describe("Missão 2.3 — Desfazer e refazer", () => {
  const add = (ts) => [...ts, { id: 99, titulo: "Nova", concluida: false }];
  const marcar = (ts) => ts.map((t) => ({ ...t, concluida: true }));

  it("criarHistorico começa sem passado e sem futuro", () => {
    assert.deepEqual(criarHistorico(base()), { passado: [], presente: base(), futuro: [] });
  });
  it("aplicar guarda o presente no passado", () => {
    const h = aplicar(congelar(criarHistorico(base())), add);
    assert.deepEqual(h.passado, [base()]);
    assert.deepEqual(h.presente, add(base()));
    assert.deepEqual(h.futuro, []);
  });
  it("desfazer volta ao estado anterior e guarda o futuro", () => {
    const h1 = congelar(aplicar(congelar(criarHistorico(base())), add));
    const h2 = desfazer(h1);
    assert.deepEqual(h2.presente, base());
    assert.deepEqual(h2.passado, []);
    assert.deepEqual(h2.futuro, [add(base())]);
  });
  it("refazer desfaz o desfazer", () => {
    const h1 = congelar(aplicar(congelar(criarHistorico(base())), add));
    assert.deepEqual(refazer(congelar(desfazer(h1))), h1);
  });
  it("desfazer sem passado e refazer sem futuro não mudam nada", () => {
    const h = congelar(criarHistorico(base()));
    assert.deepEqual(desfazer(h), h);
    assert.deepEqual(refazer(h), h);
  });
  it("uma ação nova depois de desfazer apaga o futuro", () => {
    const h1 = congelar(aplicar(congelar(criarHistorico(base())), add));
    const h3 = aplicar(congelar(desfazer(h1)), marcar);
    assert.deepEqual(h3.futuro, []);
    assert.deepEqual(h3.passado, [base()]);
  });
  it("várias ações e vários desfazer", () => {
    let h = congelar(criarHistorico(base()));
    h = congelar(aplicar(h, add));
    h = congelar(aplicar(h, marcar));
    h = congelar(desfazer(h));
    h = congelar(desfazer(h));
    assert.deepEqual(h.presente, base());
    assert.equal(h.futuro.length, 2);
  });
});
