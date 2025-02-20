import reflex as rx
from reflex_motion import motion

def test() -> rx.Component:
    return motion( 
        rx.button(
            "Spin me!",
            variant="soft",
        ),
        initial={"scale": 1},
        while_hover={"scale": 1.2, "rotate": 45},
        while_tap={"scale": 0.9},
        transition={"type": "spring", "stiffness": 260, "damping": 20},
    )
