"""
Arma el press kit para mandar por mail: Drive > Marketing > Kit de marketing > 06 Prensa y presentaciones.
Sigue la guía del taller de BA GameDevs: ficha completa, descripciones, features, permisos, info del
equipo, logos (color, blanco y negro), key art en 16:9, 1:1, 4:5 y 9:16 con las capas sueltas, y capturas.

Los textos salen de build.py (los mismos de la web); acá van solo los datos que la web no muestra.

Uso: python fuente/presskit.py
"""
import sys
import zipfile
from io import BytesIO
from pathlib import Path

from PIL import Image

from build import INSTAGRAM, LINKTREE, MAIL, TEXTOS, TIKTOK, URL

KIT = Path(r"G:\Mi unidad\Conurban Streets\Marketing\Kit de marketing")
CAPTURAS = Path(r"G:\Mi unidad\Conurban Streets\Marketing\Steam\capturas")
LOGOS = KIT / "01 Logos"
PORTADA = Path(r"G:\Mi unidad\Conurban Streets\Marketing\Pitch deck\fuente\assets\portada.png")
# Las cápsulas de Steam ya saben recortar la captura y poner el logo: el key art usa lo mismo.
sys.path.insert(0, r"G:\Mi unidad\Conurban Streets\Marketing\Steam\fuente")
import capsulas  # noqa: E402

# Va a Drive y no al sitio: el press kit se manda por mail a quien lo pide, no se publica.
SALIDA = KIT / "06 Prensa y presentaciones" / "conurban-streets-presskit.zip"
CARPETA = "Conurban Streets Presskit"

# (nombre, ancho, alto, ancho del logo, y del logo, alto del degradé, foco horizontal, foco vertical)
# El foco es dentro de capsulas.ZONA, que ya deja afuera el cartel de Panchos Ricky.
KEY_ART = [
    ("16x9", 1920, 1080, 0.58, 0.03, 0.55, 0.74, 0.62),
    ("1x1", 1080, 1080, 0.82, 0.04, 0.5, 0.74, 0.66),
    ("4x5", 1080, 1350, 0.86, 0.05, 0.45, 0.74, 0.7),
    ("9x16", 1080, 1920, 0.88, 0.06, 0.4, 0.74, 0.7),
]
# Capturas que no van al kit: la 01 tiene el cartel de Panchos Ricky y recortarla la baja de 1920x1080.
SIN_MARCAS = {"01_escalada_chevrones.png"}

# Lo que pide la guía y la web no muestra. Lo que todavía no está definido (duración, precio,
# edad, idiomas previstos) no se pone: mejor que falte a que diga "a definir".
EXTRA = {
    "es": {
        "titulo": "CONURBAN STREETS - PRESS KIT",
        "datos": "DATOS",
        "ficha": [
            ("Nombre", "Conurban Streets"),
            ("Desarrollador y publisher", "Lado Positivo Games (autopublicado)"),
            ("Género", "Carreras arcade 3D con autos clásicos argentinos tuneados, en un conurbano cyberpunk"),
            ("Plataforma", "PC (Steam)"),
            ("Fechas", "Demo a mediados de 2027 · lanzamiento a fines de 2027"),
            ("Estado", "En desarrollo, todavía sin demo pública"),
            ("Jugadores y modos", "1 jugador, carreras contra rivales controlados por la computadora"),
            ("Idiomas", "Castellano"),
            ("Engine", "Unity"),
            ("País", "Argentina"),
            ("Contacto de prensa", f"Cristian Almoniga · {MAIL}"),
        ],
        "corta": "DESCRIPCIÓN CORTA",
        "larga": "DESCRIPCIÓN LARGA",
        "features": "FEATURES",
        "circuitos": "Circuitos",
        "estudio_t": "ESTUDIO Y EQUIPO",
        "estudio": "Lado Positivo Games es un estudio independiente de Buenos Aires, Argentina, que arma Conurban Streets a pulmón y a distancia.",
        "equipo": "Equipo",
        "anecdotas_t": "Para contar",
        "anecdotas": [
            "Los circuitos de La Boca y Dock Sud y del Mercado Central siguen el trazado real de sus calles.",
        ],
        "permisos_t": "PERMISOS",
        "permisos": "Podés streamear el juego y subir videos, y monetizarlos. Podés usar el logo, el key art y las capturas de este kit en notas y videos sobre el juego. Por ahora no hay embargo.",
        "contacto_t": "CONTACTO Y REDES",
        "kit_t": "QUÉ HAY EN ESTE KIT",
        "kit": [
            "logo/ - a color (crema), blanco, negro y púrpura sobre transparente; sobre fondo púrpura y negro; ícono",
            "key-art/ - portada y key art en 16:9, 1:1, 4:5 y 9:16; en capas/ están el fondo sin logo y el logo por separado",
            "capturas/ - capturas del juego en 1920x1080, sin HUD ni marcas",
        ],
    },
    "en": {
        "titulo": "CONURBAN STREETS - PRESS KIT (ENGLISH)",
        "datos": "FACTS",
        "ficha": [
            ("Title", "Conurban Streets"),
            ("Developer and publisher", "Lado Positivo Games (self-published)"),
            ("Genre", "3D arcade racing with tuned classic Argentine cars in a cyberpunk Buenos Aires suburb"),
            ("Platform", "PC (Steam)"),
            ("Dates", "Demo mid-2027 · launch late 2027"),
            ("Status", "In development, no public demo yet"),
            ("Players and modes", "Single player, races against computer-controlled rivals"),
            ("Languages", "Spanish"),
            ("Engine", "Unity"),
            ("Country", "Argentina"),
            ("Press contact", f"Cristian Almoniga · {MAIL}"),
        ],
        "corta": "SHORT DESCRIPTION",
        "larga": "LONG DESCRIPTION",
        "features": "FEATURES",
        "circuitos": "Circuits",
        "estudio_t": "STUDIO AND TEAM",
        "estudio": "Lado Positivo Games is an independent studio from Buenos Aires, Argentina, building Conurban Streets on a shoestring and fully remote.",
        "equipo": "Team",
        "anecdotas_t": "Worth telling",
        "anecdotas": [
            "The La Boca and Dock Sud and the Mercado Central circuits follow the real layout of their streets.",
        ],
        "permisos_t": "PERMISSIONS",
        "permisos": "You can stream the game and upload videos, and monetize them. You can use the logo, key art and screenshots in this kit in articles and videos about the game. No embargo for now.",
        "contacto_t": "CONTACT AND SOCIAL",
        "kit_t": "WHAT'S IN THIS KIT",
        "kit": [
            "logo/ - color (cream), white, black and purple on transparent; on purple and black backgrounds; icon",
            "key-art/ - cover and key art in 16:9, 1:1, 4:5 and 9:16; capas/ has the background without logo and the logo on its own",
            "capturas/ - in-game screenshots at 1920x1080, no HUD or watermarks",
        ],
    },
}


