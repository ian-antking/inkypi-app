#!/usr/bin/env python
import paho.mqtt.client as mqtt
import json
from state import State
from screen_controller import ScreenController
from time import sleep

class MessageState(State):
  def __init__(self):
    super().__init__('message')
    self.messages = []
    self.current_message = 0
    self.screen_controller = ScreenController()
    self.client = mqtt.Client('inky')
    self.client.on_message = self.on_message
    self.client.connect('192.168.1.128')
    self.client.loop_start()
    self.client.subscribe('test/message')

  def on_message(self, client, userdata, message):
    payload = str(message.payload.decode("utf-8", "ignore"))
    payload_dictionary = json.loads(payload)
    print('message recieved {}'.format(payload_dictionary['text']))
    self.messages.append(payload_dictionary)

  def update(self):
    if len(self.messages):
      self.screen_controller.display_quote(self.messages[self.current_message % len(self.messages)])
      self.current_message += 1

    sleep(60)
