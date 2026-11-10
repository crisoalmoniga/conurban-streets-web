"""
Genera el sitio: index.html (castellano) y en/index.html (inglés) desde la misma plantilla.
Los textos de cada idioma están en TEXTOS; la estructura, en PLANTILLA.

Uso: python fuente/build.py
"""
import hashlib
import json
from html import escape
from pathlib import Path
from urllib.parse import urlparse

RAIZ = Path(__file__).resolve().parent.parent
URL = "https://crisoalmoniga.github.io/conurban-streets-web"  # cambiar por el dominio cuando esté (tarjeta 38)
MAIL = "conurbanstreets@gmail.com"
# Versión de la hoja de estilos: cambia con su contenido, así el navegador no usa una copia vieja.
VERSION_CSS = hashlib.md5((RAIZ / "assets" / "css" / "estilo.css").read_bytes()).hexdigest()[:8]
INSTAGRAM = "https://www.instagram.com/conurbanstreets/"
TIKTOK = "https://www.tiktok.com/@conurbanstreets"

CAPTURAS = [
    "01_escalada_atardecer", "02_escalada_reno", "19_autodromo_grilla", "03_autodromo_turbinas",
    "25_autodromo_147", "24_autodromo_c10", "05_autodromo_neon", "06_caminonegro_curva",
    "07_caminonegro_autopista", "08_caminonegro_chevrones", "17_caminonegro_colectivo", "20_docksud_grilla",
    "09_docksud_usina", "22_docksud_504", "10_docksud_puente", "18_docksud_laboca", "11_mercado_nave",
    "21_mercado_504", "23_mercado_c10", "12_mercado_turbinas", "13_menemista_largada", "14_menemista_favela",
    "15_menemista_subida", "16_menemista_tunel",
]

