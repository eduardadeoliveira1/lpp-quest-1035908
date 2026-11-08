#!/usr/bin/env python3
"""A JORNADA FUNCIONAL — o placar do jogo.

Uso (no terminal do VS Code, na pasta do jogo):
    python quest.py              roda todos os níveis, mostra o placar e atualiza o mapa
    python quest.py 3            mostra os detalhes do nível 3
    python quest.py escolher ts  usa TypeScript nos níveis de Node (apaga os .js iniciais)
    python quest.py escolher js  usa JavaScript nos níveis de Node (apaga os .ts iniciais)
    python quest.py ambiente     confere se Python, Node e Git estão instalados

No Mac/Linux, troque `python` por `python3`. No Windows, se `python` não funcionar, tente `py`.
"""
import ast
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / "tools"))
from mapa import gerar_svg  # noqa: E402

try:  # emojis no terminal do Windows
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

XP_MISSAO = 10
XP_BONUS_NIVEL = 10
TITULOS = [(240, "Lenda Funcional"), (160, "Mago da Composição"), (100, "Cavaleiro da Pureza"),
           (40, "Escudeiro Funcional"), (0, "Aprendiz de Código")]

NIVEIS = [
    dict(n=1, nome="Vila do Boletim", linguagem="Python", pasta="nivel1_boletim", teste="test_boletim", base="boletim",
         conceito="Funções puras, map, filter e reduce", snippet="media([8, 6, 10])",
         missoes=[("1.1", "Funções puras: média e situação"), ("1.2", "map: o boletim da turma"),
                  ("1.3", "filter e reduce: aprovados e ranking")]),
    dict(n=2, nome="Floresta das Tarefas", linguagem="Node", pasta="nivel2_tarefas", teste="tarefas.test.mjs", base="tarefas",
         conceito="Imutabilidade e desfazer/refazer", snippet="concluir(tarefas, 2)",
         missoes=[("2.1", "Adicionar e concluir sem mutar"), ("2.2", "Remover, filtrar e resumir"),
                  ("2.3", "Desfazer e refazer")]),
    dict(n=3, nome="Cânions dos Logs", linguagem="Python", pasta="nivel3_logs", teste="test_logs", base="logs",
         conceito="Pipeline de transformações", snippet="pipe(parsear, erros)(log)",
         missoes=[("3.1", "Ler o log"), ("3.2", "Filtrar e contar"), ("3.3", "O pipeline final")]),
    dict(n=4, nome="Torre do Validador", linguagem="Node", pasta="nivel4_validador", teste="validador.test.mjs", base="validador",
         conceito="Closures e composição", snippet="minimo('Senha', 8)",
         missoes=[("4.1", "Fábricas de regras (closures)"), ("4.2", "Compondo regras"), ("4.3", "O formulário completo")]),
    dict(n=5, nome="Vulcão dos Sensores", linguagem="Python", pasta="nivel5_sensores", teste="test_sensores", base="sensores",
         conceito="Recursão e síntese", snippet="somar(v[1:]) + v[0]",
         missoes=[("5.1", "Recursão: o básico"), ("5.2", "Limpar e janelas"), ("5.3", "Alertas e o painel final")]),
    dict(n=6, nome="Castelo da Playlist", linguagem="Node", pasta="nivel6_playlist", teste="playlist.test.mjs", base="playlist",
         conceito="Agrupar e ordenar (o chefão)", snippet="agruparPor(lista, chave)",
         missoes=[("6.1", "Filtrar e somar"), ("6.2", "Agrupar"), ("6.3", "Ordenar e o chefão")]),
]
XP_TOTAL = sum(len(n["missoes"]) * XP_MISSAO + XP_BONUS_NIVEL for n in NIVEIS)
PREFIXO = "@@QUEST@@ "


# ------------------------------------------------------------------ execução dos testes
def _linhas_quest(saida):
    for linha in saida.splitlines():
        if linha.startswith(PREFIXO):
            try:
                yield json.loads(linha[len(PREFIXO):])
            except json.JSONDecodeError:
                continue