def ficha(idioma):
    t, x = TEXTOS[idioma], EXTRA[idioma]
    equipo = dict(t["ficha"])[x["equipo"]]
    lineas = [x["titulo"], "", f"== {x['datos']} =="]
    lineas += [f"{k}: {v}" for k, v in x["ficha"]]
    lineas += ["", f"== {x['corta']} ==", t["desc"], "", f"== {x['larga']} ==", t["intro"], ""]
    lineas += [f"{x['circuitos']}:"] + [f"- {n}: {d}" for _, n, d in t["pistas"]]
    lineas += ["", f"== {x['features']} =="] + [f"- {h}: {p}" for h, p in t["pilares"]]
    lineas += ["", f"== {x['estudio_t']} ==", x["estudio"], f"{x['equipo']}: {equipo}", ""]
    lineas += [f"{x['anecdotas_t']}:"] + [f"- {a}" for a in x["anecdotas"]]
    lineas += ["", f"== {x['permisos_t']} ==", x["permisos"]]
    lineas += ["", f"== {x['contacto_t']} ==", f"Mail: {MAIL}", f"Web: {URL}/" + ("" if idioma == "es" else "en/"),
               f"Instagram: {INSTAGRAM}", f"TikTok: {TIKTOK}", f"Linktree: {LINKTREE}"]
    lineas += ["", f"== {x['kit_t']} =="] + [f"- {k}" for k in x["kit"]]
    return "\n".join(lineas) + "\n"


def png(img):
    b = BytesIO()
    img.save(b, "PNG", optimize=True)
    return b.getvalue()


def logo_de_color(rgb):
    m = Image.open(LOGOS / "conurban-streets-logo-crema-transparente.png").convert("RGBA")
    plano = Image.new("RGBA", m.size, rgb + (255,))
    plano.putalpha(m.getchannel("A"))
    return plano


def key_art(w, h, ancho_logo, y_logo, alto_degrade, foco_x, foco_y):
    """Devuelve (fondo sin logo, key art completo) con el mismo recorte que las cápsulas de Steam."""
    fondo = capsulas.recorte(capsulas.fondo(), w, h, foco_x, foco_y).convert("RGBA")
    completo = fondo.copy()
    completo.alpha_composite(capsulas.degrade(w, h, alto_degrade))
    lg = capsulas.logo(int(w * ancho_logo))
    completo.alpha_composite(lg, ((w - lg.width) // 2, int(h * y_logo)))
    return fondo.convert("RGB"), completo.convert("RGB")


def main():
    SALIDA.parent.mkdir(exist_ok=True)
    c = CARPETA
    with zipfile.ZipFile(SALIDA, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{c}/Conurban Streets - ficha (fact sheet).txt", ficha("es") + "\n\n" + ficha("en"))
        for f in sorted(LOGOS.glob("*.png")):
            z.write(f, f"{c}/logo/{f.name}")
        z.writestr(f"{c}/logo/conurban-streets-logo-blanco-transparente.png", png(logo_de_color((255, 255, 255))))
        z.write(PORTADA, f"{c}/key-art/conurban-streets-portada-16x9.png")
        for nombre, *medidas in KEY_ART:
            fondo, completo = key_art(*medidas)
            z.writestr(f"{c}/key-art/conurban-streets-key-art-{nombre}.png", png(completo))
            z.writestr(f"{c}/key-art/capas/fondo-sin-logo-{nombre}.png", png(fondo))
        z.write(LOGOS / "conurban-streets-logo-crema-transparente.png", f"{c}/key-art/capas/logo-crema-transparente.png")
        for f in sorted(CAPTURAS.glob("*.png")):
            if f.name not in SIN_MARCAS:
                z.write(f, f"{c}/capturas/{f.name}")
    print(SALIDA, SALIDA.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
