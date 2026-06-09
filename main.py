import machine
import time
import network
import urequests

def transition():
  print("Switching tasks...")
  time.sleep(1)
  red.value(0)
  time.sleep(1)
  red.value(1)

def blue_log_info():
  time.sleep(1)
  blue.value(0)
  time.sleep(1)
  blue.value(1)

def blink_grn_success():
  #Blinks twice
  green.value(0)
  time.sleep(0.25)
  green.value(1)
  time.sleep(0.25)
  green.value(0)
  time.sleep(0.25)
  green.value(1)

def flash_red_err():
  #Flashes red 3 times
  red.value(0)
  time.sleep(0.25)
  red.value(1)
  time.sleep(0.25)
  red.value(0)
  time.sleep(0.25)
  red.value(1)
  time.sleep(0.25)
  red.value(0)
  time.sleep(0.25)
  red.value(1)

#COLORS:red
#46: Red
#0: Green
#45: Blue
red = machine.Pin(46, machine.Pin.OUT) #We create new Pin objects named red, green, blue and set pin 46, 0, 25 as outputsz1 
green = machine.Pin(0, machine.Pin.OUT)
blue = machine.Pin(45, machine.Pin.OUT)

#Below are some examples
#Solid white for 5s

#Turn LEDs on
red.value(0)
green.value(0)
blue.value(0)
print("LEDs turned on")

#Sleep for 5 seconds
print("Allowing light to show for 5s")
time.sleep(5)

#Turn LEDs off
print('LEDS turned off')
red.value(1)
green.value(1)
blue.value(1)

#[NOTE]
#Lines 60-87 are commented out because they are not needed and will stay uncommented til'
#i eventually delete them when im done with this project

#[NOTE 2]
#Me five minutes later, this code is obsolete. If i were to uncomment it i would have to replace some stuff for cleanness and functions for simplicity.
#TLDR: i dont wanna be reminded of this code

#Switching sequence
#time.sleep(1)
#red.value(0)
#time.sleep(1)
#red.value(1)

#Christmas colors
#print("Example 2: Chriostmas colors")

#while True:
  #Turn red on
#  red.value(0)
#  print("Red turned on")
   #Sleep 0.5s
#  print("Waiting")
#  time.sleep(0.5)

  #Turn red off then green on
#  red.value(1)
#  green.value(0)
#  print("red turned off, green turned on")
   #Sleep 0.5s
#  print("Waiting")
#  time.sleep(0.5)
   #Turn all LEDs off
#  red.value(1)
#  green.value(1)

#Switching sequence
print("Switching tasks...")
time.sleep(1)
red.value(0)
time.sleep(1)
red.value(1)

#Connect to wifi
nic = network.WLAN(network.WLAN.IF_STA) #Create nic
nic.active(True)                        #Put nic up
nic.connect("SSID", "PASSWD") #Connect
#Loop to check if it succesfully connected
print("Waiting 5s for network connection to finish")
time.sleep(5)
while True:
  if nic.isconnected() == True:
    print("Successfully connected to network.")
    blink_grn_success()
    break
  else:
    print("Couldn't connect to the network TP-Link_6A23")
    flash_red_err()

#Show network info like the ip assigned to it
#Get ip, subnet, gateway, and dns
ip = nic.ifconfig()[0]
subnet = nic.ifconfig()[1]
gateway = nic.ifconfig()[2]
dns = nic.ifconfig()[3]
#Print ip, subnet, gateway, and dns
print(f"IP address is {ip}")
print(f"Subnet is {subnet}")
print(f"Gateway is {gateway}")
print(f"DNS is {dns}")

#Calling the OpenWeatherMap API and printing output, tommorow (now is june 8) i will use tts card to translate it into tts
print("Calling OpenWeatherMap API to get weather data, this might take a few seconds")
resp = urequests.get("https://api.openweathermap.org/data/2.5/weather?lat=LATITUDE&lon=LONGITUDE&appid=API_KEY&units=imperial")
#Turn JSON into a Python dictionary
weatherdata = resp.json()
#Parse temp, feels like, and craft conditions string for the sentence
temp = weatherdata["main"]["temp"]
temp_fl = weatherdata["main"]["feels_like"]
conditions_str = ""
if weatherdata["weather"][0]["main"] == "Rain":
  conditions_str = "rainy"
elif weatherdata["weather"][0]["main"] == "Thunderstorm":
  conditions_str = "stormy"
elif weatherdata["weather"][0]["main"] == "Drizzle":
  conditions_str = "drizzily"
elif weatherdata["weather"][0]["main"] == "Snow":
  conditions_str = "snowy"
elif weatherdata["weather"][0]["main"] == "Clear":
  conditions_str = "clear"
elif weatherdata["weather"][0]["main"] == "Clouds":
  conditions_str = "cloudy"
else:
  conditions_str = "WIP"


#[TESTING ONLY]
#This code will be here until i am done with the tts module.
#blue_log_info() is created and called to tell the user to look at the log
blue_log_info()
print(f"The current temperature outside is {temp}, but it feels like {temp_fl}. It is currently {conditions_str} outside.")
#Update, its currently 9:00 PM. It worked!!It printed:
#The current temperature outside is 66.33, but it feels like 65.8. It is currently cloudy outside.
#I feel so powerful!
