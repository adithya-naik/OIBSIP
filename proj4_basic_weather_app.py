#COMMAND LINE BASIC WEATHER APP

#Author : Jatoth Adithya Naik
#for    : Intenship (PROJECT-4)

# Discription :
# takes the city name as input
# gives current temperature,humidity,wind speed and description of the wheather as output 

import requests ,jsons

print("\n\n\t\t\tby @JATOTH ADITHYA NAIK")
print("\t\t________________________________________")
print("\n\t\t\t***BASIC WHEATHER APP***\n")
apiKey="62994c87fab97dc8667d603ab1fc4dbe"
baseurl="https://api.openweathermap.org/data/2.5/weather?q="
city=input("\n\t\tEnter city name: ")
curl=baseurl+city+"&appid="+apiKey
response=requests.get(curl)
data=response.json()
k=data['main']['temp']
celsius=273.15-k
if(data['cod']==401):
    print("\t\tInvalid Location:{}, Please check you city name.".format(city))
else:
    print("\n\n\t\t$Weather Forecasting of {}-$".format(city))
    print("\n\n\t\t*----------------------------------------*")
    print("\n\t\tCurrent Temperature of {} is {}".format(city,celsius))
    print("\n\t\tCurrent humidity:{}".format(data['main']['humidity']))
    print("\n\t\tCurrent wind speed:{}".format(data['wind']['speed']))
    print("\n\t\tDescription of weather: {}".format(data['weather'][0]['description']))
    print("\n\t\t\t**Thanks for using*\n\n")