TEXTOS = {
    "es": {
        "lang": "es-AR", "base": "", "otro": "en/", "otro_txt": "EN",
        "og_locale": "es_AR", "og_locale_otro": "en_US",
        "og_alt": "Logo de Conurban Streets sobre un auto tuneado con fuego en una pista del conurbano",
        "titulo": "Conurban Streets – Carreras arcade por las calles de Buenos Aires",
        "desc": "Carreras arcade para PC por las calles de Buenos Aires, de la Ciudad al conurbano, con clásicos argentinos y un futuro atado con alambre. Lanzamiento previsto para 2027.",
        "nav": ["El juego", "Galería", "Prensa", "Colaborá"],
        "lema": "El futuro, pero acá nomás.",
        "bajada": "Carreras arcade para PC · Próximamente",
        "b_redes": "Seguinos en Instagram", "b_prensa": "Prensa",
        "juego_t": "Qué es",
        "intro": "Conurban Streets es un arcade de autos por las calles de Buenos Aires, de la Ciudad al conurbano. Arrancás con fierros de los de siempre, clásicos argentinos gastados y sobre ruedas, y carrera a carrera vas por el premio mayor: autos rearmados con turbinas que flotan sobre el asfalto. Nada de megaciudades cromadas: un futuro atado con alambre y calles que casi se pueden oler. El lanzamiento está pensado para 2027.",
        "pilares": [
            ("Los fierros de siempre", "El Renault 12, el Fiat 147, el Peugeot 504 y la Chevrolet C10: clásicos argentinos gastados y rearmados con lo que había, cada uno con su manejo. Todos andan sobre ruedas, hasta que te ganás el premio mayor: el 12 con turbinas, que flota."),
            ("Lugares que conocés", "Pistas inspiradas en toda Buenos Aires, en las calles por donde caminás todos los días: de La Boca y el Autódromo a Escalada y el Mercado Central, en clave futurista improvisada."),
            ("Carreras cortas y caóticas", "Manejo arcade para agarrar y jugar, tres dificultades, nitro para el último empujón, rivales que pelean cada curva y muros que no perdonan."),
            ("Armá tu colección", "Cada carrera suma puntos y cada pista que ganás destraba un fierro nuevo. Con los puntos comprás piezas de motor, dirección y nitro, y tuneás cada auto a mano en el taller."),
            ("La calle no espera", "Bondis que frenan en cada parada, semáforos, camiones con acoplado y piedras que caen de los puentes peatonales y te rajan el parabrisas."),
            ("Humor de barrio", "Carteles, murales y lugares de siempre, llenos de guiños para quien se crió de un lado o del otro de la General Paz. Con las calles que ya conocés y música de artistas urbanos de acá nomás."),
        ],
        "pistas_t": "Los circuitos",
        "pistas": [
            ("02_escalada_reno", "Remedios de Escalada", "Al lado de las vías del tren, entre esculturas y carteles de barrio."),
            ("03_autodromo_turbinas", "Autódromo del Parque", "El autódromo de noche, con la ciudad de fondo."),
            ("07_caminonegro_autopista", "Camino Negro", "Barrio, Riachuelo, el viaducto de Puente La Noria y puentes peatonales desde donde te tiran piedras."),
            ("09_docksud_usina", "La Boca y Dock Sud", "Por la ribera del Riachuelo, entre la Usina del Arte y los puentes de hierro."),
            ("11_mercado_nave", "Mercado Central", "De madrugada, entre camiones y por adentro de las naves."),
            ("14_menemista_favela", "Vacaciones menemistas", "El premio para quien lo gana todo: las subidas de una favela de Río, el túnel bajo el morro y el Cristo mirando desde arriba.", "Desbloqueable"),
        ],
        "galeria_t": "Galería",
        "galeria_nota": "Capturas del juego en desarrollo. El tráiler llega pronto.",
        "alt": [
            "Un Fiat 147 con los faros encendidos bajo el cielo rojo del atardecer en Escalada",
            "El Renault 12 de frente en una avenida de Escalada, al atardecer",
            "El Renault 12 con turbinas flota en la grilla del Autódromo, al lado de un Fiat 147 sobre ruedas",
            "El Renault 12 con las turbinas a fondo junto al vallado rojo y blanco del Autódromo",
            "Un Fiat 147 sobre ruedas en el Autódromo, con la ciudad de fondo",
            "La Chevrolet C10 junto al vallado rojo y blanco del Autódromo",
            "Flechas de neón sobre la pista del Autódromo",
            "Dos autos en una curva cerrada de Camino Negro, vistos desde un dron",
            "El Renault 12 en la autopista de Camino Negro, entre torres de alta tensión",
            "El Renault 12 con turbinas entre carteles de curva en Camino Negro",
            "Un colectivo de la 160 frena en el semáforo bajo un pórtico de neón en Camino Negro",
            "Largada en Dock Sud: el Renault 12 con turbinas entre los Fiat 147 de siempre",
            "La Usina del Arte iluminada de noche en Dock Sud, con un auto en la pista",
            "El Peugeot 504 en una curva de Dock Sud, de noche",
            "Cruzando el puente de hierro rojo sobre el Riachuelo",
            "Un auto entre conventillos de colores en La Boca, con un colectivo de frente",
            "La pista entra a una nave del Mercado Central",
            "Un Peugeot 504 rojo y blanco entre los puestos de fruta del Mercado Central",
            "Una Chevrolet C10 verde y oxidada adentro de una nave del Mercado Central",
            "El Renault 12 con las turbinas a fondo en el Mercado Central",
            "La largada de Vacaciones menemistas al atardecer, con palmeras y el Cristo sobre el morro",
            "Bajada entre casas de ladrillo a la vista, cables y carteles de curva en la favela",
            "Subida por la favela con el guardrail verde y amarillo",
            "Saliendo del túnel bajo el morro, con la favela iluminada de fondo",
        ],
        "cerrar": "Cerrar", "saltar": "Saltar al contenido", "menu": "Abrir el menú",
        "prensa_t": "Prensa",
        "prensa_intro": "¿Escribís sobre juegos o hacés contenido? Escribinos y te mandamos el press kit o una build para probar.",
        "ficha": [
            ("Desarrollador", "Lado Positivo Games (Buenos Aires, Argentina)"),
            ("Género", "Carreras arcade 3D"),
            ("Plataforma", "PC"),
            ("Lanzamiento", "Pensado para 2027"),
            # Igual que los créditos del juego (Assets/_Project/Resources/Creditos.txt)
            ("Equipo", [
                ("Dirección y game design", "Cristian Almóniga"),
                ("Chief Poronguer Officer", "Pablo Sekine"),
                ("Programación", "Cristian Almóniga · Mayra"),
                ("Diseño gráfico", "Romina Wendling"),
                ("Modelado 3D", "Cristian Almóniga · Héctor Donoso"),
                ("Audio", "Pablo Sekine · Lautaro Dichio"),
                ("Música", "Chebrolet · Hocus Pocus"),
                ("Testing", "Jota Barbagallo"),
            ]),
        ],
        "b_kit": "Pedir el press kit",
        "kit_det": "Te lo mandamos por mail: logo, key art, capturas en alta resolución y descripciones en castellano e inglés.",
        "b_mail": "Escribinos",
        "asunto_prensa": "Prensa – Conurban Streets",
        "asunto_kit": "Pedido de press kit – Conurban Streets",
        "redes_t": "Seguinos",
        "redes_intro": "Novedades, capturas y clips del desarrollo.",
        "sumate_t": "¿Querés colaborar?",
        "sumate_intro": "Conurban Streets es un proyecto indie que se arma a pulmón y a distancia. Si te copa el juego y tenés ganas de darnos una mano, escribinos y charlamos.",
        "asunto_sumate": "Quiero colaborar – Conurban Streets",
        "pie": "© 2026 Lado Positivo Games. Conurban Streets está en desarrollo.",
    },
    "en": {
        "lang": "en", "base": "../", "otro": "../", "otro_txt": "ES",
        "og_locale": "en_US", "og_locale_otro": "es_AR",
        "og_alt": "Conurban Streets logo over a tuned car shooting flames on a suburban race track",
        "titulo": "Conurban Streets – Arcade racing through the streets of Buenos Aires",
        "desc": "Arcade racing for PC through the streets of Buenos Aires, from the city to its suburbs, with Argentine classics and a future held together with wire. Planned for release in 2027.",
        "nav": ["The game", "Gallery", "Press", "Collaborate"],
        "lema": "The future, right around the corner.",
        "bajada": "Arcade racing for PC · Coming soon",
        "b_redes": "Follow us on Instagram", "b_prensa": "Press",
        "juego_t": "The game",
        "intro": "Conurban Streets is an arcade racer through the streets of Buenos Aires, from the city to its suburbs. You start out in everyday rides, beaten-up Argentine classics on good old wheels, and race by race you chase the grand prize: cars rebuilt with thrusters that hover over the asphalt. No chrome megacities here: just a future held together with wire and streets you can almost smell. Release is planned for 2027.",
        "pilares": [
            ("Good old rides", "The Renault 12, the Fiat 147, the Peugeot 504 and the Chevrolet C10 pickup: classic Argentine cars, beaten up and rebuilt with whatever was lying around, each with its own handling. They all roll on good old wheels, until you earn the grand prize: the 12 on thrusters, hovering."),
            ("Places you know", "Tracks inspired by all of Buenos Aires, on the streets you walk every day: from La Boca and the Autódromo to Escalada and the Mercado Central, in an improvised retro-futuristic key."),
            ("Short, chaotic races", "Pick-up-and-play arcade handling, three difficulty levels, nitro for that last push, rivals that fight for every corner and walls that bite back."),
            ("Build your collection", "Every race earns points and every circuit you win unlocks a new ride. Spend the points on engine, handling and nitro parts, then tune each car by hand in the workshop."),
            ("The street won't wait", "City buses pulling over at every stop, traffic lights, trucks hauling trailers and rocks dropped from footbridges that crack your windshield."),
            ("Barrio humor", "Street signs, murals and local landmarks full of nods for anyone who grew up on either side of the General Paz. With streets you already know and music by local urban artists from right around the corner."),
        ],
        "pistas_t": "The circuits",
        "pistas": [
            ("02_escalada_reno", "Remedios de Escalada", "Next to the train line, among sculptures and neighborhood signs."),
            ("03_autodromo_turbinas", "Autódromo del Parque", "The speedway at night, with the city skyline behind."),
            ("07_caminonegro_autopista", "Camino Negro", "Narrow streets, the Riachuelo river, the Puente La Noria overpass and footbridges where someone's waiting with rocks."),
            ("09_docksud_usina", "La Boca and Dock Sud", "Along the Riachuelo riverside, past the Usina del Arte and the iron bridges."),
            ("11_mercado_nave", "Mercado Central", "Before dawn, between trucks and right through the market halls."),
            ("14_menemista_favela", "Vacaciones menemistas", "The prize for winning it all: the steep streets of a Rio favela, the tunnel under the hill and Christ the Redeemer watching from above.", "Unlockable"),
        ],
        "galeria_t": "Gallery",
        "galeria_nota": "Screenshots from the game in development. Trailer coming soon.",
        "alt": [
            "A Fiat 147 with its headlights on under a red sunset sky in Escalada",
            "The Renault 12 head-on along an avenue in Escalada at dusk",
            "The Renault 12 hovers on thrusters on the speedway grid, next to a Fiat 147 on wheels",
            "The Renault 12 at full thrust next to the red-and-white barriers of the speedway",
            "A Fiat 147 on wheels at the speedway, with the city skyline behind",
            "The Chevrolet C10 by the red-and-white barriers of the speedway",
            "Neon arrows over the speedway track",
            "Two cars in a tight corner in Camino Negro, seen from a drone",
            "The Renault 12 on the Camino Negro highway, between high-voltage towers",
            "The Renault 12 with thrusters between curve signs in Camino Negro",
            "A 160 bus stopping at the traffic light under a neon gantry in Camino Negro",
            "Starting grid in Dock Sud: the thruster-powered Renault 12 among good old Fiat 147s",
            "The Usina del Arte lit up at night in Dock Sud, with a car on the track",
            "The Peugeot 504 through a corner in Dock Sud at night",
            "Crossing the red iron bridge over the Riachuelo",
            "A car between colorful tenement houses in La Boca, with a bus coming the other way",
            "The track heads into one of the Mercado Central halls",
            "A red-and-white Peugeot 504 between the fruit stalls of the Mercado Central",
            "A rusty green Chevrolet C10 inside one of the Mercado Central halls",
            "The Renault 12 at full thrust in the Mercado Central",
            "The Vacaciones menemistas starting line at sunset, with palm trees and Christ the Redeemer on the hill",
            "Downhill between bare-brick houses, power lines and curve signs in the favela",
            "Climbing through the favela along the green-and-yellow guardrail",
            "Coming out of the tunnel under the hill, with the favela lit up behind",
        ],
        "cerrar": "Close", "saltar": "Skip to content", "menu": "Open menu",
        "prensa_t": "Press",
        "prensa_intro": "Writing about games or making content? Get in touch and we'll send you the press kit or a build to try.",
        "ficha": [
            ("Developer", "Lado Positivo Games (Buenos Aires, Argentina)"),
            ("Genre", "3D arcade racing"),
            ("Platform", "PC"),
            ("Release", "Planned for 2027"),
            ("Team", [
                ("Direction & game design", "Cristian Almóniga"),
                ("Chief Poronguer Officer", "Pablo Sekine"),
                ("Programming", "Cristian Almóniga · Mayra"),
                ("Graphic design", "Romina Wendling"),
                ("3D modeling", "Cristian Almóniga · Héctor Donoso"),
                ("Audio", "Pablo Sekine · Lautaro Dichio"),
                ("Music", "Chebrolet · Hocus Pocus"),
                ("Testing", "Jota Barbagallo"),
            ]),
        ],
        "b_kit": "Request the press kit",
        "kit_det": "We'll email it to you: logo, key art, high-res screenshots and descriptions in Spanish and English.",
        "b_mail": "Contact us",
        "asunto_prensa": "Press – Conurban Streets",
        "asunto_kit": "Press kit request – Conurban Streets",
        "redes_t": "Follow us",
        "redes_intro": "News, screenshots and dev clips.",
        "sumate_t": "Want to collaborate?",
        "sumate_intro": "Conurban Streets is an indie project, built with heart and from afar. If you dig the game and feel like lending a hand, drop us a line and let's talk.",
        "asunto_sumate": "I want to collaborate – Conurban Streets",
        "pie": "© 2026 Lado Positivo Games. Conurban Streets is in development.",
    },
}


