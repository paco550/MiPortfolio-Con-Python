from enum import Enum
import reflex as rx

MAX_WIDTH = "600PX"

class size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8EM"
    DEFAULT = "1em"
    BIG = "13em"

# styles

BASE_STYLE = {
   rx.button: {
       "width": "100%",
       "height": "100%",
       "display": "block",
       "padding": size.SMALL.value,
       "border_radius": size.DEFAULT.value,

   },
   rx.link:{
       
   }
}

title_style = dict(
    size="md",
    width="100%",
    padding_top=size.DEFAULT.value
)

button_title_style = dict(
    font_size=size.DEFAULT.value,   
)

button_body_style = dict(
    font_size=size.SMALL.value,   
)