// NÍVEL 6 — Castelo da Playlist (Node: JavaScript) — O CHEFÃO!
//
// Última fase: você vai juntar tudo (filter, map, reduce, agrupar e ordenar) para montar o relatório
// de uma playlist de músicas. Siga as missões na ordem e rode:  python quest.py 6   (veja o LEIAME.md).
//
// Quer usar TypeScript? Apague este arquivo (playlist.js) e implemente o playlist.ts.
//
// Uma música é { titulo: "Aurora", artista: "Lia", genero: "pop", duracao: 200 (segundos), plays: 500 }.
// Lembre: nada de alterar a lista recebida! sort() altera o array, então ordene uma CÓPIA: [...lista].sort(...)

// ============================================================ MISSÃO 6.1 — Filtrar e somar
/** Só as músicas desse gênero. */
export function porGenero(musicas, genero) {
  throw new Error("Missão 6.1 ainda não implementada: porGenero");
}

/** Soma das durações (em segundos). */
export function duracaoTotal(musicas) {
  throw new Error("Missão 6.1 ainda não implementada: duracaoTotal");
}

/** Segundos => "m:ss".   65 => "1:05"   0 => "0:00"   3725 => "62:05"   Dica: Math.floor e padStart(2, "0"). */
export function formatarDuracao(segundos) {
  throw new Error("Missão 6.1 ainda não implementada: formatarDuracao");
}

// ============================================================ MISSÃO 6.2 — Agrupar
/** Agrupa os itens pelo valor que funcaoChave devolve: { chave: [itens...] }, mantendo a ordem original.
 *  Dica: reduce com um objeto NOVO a cada passo:  { ...acc, [k]: [...(acc[k] ?? []), item] } */
export function agruparPor(lista, funcaoChave) {
  throw new Error("Missão 6.2 ainda não implementada: agruparPor");
}

/** { chave: quantidade de itens }. Dica: use agruparPor. */
export function contarPor(lista, funcaoChave) {
  throw new Error("Missão 6.2 ainda não implementada: contarPor");
}

/** { artista: soma dos plays de todas as músicas dele(a) }. */
export function playsPorArtista(musicas) {
  throw new Error("Missão 6.2 ainda não implementada: playsPorArtista");
}

// ============================================================ MISSÃO 6.3 — Ordenar e o chefão
/** Lista NOVA ordenada pelo valor de funcaoChave (crescente; decrescente se o 3º argumento for true).
 *  Empate: mantém a ordem original. Dica: [...lista].sort((a, b) => ...) */
export function ordenarPor(lista, funcaoChave, decrescente = false) {
  throw new Error("Missão 6.3 ainda não implementada: ordenarPor");
}

/** Títulos das n músicas mais tocadas, da mais para a menos tocada. Empate: ordem alfabética do título. */
export function maisTocadas(musicas, n) {
  throw new Error("Missão 6.3 ainda não implementada: maisTocadas");
}

/** O CHEFÃO:  { totalMusicas, duracaoTotal: "m:ss", generos: { genero: quantidade },
 *               topArtista: nome do artista com mais plays no total (empate: ordem alfabética; null se vazio),
 *               top3: títulos das 3 mais tocadas }  */
export function relatorioPlaylist(musicas) {
  throw new Error("Missão 6.3 ainda não implementada: relatorioPlaylist");
}
