import time
import random
from machine import Pin

SOUND_SENSOR_PIN = 0
sound_sensor = Pin(SOUND_SENSOR_PIN, Pin.IN)

Topics = [
    "Would you run after a bus after it drives away?",
    "How do you professionally say you give me the ick to someone?",
    "Do you envision yourself with a low taper fade?",
    "What's something you wish you could eat but it's an object?",
    "What's the best aura moment you've had?",
    "Do you like your tea watery?",
    "If you could speak to a newborn baby from 2025, what lore would you tell them?",
    "What's that one kid you hung out with at the family party and never saw again when you were 7?"
]

def detect_silence(duration=6):
    start_time = time.time()
    
    while time.time() - start_time < duration:
        if sound_sensor.value() == 1:
            start_time = time.time()
        time.sleep(0.1)
        
    return True

while True:
    print("Listening for conversation...")
    
    if detect_silence(6):
        chosen_topic = random.choice(topics)
        print("Conversation Starter: " + chosen_topic)
        
    time.sleep(1)
    
    
