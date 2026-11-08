// Carrega o código do aluno: usa o .js se existir; senão usa o .ts (Node 22.18+ importa TypeScript direto).
import { existsSync } from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";

export async function carregar(pasta, nome) {
  const js = path.join(pasta, `${nome}.js`);
  const ts = path.join(pasta, `${nome}.ts`);
  const alvo = existsSync(js) ? js : ts;
  return import(pathToFileURL(alvo).href);
}

// Envolve uma função exportada para dar uma mensagem clara quando ela não existe.
export function usar(modulo, nome) {
  return (...args) => {
    if (typeof modulo[nome] !== "function") {
      throw new Error(`A função ${nome} não existe ou não foi exportada (export function ${nome}...)`);
    }
    return modulo[nome](...args);
  };
}

// Congela objetos e listas recursivamente: qualquer tentativa de alterar a entrada vira erro.
export function congelar(valor) {
  if (valor && typeof valor === "object" && !Object.isFrozen(valor)) {
    Object.values(valor).forEach(congelar);
    Object.freeze(valor);
  }
  return valor;
}
