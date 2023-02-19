from bs4 import BeautifulSoup
import requests

class Parcer:
    def __init__(self):
        self.url = "https://myfin.by/crypto-rates"
        
    def load(self):
        self.name = []
        self.price = []
        self.price_ch = []
        self.price_ch_procents = []
        
        name_f = []
        price_f = []
        price_ch_f = []
        price_ch_procents_f = []

        for j in range(1, 4):
            name = []
            price = []
            price_ch = []
            price_ch_procents = []

            response = requests.get(self.url + "?page=" + str(j))
            soup = BeautifulSoup(response.text, "lxml")
            m = soup.find_all("td", _class = "")
            #print(response)

            for i in range(0, len(m), 7):
                name.append(str(m[i].text))
                price.append(str(m[i + 1].text))
                price_ch_procents.append(str(m[i + 4].text))

            a = []
            for i in name:
                a.append(i[0:len(i) - 1])
            name = a

            a = []
            for i in price:
                n = i.split(sep = " ")
                a.append(n[0])
                price_ch.append(n[1])
            price = a

            name_f.append(name)
            price_f.append(price)
            price_ch_f.append(price_ch)
            price_ch_procents_f.append(price_ch_procents)


        for i in range(0, 3):
            for j in range(0, len(name_f[i])):
                self.name.append(name_f[i][j])
                self.price.append(price_f[i][j])
                self.price_ch.append(price_ch_f[i][j])
                self.price_ch_procents.append(price_ch_procents_f[i][j])
