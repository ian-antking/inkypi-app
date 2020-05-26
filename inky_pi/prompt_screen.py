from PIL import ImageFont
from font_source_sans_pro import SourceSansProSemibold
from font_source_serif_pro import SourceSerifProSemibold
from screen import Screen

class PromptScreen(Screen):
  def __init__(self, colour_scheme, inky_display, message, instruction):
    super().__init__(colour_scheme, inky_display)

    message_font = ImageFont.truetype(SourceSansProSemibold, 18)
    instruction_font = ImageFont.truetype(SourceSansProSemibold, 16)

    message_text = self.reflow_message(message, self.width, message_font, False)
    instruction_text = self.reflow_message(instruction, self.width, instruction_font, False)

    tw, th = message_font.getsize(message)
    iw, ih = instruction_font.getsize(instruction)

    text_x = (self.width  / 2) - (tw / 2)
    text_y = (self.height / 2) - (th / 2)

    instruction_x = (self.width  / 2) - (iw / 2)
    instruction_y = ((self.height / 3) * 2)

    self.draw.rectangle((0, 0, self.width, (self.height - th) / 2), fill=self.theme.highlight)

    self.render_hatches(24, 3)

    self.draw.rectangle((0, text_y + th + 5, self.width, self.height), fill=self.theme.highlight)

    self.draw.multiline_text((text_x, text_y), message_text, self.theme.text, message_font, align='center')
    self.draw.multiline_text((instruction_x, instruction_y), instruction_text, self.theme.background, instruction_font, align='center')