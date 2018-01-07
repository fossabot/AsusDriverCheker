from win10toast import ToastNotifier
import requests
import json

#Inicialize Notification Toastes
toaster = ToastNotifier()

#My installed Drivers Version
MVGA = "23.20.16.4849"
MBIOS = "0606"
MAudio = "6.0.1.8273"
MLAN = "22.9.16.0"
MWireless = "2023.66.1104.2017"
MChipset = "10.1.1.45"
MSata = "15.9.0.1015"
MBluetooth = "1.5.1004.3"

#API URL
url = r"https://www.asus.com/support/api/product.asmx/GetPDDrivers?cpu=&osid=45&website=br&pdhashedid=J5gI4IJdkmAgKEpd&model=ROG%20STRIX%20Z370-I%20GAMING&callback=supportpdpage"

#Download URL
pagina = requests.get(url).text

#Verify Status
VGA = str(json.loads(pagina[14:-1])["Result"]
          ["Obj"][0]["Files"][0]["Version"]).strip() == MVGA
BIOS = str(json.loads(pagina[14:-1])["Result"]
           ["Obj"][1]["Files"][0]["Version"]).strip() == MBIOS
Audio = str(json.loads(pagina[14:-1])["Result"]
            ["Obj"][2]["Files"][0]["Version"]).strip() == MAudio
LAN = str(json.loads(pagina[14:-1])["Result"]
          ["Obj"][3]["Files"][0]["Version"]).strip() == MLAN
Wireless = str(json.loads(pagina[14:-1])["Result"]
               ["Obj"][5]["Files"][0]["Version"]).strip() == MWireless
Chipset = str(json.loads(pagina[14:-1])["Result"]
              ["Obj"][6]["Files"][0]["Version"]).strip() == MChipset
Sata = str(json.loads(pagina[14:-1])["Result"]
           ["Obj"][7]["Files"][0]["Version"]).strip() == MSata
Bluetooth = str(json.loads(pagina[14:-1])["Result"]
                ["Obj"][8]["Files"][0]["Version"]).strip() == MBluetooth

Status = 0

if VGA == True:
    Status += 1
else:
    toaster.show_toast("Driver de VGA Desatualizado", "Favor atualizar!")

if BIOS == True:
    Status += 1
else:
    toaster.show_toast("BIOS Desatualizada", "Favor atualizar!")

if Audio == True:
    Status += 1
else:
    toaster.show_toast("Driver de Audio Desatualizado", "Favor atualizar!")

if LAN == True:
    Status += 1
else:
    toaster.show_toast("Driver de LAN Desatualizado", "Favor atualizar!")

if Wireless == True:
    Status += 1
else:
    toaster.show_toast("Driver de Wireless Desatualizado", "Favor atualizar!")

if Chipset == True:
    Status += 1
else:
    toaster.show_toast("Driver de Chipset Desatualizado", "Favor atualizar!")

if Sata == True:
    Status += 1
else:
    toaster.show_toast("Driver de Sata Desatualizado", "Favor atualizar!")

if Bluetooth == True:
    Status += 1
else:
    toaster.show_toast("Driver de Bluetooth Desatualizado", "Favor atualizar!")

if Status == 8:
    toaster.show_toast("Tudo Atualizado", ":)")
