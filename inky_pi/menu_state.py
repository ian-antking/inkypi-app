import paho.mqtt.client as mqtt
import json
from state import State

class MessageState(State):
  def __init__(self, state_name):
    super().__init__(state_name)

  def a_button(self):
    self.next_state = 'message'