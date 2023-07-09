#Replace "your_api_key" with your MapQuest API key

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "bNzzUv5NWpOoFMYpMN3kTUkYYdXp7RCx"


while True:
    orig = input("Ciudad de Origen: ")
    if orig == "Salir" or orig == "S":
        break
    dest = input("Ciudad de Destino: ")
    if dest == "Salir" or dest == "S":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 
    json_data = requests.get(url).json()
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Direcciones desde " + (orig) + " a " + (dest))
        print("Duracion del viaje:   " + (json_data["route"]["formattedTime"]))
        print("Distancia en kilometros:      " + str("{:.1f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.1f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")