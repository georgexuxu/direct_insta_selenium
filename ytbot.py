from tkinter import *
from selenium import webdriver

root = Tk()

root.title('xuxisfy')
root.geometry('500x350')
root.config(bg = 'black',  borderwidth = 0)

def get_video():
    PATH = 'C:\Program Files (x86)/chromedriver.exe'

    driver = webdriver.Chrome(PATH)
    driver.get("https://www.youtube.com/?gl=BR")


get_bt = Button(command = get_video)
get_bt.pack()





root.mainloop()