def _vazio(nivel, erro=None):
    return {"erro_geral": erro, "missoes": {m[0]: {"ok": False, "testes_ok": 0, "testes_total": 0, "falhas": []} for m in nivel["missoes"]}}


def rodar_python(nivel):
    resultado = _vazio(nivel)
    ambiente = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    try:
        proc = subprocess.run(
            [sys.executable, "-B", "tools/rodar_py.py", nivel["pasta"], nivel["teste"], "tools"],
            cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=40, env=ambiente)
    except subprocess.TimeoutExpired:
        return _vazio(nivel, "tempo esgotado: tem algum laço infinito ou recursão sem fim?")
    eventos = list(_linhas_quest(proc.stdout))
    if not eventos:
        return _vazio(nivel, (proc.stderr.strip().splitlines() or ["os testes não rodaram"])[-1][:200])
    for ev in eventos:
        achou = re.fullmatch(r"Missao_(\d)_(\d)", ev["classe"])
        if not achou:  # falha ao importar o seu código
            return _vazio(nivel, ev["msg"] or "não foi possível carregar o seu código")
        m = resultado["missoes"][f"{achou.group(1)}.{achou.group(2)}"]
        m["testes_total"] += 1
        m["testes_ok"] += ev["ok"]
        if not ev["ok"]:
            m["falhas"].append((ev["teste"].replace("test_", "").replace("_", " "), ev["msg"]))
    return resultado


def _versao_node():
    try:
        saida = subprocess.run(["node", "--version"], capture_output=True, text=True, timeout=10).stdout.strip()
        achou = re.match(r"v(\d+)\.(\d+)", saida)
        return (int(achou.group(1)), int(achou.group(2))) if achou else None
    except Exception:  # noqa: BLE001
        return None


def arquivo_node(nivel):
    pasta = RAIZ / nivel["pasta"]
    js, ts = pasta / f"{nivel['base']}.js", pasta / f"{nivel['base']}.ts"
    return js if js.exists() else ts if ts.exists() else None


def rodar_node(nivel):
    if shutil.which("node") is None:
        return _vazio(nivel, "Node.js não encontrado. Instale o Node (veja o PREPARAR_AMBIENTE.md).")
    alvo = arquivo_node(nivel)
    if alvo is None:
        return _vazio(nivel, f"não encontrei {nivel['base']}.js nem {nivel['base']}.ts em {nivel['pasta']}")
    js_inicial, ts_feito = alvo.with_suffix(".js"), alvo.with_suffix(".ts")
    if js_inicial.exists() and ts_feito.exists():
        if "ainda não implementada" in js_inicial.read_text(encoding="utf-8") and "ainda não implementada" not in ts_feito.read_text(encoding="utf-8"):
            return _vazio(nivel, f"você implementou o {ts_feito.name}, mas o {js_inicial.name} inicial ainda existe e tem prioridade. Rode:  python quest.py escolher ts")
    versao = _versao_node()
    if versao is None or versao < (20, 11):
        return _vazio(nivel, "seu Node é antigo demais: instale o Node 22 LTS ou mais novo (rode  python quest.py ambiente)")
    if alvo.suffix == ".ts" and versao < (22, 18):
        return _vazio(nivel, "para rodar TypeScript direto você precisa do Node 22.18 ou mais novo (use .js ou atualize o Node)")
    resultado = _vazio(nivel)
    try:
        proc = subprocess.run(
            ["node", "--test", "--test-reporter=./tools/reporter.mjs", f"{nivel['pasta']}/{nivel['teste']}"],
            cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=40)
    except subprocess.TimeoutExpired:
        return _vazio(nivel, "tempo esgotado: tem algum laço infinito?")
    pendentes = []
    for ev in _linhas_quest(proc.stdout):
        if ev["nest"] >= 1:
            pendentes.append(ev)
            continue
        achou = re.match(r"Miss[aã]o (\d)\.(\d)", ev["nome"])
        if not achou:  # falha no arquivo inteiro (por exemplo, erro de sintaxe no seu código)
            if not ev["ok"]:
                return _vazio(nivel, ev["msg"] or "não foi possível carregar o seu código")
            continue
        m = resultado["missoes"][f"{achou.group(1)}.{achou.group(2)}"]
        for t in pendentes:
            m["testes_total"] += 1
            m["testes_ok"] += t["ok"]
            if not t["ok"]:
                m["falhas"].append((t["nome"], t["msg"]))
        pendentes = []
    if all(m["testes_total"] == 0 for m in resultado["missoes"].values()):
        return _vazio(nivel, (proc.stderr.strip().splitlines() or ["os testes não rodaram"])[-1][:200])
    return resultado


