#to install requests we would need to use the command python -m pip install requests
#to install pip directly from the terminal download the following file https://bootstrap.pypa.io/get-pip.py and use the command python3 get-pip.py
#from  pprint import pprint - can also be used to print when we receive a response in a json format and pprint makes into a readable tree
#run your script using the command python3 <name of your file>
import requests
area = input("Enter a location: ")
api_key = "e21a3caab2mshaae6c41e1d1b706p194fd4jsn31735ff6a304"
base_url = "https://community-open-weather-map.p.rapidapi.com/weather?q="+area+"&rapidapi-key="+api_key
final_data = requests.get(base_url).json()
if 'message'  in final_data:
  raise Exception("City cannot be found")
try:
  print("The weather of your location", area, "is:")
  print("Humidity :", final_data["main"]["humidity"] )
  print(final_data["weather"][0]["main"], ":", final_data["weather"][0]['description'])

except:
  print("An exception occured, please try again")
