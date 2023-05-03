# importing module 
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox 
import requests 


def data_get():
    try:
        city = city_name.get()
        data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
        c_label1.config(text = data["weather"][0]["main"])
        d_label1.config(text = data["weather"][0]["description"])
        temp_label1.config(text =str(int(data["main"]["temp"]-273.15 )))
        pr_label1.config(text = data["main"]["pressure"])
    
    except Exception as e:
        messagebox.showerror("weather App","invalid entry!")



win = Tk()
win.title("WEATHER FORECAST")
win.config(bg = "sky blue")
win.geometry("700x600")
win.resizable(width='False',height='False')




city_name = StringVar()


# background
Search_image = PhotoImage(file="BG.png")
myimage = Label(image=Search_image)
myimage.place(x=0,y=0, height=600 , width=700)


# search icon 
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win, justify="center", text =  "WEATHER FORECAST APP" , values = list_name ,font = ("Time New Roman" , 15 ), textvariable = city_name)
com.place( x=175 , y=50 , height=50 , width=350 )

# location icon
Logo_image=PhotoImage(file = "location.png")
logo=Label(image=Logo_image)
logo.place(x=180,y=53, height=45, width=45)

# search button 
done_button = Button(win,text =  "search" , font = ("Time New Roman" , 10 ) , command = data_get )
done_button.place( x=445 , y=55 , height=40 , width=75)


# table 
# climate
c_label = Label(win,text = "Climate" , font = ("Time New Roman" , 15 ))
c_label.place( x=40 , y=310 , height=50 , width=200 )

c_label1 = Label(win,text = "" , font = ("Time New Roman" , 15 ))
c_label1.place( x=40 , y=375 , height=100 , width=200 )

# pressure
pr_label = Label(win,text = "Pressure" , font = ("Time New Roman" , 15 )) 
pr_label.place( x=250 , y=310 , height=50 , width=200 )

pr_label1 = Label(win,text = "" , font = ("Time New Roman" , 15 ))
pr_label1.place( x=250 , y=375 , height=100 , width=200 )

# temperature
temp_label = Label(win,text = "Temperature" , font = ("Time New Roman" , 15 ))
temp_label.place( x=460 , y=310 , height=50 , width=200 )

temp_label1 = Label(win,text = "" , font = ("Time New Roman" , 15 ))
temp_label1.place( x=460 , y=375 , height=100 , width=200 )

# description
d_label = Label(win,text = "Description" , font = ("Time New Roman" , 15 ))
d_label.place( x=100 , y=500 , height=75 , width=200)

d_label1 = Label(win,text = "" , font = ("Time New Roman" , 15 ))
d_label1.place( x=310 , y=500 , height=75 , width=300)

win.mainloop()