# ------------------------------------------------------------------ conquistas (só diversão, não valem nota)
def _sem_comentarios_js(codigo):
    codigo = re.sub(r"/\*.*?\*/", "", codigo, flags=re.S)
    codigo = re.sub(r"//[^\n]*", "", codigo)
    return re.sub(r"(\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'|`(?:\\.|[^`\\])*`)", '""', codigo)


def conquistas(nivel):
    """🔁 Zero laços  ·  🧊 Mãos limpas (nenhum método que altera a lista/objeto recebido)."""
    if nivel["linguagem"] == "Python":
        arquivo = RAIZ / nivel["pasta"] / f"{nivel['base']}.py"
        try:
            arvore = ast.parse(arquivo.read_text(encoding="utf-8"))
        except (OSError, SyntaxError):
            return []
        nos = list(ast.walk(arvore))
        sem_lacos = not any(isinstance(n, (ast.For, ast.While, ast.AsyncFor)) for n in nos)
        mutantes = {"append", "extend", "insert", "remove", "pop", "sort", "reverse", "update", "clear", "setdefault", "add", "discard"}
        limpas = not any(isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr in mutantes for n in nos) \
            and not any(isinstance(n, ast.AugAssign) or (isinstance(n, ast.Assign) and any(isinstance(t, (ast.Subscript, ast.Attribute)) for t in n.targets)) for n in nos)
    else:
        arquivo = arquivo_node(nivel)
        if arquivo is None:
            return []
        codigo = _sem_comentarios_js(arquivo.read_text(encoding="utf-8"))
        sem_lacos = not re.search(r"\b(for|while)\s*\(|\.forEach\s*\(", codigo)
        limpas = not re.search(r"\.(push|pop|shift|unshift|splice)\s*\(|\bdelete\s+\w|\b\w+(\.\w+|\[[^\]]+\])\s*(\+|-)?=(?!=)", codigo)
    return (["🔁 Zero laços"] if sem_lacos else []) + (["🧊 Mãos limpas"] if limpas else [])


# ------------------------------------------------------------------ cálculo do estado
def titulo_para(xp):
    return next(nome for minimo, nome in TITULOS if xp >= minimo)


def avaliar(nivel, bruto):
    missoes, ok = [], 0
    for mid, titulo in nivel["missoes"]:
        r = bruto["missoes"][mid]
        passou = r["testes_total"] > 0 and r["testes_ok"] == r["testes_total"]
        ok += passou
        missoes.append({"id": mid, "titulo": titulo, "ok": passou, "testes_ok": r["testes_ok"], "testes_total": r["testes_total"],
                        "falhas": r["falhas"], "xp": XP_MISSAO if passou else 0})
    limpo = ok == len(nivel["missoes"])
    return {"n": nivel["n"], "nome": nivel["nome"], "linguagem": nivel["linguagem"], "conceito": nivel["conceito"],
            "snippet": nivel["snippet"], "total": len(nivel["missoes"]), "ok": ok, "limpo": limpo,
            "xp": ok * XP_MISSAO + (XP_BONUS_NIVEL if limpo else 0), "erro_geral": bruto["erro_geral"], "missoes": missoes,
            "conquistas": conquistas(nivel) if limpo else []}


