"""
Arma el press kit para mandar por mail: Drive > Marketing > Kit de marketing > 06 Prensa y presentaciones.
Sigue la guía del taller de BA GameDevs: ficha completa, descripciones, features, permisos, info del
equipo, logos (color, blanco y negro), key art en 16:9, 1:1, 4:5 y 9:16 con las capas sueltas, y capturas.

Los textos salen de build.py (los mismos de la web); acá van solo los datos que la web no muestra.

Uso: python fuente/presskit.py
"""
import subprocess
import sys
import zipfile
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageFilter

from build import INSTAGRAM, MAIL, TEXTOS, TIKTOK, URL

KIT = Path(r"G:\Mi unidad\Conurban Streets\Marketing\Kit de marketing")
CAPTURAS = Path(r"F:\Lado Positivo Games\conurban-streets\conurban-streets\Capturas")
RECORTES = KIT / "04 Videos" / "Recortes del Modo Cine"
LOGOS = KIT / "01 Logos"
# Fondo del key art (20/11/2026): el R12 con turbinas entre chevrones en Camino Negro, sacado del video
# original del Modo Cine (no del recorte, que está más comprimido). Es la misma imagen de la portada del
# dossier de prensa. Las líneas de velocidad son las del menú principal del juego.
TOMA_KEY_ART = KIT / "04 Videos" / "Modo Cine - tomas completas" / "12_Level_CaminoNegro_20261111_015444_Director.mp4"
SEGUNDO_KEY_ART = 75.5
LINEAS = Path(r"F:\Lado Positivo Games\conurban-streets\conurban-streets\Assets\_Project\UI\Fondos\Sprite_FondoMenu_LineasVelocidad.png")
# Las cápsulas de Steam ya saben recortar la captura y poner el logo: el key art usa lo mismo.
sys.path.insert(0, r"G:\Mi unidad\Conurban Streets\Marketing\Steam\fuente")
import capsulas  # noqa: E402

# Va a Drive y no al sitio: el press kit se manda por mail a quien lo pide, no se publica.
SALIDA = KIT / "06 Prensa y presentaciones" / "conurban-streets-presskit.zip"
CARPETA = "Conurban Streets Presskit"

# (nombre, ancho, alto, ancho del logo, y del logo, alto del degradé, foco horizontal, foco vertical)
# El foco es sobre el cuadro de 1920x1080: el auto está en el centro, un poco abajo.
KEY_ART = [
    ("16x9", 1920, 1080, 0.56, 0.05, 0.5, 0.5, 0.5),
    ("1x1", 1080, 1080, 0.84, 0.05, 0.5, 0.5, 0.5),
    ("4x5", 1080, 1350, 0.86, 0.06, 0.45, 0.52, 0.5),
    ("9x16", 1080, 1920, 0.9, 0.09, 0.42, 0.52, 0.5),
]
# Capturas del kit: (nombre en el kit, original en Capturas/). Todas después del salto visual del 02/11,
# sin HUD. La pista secreta (Vacaciones menemistas) no aparece: en prensa no se muestra ni se nombra.
SELECCION = [
    ("01_escalada_504", "Web/10_Level_Conurban_peugeot504_largada_costado.png"),
    ("02_escalada_147", "Web/10_Level_Conurban_fiat147_largada_tres_cuartos.png"),
    ("03_escalada_grilla", "Web/mezcla_10_Level_Conurban_renault12_grilla_atras_der.png"),
    ("04_autodromo_grilla", "Web/mezcla_11_Level_Autodromo_renault12_grilla_atras_der.png"),
    ("05_autodromo_147", "Web/11_Level_Autodromo_fiat147_tramo2_costado.png"),
    ("06_autodromo_c10", "Web/11_Level_Autodromo_chevroletC10_tramo2_costado.png"),
    ("07_caminonegro_c10", "Web/12_Level_CaminoNegro_chevroletC10_tramo2_costado.png"),
    ("08_caminonegro_504", "Web/12_Level_CaminoNegro_peugeot504_tramo2_costado.png"),
    ("09_caminonegro_colectivo", "12_Level_CaminoNegro_20261023_002822_044.png"),
    ("10_docksud_grilla", "Web/mezcla_13_Level_DockSud_renault12_grilla_atras_izq.png"),
    ("11_docksud_504", "Web/13_Level_DockSud_peugeot504_tramo3_costado.png"),
    ("12_laboca_conventillos", "13_Level_DockSud_20261017_043734_861.png"),
    ("13_mercado_504", "Web/14_Level_MercadoCentral_peugeot504_tramo1_costado.png"),
    ("14_mercado_c10", "Web/14_Level_MercadoCentral_chevroletC10_tramo1_costado.png"),
]
# Clips cortos del Modo Cine (sin audio, 1080p), de los recortes del kit de marketing.
CLIPS = [
    "01_Largada_Escalada_R12_01.mp4", "02_Persecucion_Escalada_147_01.mp4",
    "05_AutoDeCerca_Autodromo_504_03.mp4", "02_Persecucion_CaminoNegro_R12_04.mp4",
    "05_AutoDeCerca_DockSud_R12_07.mp4", "02_Persecucion_MercadoCentral_C10_06.mp4",
    "08_Aereo_Autodromo_147_04.mp4", "06_Detalle_Escalada_R12_01.mp4",
]
SECRETA = "Vacaciones menemistas"

