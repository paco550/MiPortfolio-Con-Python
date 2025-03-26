import reflex as rx
from reflexWebPy.components.link_icon import link_icon
from reflexWebPy.components.linksButton import links_button
from reflexWebPy.components.title import title
from reflexWebPy.components.info_text import info_text
from reflexWebPy.styles.styles import size as size
from reflexWebPy.styles.colors import TextColor as textcolor
from reflexWebPy.styles.colors import Color as color


def education_section() -> rx.components:
 return rx.vstack(
        rx.section(id="estudios"),
        title("Estudios"),
        links_button(
         image="/icons/code-solid.svg",
            title="Certificado de Profesionalidad en Desarrollo de Aplicaciones con Tecnologías Web (IFCD0210)", 
            institution="IES Puerta Arenas", 
            duration="Julio 2024 – Octubre 2024", 
            description="Formación intensiva en desarrollo de aplicaciones web, abarcando desde el diseño hasta la implementación, utilizando tecnologías modernas."
        ),

links_button(
    image="/icons/code-solid.svg",
    title="Curso de Introducción a la Programación", 
    institution="Arelance", 
    duration="Febrero 2023 - Abril 2023", 
    description="Curso cofinanciado por el Fondo Social Europeo y la Fundación ONCE, enfocado en accesibilidad, HTML5, CSS3 y JavaScript."
),
links_button(
 image="/icons/code-solid.svg",
    title="Curso de Desarrollo JavaScript con Angular, React y Node.js", 
    institution="Arelance", 
    duration="Mayo 2023 - Julio 2023", 
    description="Formación avanzada en frameworks JavaScript, incluyendo Angular, React, Node.js y bases de datos."
),
links_button(
 image="/icons/code-solid.svg",
    title="Curso de Forense Digital y Respuesta ante Incidentes (DFIR)", 
    institution="Arelance e INCIBE", 
    duration="Septiembre 2023 - Diciembre 2023", 
    description="Capacitación en ciberseguridad, análisis forense y respuesta a incidentes con casos prácticos."
),
links_button(
 image="/icons/code-solid.svg",
    title="Desarrollador Full Stack .NET", 
    institution="Arelance", 
    duration="Septiembre 2023 - Febrero 2024", 
    description="Formación en desarrollo de aplicaciones web con .NET, incluyendo SignalR, micro-servicios y sistemas de contabilidad."
),
links_button(
 image="/icons/code-solid.svg",
    title="Curso de Full Stack Python", 
    institution="Bejob e IBM SkillsBuild", 
    duration="Abril 2024 - Mayo 2024", 
    description="Desarrollo de aplicaciones con Python, incluyendo API, Git y diseño front-end."
),
links_button(
image="/icons/code-solid.svg",
    title="Certificado de Analista de Datos", 
    institution="Skill Build", 
    duration="Mayo 2024 - Junio 2024", 
    description="Capacitación en análisis de datos con Power BI, bases de datos y estrategias de análisis."
),
links_button(
 image="/icons/code-solid.svg",
    title="Curso de SQL y Modelado de Datos", 
    institution="Datahack School", 
    duration="Octubre 2024 - Diciembre 2024", 
    description="Formación en SQL avanzado y modelado de datos con proyectos grupales."
),
links_button(
 image="/icons/code-solid.svg",
    title="Curso de Inglés para Programadores", 
    institution="Skill Build", 
    duration="", 
    description="Inglés técnico especializado para programadores, documentación técnica y comunicación en TI."
),
links_button(
 image="/icons/code-solid.svg",
    title="Graduado en Educación Secundaria Obligatoria (E.S.O.)", 
    institution="IES Puerta Arenas", 
    duration="", 
    description=""
),
width="100%",
margin="20px 20px",

 )