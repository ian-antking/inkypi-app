#!/usr/bin/env python
import paho.mqtt.client as mqtt
import json
from state import State
from screen_controller import ScreenController

class MessageState(State):
  def __init__(self):
    super().__init__('message')
    self.screen_controller = ScreenController()
    self.client = mqtt.Client('inky')
    self.client.on_message = self.on_message
    self.client.connect('192.168.1.128')

  def enterState(self):
    self.screen_controller.display_message('Message Mode')

    self.client.loop_start()
    self.client.subscribe('test/message')

  def on_message(self, client, userdata, message):
      payload = str(message.payload.decode("utf-8", "ignore"))
      payload_dictionary = json.loads(payload)
      self.screen_controller.display_quote(payload_dictionary)

  def exitState(self):
    self.client.loop_stop()