def jogar(so_nivel=None):
    niveis = []
    for nivel in NIVEIS:
        bruto = rodar_python(nivel) if nivel["linguagem"] == "Python" else rodar_node(nivel)
        niveis.append(avaliar(nivel, bruto))
    xp = sum(n["xp"] for n in niveis)
    return {"xp": xp, "xp_total": XP_TOTAL, "titulo": titulo_para(xp), "tudo_limpo": all(n["limpo"] for n in niveis),
            "nota_1_ponto": round(xp / XP_TOTAL, 2), "niveis": niveis}


# ------------------------------------------------------------------ apresentação
def barra(xp, total, tamanho=24):
    cheios = round(tamanho * xp / total) if total else 0
    return "█" * cheios + "░" * (tamanho - cheios)


def mostrar(estado, detalhe=None):
    print()
    print("  ⚔️   A JORNADA FUNCIONAL")
    print(f"  {estado['titulo']}   [{barra(estado['xp'], estado['xp_total'])}] {estado['xp']}/{estado['xp_total']} XP")
    print()
    proxima = None
    for nv in estado["niveis"]:
        selo = "🏆 LEVEL CLEAR!" if nv["limpo"] else f"{nv['ok']}/{nv['total']} missões"
        print(f"  Nível {nv['n']} · {nv['nome']} ({nv['linguagem']}) — {selo}   +{nv['xp']} XP")
        mostrar_missoes = detalhe == nv["n"] or (detalhe is None and not nv["limpo"] and proxima is None)
        if nv["erro_geral"]:
            print(f"      ⚠️  {nv['erro_geral']}")
        for m in nv["missoes"]:
            marca = "✅" if m["ok"] else "❌"
            extra = f"  ({m['testes_ok']}/{m['testes_total']} testes)" if m["testes_total"] and not m["ok"] else ""
            print(f"      {marca} Missão {m['id']} · {m['titulo']}{extra}")
            if mostrar_missoes and not m["ok"]:
                limite = 6 if detalhe == nv["n"] else 2
                for teste, msg in m["falhas"][:limite]:
                    print(f"           ↳ {teste}: {msg}")
        if nv["conquistas"]:
            print(f"      🎖️  Conquistas: {'  '.join(nv['conquistas'])}")
        if not nv["limpo"] and proxima is None:
            proxima = next((m for m in nv["missoes"] if not m["ok"]), None)
            if proxima:
                proxima = (nv, proxima)
        print()
    if estado["tudo_limpo"]:
        print("  🏰 Você chegou ao castelo! Faça o commit e o push para entregar. 🎉")
    elif proxima:
        nv, m = proxima
        print(f"  👉 Próxima missão: {m['id']} · {m['titulo']}  (abra nivel{nv['n']}_*/LEIAME.md)")
        print(f"     Para ver mais detalhes: python quest.py {nv['n']}")
    print()


def md_progresso(estado):
    linhas = ["# 🗺️ Meu progresso", "", f"**{estado['titulo']}** — `{barra(estado['xp'], estado['xp_total'])}` **{estado['xp']}/{estado['xp_total']} XP**", "",
              "![Mapa da jornada](assets/mapa_progresso.svg)", "", "| Nível | Missão | Situação |", "|---|---|---|"]
    for nv in estado["niveis"]:
        for m in nv["missoes"]:
            linhas.append(f"| {nv['n']} · {nv['nome']} ({nv['linguagem']}) | {m['id']} · {m['titulo']} | {'✅' if m['ok'] else '❌'} |")
        if nv["limpo"]:
            linhas.append(f"| {nv['n']} · {nv['nome']} | 🏆 LEVEL CLEAR (+{XP_BONUS_NIVEL} XP) {' '.join(nv['conquistas'])} | ✅ |")
    linhas += ["", f"_Nota estimada da atividade: {estado['nota_1_ponto']:.2f} de 1,00 (a nota oficial é calculada pelo professor)._", ""]
    return "\n".join(linhas)


