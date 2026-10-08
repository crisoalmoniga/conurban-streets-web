"""
Íconos del sitio a partir de la "C" del logo (el recorte de papel crema), sobre el púrpura de la marca:
favicon.ico (16/32/48), favicon-32.png, apple-touch-icon (180), icon-192, icon-512 e icon-maskable-512.

Uso: python fuente/iconos.py
"""
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
LOGO = Path(r"G:\Mi unidad\Conurban Streets\Marketing\Pitch deck\fuente\assets\marca.png")
SALIDA = RAIZ / "assets" / "img"
PURPURA = (53, 7, 44, 255)
RECORTE_C = (0, 12, 212, 350)  # la tira de papel con la "C", en píxeles del logo


def tira_c():
    """La tira de papel de la "C" sola, sin las salpicaduras de las letras vecinas."""
    tira = np.array(Image.open(LOGO).convert("RGBA").crop(RECORTE_C))
    _, etiquetas, stats, _ = cv2.connectedComponentsWithStats((tira[..., 3] > 40).astype(np.uint8), connectivity=8)
    mayor = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    mascara = cv2.morphologyEx((etiquetas == mayor).astype(np.uint8), cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    tira[..., 3] = np.where(mascara > 0, tira[..., 3], 0)
    img = Image.fromarray(tira)
    return img.crop(img.getbbox())


def icono(lado, ocupa=0.82, giro=-4):
    letra = tira_c().rotate(giro, Image.BICUBIC, expand=True)
    escala = lado * ocupa / max(letra.size)
    letra = letra.resize((max(1, round(letra.width * escala)), max(1, round(letra.height * escala))), Image.LANCZOS)
    img = Image.new("RGBA", (lado, lado), PURPURA)
    img.alpha_composite(letra, ((lado - letra.width) // 2, (lado - letra.height) // 2))
    return img


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    icono(32).save(SALIDA / "favicon-32.png")
    icono(180).save(SALIDA / "apple-touch-icon.png")
    icono(192).save(SALIDA / "icon-192.png")
    icono(512).save(SALIDA / "icon-512.png")
    icono(512, ocupa=0.6).save(SALIDA / "icon-maskable-512.png")  # margen para los recortes redondos de Android
    icono(256).save(RAIZ / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    vieja = SALIDA / "favicon.png"
    if vieja.exists():
        vieja.unlink()
    print("íconos generados")


if __name__ == "__main__":
    main()
