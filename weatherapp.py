from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests





# I made a comment here on my mac
# I added another comment from my PC

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

print(api_key)

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp = json['main']['temp']
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        ['main']
        final = (city, country, temp, icon, weather)
        return final

    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    img['file'] = f'imgs\\{weather[3]}.png'

    if weather:
        location_lbl['text'] = f'{weather[0]}, {weather[1]}'
        # image['bitmap'] = f'/imgs/{weather[3]}.png'


        temp_lbl['text'] = f'{weather[2]:.2f}°'
    else:
        messagebox.showerror('Error', f'Cannot find city {city}')

# Setting up basic GUI
app = Tk()
app.title('Weather App')
app.geometry('700x350')


city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search Weather', width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text='', font=('bold', 20))
location_lbl.pack()

img = PhotoImage(file="")

Image = Label(app, image=img, relief=RAISED)
Image.pack()

temp_lbl = Label(app, text='')
temp_lbl.pack()

weather_lbl = Label(app, text='')
weather_lbl.pack()

app.mainloop()