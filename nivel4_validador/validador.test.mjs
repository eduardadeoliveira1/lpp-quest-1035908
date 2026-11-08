import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { carregar, congelar, usar } from "../tools/carregar.mjs";

const lib = await carregar(import.meta.dirname, "validador");
const obrigatorio = usar(lib, "obrigatorio");
const minimo = usar(lib, "minimo");
const padrao = usar(lib, "padrao");
const todas = usar(lib, "todas");
const acumular = usar(lib, "acumular");
const validarFormulario = usar(lib, "validarFormulario");

describe("Missão 4.1 — Fábricas de regras (closures)", () => {
  it("obrigatorio rejeita vazio, espaços, null e undefined", () => {
    const nome = obrigatorio("Nome");
    assert.equal(nome(""), "Nome é obrigatório");
    assert.equal(nome("   "), "Nome é obrigatório");
    assert.equal(nome(null), "Nome é obrigatório");
    assert.equal(nome(undefined), "Nome é obrigatório");
  });
  it("obrigatorio aceita texto", () => {
    assert.equal(obrigatorio("Nome")("Ana"), null);
  });
  it("minimo confere o tamanho", () => {
    const senha = minimo("Senha", 8);
    assert.equal(senha("1234"), "Senha deve ter pelo menos 8 caracteres");
    assert.equal(senha("12345678"), null);
  });
  it("minimo lembra os próprios parâmetros (cada validador é independente)", () => {
    const a = minimo("A", 2);
    const b = minimo("B", 5);
    assert.equal(a("abc"), null);
    assert.equal(b("abc"), "B deve ter pelo menos 5 caracteres");
    assert.equal(a("x"), "A deve ter pelo menos 2 caracteres");
  });
  it("padrao usa a regex e a descrição", () => {
    const email = padrao("E-mail", /@/, "conter @");
    assert.equal(email("abc"), "E-mail deve conter @");
    assert.equal(email("a@b"), null);
  });
});

describe("Missão 4.2 — Compondo regras", () => {
  const regra = () => [obrigatorio("A"), minimo("A", 3), padrao("A", /\d/, "conter um número")];
  it("todas devolve o primeiro erro", () => {
    const v = todas(...regra());
    assert.equal(v(""), "A é obrigatório");
    assert.equal(v("ab"), "A deve ter pelo menos 3 caracteres");
    assert.equal(v("abc"), "A deve conter um número");
  });
  it("todas devolve null quando tudo passa", () => {
    assert.equal(todas(...regra())("abc1"), null);
  });
  it("todas sem validadores aceita tudo", () => {
    assert.equal(todas()("qualquer coisa"), null);
  });
  it("acumular devolve todos os erros", () => {
    assert.deepEqual(acumular(...regra())(""), [
      "A é obrigatório",
      "A deve ter pelo menos 3 caracteres",
      "A deve conter um número",
    ]);
  });
  it("acumular devolve lista vazia quando tudo passa", () => {
    assert.deepEqual(acumular(...regra())("abc1"), []);
  });
});

describe("Missão 4.3 — O formulário completo", () => {
  const regras = () => ({
    nome: todas(obrigatorio("Nome"), minimo("Nome", 3)),
    email: padrao("E-mail", /^[^@\s]+@[^@\s]+\.[^@\s]+$/, "ser um e-mail válido"),
    senha: todas(obrigatorio("Senha"), minimo("Senha", 8), padrao("Senha", /\d/, "conter um número")),
  });
  it("formulário válido", () => {
    const dados = congelar({ nome: "Ana Lima", email: "ana@exemplo.com", senha: "segredo123" });
    assert.deepEqual(validarFormulario(regras(), dados), { valido: true, erros: {} });
  });
  it("formulário com vários erros", () => {
    const dados = congelar({ nome: "A", email: "ana", senha: "abc" });
    assert.deepEqual(validarFormulario(regras(), dados), {
      valido: false,
      erros: {
        nome: "Nome deve ter pelo menos 3 caracteres",
        email: "E-mail deve ser um e-mail válido",
        senha: "Senha deve ter pelo menos 8 caracteres",
      },
    });
  });
  it("campo ausente conta como vazio", () => {
    const dados = congelar({ nome: "Ana Lima", email: "ana@exemplo.com" });
    assert.deepEqual(validarFormulario(regras(), dados), {
      valido: false,
      erros: { senha: "Senha é obrigatório" },
    });
  });
  it("campos que não têm regra são ignorados", () => {
    const dados = congelar({ nome: "Ana Lima", email: "ana@exemplo.com", senha: "segredo123", extra: "x" });
    assert.equal(validarFormulario(regras(), dados).valido, true);
  });
  it("não altera os dados recebidos", () => {
    const dados = congelar({ nome: "", email: "", senha: "" });
    assert.doesNotThrow(() => validarFormulario(regras(), dados));
  });
});
