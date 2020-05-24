import paho.mqtt.client as mqtt
import sys
import signal
import json
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

broker_address = sys.argv[1]
topic = sys.argv[2]
inky_display = InkyPHAT(sys.argv[3])

def display_message(message):
    message_text = message['text']
    message_author = "--" + message['author']

    inky_display.set_border(inky_display.BLACK)
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT), inky_display.BLACK)

    draw = ImageDraw.Draw(img)

    message_font = ImageFont.truetype(FredokaOne, 18)
    author_font = ImageFont.truetype(FredokaOne, 16)

    tw, th = message_font.getsize(message_text)
    aw, ah = author_font.getsize(message_author)

    text_x = (inky_display.WIDTH / 2) - (tw / 2)
    text_y = (inky_display.HEIGHT / 3) - (th / 2)

    author_x = (inky_display.WIDTH / 3) * 2 - (aw /  2)
    author_y = (inky_display.HEIGHT / 3) * 2 - (ah / 2)

    draw.text((text_x, text_y), message_text, inky_display.WHITE, message_font)
    draw.text((author_x, author_y), message_author, inky_display.RED, author_font)
    inky_display.set_image(img)

    inky_display.show()

def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8", "ignore"))
    payload_dictionary = json.loads(payload)
    display_message(payload_dictionary)

client = mqtt.Client("inky")
client.on_message = on_message
client.connect(broker_address)
client.loop_start()
client.subscribe(topic)

signal.pause()