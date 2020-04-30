from bs4 import BeautifulSoup
import requests
import math

####openweather password = #Tanish#

'''
url = ("https://search.yahoo.com/search?fr=mcafee&type=E211US1144G0&p=weather")
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")
temp = soup.find('span', class_ = "currTemp")
print(math.floor((int(temp.text)-32)*5/9))
desc = soup.find('span', class_ = "condition")
print(desc.text)
'''
'''
city = input("Enter the city : ")
url = (f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=2072b6ef83ef2f559769c31b971728f0")
r = requests.get(url)
res = dict(r.json())
temp = math.floor(res['main']['temp'] - 273.15)
desc = res['weather'][0]['description']
humidity = res['main']['humidity']
print(desc)
print(humidity)


#print(r.text)
'''

'''
        self.pushButton.clicked.connect(self.get_info)

    def get_info(self):
        topic = self.lineEdit.text()
        try:
            self.textEdit.setText(wikipedia.summary(topic, sentences = 3))
        except:
            print(Exception)
            self.textEdit.setText("Please Enter Search item in detail")
'''

''''

url = (f"https://www.timeanddate.com/worldclock/{country}/{City}")
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")
soup = soup.find('span', class_="h1")

print(soup.text)
'''

url = (f"https://24timezones.com/Mumbai/time")
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
soup = soup.find('div', class_="time")
hours = soup.find('span', class_='hours').text
minutes = soup.find('span', class_='minutes').text
seconds = soup.find('span', class_='seconds').text
print(str(hours) + str(minutes) + str(seconds))














