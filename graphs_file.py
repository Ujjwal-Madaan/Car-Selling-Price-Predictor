import numpy as np
import tkinter
from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class graphs:
    def __init__(self, root, car_data):
        self.root = root
        self.root.geometry("1650x900+0+0")
        self.root.title("Graphs")

        # img1 = main background
        img1 = Image.open("Sel_cars/gradientBg1.jpg")
        img1 = img1.resize((1650, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1650, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="STATISTICAL DATA",
            font=("times new roman", 33, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1650, height=55)

        # main frame
        main_frame = Frame(bg_img, bd=2, bg="black")
        main_frame.place(x=40, y=70, width=1570, height=800)

        # left label frame
        Left_frame = LabelFrame(
            main_frame,
            bd=5,
            bg="white",
            relief=RAISED,
            font=("times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=10, width=772, height=780) 

        ############### Making the bar graph in tkinter window ####################################################

        fig1 = plt.figure(figsize=(20,8)) # Figure dimension (width, height) in inches

        # Set up Axes
        ax1 = fig1.add_subplot(111) # This tells the the 1x1 grid's 1st subplot

        ax1.bar(car_data["Year"]-0.20, car_data["Present_Price"], color ='red', width = 0.4, label='Present_Price')
        ax1.bar(car_data["Year"]+0.20, car_data["Selling_Price"], color ='green', width = 0.4, label='Selling_Price')

        # Setting labels
        ax1.set_xlabel('Year', fontsize = 15)
        ax1.set_ylabel('Price in Lakhs', fontsize = 15)
        ax1.legend() # To add the legends on the graph
        ax1.set_title("Average Pricing of cars in respectve year", fontsize = 15)

        # Making tkintre canvas to place the graph on the left frame
        canvas1 = FigureCanvasTkAgg(fig1, master = Left_frame) # DrawingArea
        canvas1.draw()
        canvas1.get_tk_widget().pack()
        

        ###########################################################################

        # right label
        Right_frame = LabelFrame(
            main_frame,
            bd=5,
            bg="white",
            relief=RAISED,
            font=("times new roman", 12, "bold"),
        )
        Right_frame.place(x=790, y=10, width=770, height=777) 


        fig = plt.figure(figsize=(20,8))

        # Set up Axes
        ax = fig.add_subplot(111)

        # Histogram of the data
        ax.hist(car_data.Selling_Price, bins=20)
        ax.set_xlabel("Selling Price in Lakhs", fontsize = 15)
        ax.set_ylabel("Frequency", fontsize = 15)
        ax.set_title('Distribution of the Selling Price of Cars')

        canvas2 = FigureCanvasTkAgg(fig, master = Right_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack()
      


if __name__ == "__main__":
    root = Tk()
    obj = graphs(root,pd.read_csv('car_data.csv'))
    root.mainloop()