# Lo que pide la guía y la web no muestra. Lo que no está definido o no se anunció (precio, fecha
# exacta, modos nuevos, idiomas previstos) no se pone: mejor que falte a que diga "a definir".
EXTRA = {
    "es": {
        "titulo": "CONURBAN STREETS - PRESS KIT",
        "datos": "DATOS",
        "ficha": [
            ("Nombre", "Conurban Streets"),
            ("Desarrollador y publisher", "Lado Positivo (autopublicado)"),
            ("Género", "Carreras arcade 3D con clásicos argentinos rearmados, por las calles de Buenos Aires y el conurbano"),
            ("Plataforma", "PC (Steam)"),
            ("Lanzamiento", "Previsto para 2027"),
            ("Estado", "En desarrollo, todavía sin demo pública"),
            ("Jugadores y modos", "1 jugador: carreras contra rivales controlados por la computadora, tres dificultades, colección de autos y taller para tunearlos"),
            ("Idiomas", "Castellano"),
            ("Engine", "Unity"),
            ("País", "Argentina"),
            ("Contacto de prensa", f"Luciana Cardiello · {MAIL}"),
        ],
        "corta": "DESCRIPCIÓN CORTA",
        "larga": "DESCRIPCIÓN LARGA",
        "features": "FEATURES",
        "circuitos": "Circuitos",
        "secreta": "Y un circuito secreto para quien lo gana todo.",
        "estudio_t": "ESTUDIO Y EQUIPO",
        "estudio": "Lado Positivo es un estudio independiente de Buenos Aires, Argentina, que arma Conurban Streets a pulmón y a distancia.",
        "equipo": "Equipo",
        "anecdotas_t": "Para contar",
        "anecdotas": [
            "Los circuitos de La Boca y Dock Sud y del Mercado Central se arman sobre el trazado real de sus calles, sacado de OpenStreetMap, con las libertades de un videojuego.",
            "Por la pista circulan colectivos de las líneas 160, 164 y 60, que frenan en sus paradas y respetan los semáforos.",
            "Todos los autos andan sobre ruedas menos uno: el Renault 12 con turbinas, el premio mayor, con el que también se juega el tutorial.",
            "La música es de bandas urbanas de Buenos Aires: Chebrolet y Hocus Pocus.",
        ],
        "permisos_t": "PERMISOS",
        "permisos": "Podés streamear el juego y subir videos, y monetizarlos. Podés usar el logo, el key art, las capturas y los clips de este kit en notas y videos sobre el juego.",
        "contacto_t": "CONTACTO Y REDES",
        "kit_t": "QUÉ HAY EN ESTE KIT",
        "kit": [
            "logo/ - a color (crema), blanco, negro y púrpura sobre transparente; sobre fondo púrpura y negro; ícono",
            "key-art/ - key art en 16:9, 1:1, 4:5 y 9:16; en capas/ están el fondo sin logo y el logo por separado",
            "capturas/ - capturas del juego en 1920x1080, sin HUD ni marcas",
            "clips/ - clips cortos del juego (1080p, sin audio) para usar en notas y videos",
        ],
    },
    "en": {
        "titulo": "CONURBAN STREETS - PRESS KIT (ENGLISH)",
        "datos": "FACTS",
        "ficha": [
            ("Title", "Conurban Streets"),
            ("Developer and publisher", "Lado Positivo (self-published)"),
            ("Genre", "3D arcade racing with rebuilt Argentine classics through the streets of Buenos Aires and its suburbs"),
            ("Platform", "PC (Steam)"),
            ("Release", "Planned for 2027"),
            ("Status", "In development, no public demo yet"),
            ("Players and modes", "Single player: races against computer-controlled rivals, three difficulty levels, a car collection and a workshop to tune them"),
            ("Languages", "Spanish"),
            ("Engine", "Unity"),
            ("Country", "Argentina"),
            ("Press contact", f"Luciana Cardiello · {MAIL}"),
        ],
        "corta": "SHORT DESCRIPTION",
        "larga": "LONG DESCRIPTION",
        "features": "FEATURES",
        "circuitos": "Circuits",
        "secreta": "And a secret circuit for whoever wins it all.",
        "estudio_t": "STUDIO AND TEAM",
        "estudio": "Lado Positivo is an independent studio from Buenos Aires, Argentina, building Conurban Streets on a shoestring and fully remote.",
        "equipo": "Team",
        "anecdotas_t": "Worth telling",
        "anecdotas": [
            "The La Boca and Dock Sud and the Mercado Central circuits are built on the real layout of their streets, taken from OpenStreetMap, with a video game's creative license.",
            "Real city bus lines 160, 164 and 60 drive around the track, pulling over at their stops and waiting at the lights.",
            "Every car rolls on wheels except one: the Renault 12 on thrusters, the grand prize, which is also the car you play the tutorial with.",
            "The soundtrack comes from Buenos Aires urban bands: Chebrolet and Hocus Pocus.",
        ],
        "permisos_t": "PERMISSIONS",
        "permisos": "You can stream the game and upload videos, and monetize them. You can use the logo, key art, screenshots and clips in this kit in articles and videos about the game.",
        "contacto_t": "CONTACT AND SOCIAL",
        "kit_t": "WHAT'S IN THIS KIT",
        "kit": [
            "logo/ - color (cream), white, black and purple on transparent; on purple and black backgrounds; icon",
            "key-art/ - key art in 16:9, 1:1, 4:5 and 9:16; capas/ has the background without logo and the logo on its own",
            "capturas/ - in-game screenshots at 1920x1080, no HUD or watermarks",
            "clips/ - short gameplay clips (1080p, no audio) for articles and videos",
        ],
    },
}


