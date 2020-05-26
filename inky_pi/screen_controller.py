#!/usr/bin/env python
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_source_serif_pro import SourceSerifProSemibold
from font_source_sans_pro import SourceSansProSemibold
from theme import Theme

class ScreenController():
  def __init__(self):
        self.inky_display = InkyPHAT('red')
        self.screen_width = self.inky_display.WIDTH
        self.screen_height = self.inky_display.HEIGHT

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

  def display_message(self, message, theme = 'light'):
    theme = Theme(message['theme'] or theme)
    self.inky_display.set_border(theme.background)
    img = Image.new("P", (self.screen_width, self.screen_height), theme.background)

    draw = ImageDraw.Draw(img)

    message_font = ImageFont.truetype(SourceSerifProSemibold, 16)
    author_font = ImageFont.truetype(SourceSansProSemibold, 18)

    message_text = self.reflow_message(message['text'], int(self.screen_width * 0.9), message_font)
    message_author = '- ' + message['author']

    print(message_text, message_author)

    tw, th = message_font.getsize(message_text)
    aw, ah = author_font.getsize(message_author)

    text_x = (self.screen_width - int(self.screen_width * 0.9) ) / 2
    text_y = (self.screen_height - int(self.screen_height * 0.9) ) / 2

    author_x = self.screen_width - (aw + int(self.screen_width * 0.1))
    author_y = self.screen_height - (ah + int(self.screen_height * 0.1))

    draw.multiline_text((text_x, text_y), message_text, theme.text, message_font)
    draw.text((author_x, author_y), message_author, theme.highlight, author_font)
    self.inky_display.set_image(img)

    self.inky_display.show()

  def display_alert(self, message, theme = 'light'):
    theme = Theme(message['theme'] or theme)
    self.inky_display.set_border(theme.background)
    img = Image.new("P", (self.screen_width, self.screen_height), theme.background)

    draw = ImageDraw.Draw(img)

    message_font = ImageFont.truetype(SourceSansProSemibold, 18)

    message_text = self.reflow_message(message, self.screen_width, message_font, False)

    tw, th = message_font.getsize(message)

    text_x = (self.screen_width  / 2) - (tw / 2)
    text_y = (self.screen_height / 2) - (th / 2)

    draw.rectangle((0, 0, self.screen_width, (self.screen_height - th) / 2), fill=theme.highlight)
    draw.rectangle((0, text_y + th + 5, self.screen_width, self.screen_height), fill=theme.highlight)

    hatch_spacing = 24

    for x in range(0, 2 * self.screen_width, hatch_spacing):
      draw.line((x, 0, x - self.screen_width, self.screen_height), fill=theme.background, width=3)

    draw.multiline_text((text_x, text_y), message_text, theme.text, message_font, align='center')
    self.inky_display.set_image(img)
    self.inky_display.show()

  def display_prompt(self, message, instruction, theme = 'light'):
    theme = Theme(message['theme'] or theme)
    self.inky_display.set_border(theme.background)
    img = Image.new("P", (self.screen_width, self.screen_height), theme.background)

    draw = ImageDraw.Draw(img)

    message_font = ImageFont.truetype(SourceSansProSemibold, 18)
    instruction_font = ImageFont.truetype(SourceSansProSemibold, 16)

    message_text = self.reflow_message(message, self.screen_width, message_font, False)
    instruction_text = self.reflow_message(instruction, self.screen_width, instruction_font, False)

    tw, th = message_font.getsize(message)
    iw, ih = instruction_font.getsize(instruction)

    text_x = (self.screen_width  / 2) - (tw / 2)
    text_y = (self.screen_height / 2) - (th / 2)

    instruction_x = (self.screen_width  / 2) - (iw / 2)
    instruction_y = ((self.screen_height / 3) * 2)

    draw.rectangle((0, 0, self.screen_width, (self.screen_height - th) / 2), fill=theme.highlight)

    hatch_spacing = 24

    for x in range(0, 2 * self.screen_width, hatch_spacing):
      draw.line((x, 0, x - self.screen_width, self.screen_height), fill=theme.background, width=3)

    draw.rectangle((0, text_y + th + 5, self.screen_width, self.screen_height), fill=theme.highlight)

    draw.multiline_text((text_x, text_y), message_text, theme.text, message_font, align='center')
    draw.multiline_text((instruction_x, instruction_y), instruction_text, theme.background, instruction_font, align='center')
    self.inky_display.set_image(img)
    self.inky_display.show()

