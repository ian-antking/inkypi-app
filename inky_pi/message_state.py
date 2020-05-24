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
    self.new_messages = []
    self.current_message_index = 0
    self.update_timer = 0
    self.screen_controller = ScreenController()
    self.client = mqtt.Client('inky')
    self.client.on_message = self.on_message
    self.client.connect('192.168.1.128')
    self.client.loop_start()
    self.client.subscribe('test/message')

  def enterState(self):
    if len(self.messages) == 0 and len(self.new_messages) == 0:
      self.screen_controller.display_message('Waiting for messages...')

  def on_message(self, client, userdata, message):
    payload = str(message.payload.decode("utf-8", "ignore"))
    payload_dictionary = json.loads(payload)
    print('message recieved {}'.format(payload_dictionary['text']))
    self.new_messages.append(payload_dictionary)

  def update(self):
    if len(self.new_messages) > 0:
      self.screen_controller.display_quote(self.new_messages[0])
      self.messages.append(self.new_messages.pop(0))
    elif len(self.messages) > 1 and self.update_timer == 60:
      self.screen_controller.display_quote(self.messages[self.current_message_index % len(self.messages)])
      self.current_message_index += 1
      self.update_timer = 0

    sleep(1)
    self.update_timer += 1
