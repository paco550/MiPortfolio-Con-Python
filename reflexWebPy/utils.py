import reflex as rx



#comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


imagen = "https://ffernandez.netlify.app/Video-de-WhatsApp-2025-03-22-a-las-11.39.53_925c1c81.gif"

meta = [
    {"name": "theme_color", "content": "#FFFFFF"},
    {"property": "og:type", "content": "website"},
    {"property": "og:image", "content": imagen},
    {"property":"og:url", "content":"https://ffernandez.netlify.app"},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:image", "content": imagen},
]


# index

index_titulo = "F.Fernández"
index_descripcion = "hola soy Francisco Fernández, desarrollador de software"

index_meta = [
        {"property": "og:title", "content": index_titulo},
        {"property": "og:description", "content": index_descripcion},    
]
index_meta.extend(meta)

# cursos

cursos_title = "Mis cursos"
cursos_descripcion = "Este es un listado de mis cursos"

cursos_meta = [
     {"property": "og:title", "content": cursos_title},
        {"property": "og:description", "content": cursos_descripcion},
]
cursos_meta.extend(meta)
