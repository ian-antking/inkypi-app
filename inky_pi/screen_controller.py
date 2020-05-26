#!/usr/bin/env python
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

class ScreenController():
  def __init__(self):
        self.inky_display = InkyPHAT('red')
        self.inky_display.set_border(self.inky_display.WHITE)

  def reflow_message(self, message, width, font):
    words = message.split(" ")
    reflowed = '"'
    line_length = 0

    for i in range(len(words)):
        word = words[i] + " "
        word_length = font.getsize(word)[0]
        line_length += word_length

        if line_length < width:
            reflowed += word
        else:
            line_length = word_length
            reflowed = reflowed[:-1] + "\n  " + word

    reflowed = reflowed.rstrip() + '"'

    return reflowed

  def display_quote(self, message):
    img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT), self.inky_display.WHITE)

    draw = ImageDraw.Draw(img)

    message_font = ImageFont.truetype(FredokaOne, 16)
    author_font = ImageFont.truetype(FredokaOne, 14)

    message_text = self.reflow_message(message['text'], int(self.inky_display.WIDTH * 0.9), message_font)
    message_author = message['author']

    print(message_text, message_author)

    tw, th = message_font.getsize(message_text)
    aw, ah = author_font.getsize(message_author)

    text_x = (self.inky_display.WIDTH - int(self.inky_display.WIDTH * 0.9) ) / 2
    text_y = (self.inky_display.HEIGHT - int(self.inky_display.HEIGHT * 0.9) ) / 2

    author_x = self.inky_display.WIDTH - (aw + int(self.inky_display.WIDTH * 0.1))
    author_y = self.inky_display.HEIGHT - (ah + int(self.inky_display.HEIGHT * 0.1))

    draw.text((text_x, text_y), message_text, self.inky_display.BLACK, message_font)
    draw.text((author_x, author_y), message_author, self.inky_display.RED, author_font)
    self.inky_display.set_image(img)

    self.inky_display.show()

  def display_message(self, message):
    print(message)
    img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))

    draw = ImageDraw.Draw(img)

    message_font = ImageFont.truetype(FredokaOne, 18)

    tw, th = message_font.getsize(message)

    text_x = (self.inky_display.WIDTH / 2) - (tw / 2)
    text_y = (self.inky_display.HEIGHT / 2) - (th / 2)
    print(text_x, text_y)
    draw.text((text_x, text_y), message, self.inky_display.BLACK, message_font)
    print('text drawn')
    self.inky_display.set_image(img)
    print('image set')
    self.inky_display.show()
    print('display updated')
