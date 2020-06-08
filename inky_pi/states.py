import os
from dotenv import load_dotenv
from message_state import MessageState
from menu_state import MenuState

load_dotenv()

mqtt_broker = os.getenv('MQTT_BROKER')
message_topic = os.getenv('MESSAGE_TOPIC')

states = [
  MenuState('menu'),
  MessageState('message', mqtt_broker, message_topic),
]