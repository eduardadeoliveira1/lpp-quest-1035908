"""Gera o mapa da jornada em SVG (visual "pixel art"), refletindo o progresso do aluno. Não precisa editar."""
from xml.sax.saxutils import escape

LARGURA, ALTURA = 900, 1260
FONTE = "'Courier New', Consolas, Menlo, monospace"

# posição de cada nível no mapa: painel (x, y), nó do caminho (x, y), ilha (x, y, largura, altura)
LAYOUT = {
    1: dict(painel=(40, 330), no=(150, 505), ilha=(30, 470, 300, 120)),
    2: dict(painel=(375, 275), no=(470, 440), ilha=(350, 410, 290, 120)),
    3: dict(painel=(60, 650), no=(170, 820), ilha=(30, 790, 300, 120)),
    4: dict(painel=(540, 595), no=(660, 765), ilha=(520, 735, 320, 120)),
    5: dict(painel=(50, 940), no=(160, 1100), ilha=(30, 1070, 300, 120)),
    6: dict(painel=(470, 905), no=(590, 1065), ilha=(450, 1035, 340, 120)),
}
# cores de cada bioma: topo, meio, rocha, cor da etiqueta LVL
BIOMAS = {
    1: ("#58b45a", "#8d6e4b", "#5b4330", "#2e9e4f"),
    2: ("#e2b958", "#c48a3b", "#8a5a26", "#d98a1c"),
    3: ("#62c46d", "#7a6a5c", "#4b4b5e", "#2c7ee0"),
    4: ("#eaf7ff", "#a5d6f2", "#5f8fb8", "#2fa4d9"),
    5: ("#7050aa", "#4d3380", "#2b1b4d", "#8a3fd1"),
    6: ("#4a3434", "#2f2020", "#1b1313", "#e0452b"),
}
CORES_NO = {"limpo": "#ffd34d", "parcial": "#ff9f1c", "novo": "#9b59ff"}