def mailto(asunto):
    return f"mailto:{MAIL}?subject={escape(asunto).replace(' ', '%20')}"


def etiqueta(texto):
    """Cartelito al lado del nombre de una pista (por ejemplo, "Desbloqueable")."""
    return f' <span class="etiqueta">{escape(texto)}</span>'


def dato_ficha(valor):
    """Un texto, o una lista de (rol, nombres) como la del equipo: un rol por renglón."""
    if isinstance(valor, str):
        return escape(valor)
    filas = "".join(f'<li><span class="rol">{escape(r)}</span> {escape(n)}</li>' for r, n in valor)
    return f'<ul class="equipo">{filas}</ul>'


def datos_estructurados(t, canon):
    """Ficha del juego para buscadores (schema.org/VideoGame)."""
    datos = {
        "@context": "https://schema.org",
        "@type": "VideoGame",
        "name": "Conurban Streets",
        "url": canon,
        "description": t["desc"],
        "image": f"{URL}/assets/img/og.jpg",
        "inLanguage": t["lang"],
        "genre": ["Racing", "Arcade"],
        "gamePlatform": "PC",
        "operatingSystem": "Windows",
        "playMode": "SinglePlayer",
        "author": {"@type": "Organization", "name": "Lado Positivo Games", "email": MAIL},
        "sameAs": [INSTAGRAM, TIKTOK],
    }
    return json.dumps(datos, ensure_ascii=False)


