import tkinter as tk
from tkinter import *
import pytz
import requests
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


def getweather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="current weather")
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=cceb7325f72c5b7cde0c72f00ec7e837"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    wind = json_data['wind']['speed']

    t.config(text=(temp, '°'))
    c.config(text=(condition, "|", "feels", "like", temp, '°'))

    w.config(text=wind)
    w.config(text=humidity)
    w.config(text=description)
    w.config(text=pressure)

    messagebox.showerror("weather app", "invalid entry")


# search box
Search_image = PhotoImage(file="img/search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("comic sans ms", 25, "bold"), bg="#404040",
                     border=0, fg="white")

textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="img/search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getweather)
myimage_icon.place(x=400, y=34)

# logo
Logo_image = PhotoImage(file="img/logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = PhotoImage(file="img/box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# time
name = Label(root, font=("comic sans ms", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("comic sans ms", 20))
clock.place(x=30, y=130)

# label
label1 = Label(root, text="WIND", font=("comic sans ms", 15, 'bold'), fg='white', bg='#1ab5ef')
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("comic sans ms", 15, 'bold'), fg='white', bg='#1ab5ef')
label2.place(x=225, y=400)

label3 = Label(root, text="DESCRIPTION", font=("comic sans ms", 15, 'bold'), fg='white', bg='#1ab5ef')
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("comic sans ms", 15, 'bold'), fg='white', bg='#1ab5ef')
label4.place(x=620, y=400)

t = Label(font=("comic sans ms", 70, "bold"), fg='#ee666d')
t.place(x=400, y=150)
c = Label(font=("comic sans ms", 15, 'bold'))
c.place(x=400, y=250)

w = Label(text="...", font=("comic sans ms", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("comic sans ms", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("comic sans ms", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)
p = Label(text="...", font=("comic sans ms", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()
