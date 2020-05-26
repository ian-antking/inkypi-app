#!/usr/bin/env python
import paho.mqtt.client as mqtt
import json
from state import State
from screen_controller import ScreenController
from time import sleep

class MessageState(State):
  def __init__(self):
    super().__init__('message')
    self.busy = True
    self.messages = []
    self.new_messages = []
    self.screen_controller = ScreenController()
    self.client = mqtt.Client('inky')
    self.client.on_message = self.on_message
    self.client.connect('192.168.1.128')
    self.client.loop_start()
    self.client.subscribe('test/message')

  def enterState(self):
    self.screen_controller.display_message('Waiting for messages...')
    self.busy =False


  def on_message(self, client, userdata, message):
    self.busy = True
    payload = str(message.payload.decode("utf-8", "ignore"))
    payload_dictionary = json.loads(payload)
    print('message recieved {}'.format(payload_dictionary['text']))
    self.new_messages.append(payload_dictionary)
    self.screen_controller.display_message('{} new message'.format(len(self.new_messages)))
    self.busy = False

  def c_button(self):
    self.busy = True
    if len(self.new_messages):
      message = self.new_messages.pop(0)
      print(message)
      self.messages.append(message)
      self.screen_controller.display_message('This is the message')
    
    print(self.new_messages)
    print(self.messages)
    self.busy = False