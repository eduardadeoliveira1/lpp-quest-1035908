// Relator de testes do Node para o quest.py (uso interno). Imprime linhas @@QUEST@@ com JSON.
export default async function* (source) {
  for await (const ev of source) {
    if (ev.type === "test:pass" || ev.type === "test:fail") {
      const erro = ev.data.details?.error;
      const msg = (erro?.cause?.message ?? erro?.message ?? "").replace(/\s+/g, " ").slice(0, 300);
      yield "@@QUEST@@ " + JSON.stringify({ nome: ev.data.name, nest: ev.data.nesting, ok: ev.type === "test:pass", msg }) + "\n";
    }
  }
}