def salvar(estado):
    (RAIZ / "assets").mkdir(exist_ok=True)
    (RAIZ / "assets" / "mapa_progresso.svg").write_text(gerar_svg(estado), encoding="utf-8")
    (RAIZ / "PROGRESSO.md").write_text(md_progresso(estado), encoding="utf-8")
    resumo = {k: v for k, v in estado.items() if k != "niveis"}
    resumo["niveis"] = [{"n": n["n"], "nome": n["nome"], "xp": n["xp"], "limpo": n["limpo"],
                         "missoes": [{"id": m["id"], "ok": m["ok"]} for m in n["missoes"]], "conquistas": n["conquistas"]}
                        for n in estado["niveis"]]
    (RAIZ / "progresso.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=2), encoding="utf-8")


def ambiente():
    """Checagem do ambiente: Python, Node e Git."""
    print()
    print("  🔎 Checagem do ambiente")
    ok_py = sys.version_info >= (3, 10)
    print(f"  {'✅' if ok_py else '❌'} Python {sys.version.split()[0]}" + ("" if ok_py else "  (precisa do 3.10 ou mais novo)"))
    versao = _versao_node()
    if versao is None:
        print("  ❌ Node.js não encontrado  (necessário nos níveis 2, 4 e 6; veja o PREPARAR_AMBIENTE.md)")
    else:
        js_ok, ts_ok = versao >= (20, 11), versao >= (22, 18)
        print(f"  {'✅' if js_ok else '❌'} Node {versao[0]}.{versao[1]} — JavaScript {'ok' if js_ok else 'precisa do 20.11+'}")
        print(f"  {'✅' if ts_ok else '⚠️ '} TypeScript direto {'ok' if ts_ok else 'precisa do Node 22.18+ (use JavaScript ou atualize)'}")
    try:
        git = subprocess.run(["git", "--version"], capture_output=True, text=True, timeout=10).stdout.strip()
        print(f"  ✅ {git}")
    except Exception:  # noqa: BLE001
        print("  ❌ Git não encontrado  (veja o PREPARAR_AMBIENTE.md)")
    print()


def escolher(linguagem):
    if linguagem not in ("js", "ts"):
        sys.exit("Use:  python quest.py escolher js   ou   python quest.py escolher ts")
    apagar = "ts" if linguagem == "js" else "js"
    for nivel in NIVEIS:
        if nivel["linguagem"] != "Node":
            continue
        pasta = RAIZ / nivel["pasta"]
        sobra = pasta / f"{nivel['base']}.{apagar}"
        fica = pasta / f"{nivel['base']}.{linguagem}"
        if sobra.exists() and fica.exists():
            sobra.unlink()
            print(f"Removido {sobra.relative_to(RAIZ)} (você vai usar {fica.name})")
    print(f"Pronto! Nos níveis de Node você vai usar {'TypeScript' if linguagem == 'ts' else 'JavaScript'}.")


def main():
    args = sys.argv[1:]
    if args and args[0] == "ambiente":
        ambiente()
        return
    if args and args[0] == "escolher":
        escolher(args[1] if len(args) > 1 else "")
        return
    como_json = "--json" in args
    sem_salvar = "--sem-salvar" in args or como_json
    numeros = [a for a in args if a.isdigit()]
    detalhe = int(numeros[0]) if numeros else None
    estado = jogar()
    if como_json:
        print(json.dumps(estado, ensure_ascii=False, default=str))
        return
    mostrar(estado, detalhe)
    if not sem_salvar:
        salvar(estado)
        print("  💾 Progresso salvo (PROGRESSO.md e assets/mapa_progresso.svg). Faça commit para mostrar no GitHub!")
        print()
    resumo = os.environ.get("GITHUB_STEP_SUMMARY")
    if resumo and "--ci" in args:
        with open(resumo, "a", encoding="utf-8") as f:
            f.write(md_progresso(estado))


if __name__ == "__main__":
    main()