def ficha(idioma):
    t, x = TEXTOS[idioma], EXTRA[idioma]
    # El "Chief Poronguer Officer" queda en los créditos del juego y en la web, no en prensa.
    equipo = [(r, n) for r, n in dict(t["ficha"])[x["equipo"]] if "Poronguer" not in r]
    pistas = [p for p in t["pistas"] if p[1] != SECRETA]
    lineas = [x["titulo"], "", f"== {x['datos']} =="]
    lineas += [f"{k}: {v}" for k, v in x["ficha"]]
    lineas += ["", f"== {x['corta']} ==", t["desc"], "", f"== {x['larga']} ==", t["intro"], ""]
    lineas += [f"{x['circuitos']}:"] + [f"- {p[1]}: {p[2]}" for p in pistas] + [x["secreta"]]
    lineas += ["", f"== {x['features']} =="] + [f"- {h}: {p}" for h, p in t["pilares"]]
    lineas += ["", f"== {x['estudio_t']} ==", x["estudio"], "", f"{x['equipo']}:"]
    lineas += [f"- {rol}: {nombres}" for rol, nombres in equipo] + [""]
    lineas += [f"{x['anecdotas_t']}:"] + [f"- {a}" for a in x["anecdotas"]]
    lineas += ["", f"== {x['permisos_t']} ==", x["permisos"]]
    lineas += ["", f"== {x['contacto_t']} ==", f"Mail: {MAIL}", f"Web: {URL}/" + ("" if idioma == "es" else "en/"),
               f"Instagram: {INSTAGRAM}", f"TikTok: {TIKTOK}"]
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


