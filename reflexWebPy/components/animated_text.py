import reflex as rx
import asyncio
from reflexWebPy.styles.colors import Color, TextColor
from reflexWebPy.styles.styles import size

class TextState(rx.State):
    palabras: list[str] = ["¡Hola!", "Soy", "Francisco", "Fernández", "Bailén,", "desarrollador", "web", "full", "stack."]
    palabras_mostradas: int = 0
    indices: list[int] = list(range(9))
    
    @rx.event(background=True)
    async def mostrar_palabras(self):
        for i in range(len(self.palabras)):
            async with self:  # Contexto necesario para modificar el estado
                self.palabras_mostradas = i + 1
            await asyncio.sleep(0.5)

def render_palabra(index: rx.Var[int]):
    return rx.box( rx.text(
        TextState.palabras[index],
        # color_scheme="tomato",
        aling_content="center",
        text_shadow="3px 3px 3px #14A1F0" ,
        color=Color.BACKGROUND.value,
        font_size=size.MEDIUM_BIG.value,
        size="3",
        weight="bold",
        opacity=rx.cond(index < TextState.palabras_mostradas, "1", "0"),
        transition="all 0.3s ease-in",
        margin_right="2px"
    ),)

def animated_text():
    return rx.hstack(
        rx.foreach(
            TextState.indices,
            render_palabra
        ),
        on_mount=TextState.mostrar_palabras
    )