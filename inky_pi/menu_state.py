import paho.mqtt.client as mqtt
import json
from state import State
from screen_controller import ScreenController
from time import sleep

class MessageState(State):
  def __init__(self, state_name, mqtt_broker, topic):
    super().__init__(state_name)
    self.messages = []
    self.new_messages = []
    self.screen_controller = ScreenController()
    self.client = mqtt.Client('inky')
    self.client.on_message = self.on_message
    self.client.connect(mqtt_broker)
    self.client.loop_start()
    self.client.subscribe(topic)

    