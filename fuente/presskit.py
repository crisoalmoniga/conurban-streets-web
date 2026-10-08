"""
Arma el press kit para mandar por mail: Drive > Marketing > Prensa > conurban-streets-presskit.zip
(logo, capturas en 1920x1080 y la ficha con descripciones en castellano e inglés).

Uso: python fuente/presskit.py
"""
import zipfile
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
CAPTURAS = Path(r"G:\Mi unidad\Conurban Streets\Marketing\Steam\capturas")
LOGO = Path(r"G:\Mi unidad\Conurban Streets\Marketing\Pitch deck\fuente\assets\marca.png")
PORTADA = Path(r"G:\Mi unidad\Conurban Streets\Marketing\Pitch deck\fuente\assets\portada.png")
# Va a Drive y no al sitio: el press kit se manda por mail a quien lo pide, no se publica.
SALIDA = Path(r"G:\Mi unidad\Conurban Streets\Marketing\Prensa\conurban-streets-presskit.zip")
PURPURA = (53, 7, 44)

FICHA = """CONURBAN STREETS - PRESS KIT

== DATOS ==
Desarrollador: Lado Positivo Games (Buenos Aires, Argentina)
Género: carreras arcade 3D
Plataforma: PC (Steam)
Fecha: demo a mediados de 2027, lanzamiento a fines de 2027
Equipo: Cristian Almoniga (dirección, diseño de juego y programación), Romina Wendling (diseño gráfico)
Contacto: conurbanstreets@gmail.com
Redes: Instagram y TikTok @conurbanstreets - linktr.ee/conurbanstreets

== DESCRIPCIÓN CORTA ==
Carreras arcade en un conurbano bonaerense retrofuturista. Corré con autos clásicos argentinos oxidados y tuneados con lo que había por barrios, autopistas y un autódromo iluminado, en carreras cortas y caóticas. Cyberpunk, pero del conurbano.

== DESCRIPCIÓN LARGA ==
Conurban Streets es un arcade de autos en el conurbano bonaerense, reimaginado como un futuro cyberpunk atado con alambre. Nada de megaciudades cromadas: autos clásicos oxidados, atados con alambre, y calles que casi se pueden oler.

Fierros nacionales: el Reno Doce, el Ciento47 y el Cinco Cero Cuatro, clásicos argentinos oxidados y rearmados con lo que había.
Lugares que conocés: Remedios de Escalada al lado de las vías, el Autódromo del Parque de noche y Camino Negro, con su viaducto en Puente La Noria.
Carreras cortas y caóticas: manejo arcade para agarrar y jugar, rivales que pelean cada curva y muros que no perdonan.
Humor de barrio: carteles, murales y lugares emblemáticos llenos de guiños para quien creció en el conurbano.


CONURBAN STREETS - PRESS KIT (ENGLISH)

== FACTS ==
Developer: Lado Positivo Games (Buenos Aires, Argentina)
Genre: 3D arcade racing
Platform: PC (Steam)
Dates: demo mid-2027, launch late 2027
Team: Cristian Almoniga (direction, game design and programming), Romina Wendling (graphic design)
Contact: conurbanstreets@gmail.com
Social: Instagram and TikTok @conurbanstreets - linktr.ee/conurbanstreets

== SHORT DESCRIPTION ==
Arcade racing in a retro-futuristic Buenos Aires suburb. Race rusty classic Argentine cars, tuned with whatever was lying around, through neighborhoods, overpasses and a night-lit speedway in short, chaotic races. Cyberpunk, but from the conurbano.

== LONG DESCRIPTION ==
Conurban Streets is an arcade racer set in the suburbs of Buenos Aires, reimagined as a scrappy cyberpunk future. No chrome megacities here: just rusty classics held together with wire, and streets you can almost smell.

Fierros nacionales: drive the Reno Doce, the Ciento47 and the Cinco Cero Cuatro, classic Argentine cars rusted and rebuilt with whatever was lying around.
Places you know: Remedios de Escalada next to the train line, the night-lit Autódromo del Parque, and Camino Negro with its elevated overpass at Puente La Noria.
Short, chaotic races: pick-up-and-play arcade handling, rivals that fight for every corner and walls that bite back.
Barrio humor: street signs, murals and local landmarks full of references for anyone who grew up in the conurbano.
"""


def main():
    SALIDA.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(SALIDA, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("Conurban Streets - ficha (fact sheet).txt", FICHA)
        z.write(LOGO, "logo/conurban-streets-logo-transparente.png")
        logo = Image.open(LOGO).convert("RGBA")
        fondo = Image.new("RGBA", (logo.width + 200, logo.height + 200), PURPURA + (255,))
        fondo.alpha_composite(logo, (100, 100))
        tmp = RAIZ / "fuente" / "_logo_fondo.png"
        fondo.convert("RGB").save(tmp)
        z.write(tmp, "logo/conurban-streets-logo-fondo-purpura.png")
        tmp.unlink()
        z.write(PORTADA, "key-art/conurban-streets-portada.png")
        for f in sorted(CAPTURAS.glob("*.png")):
            z.write(f, f"capturas/{f.name}")
    print(SALIDA, SALIDA.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