# Título desenhado como formas vetoriais com a fonte Pixelify Sans (SIL Open Font License; veja assets/PixelifySans-OFL.txt).
# Assim ele fica igual em qualquer visualizador, sem depender de fontes instaladas.
TITULO_1 = "M48.4 82.9V48.3H55.1V41.7H61.8V35.2H69.9V41.7H76.6V48.3H83.3V82.9H75.1V69.7H56.6V82.9ZM56.6 61.4H75.1V50H68.5V43.5H63.2V50H56.6ZM119.7 82.9V76.3H113V61.4H121.2V74.6H139.7V43.5H119.7V35.2H141.2V41.7H147.9V76.3H141.2V82.9ZM166.5 82.9V76.3H159.9V41.7H166.5V35.2H188V41.7H194.7V76.3H188V82.9ZM168 74.6H186.5V43.5H168ZM206.7 82.9V41.7H213.3V35.2H234.8V41.7H241.5V63.1H234.8V69.7H231.5V74.6H238.1V82.9H230V76.3H223.3V69.7H214.8V82.9ZM214.8 61.4H233.3V43.5H214.8ZM253.5 82.9V35.2H261.6V41.7H268.2V48.3H274.9V67.9H280.1V35.2H288.3V82.9H280.1V76.3H273.5V69.7H266.8V50H261.6V82.9ZM300.3 82.9V48.3H306.9V41.7H313.6V35.2H321.7V41.7H328.4V48.3H335.1V82.9H326.9V69.7H308.4V82.9ZM308.4 61.4H326.9V50H320.3V43.5H315V50H308.4ZM347.1 82.9V35.2H368.5V41.7H375.2V48.3H381.9V69.7H375.2V76.3H368.5V82.9ZM355.2 74.6H367.1V67.9H373.7V50H367.1V43.5H355.2ZM393.9 82.9V48.3H400.6V41.7H407.2V35.2H415.4V41.7H422V48.3H428.7V82.9H420.5V69.7H402V82.9ZM402 61.4H420.5V50H413.9V43.5H408.6V50H402Z"
TITULO_2 = "M49.3 167.1V110.3H82.7V118.1H90.7V128H81V120.2H59V133.8H74.8V143.6H59V167.1ZM112.3 167.1V159.2H104.4V110.3H114.1V157.2H136.1V110.3H145.8V159.2H137.8V167.1ZM159.5 167.1V110.3H169.2V118.1H177V125.9H185V149.3H191.2V110.3H200.9V167.1H191.2V159.2H183.3V151.4H175.3V128H169.2V167.1ZM222.5 167.1V159.2H214.6V118.1H222.5V110.3H248V118.1H256V135.7H246.2V120.2H224.2V157.2H246.2V141.4H256V159.2H248V167.1ZM269.7 167.1V157.2H277.6V120.2H269.7V110.3H295.2V120.2H287.2V157.2H295.2V167.1ZM316.8 167.1V159.2H308.8V118.1H316.8V110.3H342.3V118.1H350.3V159.2H342.3V167.1ZM318.5 157.2H340.5V120.2H318.5ZM363.9 167.1V110.3H373.6V118.1H381.4V125.9H389.4V149.3H395.6V110.3H405.4V167.1H395.6V159.2H387.8V151.4H379.8V128H373.6V167.1ZM419 167.1V125.9H426.9V118.1H434.9V110.3H444.5V118.1H452.5V125.9H460.5V167.1H450.7V151.4H428.7V167.1ZM428.7 141.4H450.7V128H442.9V120.2H436.5V128H428.7ZM482 167.1V159.2H474.1V110.3H483.8V157.2H505.8V149.3H515.6V159.2H507.6V167.1Z"
SUBTITULO = "M49.1 204.3V202.4H47.3V192.6H49.1V190.7H55.2V192.6H57.2V194.9H54.8V193.1H49.6V196.3H55.2V198.1H57.2V202.4H55.2V204.3ZM49.6 201.9H54.8V198.6H49.6ZM64.9 204.3V194.4H72.9V196.3H74.8V204.3H72.5V196.8H67.2V204.3ZM77.8 204.3V194.4H80.1V204.3ZM77.2 193.1V191.7H78.1V190.8H79V189.8H80.4V191.2H79.5V192.2H78.5V193.1ZM86.7 204.3V202.4H84.9V198.6H83V194.4H85.3V198.1H87.1V201.9H88.6V198.1H90.5V194.4H92.8V198.6H90.9V202.4H89.1V204.3ZM97.8 204.3V202.4H95.9V196.3H97.8V194.4H103.9V196.3H105.8V198.6H103.5V196.8H98.2V198.1H102V200.5H98.2V201.9H103.5V200H105.8V202.4H103.9V204.3ZM108.8 204.3V194.4H111.1V204.3ZM108.8 193.1V190.7H111.1V193.1ZM114.2 204.3V201.9H121.7V200.5H116.1V198.6H114.2V196.3H116.1V194.4H124.1V196.8H116.5V198.1H122.2V200H124.1V202.4H122.2V204.3ZM131.8 198.5V196.2H134.1V198.5ZM145.6 204.3V193.1H144.2V194.9H141.9V192.6H143.8V190.7H146V192.6H148V204.3ZM152.9 204.3V202.4H151V198.1H152.9V196.8H151V192.6H152.9V190.7H159V192.6H160.9V196.8H159V198.1H160.9V202.4H159V204.3ZM153.3 201.9H158.6V198.6H153.3ZM153.3 196.3H158.6V193.1H153.3ZM168.6 204.3V194.4H174.7V196.3H176.2V194.4H180.4V196.3H182.3V204.3H180V196.8H176.6V204.3H174.3V196.8H170.9V204.3ZM185.3 204.3V194.4H187.6V204.3ZM185.3 193.1V190.7H187.6V193.1ZM190.7 204.3V201.9H198.2V200.5H192.6V198.6H190.7V196.3H192.6V194.4H200.6V196.8H193V198.1H198.6V200H200.6V202.4H198.6V204.3ZM203.6 204.3V201.9H211.2V200.5H205.5V198.6H203.6V196.3H205.5V194.4H213.5V196.8H205.9V198.1H211.6V200H213.5V202.4H211.6V204.3ZM218.4 204.3V202.4H216.5V196.3H218.4V194.4H224.5V196.3H226.4V202.4H224.5V204.3ZM218.8 201.9H224.1V196.8H218.8ZM218.7 193.1V190.7H222.1V191.6H222.6V190.7H224V193.1H220.6V192.1H220.1V193.1ZM231.4 204.3V202.4H229.5V196.3H231.4V194.4H237.4V196.3H239.4V198.6H237V196.8H231.8V198.1H235.6V200.5H231.8V201.9H237V200H239.4V202.4H237.4V204.3ZM242.4 204.3V201.9H250V200.5H244.3V198.6H242.4V196.3H244.3V194.4H252.3V196.8H244.7V198.1H250.4V200H252.3V202.4H250.4V204.3ZM260 198.5V196.2H262.3V198.5ZM270.1 204.3V192.6H272V190.7H278.1V192.6H280V198.6H278.1V200.5H272.4V204.3ZM272.4 198.1H277.6V193.1H272.4ZM284.9 208V206.1H283V203.8H285.3V205.6H290.6V202.4H284.9V200.5H283V194.4H285.3V200H290.6V194.4H292.9V206.1H291V208ZM299.7 204.3V202.4H297.8V196.8H295.9V194.4H297.8V190.7H300.1V194.4H305.8V196.8H300.1V201.9H305.4V200H307.7V202.4H305.8V204.3ZM310.8 204.3V190.7H313.1V196.3H314.5V194.4H318.7V196.3H320.7V204.3H318.3V196.8H314.9V198.6H313.1V204.3ZM325.6 204.3V202.4H323.7V196.3H325.6V194.4H331.7V196.3H333.6V202.4H331.7V204.3ZM326 201.9H331.3V196.8H326ZM336.6 204.3V194.4H344.6V196.3H346.5V204.3H344.2V196.8H338.9V204.3ZM358.1 202.2V198.7H354.4V196.4H358.1V192.4H360.5V196.4H364.2V198.7H360.5V202.2ZM372.1 204.3V190.7H374.4V192.6H376.2V194.4H378.2V200H379.6V190.7H382V204.3H379.6V202.4H377.8V200.5H375.8V194.9H374.4V204.3ZM386.9 204.3V202.4H385V196.3H386.9V194.4H393V196.3H394.9V202.4H393V204.3ZM387.3 201.9H392.6V196.8H387.3ZM399.8 204.3V202.4H397.9V196.3H399.8V194.4H405.5V190.7H407.8V202.4H405.9V204.3ZM400.2 201.9H405.5V196.8H400.2ZM412.7 204.3V202.4H410.9V196.3H412.7V194.4H418.8V196.3H420.7V198.6H418.4V196.8H413.2V198.1H416.9V200.5H413.2V201.9H418.4V200H420.7V202.4H418.8V204.3Z"



