// NÍVEL 6 — Castelo da Playlist (Node: TypeScript) — O CHEFÃO!
//
// Mesma missão do playlist.js, agora com tipos. Para usar TypeScript, APAGUE o playlist.js
// (se os dois existirem, o jogo usa o .js). Precisa de Node 22.18 ou mais novo.
// Rode:  python quest.py 6   (veja o LEIAME.md).

export type Musica = { titulo: string; artista: string; genero: string; duracao: number; plays: number };

// ============================================================ MISSÃO 6.1 — Filtrar e somar
/** Só as músicas desse gênero. */
export function porGenero(musicas: Musica[], genero: string): Musica[] {
  throw new Error("Missão 6.1 ainda não implementada: porGenero");
}

/** Soma das durações (em segundos). */
export function duracaoTotal(musicas: Musica[]): number {
  throw new Error("Missão 6.1 ainda não implementada: duracaoTotal");
}

/** Segundos => "m:ss".   65 => "1:05"   0 => "0:00"   3725 => "62:05" */
export function formatarDuracao(segundos: number): string {
  throw new Error("Missão 6.1 ainda não implementada: formatarDuracao");
}

// ============================================================ MISSÃO 6.2 — Agrupar
/** Agrupa os itens pelo valor que funcaoChave devolve: { chave: [itens...] }, mantendo a ordem original. */
export function agruparPor<T>(lista: T[], funcaoChave: (item: T) => string): Record<string, T[]> {
  throw new Error("Missão 6.2 ainda não implementada: agruparPor");
}

/** { chave: quantidade de itens }. */
export function contarPor<T>(lista: T[], funcaoChave: (item: T) => string): Record<string, number> {
  throw new Error("Missão 6.2 ainda não implementada: contarPor");
}

/** { artista: soma dos plays de todas as músicas dele(a) }. */
export function playsPorArtista(musicas: Musica[]): Record<string, number> {
  throw new Error("Missão 6.2 ainda não implementada: playsPorArtista");
}

// ============================================================ MISSÃO 6.3 — Ordenar e o chefão
/** Lista NOVA ordenada pelo valor de funcaoChave (crescente; decrescente se o 3º argumento for true). Empate: ordem original. */
export function ordenarPor<T>(lista: T[], funcaoChave: (item: T) => string | number, decrescente = false): T[] {
  throw new Error("Missão 6.3 ainda não implementada: ordenarPor");
}

/** Títulos das n músicas mais tocadas, da mais para a menos tocada. Empate: ordem alfabética do título. */
export function maisTocadas(musicas: Musica[], n: number): string[] {
  throw new Error("Missão 6.3 ainda não implementada: maisTocadas");
}

/** O CHEFÃO: veja o playlist.js para a descrição do relatório. */
export function relatorioPlaylist(musicas: Musica[]): {
  totalMusicas: number;
  duracaoTotal: string;
  generos: Record<string, number>;
  topArtista: string | null;
  top3: string[];
} {
  throw new Error("Missão 6.3 ainda não implementada: relatorioPlaylist");
}
