# import reflex as rx

# def hover(content: rx.Component, text: str = "") -> rx.Component:
#     return rx.box(
#         rx.hover_card.root(
#             rx.hover_card.trigger(rx.box(content)),  # Asegurar que es un trigger válido
#             rx.hover_card.content(rx.text(text)),
#         )
#     )