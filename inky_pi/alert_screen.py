from PIL import Image, ImageFont, ImageDraw
from font_source_serif_pro import SourceSerifProSemibold
from font_source_sans_pro import SourceSansProSemibold
from screen import Screen

class AlertScreen(Screen):
  def __init__(self, colour_scheme, inky_display):
    super().__init__(colour_scheme, inky_display)