def _rect(x, y, w, h, fill, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" {extra}/>'


def _texto(x, y, conteudo, tamanho, fill, peso="bold", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{FONTE}" font-size="{tamanho}" font-weight="{peso}" '
            f'fill="{fill}" {extra}>{escape(conteudo)}</text>')


def _nuvem(x, y, escala=1.0):
    e = escala
    return (_rect(x, y + 18 * e, 120 * e, 26 * e, "#ffffff") + _rect(x + 20 * e, y, 60 * e, 26 * e, "#ffffff")
            + _rect(x + 70 * e, y + 8 * e, 40 * e, 22 * e, "#ffffff") + _rect(x, y + 38 * e, 120 * e, 8 * e, "#d6e6f5"))


def _ilha(nivel):
    x, y, w, h = LAYOUT[nivel]["ilha"]
    topo, meio, rocha, _ = BIOMAS[nivel]
    partes = [
        _rect(x + 40, y + h * 0.62, w - 80, h * 0.38, rocha),
        _rect(x + 16, y + h * 0.34, w - 32, h * 0.34, meio),
        _rect(x, y, w, h * 0.38, topo),
        _rect(x + 8, y + h * 0.38 - 6, w - 16, 6, "#00000022"),
    ]
    if nivel in (1, 3):  # árvores
        for dx in (w * 0.55, w * 0.7, w * 0.85):
            partes += [_rect(x + dx, y - 26, 8, 28, "#6b4a2a"), _rect(x + dx - 12, y - 52, 32, 30, "#2e8b3e"),
                       _rect(x + dx - 6, y - 64, 20, 16, "#3aa04c")]
    if nivel == 3:  # cachoeira
        partes += [_rect(x + 26, y + 12, 20, h * 0.95, "#7ad7ff"), _rect(x + 34, y + 12, 6, h * 0.95, "#c8f1ff")]
    if nivel == 2:  # ruínas
        for dx, alt in ((w * 0.55, 46), (w * 0.7, 62), (w * 0.82, 38)):
            partes += [_rect(x + dx, y - alt, 16, alt + 4, "#d9a65a"), _rect(x + dx - 4, y - alt - 8, 24, 10, "#efc27a")]
    if nivel == 4:  # montanhas de gelo
        for dx, alt in ((w * 0.5, 44), (w * 0.66, 70), (w * 0.82, 50)):
            partes += [f'<polygon points="{x + dx},{y} {x + dx + 22},{y - alt} {x + dx + 44},{y}" fill="#ffffff" stroke="#9fd0ee" stroke-width="3"/>']
    if nivel == 5:  # cristais
        for dx, alt in ((w * 0.55, 50), (w * 0.7, 74), (w * 0.84, 42)):
            partes += [f'<polygon points="{x + dx},{y} {x + dx + 12},{y - alt} {x + dx + 24},{y}" fill="#b985ff" stroke="#e5d0ff" stroke-width="2"/>']
    if nivel == 6:  # lava
        for dx in (w * 0.2, w * 0.45, w * 0.7):
            partes += [_rect(x + dx, y + h * 0.4, 18, h * 0.55, "#ff7a1a"), _rect(x + dx + 4, y + h * 0.4, 6, h * 0.55, "#ffd34d")]
    return '<g shape-rendering="crispEdges">' + "".join(partes) + "</g>"


def _forma_texto(d, fill, contorno="#1a1038", largura_contorno=14):
    """Texto vetorial com contorno: uma camada escura por baixo e a cor por cima (não depende de paint-order)."""
    return (f'<path d="{d}" fill="{contorno}" stroke="{contorno}" stroke-width="{largura_contorno}" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="{fill}"/>')


def _estrela(cx, cy, r, fill):
    import math
    pontos = []
    for i in range(10):
        raio = r if i % 2 == 0 else r * 0.45
        ang = -math.pi / 2 + i * math.pi / 5
        pontos.append(f"{cx + raio * math.cos(ang):.1f},{cy + raio * math.sin(ang):.1f}")
    return f'<polygon points="{" ".join(pontos)}" fill="{fill}" stroke="#7a4a14" stroke-width="2"/>'


def _caminho(pontos):
    dados = f"M{pontos[0][0]} {pontos[0][1]}"
    for (x1, y1), (x2, y2) in zip(pontos, pontos[1:]):
        dx, dy = x2 - x1, y2 - y1
        dados += f" C{x1 + dx * 0.1:.0f} {y1 + dy * 0.65:.0f}, {x2 - dx * 0.1:.0f} {y2 - dy * 0.65:.0f}, {x2} {y2}"
    return (f'<path d="{dados}" fill="none" stroke="#6b3d12" stroke-width="13" stroke-linecap="round"/>'
            f'<path d="{dados}" fill="none" stroke="#ffd34d" stroke-width="7" stroke-linecap="round" stroke-dasharray="14 12"/>')


def _castelo(aberto):
    g = ['<g transform="translate(640,50)" shape-rendering="crispEdges">']
    g += [_rect(0, 120, 220, 110, "#8b8fa8"), _rect(0, 205, 220, 25, "#6f738c")]
    for x, w in ((0, 50), (170, 50)):  # torres laterais
        g += [_rect(x, 60, w, 170, "#a2a6c0"), _rect(x, 50, 12, 14, "#a2a6c0"), _rect(x + 19, 50, 12, 14, "#a2a6c0"),
              _rect(x + w - 12, 50, 12, 14, "#a2a6c0"), _rect(x + 17, 100, 16, 26, "#2a2d45")]
    g += [_rect(70, 20, 80, 210, "#b4b8d2"), _rect(70, 8, 16, 16, "#b4b8d2"), _rect(102, 8, 16, 16, "#b4b8d2"),
          _rect(134, 8, 16, 16, "#b4b8d2"), _rect(95, 60, 30, 36, "#2a2d45")]
    g += [_rect(108, -30, 4, 40, "#6b4a2a"), '<polygon points="112,-30 148,-18 112,-6" fill="#3b5bdb"/>']
    g += [_rect(22, 14, 4, 40, "#6b4a2a"), '<polygon points="26,14 58,24 26,34" fill="#3b5bdb"/>']
    g += [_rect(194, 14, 4, 40, "#6b4a2a"), '<polygon points="198,14 230,24 198,34" fill="#3b5bdb"/>']
    g += [_rect(90, 150, 40, 80, "#171a26"), _rect(96, 160, 28, 70, "#ffcf4a" if aberto else "#2f3350")]
    g += ["</g>", _texto(753, 128, "λ", 44, "#ffd34d", extra='text-anchor="middle" stroke="#7a4a14" stroke-width="2" paint-order="stroke"')]
    return "".join(g)


def _painel(n, nivel, estado):
    x, y = LAYOUT[n]["painel"]
    cor_lvl = BIOMAS[n][3]
    limpo = estado["limpo"]
    borda = "#58d36b" if limpo else "#d9a441"
    g = [
        f'<rect x="{x}" y="{y}" width="270" height="124" rx="8" fill="#171a26" stroke="{borda}" stroke-width="4"/>',
        f'<rect x="{x + 12}" y="{y - 17}" width="80" height="30" rx="6" fill="{cor_lvl}" stroke="#ffffff" stroke-width="3"/>',
        _texto(x + 52, y + 5, f"LVL {n}", 19, "#ffffff", extra='text-anchor="middle"'),
        _texto(x + 16, y + 44, nivel["nome"], 22 if len(nivel["nome"]) <= 16 else 19, "#ffffff"),
        _texto(x + 16, y + 68, f"{nivel['total']} missões · {nivel['linguagem']}", 15, "#ffd34d"),
        f'<rect x="{x + 12}" y="{y + 80}" width="246" height="32" rx="4" fill="#0b0d15"/>',
        _texto(x + 20, y + 101, nivel["snippet"], 13, "#9fe3a8", peso="normal"),
    ]
    if limpo:
        g += [f'<rect x="{x + 158}" y="{y - 17}" width="100" height="30" rx="6" fill="#2fbf5b" stroke="#ffffff" stroke-width="3"/>',
              _texto(x + 208, y + 4, "CLEAR!", 17, "#ffffff", extra='text-anchor="middle"')]
    else:
        g += [f'<rect x="{x + 178}" y="{y - 17}" width="80" height="30" rx="6" fill="#3a3f55" stroke="#ffffff" stroke-width="3"/>',
              _texto(x + 218, y + 4, f"{estado['ok']}/{nivel['total']}", 17, "#ffffff", extra='text-anchor="middle"')]
    return "".join(g)


def gerar_svg(estado):
    """estado: {"xp", "xp_total", "titulo", "tudo_limpo", "niveis": [{"n","nome","linguagem","snippet","total","ok","limpo"}]}"""
    niveis = {nv["n"]: nv for nv in estado["niveis"]}
    xp, xp_total = estado["xp"], estado["xp_total"]
    partes = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {LARGURA} {ALTURA}" width="{LARGURA}" height="{ALTURA}" role="img" '
        f'aria-label="Mapa da Jornada Funcional: {xp} de {xp_total} XP">',
        '<defs><linearGradient id="mar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8fd8ff"/>'
        '<stop offset="0.35" stop-color="#4fb3f5"/><stop offset="1" stop-color="#1767cf"/></linearGradient></defs>',
        f'<rect width="{LARGURA}" height="{ALTURA}" fill="url(#mar)"/>',
        '<g shape-rendering="crispEdges">' + _nuvem(520, 20, 0.9) + _nuvem(330, 250, 0.8) + _nuvem(780, 520, 0.9)
        + _nuvem(10, 620, 0.8) + _nuvem(380, 930, 0.9) + _nuvem(760, 1180, 0.8) + "</g>",
    ]
    # título (formas vetoriais: legível em qualquer visualizador)
    partes += [_forma_texto(TITULO_1, "#ffd34d"), _forma_texto(TITULO_2, "#ffffff"),
               _forma_texto(SUBTITULO, "#ffffff", largura_contorno=5)]
    # placa com XP e título, com a barra de progresso (termina antes do painel do nível 2)
    largura_barra = 288
    preenchido = int(largura_barra * xp / xp_total) if xp_total else 0
    partes += [
        '<rect x="40" y="216" width="320" height="88" rx="8" fill="#171a26" stroke="#d9a441" stroke-width="4"/>',
        _texto(56, 241, f"XP {xp}/{xp_total}", 19, "#ffffff"),
        _texto(56, 261, estado["titulo"], 16, "#ffd34d"),
        f'<rect x="56" y="271" width="{largura_barra}" height="20" rx="4" fill="#0b0d15" stroke="#ffffff" stroke-width="2"/>',
        f'<rect x="59" y="274" width="{max(0, preenchido - 6)}" height="14" fill="#ffd34d"/>',
    ]
    # castelo
    partes.append(_castelo(estado["tudo_limpo"]))
    partes.append('<rect x="650" y="305" width="220" height="74" rx="8" fill="#171a26" stroke="#d9a441" stroke-width="4"/>')
    if estado["tudo_limpo"]:
        partes += [_texto(760, 331, "LEVEL CLEAR:", 17, "#ffd34d", extra='text-anchor="middle"'),
                   _texto(760, 352, "você domina o", 14, "#ffffff", peso="normal", extra='text-anchor="middle"'),
                   _texto(760, 369, "paradigma funcional", 14, "#ffffff", peso="normal", extra='text-anchor="middle"')]
    else:
        partes += [_texto(760, 331, "???", 20, "#ffd34d", extra='text-anchor="middle"'),
                   _texto(760, 352, "conquiste as 6 ilhas", 14, "#ffffff", peso="normal", extra='text-anchor="middle"'),
                   _texto(760, 369, "para abrir o castelo", 14, "#ffffff", peso="normal", extra='text-anchor="middle"')]
    # ilhas, caminho, painéis e nós
    for n in range(1, 7):
        partes.append(_ilha(n))
    nos = [LAYOUT[n]["no"] for n in range(1, 7)]
    partes.append(_caminho(nos))
    partes.append(_caminho([nos[5], (888, 720), (890, 420), (866, 276)]))
    for n in range(1, 7):
        nv = niveis[n]
        situacao = "limpo" if nv["limpo"] else "parcial" if nv["ok"] > 0 else "novo"
        cx, cy = LAYOUT[n]["no"]
        partes.append(f'<circle cx="{cx}" cy="{cy}" r="17" fill="{CORES_NO[situacao]}" stroke="#ffffff" stroke-width="5"/>')
        if nv["limpo"]:
            partes.append(_estrela(cx, cy, 10, "#ffffff"))
        partes.append(_painel(n, nv, nv))
    # barra de informações
    partes.append('<rect x="60" y="1195" width="780" height="46" rx="8" fill="#171a26" stroke="#d9a441" stroke-width="4"/>')
    for x, texto in ((150, "18 MISSÕES"), (360, "100% PRÁTICA"), (580, "PYTHON + NODE"), (770, "VALE 1 PONTO")):
        partes.append(_texto(x, 1225, texto, 17, "#ffffff", extra='text-anchor="middle"'))
    partes.append("</svg>")
    return "\n".join(partes)