def cuadro_key_art():
    """El cuadro del video original, con las líneas de velocidad del menú encima."""
    import imageio_ffmpeg
    crudo = subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-loglevel", "error", "-ss", str(SEGUNDO_KEY_ART),
                            "-i", str(TOMA_KEY_ART), "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
                           check=True, capture_output=True).stdout
    img = Image.open(BytesIO(crudo)).convert("RGBA")
    lineas = Image.open(LINEAS).convert("RGBA").resize(img.size, Image.LANCZOS)
    lineas.putalpha(lineas.getchannel("A").point(lambda a: int(a * 0.85)))
    img.alpha_composite(lineas)
    return img.convert("RGB")


FONDO_KEY_ART = None


def key_art(w, h, ancho_logo, y_logo, alto_degrade, foco_x, foco_y):
    """Devuelve (fondo sin logo, key art completo) con el mismo recorte que las cápsulas de Steam."""
    fondo = capsulas.recorte(FONDO_KEY_ART, w, h, foco_x, foco_y)
    if w / h < 16 / 9:  # los formatos verticales agrandan el cuadro: un poco de nitidez
        fondo = fondo.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
    fondo = fondo.convert("RGBA")
    completo = fondo.copy()
    completo.alpha_composite(capsulas.degrade(w, h, alto_degrade))
    lg = capsulas.logo(int(w * ancho_logo))
    completo.alpha_composite(lg, ((w - lg.width) // 2, int(h * y_logo)))
    return fondo.convert("RGB"), completo.convert("RGB")


def main():
    global FONDO_KEY_ART
    FONDO_KEY_ART = cuadro_key_art()
    SALIDA.parent.mkdir(exist_ok=True)
    c = CARPETA
    with zipfile.ZipFile(SALIDA, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{c}/Conurban Streets - ficha (fact sheet).txt", ficha("es") + "\n\n" + ficha("en"))
        for f in sorted(LOGOS.glob("*.png")):
            z.write(f, f"{c}/logo/{f.name}")
        z.writestr(f"{c}/logo/conurban-streets-logo-blanco-transparente.png", png(logo_de_color((255, 255, 255))))
        for nombre, *medidas in KEY_ART:
            fondo, completo = key_art(*medidas)
            z.writestr(f"{c}/key-art/conurban-streets-key-art-{nombre}.png", png(completo))
            z.writestr(f"{c}/key-art/capas/fondo-sin-logo-{nombre}.png", png(fondo))
        z.write(LOGOS / "conurban-streets-logo-crema-transparente.png", f"{c}/key-art/capas/logo-crema-transparente.png")
        for nombre, origen in SELECCION:
            img = Image.open(CAPTURAS / origen).convert("RGB")
            if img.size != (1920, 1080):
                img = img.resize((1920, 1080), Image.LANCZOS)
            z.writestr(f"{c}/capturas/conurban-streets-{nombre}.png", png(img))
        for clip in CLIPS:  # ya vienen comprimidos: se guardan tal cual
            z.write(RECORTES / clip, f"{c}/clips/{clip}", compress_type=zipfile.ZIP_STORED)
    print(SALIDA, SALIDA.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
