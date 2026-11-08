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
    return musicas.filter((musica) => musica.genero === genero);
}

/** Soma das durações (em segundos). */
export function duracaoTotal(musicas) {
    return musicas.reduce(
        (total, musica) => total + musica.duracao,
        0
    );
}

/** Segundos => "m:ss".   65 => "1:05"   0 => "0:00"   3725 => "62:05"   Dica: Math.floor e padStart(2, "0"). */
export function formatarDuracao(segundos) {
    const minutos = Math.floor(segundos / 60);
    const restante = segundos % 60;

    return `${minutos}:${String(restante).padStart(2, "0")}`;
}

// ============================================================ MISSÃO 6.2 — Agrupar
/** Agrupa os itens pelo valor que funcaoChave devolve: { chave: [itens...] }, mantendo a ordem original.
 *  Dica: reduce com um objeto NOVO a cada passo:  { ...acc, [k]: [...(acc[k] ?? []), item] } */
export function agruparPor(lista, funcaoChave) {
    return lista.reduce((grupos, item) => {
        const chave = funcaoChave(item);

        if (!grupos[chave]) {
            grupos[chave] = [];
        }

        grupos[chave].push(item);

        return grupos;
    }, {});
}

/** { chave: quantidade de itens }. Dica: use agruparPor. */
export function contarPor(lista, funcaoChave) {
    const grupos = agruparPor(lista, funcaoChave);

    return Object.fromEntries(
        Object.entries(grupos).map(([chave, itens]) => [
            chave,
            itens.length
        ])
    );
}

/** { artista: soma dos plays de todas as músicas dele(a) }. */
export function playsPorArtista(musicas) {
    const grupos = agruparPor(musicas, (musica) => musica.artista);

    return Object.fromEntries(
        Object.entries(grupos).map(([artista, itens]) => [
            artista,
            itens.reduce((total, musica) => total + musica.plays, 0)
        ])
    );
}

// ============================================================ MISSÃO 6.3 — Ordenar e o chefão
/** Lista NOVA ordenada pelo valor de funcaoChave (crescente; decrescente se o 3º argumento for true).
 *  Empate: mantém a ordem original. Dica: [...lista].sort((a, b) => ...) */
export function ordenarPor(lista, funcaoChave, decrescente = false) {
    return [...lista].sort((a, b) => {
        const valorA = funcaoChave(a);
        const valorB = funcaoChave(b);

        if (valorA < valorB) {
            return decrescente ? 1 : -1;
        }

        if (valorA > valorB) {
            return decrescente ? -1 : 1;
        }

        return 0;
    });
}

/** Títulos das n músicas mais tocadas, da mais para a menos tocada. Empate: ordem alfabética do título. */
export function maisTocadas(musicas, n) {
    return [...musicas]
        .sort((a, b) => {
            if (a.plays !== b.plays) {
                return b.plays - a.plays;
            }

            return a.titulo.localeCompare(b.titulo);
        })
        .slice(0, n)
        .map((musica) => musica.titulo);
}

/** O CHEFÃO:  { totalMusicas, duracaoTotal: "m:ss", generos: { genero: quantidade },
 *               topArtista: nome do artista com mais plays no total (empate: ordem alfabética; null se vazio),
 *               top3: títulos das 3 mais tocadas }  */
export function relatorioPlaylist(musicas) {
    const artistas = playsPorArtista(musicas);

    const topArtista = Object.entries(artistas)
        .sort((a, b) => {
            if (b[1] !== a[1]) {
                return b[1] - a[1];
            }

            return a[0].localeCompare(b[0]);
        })[0]?.[0] ?? null;

    return {
        totalMusicas: musicas.length,
        duracaoTotal: formatarDuracao(duracaoTotal(musicas)),
        generos: contarPor(musicas, (musica) => musica.genero),
        topArtista: topArtista,
        top3: maisTocadas(musicas, 3)
    };
}
