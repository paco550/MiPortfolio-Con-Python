from enum import Enum
from click import style
import reflex as rx
from .colors import Color as color, TextColor
from .fonts import Font as font


MAX_WIDTH = "600PX"

class size(Enum):
    VERY="0,0"
    VERY_SMALL = "0.1em"
    SMALL = "0.5em"
    MEDIUM = "0.8EM"
    DEFAULT = "1em"
    MEDIUM_BIG = "7em"
    BIG = "13em"

# styles

BASE_STYLE = {
    "font_family": font.DEFAULT.value,
    "background_color": color.BACKGROUND1.value,
   rx.button: {
       "width": "100%",
       "height": "100%",
       "display": "block",
       "padding": size.SMALL.value,
       "border_radius": size.DEFAULT.value,
       "color": TextColor.LINK.value,
       "box_shadow": "5px 5px #6A5ACD",
       "background_color": color.TS.value,
       "_hover": {
           "background_color": color.TD.value,
           "box_shadow": "5px 5px #6A5ACD",
           "text_shadow": "2px 3px 7px",
           "transition": "all 0.3s ease-in-out",
           "transform": "scale(1.05)"
           
       }

   },
   rx.link:{
      "color": TextColor.BODY1.value,  # Asegura que los enlaces tengan un color visible
        "text_decoration": "none",
        "font_weight": "bold",
        "_hover": {
            "color": TextColor.TITLE.value,  # Color en hover
            "text_decoration": "underline"
        } 
   }
}

navbar_title_style = dict(
    font_family=font.LOGO.value,
    font_size=size.MEDIUM.value,
    
)

title_style = dict(
    font_family=font.TITLE.value,
    size="md",
    width="100%",
    padding_top=size.DEFAULT.value,
    color=TextColor.TITLE.value,
)

button_title_style = dict(
    font_family=font.TITLE.value,
    font_size=size.DEFAULT.value, 
    color= TextColor.BODY1.value,
      
)

button_body_style = dict(
    font_size=size.MEDIUM.value,
    color=TextColor.LINK.value,
)

# style.title_style = {
#     "@media screen and (max-width: 480px)": {
#         "font_size": "1rem",
#         "padding": "0.5em"
#     },
#     "@media screen and (min-width: 481px) and (max-width: 768px)": {
#         "font_size": "1.2rem",
#         "padding": "1em"
#     },
#     "@media screen and (min-width: 769px)": {
#         "font_size": "1.5rem",
#         "padding": "2em"
#     }
# }