from inspect import getfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from time import sleep
from urllib.parse import quote
# import pillow
from PIL import Image
import os


import chromedriver_autoinstaller as chromedriver
chromedriver.install()

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE)
print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*******     *****    ******     *****   ******      ******")
print("*****  THANK YOU FOR USING WHATSAPP BULK MESSENGER  ******")
print("*****      This tool was built by Anirudh Bagri     ******")
print("*****           www.github.com/anirudhbagri         ******")
print("*****            modified by Dixon Kimandu          ******")
print("*****           www.github.com/DixonKimandu         ******")
print("*****       *****   *******     *****   ******      ******")
print("**********************************************************")
print("**********************************************************")
print(style.RESET)

filepath = Image.open("/home/kimandu/dev-proj/python/whatsapp3/wstrn.jpeg")
f = open("message.txt", "r")
message = f.read()
f.close()

print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)

# import numbers
numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		numbers.append(line.strip())
f.close()
total_number=len(numbers)
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)

# import names
names = []
f = open("names.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		names.append(line.strip())
f.close()
total_name=len(names)
n = 0
print(style.RED + 'We found ' + str(total_name) + ' names in the file' + style.RESET)

delay = 30

driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)
for idx, number in enumerate(numbers):
	number = number.strip()
	if number == "":
		continue

	print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)
	try:
		# for idx2, name in enumerate(names):
		# 	name = name.strip()
		# 	if name == "":
		# 		continue
		# print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx2+1), total_name, name) + style.RESET)
		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
		sent = False
		# for i in range(3):
		# 	if not sent:
		# 		driver.get(url)
		# 		try:
		# 			click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='_4sWnG']")))
		# 		except Exception as e:
		# 			print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
		# 			print("Make sure your phone and computer is connected to the internet.")
		# 			print("If there is an alert, please dismiss it." + style.RESET)
		# 		else:
		# 			sleep(1)
		# 			click_btn.click()
		# 			sent=True
		# 			sleep(3)
		# 			print(style.GREEN + 'Message sent to: ' + number + style.RESET)

		# user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
		# user.click()
		url2 = 'https://web.whatsapp.com/send?phone=' + number
		sent = False
		for i in range(1):
			if not sent:
				driver.get(url2)
				try:
					sleep(1)
					attachment_box = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='clip']")))
					attachment_box.click()
					sleep(1)
					image_box = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='_2QbRL']")))
					image_box.click()
					print("B4 Up")
					sleep(2)
					for i in range(2):
						print("Amost Up")
						sleep(2)
						addfile_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//input[@accept='*']")))
						print("Up....")
						sleep(3)
						# addfile_button.click()
						# addfile_button.send_keys(os.getcwd() + "wstrn.jpeg")
						# addfile_button.send_keys("/home/kimandu/dev-proj/python/whatsapp3/video.mkv")
						addfile_button.send_keys("/home/kimandu/dev-proj/python/whatsapp3/wstrn.jpeg")
						# image_box.send_keys(os.getcwd() + "wstrn.jpeg")
						sleep(5)
						# addfile_caption = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_13NKt copyable-text selectable-text']")))
						# addfile_caption = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_1UWac Z2O8p oHEu9']")))
						# addfile_caption.send_keys(message)
						# sleep(5)
						# sendfile_button = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_165_h _2HL9j']")))
						# sendfile_button.click()
						# sleep(8)
						# send_button = WebDriverWait(driver, delay).until(EC.element_to_be_clickable(('//span[@data-icon="send"]')))
						# send_button.click()
						# sleep(5)
						# addfile_caption = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_13NKt copyable-text selectable-text']")))
				except Exception as e:
					print(style.RED + f"\nFailed to send message to: {names[n]} of number {number}, retry ({i+1}/3)")
					print("Make sure your phone and computer is connected to the internet.")
					print("If there is an alert, please dismiss it." + style.RESET)
				else:
					# sleep(15)
					print("cancelling first file")
					cancel_div1 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//span[@data-icon='x-alt']")))
					cancel_div1.click()
					sleep(5)
					addfile_caption = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_13NKt copyable-text selectable-text']")))
					f2 = open("message.txt", "r")
					message2 = f2.read()
					f2.close()
					addfile_caption.send_keys('Hello ' + names[n] + ', ' + message2)
					sleep(5)
					sendfile_button = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_165_h _2HL9j']")))
					sendfile_button.click()
					sleep(5)
					send_button = WebDriverWait(driver, delay).until(EC.element_to_be_clickable(('//span[@data-icon="send"]')))
					send_button.click()
		print(n)
	except Exception as e:
		print(n)
		print(style.RED + 'Failed to send message to ' + names[n] + ' of number ' +  number + str(e) + style.RESET)
		n = n + 1
		print(n)
driver.close()
