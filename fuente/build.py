"""
Genera el sitio: index.html (castellano) y en/index.html (inglés) desde la misma plantilla.
Los textos de cada idioma están en TEXTOS; la estructura, en PLANTILLA.

Uso: python fuente/build.py
"""
from html import escape
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
URL = "https://crisoalmoniga.github.io/conurban-streets-web"  # cambiar por el dominio cuando esté (tarjeta 38)
MAIL = "conurbanstreets@gmail.com"
INSTAGRAM = "https://www.instagram.com/conurbanstreets/"
TIKTOK = "https://www.tiktok.com/@conurbanstreets"
LINKTREE = "https://linktr.ee/conurbanstreets"

CAPTURAS = [
    "01_escalada_chevrones", "02_escalada_esculturas", "03_escalada_salto", "04_escalada_tren_roca",
    "05_autodromo_turbinas", "06_autodromo_frente", "07_autodromo_fuego", "08_autodromo_noche",
    "09_caminonegro_peloton", "10_caminonegro_viaducto",
]

TEXTOS = {
    "es": {
        "lang": "es-AR", "base": "", "otro": "en/", "otro_txt": "EN",
        "titulo": "Conurban Streets – Carreras arcade en el conurbano",
        "desc": "Carreras arcade para PC en un conurbano bonaerense retrofuturista. Cyberpunk, pero del conurbano. Próximamente en Steam.",
        "nav": ["El juego", "Galería", "Prensa", "Colaborá"],
        "lema": "Cyberpunk, pero del conurbano.",
        "bajada": "Carreras arcade para PC · Próximamente en Steam",
        "b_redes": "Seguinos en Instagram", "b_prensa": "Prensa y publishers",
        "juego_t": "Qué es",
        "intro": "Conurban Streets es un arcade de autos en el conurbano bonaerense, reimaginado como un futuro cyberpunk atado con alambre. Nada de megaciudades cromadas: autos clásicos oxidados y calles que casi se pueden oler.",
        "pilares": [
            ("Fierros nacionales", "El Reno Doce, el Ciento47 y el Cinco Cero Cuatro: clásicos argentinos oxidados y rearmados con lo que había."),
            ("Lugares que conocés", "Circuitos inspirados en lugares reales del conurbano, en clave futurista improvisada."),
            ("Carreras cortas y caóticas", "Manejo arcade para agarrar y jugar, rivales que pelean cada curva y muros que no perdonan."),
            ("Humor de barrio", "Carteles, murales y lugares emblemáticos llenos de guiños para quien creció en el conurbano."),
        ],
        "pistas_t": "Los circuitos",
        "pistas": [
            ("01_escalada_chevrones", "Remedios de Escalada", "Al lado de las vías del tren, entre esculturas y carteles de barrio."),
            ("08_autodromo_noche", "Autódromo del Parque", "El autódromo de noche, con la ciudad de fondo."),
            ("10_caminonegro_viaducto", "Camino Negro", "Barrio, Riachuelo y el viaducto de Puente La Noria."),
        ],
        "galeria_t": "Galería",
        "galeria_nota": "Capturas del juego en desarrollo. El tráiler llega pronto.",
        "alt": [
            "Auto tuneado entre carteles con flechas verdes en Escalada, al atardecer",
            "Auto pasando bajo una escultura gigante de dos personas besándose",
            "Auto saltando con fuego entre flechas verdes",
            "El tren pasando al lado de la pista en Escalada",
            "Auto con turbinas a fondo en la recta del Autódromo",
            "Frente de un auto oxidado con los faros encendidos",
            "Auto verde con fuego en la recta del Autódromo",
            "Vista aérea del Autódromo iluminado de noche",
            "Pelotón entre carteles con flechas en Camino Negro",
            "Viaducto de Puente La Noria visto desde un dron",
        ],
        "cerrar": "Cerrar",
        "prensa_t": "Prensa y publishers",
        "prensa_intro": "¿Escribís sobre juegos o publicás juegos? Escribinos y te mandamos el press kit, el pitch deck o una build para probar.",
        "ficha": [
            ("Desarrollador", "Lado Positivo Games (Buenos Aires, Argentina)"),
            ("Género", "Carreras arcade 3D"),
            ("Plataforma", "PC (Steam)"),
            ("Fechas", "Demo a mediados de 2027 · lanzamiento a fines de 2027"),
            ("Equipo", "Cristian Almoniga (dirección y programación) · Romina Wendling (diseño gráfico)"),
        ],
        "b_kit": "Pedir el press kit",
        "kit_det": "Te lo mandamos por mail: logo, key art, capturas en alta resolución y descripciones en castellano e inglés.",
        "b_mail": "Escribinos",
        "asunto_prensa": "Prensa / publishers – Conurban Streets",
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
        "titulo": "Conurban Streets – Arcade racing in the Buenos Aires suburbs",
        "desc": "Arcade racing for PC in a retro-futuristic Buenos Aires suburb. Cyberpunk, but from the conurbano. Coming soon to Steam.",
        "nav": ["The game", "Gallery", "Press", "Collaborate"],
        "lema": "Cyberpunk, but from the conurbano.",
        "bajada": "Arcade racing for PC · Coming soon to Steam",
        "b_redes": "Follow us on Instagram", "b_prensa": "Press & publishers",
        "juego_t": "The game",
        "intro": "Conurban Streets is an arcade racer set in the suburbs of Buenos Aires, reimagined as a scrappy cyberpunk future. No chrome megacities here: just rusty classics and streets you can almost smell.",
        "pilares": [
            ("Fierros nacionales", "The Reno Doce, the Ciento47 and the Cinco Cero Cuatro: classic Argentine cars, rusted and rebuilt with whatever was lying around."),
            ("Places you know", "Circuits inspired by real places in the Buenos Aires suburbs, in an improvised retro-futuristic key."),
            ("Short, chaotic races", "Pick-up-and-play arcade handling, rivals that fight for every corner and walls that bite back."),
            ("Barrio humor", "Street signs, murals and local landmarks full of references for anyone who grew up in the conurbano."),
        ],
        "pistas_t": "The circuits",
        "pistas": [
            ("01_escalada_chevrones", "Remedios de Escalada", "Next to the train line, among sculptures and neighborhood signs."),
            ("08_autodromo_noche", "Autódromo del Parque", "The speedway at night, with the city skyline behind."),
            ("10_caminonegro_viaducto", "Camino Negro", "Narrow streets, the Riachuelo river and the Puente La Noria overpass."),
        ],
        "galeria_t": "Gallery",
        "galeria_nota": "Screenshots from the game in development. Trailer coming soon.",
        "alt": [
            "Tuned car racing between green arrow signs in Escalada at dusk",
            "Car passing under a giant sculpture of two people kissing",
            "Car jumping with flames between green arrow signs",
            "The train passing next to the track in Escalada",
            "Car at full throttle on the speedway straight",
            "Front of a rusty car with its headlights on",
            "Green car with flames on the speedway straight",
            "Aerial view of the speedway lit up at night",
            "Pack of cars between arrow signs in Camino Negro",
            "The Puente La Noria overpass seen from a drone",
        ],
        "cerrar": "Close",
        "prensa_t": "Press & publishers",
        "prensa_intro": "Writing about games or publishing them? Get in touch and we'll send you the press kit, our pitch deck or a build to try.",
        "ficha": [
            ("Developer", "Lado Positivo Games (Buenos Aires, Argentina)"),
            ("Genre", "3D arcade racing"),
            ("Platform", "PC (Steam)"),
            ("Dates", "Demo mid-2027 · launch late 2027"),
            ("Team", "Cristian Almoniga (direction & programming) · Romina Wendling (graphic design)"),
        ],
        "b_kit": "Request the press kit",
        "kit_det": "We'll email it to you: logo, key art, high-res screenshots and descriptions in Spanish and English.",
        "b_mail": "Contact us",
        "asunto_prensa": "Press / publishers – Conurban Streets",
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


def pagina(t):
    b = t["base"]
    e = escape
    pilares = "\n".join(
        f'<article class="pilar"><h3>{e(h)}</h3><p>{e(p)}</p></article>' for h, p in t["pilares"])
    pistas = "\n".join(
        f'<article class="pista"><img src="{b}assets/img/{img}_800.webp" alt="" loading="lazy" width="800" height="450">'
        f'<h3>{e(n)}</h3><p>{e(d)}</p></article>' for img, n, d in t["pistas"])
    galeria = "\n".join(
        f'<button type="button" data-grande="{b}assets/img/{c}_1600.webp" aria-label="{e(a)}">'
        f'<img src="{b}assets/img/{c}_800.webp" alt="{e(a)}" loading="lazy" width="800" height="450"></button>'
        for c, a in zip(CAPTURAS, t["alt"]))
    ficha = "\n".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in t["ficha"])
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
<meta property="og:type" content="website">
<meta property="og:title" content="Conurban Streets">
<meta property="og:description" content="{e(t['desc'])}">
<meta property="og:image" content="{URL}/assets/img/og.jpg">
<meta property="og:url" content="{canon}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#35072C">
<link rel="icon" href="{b}assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geom:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{b}assets/css/estilo.css">
</head>
<body>
<header class="barra">
  <a class="marca" href="#inicio"><img src="{b}assets/img/logo_600.webp" alt="Conurban Streets" width="600" height="194"></a>
  <nav>
    <a href="#juego">{e(n[0])}</a><a href="#galeria">{e(n[1])}</a><a href="#prensa">{e(n[2])}</a><a href="#sumate">{e(n[3])}</a>
    <a class="idioma" href="{t['otro']}" hreflang="{'en' if t['lang'] != 'en' else 'es'}">{t['otro_txt']}</a>
  </nav>
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
      <a class="boton secundario" href="{LINKTREE}" rel="noopener" target="_blank">Discord y más</a>
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
    en = pagina(TEXTOS["en"]).replace("Discord y más", "Discord & more")
    (RAIZ / "en" / "index.html").write_text(en, encoding="utf-8")
    print("index.html y en/index.html generados")


if __name__ == "__main__":
    main()
