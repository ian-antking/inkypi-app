from PIL import Image, ImageFont, ImageDraw
from font_source_serif_pro import SourceSerifProSemibold
from font_source_sans_pro import SourceSansProSemibold
from theme import Theme

class Screen():
  def __init__(self, colour_scheme, inky_display):
    self.theme = Theme(colour_scheme, inky_display)
    self.width = inky_display.WIDTH
    self.height = inky_display.HEIGHT
    self.image = Image.new('P', (self.width, self.height), self.theme.background)
    self.draw = ImageDraw.Draw(self.background)
