from PIL import Image, ImageDraw
from theme import Theme

class Screen():
  def __init__(self, colour_scheme, inky_display):
    self.theme = Theme(colour_scheme, inky_display)
    self.width = inky_display.WIDTH
    self.height = inky_display.HEIGHT
    self.image = Image.new('P', (self.width, self.height), self.theme.background)
    self.draw = ImageDraw.Draw(self.image)

  def reflow_message(self, message, width, font, quote=True):
    words = message.split(" ")
    reflowed = '"' if quote else ''
    line_length = 0

    end_of_string = '"' if quote else ''

    for i in range(len(words)):
        word = words[i] + " "
        word_length = font.getsize(word)[0]
        line_length += word_length

        if line_length < width:
            reflowed += word
        else:
            line_length = word_length
            reflowed = reflowed[:-1] + "\n  " + word

    reflowed = reflowed.rstrip() + end_of_string

    return reflowed

    def render_hatches(self, hatch_spacing, hatch_width):
      for x in range(0, 2 * self.width, hatch_spacing):
        self.draw.line((x, 0, x - self.width, self.height), fill=self.theme.background, width=hatch_width)