def extras():
    """Archivos que acompañan a la página: 404, manifiesto, robots, sitemap y .nojekyll."""
    base = urlparse(URL).path.rstrip("/") + "/"
    (RAIZ / "404.html").write_text(f"""<!doctype html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Página no encontrada – Conurban Streets</title>
<meta name="robots" content="noindex">
<meta name="theme-color" content="#35072C">
<link rel="icon" href="{base}favicon.ico" sizes="48x48">
<link href="https://fonts.googleapis.com/css2?family=Geom:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/css/estilo.css?v={VERSION_CSS}">
</head>
<body>
<main class="perdido">
  <img src="{base}assets/img/logo_600.webp" alt="Conurban Streets" width="600" height="194">
  <h1><span class="tira">404</span></h1>
  <p>Esta calle no existe. Capaz que doblaste donde no era.</p>
  <p lang="en">This street doesn't exist. Looks like you took a wrong turn.</p>
  <p><a class="boton" href="{base}">Volver al inicio</a> <a class="boton secundario" href="{base}en/">Home (English)</a></p>
</main>
</body>
</html>
""", encoding="utf-8")
    manifiesto = {
        "name": "Conurban Streets",
        "short_name": "Conurban",
        "description": TEXTOS["es"]["desc"],
        "start_url": base,
        "scope": base,
        "display": "browser",
        "background_color": "#35072C",
        "theme_color": "#35072C",
        "icons": [
            {"src": f"{base}assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": f"{base}assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": f"{base}assets/img/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
    }
    (RAIZ / "site.webmanifest").write_text(json.dumps(manifiesto, ensure_ascii=False, indent=2), encoding="utf-8")
    (RAIZ / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {URL}/sitemap.xml\n", encoding="utf-8")
    alternos = (f'    <xhtml:link rel="alternate" hreflang="es" href="{URL}/"/>\n'
                f'    <xhtml:link rel="alternate" hreflang="en" href="{URL}/en/"/>\n')
    urls = "".join(f"  <url>\n    <loc>{URL}{p}</loc>\n{alternos}  </url>\n" for p in ("/", "/en/"))
    (RAIZ / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        f"{urls}</urlset>\n", encoding="utf-8")
    (RAIZ / ".nojekyll").write_text("", encoding="utf-8")


def pagina(t):
    b = t["base"]
    e = escape
    pilares = "\n".join(
        f'<article class="pilar"><h3>{e(h)}</h3><p>{e(p)}</p></article>' for h, p in t["pilares"])
    pistas = "\n".join(
        f'<article class="pista"><img src="{b}assets/img/{img}_800.webp" alt="" loading="lazy" width="800" height="450">'
        f'<h3>{e(n)}{"".join(etiqueta(x) for x in extra)}</h3><p>{e(d)}</p></article>'
        for img, n, d, *extra in t["pistas"])
    galeria = "\n".join(
        f'<button type="button" data-grande="{b}assets/img/{c}_1600.webp" aria-label="{e(a)}">'
        f'<img src="{b}assets/img/{c}_800.webp" alt="{e(a)}" loading="lazy" width="800" height="450"></button>'
        for c, a in zip(CAPTURAS, t["alt"]))
    ficha = "\n".join(f"<dt>{e(k)}</dt><dd>{dato_ficha(v)}</dd>" for k, v in t["ficha"])
    n = t["nav"]
    canon = URL + ("/" if t["lang"] != "en" else "/en/")
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t['titulo'])}</title>
<meta name="description" content="{e(t['desc'])}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="es" href="{URL}/">
<link rel="alternate" hreflang="en" href="{URL}/en/">
<link rel="alternate" hreflang="x-default" href="{URL}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Conurban Streets">
<meta property="og:title" content="Conurban Streets">
<meta property="og:description" content="{e(t['desc'])}">
<meta property="og:image" content="{URL}/assets/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(t['og_alt'])}">
<meta property="og:url" content="{canon}">
<meta property="og:locale" content="{t['og_locale']}">
<meta property="og:locale:alternate" content="{t['og_locale_otro']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Conurban Streets">
<meta name="twitter:description" content="{e(t['desc'])}">
<meta name="twitter:image" content="{URL}/assets/img/og.jpg">
<meta name="theme-color" content="#35072C">
<meta name="color-scheme" content="dark">
<link rel="icon" href="{b}favicon.ico" sizes="48x48">
<link rel="icon" href="{b}assets/img/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="{b}assets/img/apple-touch-icon.png">
<link rel="manifest" href="{b}site.webmanifest">
<link rel="preload" as="image" href="{b}assets/video/loop_poster.jpg">
<script type="application/ld+json">{datos_estructurados(t, canon)}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geom:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{b}assets/css/estilo.css?v={VERSION_CSS}">
</head>
<body>
<a class="saltar" href="#juego">{e(t['saltar'])}</a>
<header class="barra">
  <a class="marca" href="#inicio"><img src="{b}assets/img/logo_600.webp" alt="Conurban Streets" width="600" height="194"></a>
  <div class="acciones">
    <nav class="menu" id="menu">
      <a href="#juego">{e(n[0])}</a><a href="#galeria">{e(n[1])}</a><a href="#prensa">{e(n[2])}</a><a href="#sumate">{e(n[3])}</a>
    </nav>
    <a class="idioma" href="{t['otro']}" hreflang="{'en' if t['lang'] != 'en' else 'es'}">{t['otro_txt']}</a>
    <button class="hamburguesa" type="button" aria-expanded="false" aria-controls="menu" aria-label="{e(t['menu'])}"><span></span><span></span><span></span></button>
  </div>
</header>

<main>
<section class="hero" id="inicio">
  <video autoplay muted loop playsinline poster="{b}assets/video/loop_poster.jpg" aria-hidden="true">
    <source src="{b}assets/video/loop.mp4" type="video/mp4">
  </video>
  <div>
    <h1 style="margin:0"><img class="logo" src="{b}assets/img/logo_1200.webp" alt="Conurban Streets" width="1200" height="388"></h1>
    <span class="tira">Conurpunk</span>
    <p class="lema">{e(t['lema'])}</p>
    <p class="bajada">{e(t['bajada'])}</p>
    <div class="botones">
      <a class="boton" href="{INSTAGRAM}" rel="noopener" target="_blank">{e(t['b_redes'])}</a>
      <a class="boton secundario" href="#prensa">{e(t['b_prensa'])}</a>
    </div>
  </div>
</section>

<section id="juego">
  <div class="contenedor">
    <h2><span class="tira">{e(t['juego_t'])}</span></h2>
    <p class="intro">{e(t['intro'])}</p>
    <div class="pilares">
{pilares}
    </div>
  </div>
</section>

<section class="alterna" id="pistas">
  <div class="contenedor">
    <h2><span class="tira">{e(t['pistas_t'])}</span></h2>
    <div class="pistas">
{pistas}
    </div>
  </div>
</section>

<section id="galeria">
  <div class="contenedor">
    <h2><span class="tira">{e(t['galeria_t'])}</span></h2>
    <div class="galeria">
{galeria}
    </div>
    <p class="nota">{e(t['galeria_nota'])}</p>
  </div>
  <dialog class="visor" id="visor">
    <form method="dialog"><button aria-label="{e(t['cerrar'])}">×</button></form>
    <img alt="">
  </dialog>
</section>

<section class="alterna" id="prensa">
  <div class="contenedor">
    <h2><span class="tira">{e(t['prensa_t'])}</span></h2>
    <div class="prensa">
      <div>
        <p>{e(t['prensa_intro'])}</p>
        <dl class="ficha">
{ficha}
        </dl>
      </div>
      <div>
        <p><a class="boton" href="{mailto(t['asunto_kit'])}">{e(t['b_kit'])}</a></p>
        <p>{e(t['kit_det'])}</p>
        <p><a class="boton secundario" href="{mailto(t['asunto_prensa'])}">{e(t['b_mail'])}: {MAIL}</a></p>
      </div>
    </div>
  </div>
</section>

<section id="redes">
  <div class="contenedor">
    <h2><span class="tira">{e(t['redes_t'])}</span></h2>
    <p>{e(t['redes_intro'])}</p>
    <div class="redes">
      <a class="boton" href="{INSTAGRAM}" rel="noopener" target="_blank">Instagram</a>
      <a class="boton" href="{TIKTOK}" rel="noopener" target="_blank">TikTok</a>
    </div>
  </div>
</section>

<section class="alterna" id="sumate">
  <div class="contenedor">
    <h2><span class="tira">{e(t['sumate_t'])}</span></h2>
    <p>{e(t['sumate_intro'])}</p>
    <p><a class="boton" href="{mailto(t['asunto_sumate'])}">{MAIL}</a></p>
  </div>
</section>
</main>

<footer>{e(t['pie'])}</footer>

<script>
  // Visor de capturas
  const visor = document.getElementById('visor');
  const grande = visor.querySelector('img');
  document.querySelectorAll('.galeria button').forEach(b => b.addEventListener('click', () => {{
    grande.src = b.dataset.grande; grande.alt = b.getAttribute('aria-label'); visor.showModal();
  }}));
  visor.addEventListener('click', ev => {{ if (ev.target === visor) visor.close(); }});
  // Menú hamburguesa (celular)
  const boton = document.querySelector('.hamburguesa'), cabecera = document.querySelector('.barra');
  const menu = abierto => {{ cabecera.classList.toggle('abierta', abierto); boton.setAttribute('aria-expanded', abierto); }};
  boton.addEventListener('click', () => menu(!cabecera.classList.contains('abierta')));
  document.querySelectorAll('#menu a').forEach(a => a.addEventListener('click', () => menu(false)));
  document.addEventListener('keydown', ev => {{ if (ev.key === 'Escape') menu(false); }});
  matchMedia('(min-width: 721px)').addEventListener('change', ev => {{ if (ev.matches) menu(false); }});
  // La barra toma fondo y muestra el logo chico al bajar de la portada
  const barra = document.querySelector('.barra'), hero = document.querySelector('.hero');
  new IntersectionObserver(([en]) => barra.classList.toggle('abajo', !en.isIntersecting), {{ rootMargin: '-80px 0px 0px 0px' }}).observe(hero);
  // Sin video en movimiento si el sistema pide reducir animaciones
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) document.querySelector('.hero video').pause();
</script>
</body>
</html>
"""


def main():
    (RAIZ / "index.html").write_text(pagina(TEXTOS["es"]), encoding="utf-8")
    (RAIZ / "en").mkdir(exist_ok=True)
    en = pagina(TEXTOS["en"])
    (RAIZ / "en" / "index.html").write_text(en, encoding="utf-8")
    extras()
    print("index.html, en/index.html, 404.html, site.webmanifest, robots.txt y sitemap.xml generados")


if __name__ == "__main__":
    main()
