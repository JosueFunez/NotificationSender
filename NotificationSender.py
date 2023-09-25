import os
import requests
import argparse
from dotenv import load_dotenv

load_dotenv()

def _parse_arguments(args=None):

    parser = argparse.ArgumentParser(description="Notification sender throught Telegram bot")
    parser.add_argument("-p", dest="process", action="store")

    return parser.parse_args(args=args)

def send_notification(args):
    TOKEN = os.getenv('T_TOKEN') 
    chat_id = os.getenv('T_CHAT_ID') 
    process = args.process
    message = "Process: %s ended with code 0" % (process)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) 

def _run(args):
    send_notification(args)

if __name__ == "__main__":
    _run(args=_parse_arguments())


