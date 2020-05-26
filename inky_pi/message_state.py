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

  def enterState(self):
    self.set_busy()
    self.screen_controller.display_message('Waiting for messages...', 'red')
    self.set_idle()


  def on_message(self, client, userdata, message):
    self.set_busy()
    payload = str(message.payload.decode("utf-8", "ignore"))
    payload_dictionary = json.loads(payload)
    print('message recieved {}'.format(payload_dictionary['text']))
    self.new_messages.append(payload_dictionary)
    self.screen_controller.display_message('{} new message'.format(len(self.new_messages)))
    self.set_idle()

  def c_button(self):
    self.set_busy()
    if len(self.new_messages):
      message = self.new_messages.pop(0)
      print(message)
      self.messages.append(message)
      self.screen_controller.display_quote(message, 'dark')
    
    print(self.new_messages)
    print(self.messages)
    self.set_idle()