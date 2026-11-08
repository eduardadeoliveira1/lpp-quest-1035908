import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { carregar, congelar, usar } from "../tools/carregar.mjs";

const lib = await carregar(import.meta.dirname, "playlist");
const porGenero = usar(lib, "porGenero");
const duracaoTotal = usar(lib, "duracaoTotal");
const formatarDuracao = usar(lib, "formatarDuracao");
const agruparPor = usar(lib, "agruparPor");
const contarPor = usar(lib, "contarPor");
const playsPorArtista = usar(lib, "playsPorArtista");
const ordenarPor = usar(lib, "ordenarPor");
const maisTocadas = usar(lib, "maisTocadas");
const relatorioPlaylist = usar(lib, "relatorioPlaylist");

const musicas = () => congelar([
  { titulo: "Aurora", artista: "Lia", genero: "pop", duracao: 200, plays: 500 },
  { titulo: "Brisa", artista: "Lia", genero: "pop", duracao: 185, plays: 300 },
  { titulo: "Concreto", artista: "Max", genero: "rock", duracao: 240, plays: 900 },
  { titulo: "Delta", artista: "Max", genero: "rock", duracao: 260, plays: 900 },
  { titulo: "Eclipse", artista: "Nina", genero: "jazz", duracao: 310, plays: 150 },
  { titulo: "Faísca", artista: "Zeca", genero: "pop", duracao: 175, plays: 700 },
]);
const titulos = (lista) => lista.map((m) => m.titulo);

describe("Missão 6.1 — Filtrar e somar", () => {
  it("porGenero filtra pelo gênero", () => {
    assert.deepEqual(titulos(porGenero(musicas(), "pop")), ["Aurora", "Brisa", "Faísca"]);
  });
  it("porGenero de um gênero que não existe", () => {
    assert.deepEqual(porGenero(musicas(), "funk"), []);
  });
  it("duracaoTotal soma os segundos", () => {
    assert.equal(duracaoTotal(musicas()), 1370);
    assert.equal(duracaoTotal(congelar([])), 0);
  });
  it("formatarDuracao usa m:ss", () => {
    assert.equal(formatarDuracao(65), "1:05");
    assert.equal(formatarDuracao(0), "0:00");
    assert.equal(formatarDuracao(1370), "22:50");
    assert.equal(formatarDuracao(3725), "62:05");
  });
});

describe("Missão 6.2 — Agrupar", () => {
  it("agruparPor agrupa e mantém a ordem", () => {
    const grupos = agruparPor(musicas(), (m) => m.genero);
    assert.deepEqual(Object.keys(grupos).sort(), ["jazz", "pop", "rock"]);
    assert.deepEqual(titulos(grupos.pop), ["Aurora", "Brisa", "Faísca"]);
    assert.deepEqual(titulos(grupos.rock), ["Concreto", "Delta"]);
  });
  it("agruparPor funciona com qualquer função de chave", () => {
    const grupos = agruparPor(congelar([1, 2, 3, 4, 5]), (n) => (n % 2 === 0 ? "par" : "impar"));
    assert.deepEqual(grupos, { impar: [1, 3, 5], par: [2, 4] });
  });
  it("agruparPor em lista vazia", () => {
    assert.deepEqual(agruparPor(congelar([]), (x) => x), {});
  });
  it("contarPor conta os itens de cada grupo", () => {
    assert.deepEqual(contarPor(musicas(), (m) => m.genero), { pop: 3, rock: 2, jazz: 1 });
  });
  it("playsPorArtista soma os plays", () => {
    assert.deepEqual(playsPorArtista(musicas()), { Lia: 800, Max: 1800, Nina: 150, Zeca: 700 });
  });
});

describe("Missão 6.3 — Ordenar e o chefão", () => {
  it("ordenarPor crescente", () => {
    assert.deepEqual(titulos(ordenarPor(musicas(), (m) => m.duracao)),
      ["Faísca", "Brisa", "Aurora", "Concreto", "Delta", "Eclipse"]);
  });
  it("ordenarPor decrescente mantém a ordem original nos empates", () => {
    assert.deepEqual(titulos(ordenarPor(musicas(), (m) => m.plays, true)),
      ["Concreto", "Delta", "Faísca", "Aurora", "Brisa", "Eclipse"]);
  });
  it("ordenarPor funciona com texto e não altera a lista original", () => {
    const entrada = musicas();
    assert.deepEqual(titulos(ordenarPor(entrada, (m) => m.artista, true)),
      ["Faísca", "Eclipse", "Concreto", "Delta", "Aurora", "Brisa"]);
    assert.deepEqual(titulos(entrada), ["Aurora", "Brisa", "Concreto", "Delta", "Eclipse", "Faísca"]);
  });
  it("maisTocadas devolve os títulos (empate: ordem alfabética)", () => {
    assert.deepEqual(maisTocadas(musicas(), 3), ["Concreto", "Delta", "Faísca"]);
    assert.deepEqual(maisTocadas(musicas(), 1), ["Concreto"]);
  });
  it("O CHEFÃO: relatorioPlaylist", () => {
    assert.deepEqual(relatorioPlaylist(musicas()), {
      totalMusicas: 6,
      duracaoTotal: "22:50",
      generos: { pop: 3, rock: 2, jazz: 1 },
      topArtista: "Max",
      top3: ["Concreto", "Delta", "Faísca"],
    });
  });
  it("O CHEFÃO: playlist vazia", () => {
    assert.deepEqual(relatorioPlaylist(congelar([])), {
      totalMusicas: 0,
      duracaoTotal: "0:00",
      generos: {},
      topArtista: null,
      top3: [],
    });
  });
});
