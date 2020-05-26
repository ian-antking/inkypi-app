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
    self.screen_controller = ScreenController()
    self.client = mqtt.Client('inky')
    self.client.on_message = self.on_message
    self.client.connect('192.168.1.128')
    self.client.loop_start()
    self.client.subscribe('test/message')

  def display_new_message(self):
        self.screen_controller.display_quote(self.new_messages[0])
        self.messages.append(self.new_messages.pop(0))

  def display_message(self):
    self.screen_controller.display_quote(self.messages[self.current_message_index % len(self.messages)])

  def enterState(self):
    if len(self.messages) == 0 and len(self.new_messages) == 0:
      self.screen_controller.display_message('Waiting for messages...')
    elif len(self.new_messages) > 0:
      self.display_new_message()
    else:
      self.screen_controller.display_message(self.messages[self.current_message_index])

  def on_message(self, client, userdata, message):
    payload = str(message.payload.decode("utf-8", "ignore"))
    payload_dictionary = json.loads(payload)
    print('message recieved {}'.format(payload_dictionary['text']))
    self.new_messages.append(payload_dictionary)
    self.screen_controller.display_message('{} new message'.format(len(self.new_messages)))