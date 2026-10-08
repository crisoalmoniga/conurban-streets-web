# Conurban Streets – sitio web

Página del juego con sección de prensa. Sitio estático: no necesita servidor ni base de datos.

- `index.html` (castellano) y `en/index.html` (inglés) **se generan**: no editarlos a mano.
- Textos de los dos idiomas: `fuente/build.py` (diccionario `TEXTOS`).
- Estilos: `assets/css/estilo.css` (colores del brand book).
- Press kit: **no se publica en el sitio**. `fuente/presskit.py` lo arma en Drive (`Marketing/Prensa/conurban-streets-presskit.zip`) con el logo, el key art, las capturas de `Marketing/Steam/capturas` y la ficha, para mandarlo por mail a quien lo pida. La página tiene un botón que abre un mail de pedido.

## Actualizar

```bash
python fuente/build.py     # página en los dos idiomas + 404, manifiesto, robots.txt y sitemap.xml
python fuente/iconos.py    # favicon e íconos (solo si cambia el logo)
python fuente/presskit.py  # press kit en Drive
```

Para verla en la compu: `python -m http.server 8765` y abrir http://localhost:8765

## Publicar (gratis)

Opción A, GitHub Pages:
1. Crear un repositorio nuevo en GitHub (por ejemplo `conurban-streets-web`) y subir esta carpeta.
2. En el repositorio: Settings > Pages > Deploy from a branch > `main` / raíz.
3. Queda en `https://<usuario>.github.io/conurban-streets-web/`.

Opción B, Cloudflare Pages: conectar el repositorio, sin comando de build y con la raíz como carpeta de salida.

Cuando esté el dominio (tarjeta 38), apuntarlo al sitio y cambiar `URL` en `fuente/build.py`: la usan los links para compartir, la imagen de vista previa, el sitemap, el manifiesto y la página 404. Mientras el sitio esté en `github.io/conurban-streets-web`, los buscadores no leen el `robots.txt` (solo lo buscan en la raíz del dominio); con el dominio propio empieza a contar.

## Pendiente

- Tráiler (tarjeta 51): sumar la sección cuando esté y reemplazar el aviso de la galería.
- Link a Steam cuando la página esté aprobada (tarjeta 54).
- Newsletter: hace falta una cuenta (por ejemplo Tally o Mailchimp) para el formulario.
- Analytics simple (por ejemplo Cloudflare Web Analytics, sin cookies).
