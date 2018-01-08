from win10toast import ToastNotifier
import requests
import json


def run():
    #My installed Drivers Version
    drivers = {'VGA': "23.20.16.4849",
               'BIOS': "0606",
               'Audio': "6.0.1.8273",
               'LAN': "22.9.16.0",
               'Wireless': "2023.66.1104.2017",
               'Chipset': "10.1.1.45",
               'Sata': "15.9.0.1015",
               'Bluetooth': "1.5.1004.3"}
    Status = 0

    #get data
    url = r"https://www.asus.com/support/api/product.asmx/GetPDDrivers?cpu=&osid=45&website=br&pdhashedid=J5gI4IJdkmAgKEpd&model=ROG%20STRIX%20Z370-I%20GAMING&callback=supportpdpage"
    data = json.loads(requests.get(url).text[14:-1])["Result"]["Obj"]
    # locations of drivers in data object
    json_objects = [0, 1, 2, 3, 5, 6, 7, 8]
    for (driver, d_val), jo, in zip(drivers.items(), json_objects):
        if data[jo]["Files"][0]["Version"].strip() != d_val:
            ToastNotifier().show_toast("{} Desatualizado(a)".format(driver), "Favor atuliazar!")
        else:
            Status += 1

    if Status == 8:
        ToastNotifier().show_toast("Tudo Atualizado!", ":)")


run()
