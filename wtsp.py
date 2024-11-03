import os
from twilio.rest import Client
import schedule
import time
import random


TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Sandbox number
YOUR_WHATSAPP_NUMBER = 'whatsapp:+yournumber'  # Your WhatsApp number

MORNING_QUOTES = [
    "Start your day with a smile 😊",
    "Rise and shine! Today is a new day, full of possibilities 🌞",
    "Let’s make today amazing 💪",
    "The sun is up, the sky is blue, it’s beautiful, and so are you.",
    "Morning comes with a chance to start a new day.",
    "Wake up with determination and go to bed with satisfaction.",
    "Take the opportunity and build the tomorrow you want.",
    "Opportunities don’t come easily, you have to create them.",
    "To do great work is to do your work.",
    "Believe in yourself and you’re already on the way to success.",
    "The future is for those who believe in their dreams.",
    "Success is not final, failure is not the end.",
    "The best way to predict the future is to create it.",
    "Discipline is important every day regardless of how you feel.",
    "Do not limit the realization of tomorrow with your doubts of today.",
    "Challenges make life interesting and overcoming them makes life meaningful.",
    "Start early to get ahead.",
    "The future depends on what you do today."
]
NIGHT_QUOTES = [
    "Sleep well and dream big 🌙",
    "Tomorrow is a new day 🌌",
    "Sweet dreams! Rest up for a wonderful tomorrow 😴",
    "Be aware of your breathing. Notice how this takes attention away from your thinking and creates space.",
    "Night is the other half of life, and the better half.",
    "It is a common experience that a problem difficult at night is resolved in the morning after the committee of sleep has worked on it.",
    "Tired minds don't plan well. Sleep first, plan later.",
    "The best bridge between despair and hope is a good night’s sleep.",
    "Take rest; a field that has rested gives a bountiful crop.",
    "Surrender to what is. Let go of what was. Have faith in what will be.",
    "Day is over, night has come. Today is gone, what’s done is done. Embrace your dreams, through the night. Tomorrow comes with a whole new light.",
    "You must learn to let go. Release the stress. You were never in control anyway.",
    "Let gratitude be the pillow upon which you kneel to say your nightly prayer.",
    "Goodnight stars, goodnight air, goodnight noises everywhere.",
    "A ruffled mind makes a restless pillow.",
    "Never waste any time you can spend sleeping."
    
]


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Function to send a message
def send_whatsapp_message(body):
    message = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        body=body,
        to=YOUR_WHATSAPP_NUMBER
    )
    print(f"Message sent: {message.sid}")

def send_morning_message():
    quote = random.choice(MORNING_QUOTES)
    send_whatsapp_message(f"🌅 Good Morning! 🌅\n{quote}")

def send_night_message():
    quote = random.choice(NIGHT_QUOTES)
    send_whatsapp_message(f"🌙 Good Night! 🌙\n{quote}")

# Schedule 
schedule.every().day.at("08:30").do(send_morning_message)  
schedule.every().day.at("22:00").do(send_night_message)    

# Run the scheduler
print("WhatsApp bot is running...")
while True:
    schedule.run_pending()
    time.sleep(60)
