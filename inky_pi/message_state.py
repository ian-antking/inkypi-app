#!/usr/bin/env python
import paho.mqtt.client as mqtt
import json
from state import State

class MessageState(State):
  def __init__(self, state_name, mqtt_broker, topic):
    super().__init__(state_name)
    self.messages = []
    self.new_messages = []
    self.client = mqtt.Client('inky')
    self.client.on_message = self.on_message
    self.client.connect(mqtt_broker)
    self.client.loop_start()
    self.client.subscribe(topic)

  def display_new_massage_notification(self):
    message = '{} new message'.format(len(self.new_messages))
    instruction = 'Press A'
    self.screen_controller.display_prompt(message, instruction)


  def enter_state(self):
    self.set_active()
    if len(self.new_messages):
      self.display_new_massage_notification()
    elif len(self.messages):
      self.screen_controller.display_message(self.messages[0])
    else:  
      self.screen_controller.display_alert('Waiting for messages...') 
    self.set_idle()


  def on_message(self, client, userdata, message):
    self.set_busy()
    payload = str(message.payload.decode("utf-8", "ignore"))
    payload_dictionary = json.loads(payload)
    self.new_messages.append(payload_dictionary)
    if self.is_current_state:
      self.display_new_massage_notification()
    self.set_idle()

  def handle_a(self):
    if len(self.new_messages):
      self.set_busy()
      message = self.new_messages.pop(0)
      self.messages.append(message)
      self.screen_controller.display_message(message)
      self.set_idle()
    