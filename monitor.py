
import psutil
import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()
threshold = 60
token= os.getenv("tele_token")
chat_id= os.getenv("tele_chat_id")

def send_tele_msg(message):
	url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
	try:
		requests.get(url)
	except Exception as e:
		print(f"faild to send alert:{e}")


def check_sys():
	cpu_usg = psutil.cpu_percent(interval=1)
	ram_usg = psutil.virtual_memory().percent

	print(f"checking sys ... cpu: {cpu_usg}% | ram: {ram_usg}%")

	if cpu_usg > threshold or ram_usg > threshold:
		msg=f"ALERT: high resource usage detected! \n cpu = {cpu_usg}% | ram = {ram_usg}% !!"
		print(msg)
		send_tele_msg(msg)
	else:
		print("system healthy ")


if __name__ == "__main__":
	try:
		while True:
			check_sys()
			time.sleep(10)
	except KeyboardInterrupt:
		print("monitoring stopped.")



