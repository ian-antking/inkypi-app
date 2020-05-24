#!/usr/bin/env python
from state import State

import paho.mqtt.client as mqtt
import json
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

class MessageState(State):
  def __init__(self):
    super().__init__('message')
    self.inky_display = InkyPHAT('red')
    self.client = mqtt.Client('inky')
    self.client.on_message = self.on_message
    self.client.connect('192.168.1.128')
  
  def display_message(self, message):
    message_text = message['text']
    message_author = "--" + message['author']

    self.inky_display.set_border(inky_display.BLACK)
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT), inky_display.BLACK)

    draw = ImageDraw.Draw(img)

    message_font = ImageFont.truetype(FredokaOne, 18)
    author_font = ImageFont.truetype(FredokaOne, 16)

    tw, th = message_font.getsize(message_text)
    aw, ah = author_font.getsize(message_author)

    text_x = (inky_display.WIDTH / 2) - (tw / 2)
    text_y = (inky_display.HEIGHT / 3) - (th / 2)

    author_x = (inky_display.WIDTH / 3) * 2 - (aw /  2)
    author_y = (inky_display.HEIGHT / 3) * 2 - (ah / 2)

    draw.text((text_x, text_y), message_text, inky_display.WHITE, message_font)
    draw.text((author_x, author_y), message_author, inky_display.RED, author_font)
    inky_display.set_image(img)

    inky_display.show()

  def on_message(self, client, userdata, message):
      payload = str(message.payload.decode("utf-8", "ignore"))
      payload_dictionary = json.loads(payload)
      self.display_message(payload_dictionary)

  def enterState(self):
    self.inky_display.set_border(inky_display.BLACK)
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT), inky_display.BLACK)

    draw = ImageDraw.Draw(img)
    inky_display.set_image(img)

    self.client.loop_start()
    self.client.subscribe('test/message')

  def exitState(self):
    self.client.loop_stop()
