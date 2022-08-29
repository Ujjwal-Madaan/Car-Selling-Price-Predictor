import numpy as np
from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import messagebox
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from graphs_file import graphs

class interface:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1650x900+0+0") # This specifies the size of the window
        self.root.title("Car Selling Portal") # Through this we gives the name to the window

        # ======= Variables ============
        # StringVar is used in tkinter and it is a class whose function is get()
        
        self.var_name_str = StringVar()
        self.var_name_int = IntVar()
        self.var_current_price = IntVar()
        self.var_fuel_str = StringVar()
        self.var_fuel_int = IntVar()
        self.var_kms_driven = StringVar()
        self.var_owner_str = StringVar()
        self.var_owner_int = IntVar()
        self.var_seller_str = StringVar()
        self.var_seller_int = IntVar()
        self.var_transmission_str = StringVar()
        self.var_transmission_int = IntVar()
        self.var_year = IntVar()
        self.text = StringVar()

        #################### Preparing for the car dataset #####################################
        self.car_data = pd.read_csv('car_data.csv')

        # encoding "Car_Name" Column
        self.car_data.replace({'Car_Name':{'fortuner':0,'ciaz':1, 'i20':2, 'brio':3, 'verna':4, 'corolla altis':5, 'grand i10':6, 'innova':7, 'city':8}},inplace=True)
        # encoding "Fuel_Type" Column
        self.car_data.replace({'Fuel_Type':{'Petrol':0,'Diesel':1,'CNG':2}},inplace=True)
        # encoding "Seller_Type" Column
        self.car_data.replace({'Seller_Type':{'Dealer':0,'Individual':1}},inplace=True)
        # encoding "Transmission" Column
        self.car_data.replace({'Transmission':{'Manual':0,'Automatic':1}},inplace=True)
        
        
        ############################ Removing outliers ##########################################
        # Year
        Highest_year = float(self.car_data['Year'].mean()) + float(3*self.car_data['Year'].std())
        Lowest_year = self.car_data['Year'].mean() - 3*self.car_data['Year'].std()
        self.car_data = self.car_data[(self.car_data['Year'] < Highest_year) & (self.car_data['Year'] > Lowest_year)]
        print(self.car_data.shape)
        
        # Present Price
        Highest = self.car_data['Present_Price'].mean() + 3*self.car_data['Present_Price'].std()
        Lowest = self.car_data['Present_Price'].mean() - 3*self.car_data['Present_Price'].std()
        self.car_data = self.car_data[(self.car_data['Present_Price'] < Highest) & (self.car_data['Present_Price'] > Lowest)]
        print(self.car_data.shape)
        
        # selling Price
        Highest = self.car_data['Selling_Price'].mean() + 3*self.car_data['Selling_Price'].std()
        Lowest = self.car_data['Selling_Price'].mean() - 3*self.car_data['Selling_Price'].std()
        self.car_data = self.car_data[(self.car_data['Selling_Price'] < Highest) & (self.car_data['Selling_Price'] > Lowest)]
        print(self.car_data.shape)
        
        # Kms_Driven
        Highest = self.car_data['Kms_Driven'].mean() + 3*self.car_data['Kms_Driven'].std()
        Lowest = self.car_data['Kms_Driven'].mean() - 3*self.car_data['Kms_Driven'].std()
        self.car_data = self.car_data[(self.car_data['Kms_Driven'] < Highest) & (self.car_data['Kms_Driven'] > Lowest)]
        print(self.car_data.shape)
        
        # Fuel_Type
        Highest = self.car_data['Fuel_Type'].mean() + 3*self.car_data['Fuel_Type'].std()
        Lowest = self.car_data['Fuel_Type'].mean() - 3*self.car_data['Fuel_Type'].std()
        self.car_data = self.car_data[(self.car_data['Fuel_Type'] < Highest) & (self.car_data['Fuel_Type'] > Lowest)]
        print(self.car_data.shape)
        
        # Seller_Type
        Highest = self.car_data['Seller_Type'].mean() + 3*self.car_data['Seller_Type'].std()
        Lowest = self.car_data['Seller_Type'].mean() - 3*self.car_data['Seller_Type'].std()
        self.car_data = self.car_data[(self.car_data['Seller_Type'] < Highest) & (self.car_data['Seller_Type'] > Lowest)]
        print(self.car_data.shape)
        
        # Transmission
        Highest = self.car_data['Transmission'].mean() + 3*self.car_data['Transmission'].std()
        Lowest = self.car_data['Transmission'].mean() - 3*self.car_data['Transmission'].std()
        self.car_data = self.car_data[(self.car_data['Transmission'] < Highest) & (self.car_data['Transmission'] > Lowest)]
        print(self.car_data.shape)
        
        # Fuel_Type
        Highest = self.car_data['Owner'].mean() + 3*self.car_data['Owner'].std()
        Lowest = self.car_data['Owner'].mean() - 3*self.car_data['Owner'].std()
        self.car_data = self.car_data[(self.car_data['Owner'] < Highest) & (self.car_data['Owner'] > Lowest)]
        print(self.car_data.shape)
        
        
        #################################### Preparing the Interface ##########################################

        # img1 = main background
        img1 = Image.open("Sel_cars/black_white.jpeg")
        img1 = img1.resize((1650, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1650, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="ALL IN ONE CAR SELLING PORTAL",
            font=("times new roman", 33, "bold"),
            bg="#0F00FF",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1650, height=55)

        ##########################################################

        # main frame
        main_frame = Frame(bg_img, bd=2, bg="black")
        main_frame.place(x=40, y=70, width=1570, height=800)
        # divide into label frame in main frame .... # label frame m ham title daal skte hai

        #########################################################

        img0 = Image.open('Sel_cars/CoolBlues.jpeg')
        img0 = img0.resize((1550, 780), Image.ANTIALIAS)
        self.c1 = ImageTk.PhotoImage(img0)
        

        Left_frame = Label(
            main_frame,
            bd=5,
            bg="white",
            image=self.c1,
            relief=RAISED,
            font=("times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=10, width=1550, height=780) # width = 700

        ###########################################################################################################################################

        # card 1
        # CarName frame
        car_name_frame = Frame(Left_frame, bd=2, bg="white", highlightthickness=5)
        car_name_frame.place(x=75, y=40, width=600, height=125) #x=20, width=290

        car_name_frame.config(highlightbackground="black", highlightcolor="black")

        # img2 = CarName image
        img2 = Image.open("Sel_cars/Car_name.jpg")
        img2 = img2.resize((185, 100), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        car_img = Label(car_name_frame, image=self.photoimg2)
        car_img.pack()
        car_img.place(x=20, y=10, width=185, height=100)

        car_name_combo = ttk.Combobox(
            car_name_frame,
            textvariable=self.var_name_str,
            font=("times new roman", 20),
            state="readonly",
            width=19,
        )
        car_name_combo["values"] = ['Select Car','fortuner', 'i20', 'brio', 'innova', 'verna', 'city', 'corolla altis', 'grand i10', 'ciaz']
        car_name_combo.current(0)  # to give the bydeafault index
        car_name_combo.place(x=270, y=42, anchor=NW)

        ###########################################################################################################################################
        
        # card 2
        # Car Year frame
        year_frame = Frame(Left_frame, bd=2, bg="white", highlightthickness=5)
        year_frame.place(x=75, y=200, width=600, height=125) 

        year_frame.config(highlightbackground="black", highlightcolor="black")

        # img3 = year image
        img3 = Image.open("Sel_cars/Year.jpg")
        img3 = img3.resize((185, 100), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        car_img = Label(year_frame, image=self.photoimg3)
        car_img.pack()
        car_img.place(x=20, y=10, width=185, height=100)

        year_combo = ttk.Combobox(
            year_frame,
            textvariable=self.var_year,
            font=("times new roman", 20),
            state="readonly",
            width=19,
        )
        year_combo["values"] = ["Select Year"]+[i for i in range(2018,2002,-1)]
        year_combo.current(0)  # to give the bydeafault index
        year_combo.place(x=270, y=42, anchor=NW)


        ###########################################################################################################################################

        # card 3
        # Present price frame
        present_price_frame = Frame(Left_frame, bd=2, bg="white", highlightthickness=5)
        present_price_frame.place(x=75, y=360, width=600, height=125) 

        present_price_frame.config(highlightbackground="black", highlightcolor="black")

        # img4 = Present price image
        img4 = Image.open("Sel_cars/Current_price.jpg")
        img4 = img4.resize((185, 100), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        car_img = Label(present_price_frame, image=self.photoimg4)
        car_img.pack()
        car_img.place(x=20, y=10, width=185, height=100)

        # Box
        present_price_entry = ttk.Entry(
            present_price_frame,
            textvariable=self.var_current_price,
            width=20,
            font=("times new roman", 20), 
        )
        present_price_entry.place(x=270, y=42, anchor=NW)

        ###########################################################################################################################################

        # card 4
        # Kms frame
        kms_frame = Frame(Left_frame, bd=2, bg="white", highlightthickness=5)
        kms_frame.place(x=75, y=520, width=600, height=125) 

        kms_frame.config(highlightbackground="black", highlightcolor="black")

        # img5 =  Kms image
        img5 = Image.open("Sel_cars/Kms_driven.jpg")
        img5 = img5.resize((185, 100), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        car_img = Label(kms_frame, image=self.photoimg5)
        car_img.pack()
        car_img.place(x=20, y=10, width=185, height=100)

        # Box
        kms_entry = ttk.Entry(
            kms_frame,
            textvariable=self.var_kms_driven,
            width=20,
            font=("times new roman", 20),
        )
        kms_entry.place(x=270, y=42, anchor=NW)

        ###########################################################################################################################################

        # card 5
        # Owner frame
        owner_frame = Frame(Left_frame, bd=2, bg="white", highlightthickness=5)
        owner_frame.place(x=860, y=40, width=600, height=125) 

        owner_frame.config(highlightbackground="black", highlightcolor="black")

        # img6 = Owner image
        img6 = Image.open("Sel_cars/Owner.jpg")
        img6 = img6.resize((185, 100), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        car_img = Label(owner_frame, image=self.photoimg6)
        car_img.pack()
        car_img.place(x=20, y=10, width=185, height=100)

        owner_combo = ttk.Combobox(
            owner_frame,
            textvariable=self.var_owner_str,
            font=("times new roman", 20),
            state="readonly",
            width=19,
        )
        owner_combo["values"] = ["Select Owner", 'Brand New', '2nd Hand', '3rd Hand']
        owner_combo.current(0)  # to give the bydeafault index
        owner_combo.place(x=270, y=42, anchor=NW)



        ###########################################################################################################################################

        # card 6
        # Fuel frame
        fuel_frame = Frame(Left_frame, bd=2, bg="white", highlightthickness=5)
        fuel_frame.place(x=860, y=200, width=600, height=125) 

        fuel_frame.config(highlightbackground="black", highlightcolor="black")

        # img7 = Fuel image
        img7 = Image.open("Sel_cars/Fuel_type.jpg")
        img7 = img7.resize((185, 100), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7) 
        car_img = Label(fuel_frame, image=self.photoimg7)
        car_img.pack()
        car_img.place(x=20, y=10, width=185, height=100)

        fuel_combo = ttk.Combobox(
            fuel_frame,
            textvariable=self.var_fuel_str,
            font=("times new roman", 20),  #, "bold"),
            state="readonly",
            width=19,
        )
        fuel_combo["values"] = ('Select Fuel Type', 'Petrol', 'Diesel', 'CNG')
        fuel_combo.current(0)  # to give the bydeafault index
        fuel_combo.place(x=270, y=42, anchor=NW)



        ###########################################################################################################################################

        # card 7
        # Transmission frame
        transmission_frame = Frame(Left_frame, bd=2, bg="white", highlightthickness=5)
        transmission_frame.place(x=860, y=360, width=600, height=125) #x=20, width=290

        transmission_frame.config(highlightbackground="black", highlightcolor="black")

        # img8 = transmission image
        img8 = Image.open("Sel_cars/Transmission.jpg")
        img8 = img8.resize((185, 100), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)  
        car_img = Label(transmission_frame, image=self.photoimg8)
        car_img.pack()
        car_img.place(x=20, y=10, width=185, height=100)

        transmission_combo = ttk.Combobox(
            transmission_frame,
            textvariable=self.var_transmission_str,
            font=("times new roman", 20),  #, "bold"),
            state="readonly",
            width=19,
        )
        transmission_combo["values"] = ["Select Transmission", 'Manual', 'Automatic']
        transmission_combo.current(0)  # to give the bydeafault index
        transmission_combo.place(x=270, y=42, anchor=NW)


    
        ###########################################################################################################################################

        # card 8
        # Seller type frame
        seller_frame = Frame(Left_frame, bd=2, bg="white", highlightthickness=5)
        seller_frame.place(x=860, y=520, width=600, height=125) #x=20, width=290

        seller_frame.config(highlightbackground="black", highlightcolor="black")

        # img9 = seller image
        img9 = Image.open("Sel_cars/Seller_type.jpg")
        img9 = img9.resize((185, 100), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        car_img = Label(seller_frame, image=self.photoimg9)
        car_img.pack()
        car_img.place(x=20, y=10, width=185, height=100)

        seller_combo = ttk.Combobox(
            seller_frame,
            textvariable=self.var_seller_str,
            font=("times new roman", 20),
            state="readonly",
            width=19,
        )
        seller_combo["values"] = ['Select Seller Type', 'Dealer', 'Individual']
        seller_combo.current(0)  # to give the bydeafault index
        seller_combo.place(x=270, y=42, anchor=NW)

        ###########################################################################################################################################

               
        # card 9
        # Button frame 1
        button_frame1 = Frame(Left_frame, bd=2, bg="white", highlightthickness=5)
        button_frame1.place(x=150, y=670, width=375, height=85) 

        button_frame1.config(highlightbackground="black", highlightcolor="black")

        # img9 = seller image
        img10 = Image.open("Sel_cars/button.jfif")
        img10 = img10.resize((360, 70), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        self.text.set("Predict Price")

        self.predict_btn = Button(
            button_frame1,
            command=self.predict_price,
            textvariable=self.text,
            font=("times new roman", 16, "bold"),
            image=self.photoimg10,
            compound='center'
        ).pack()

#####################################################################################################

        # card 10
        # Button frame 2
        button_frame2 = Frame(Left_frame, bd=2, bg="white", highlightthickness=5)
        button_frame2.place(x=580, y=670, width=375, height=85) #x=20, width=290

        button_frame2.config(
            highlightbackground="black", highlightcolor="black"
        )

        # img11 = Reset image
        img11 = Image.open("Sel_cars/button.jfif")
        img11 = img11.resize((360, 70), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        self.text.set("Predict Price")

        self.reset_btn = Button(
            button_frame2,
            command=self.reset_data,
            text="Reset",
            font=("times new roman", 16, "bold"),
            image=self.photoimg11,
            compound='center'
        ).pack()

        #####################################################################################################

        # card 11
        # Button frame 3
        button_frame3 = Frame(Left_frame, bd=2, bg="white", highlightthickness=5)
        button_frame3.place(x=1010, y=670, width=375, height=85) #x=20, width=290

        button_frame3.config(
            highlightbackground="black", highlightcolor="black"
        )

        # img12 = graphs
        img12 = Image.open("Sel_cars/button.jfif")
        img12 = img12.resize((360, 70), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        self.text.set("Predict Price")

        self.graphs_btn = Button(
            button_frame3,
            command=self.graphs_fun,
            text="Statistical Info",
            font=("times new roman", 16, "bold"),
            image=self.photoimg12,
            compound='center'
        ).pack()



    #####################################################################################################################

    def predict_price(self):
        if (
            self.var_name_str.get() == "Select Car"
            or self.var_current_price.get() == ""
            or self.var_year.get() == "Select Year"
            or self.var_fuel_str.get() == "Select Fuel Type"
            or self.var_transmission_str.get() == "Select Transmission"
            or self.var_seller_str.get() == "Select Seller Type"
            or self.var_kms_driven.get() == ""
            or self.var_owner_str.get() == "Select Owner"
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        elif (int(self.var_current_price.get()) < 0 & int(self.var_kms_driven.get()) < 0):
            messagebox.showerror("Error", "Insert the positive current price and distance driven", parent=self.root)

        elif (int(self.var_current_price.get()) < 0):
            messagebox.showerror("Error", "Insert the positive current price", parent=self.root)

        elif (int(self.var_kms_driven.get()) < 0):
            messagebox.showerror("Error", "Insert the positive distance driven", parent=self.root)
        
        else:
            ############### Extracting and Modifying values from the entries ############################
            if self.var_name_str.get() == 'fortuner':
                self.var_name_int.set(0)
            elif self.var_name_str.get() == 'ciaz':
                self.var_name_int.set(1)
            elif self.var_name_str.get() == 'i20':
                self.var_name_int.set(2)
            elif self.var_name_str.get() == 'brio':
                self.var_name_int.set(3)
            elif self.var_name_str.get() == 'verna':
                self.var_name_int.set(4)
            elif self.var_name_str.get() == 'corolla altis':
                self.var_name_int.set(5)
            elif self.var_name_str.get() == 'grand i10':
                self.var_name_int.set(6)
            elif self.var_name_str.get() == 'innova':
                self.var_name_int.set(7)
            elif self.var_name_str.get() == 'city':
                self.var_name_int.set(8)

            # {'fortuner':0,'ciaz':1, 'i20':2, 'brio':3, 'verna':4, 'corolla altis':5, 'grand i10':6, 'innova':7, 'city':8}

            if self.var_fuel_str.get() == 'Petrol':
                self.var_fuel_int.set(0)
            elif self.var_fuel_str.get() == 'Diesel':
                self.var_fuel_int.set(1)
            elif self.var_fuel_str.get() == 'CNG':
                self.var_fuel_int.set(2)
            
            if self.var_seller_str.get() == 'Dealer':
                self.var_seller_int.set(0)
            elif self.var_seller_str.get() == 'Individual':
                self.var_seller_int.set(1)
            
            if self.var_transmission_str.get() == 'Manual':
                self.var_transmission_int.set(0)
            elif self.var_transmission_str.get() == 'Automatic':
                self.var_transmission_int.set(1)

            ########################## Dividing between the X and Y ############################

            X = self.car_data.drop(['Selling_Price'],axis=1)
            Y = self.car_data['Selling_Price']

            ########################## Dividing between the training and testing set ############################

            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.15, random_state=2)

            ############################## Applying the Linear Regression on the model ######################

            lin_reg_model = LinearRegression()

            lin_reg_model.fit(X_train,Y_train)

            ############################# Prediction on Training data ######################################
            test_data_prediction = lin_reg_model.predict(X_test)
            print(test_data_prediction)

            # R squared Error
            error_score = metrics.r2_score(Y_test, test_data_prediction)
            print("R squared Error : ", error_score)

            ############################# Predicting the input data #########################################

            data = [{'Car_Name': self.var_name_int.get(), 'Year':self.var_year.get(), 'Present_Price':self.var_current_price.get(), 'Kms_Driven':self.var_kms_driven.get(), 'Fuel_Type':self.var_fuel_int.get(), 'Seller_Type': self.var_transmission_int.get(), 'Transmission': self.var_transmission_int.get(), 'Owner': self.var_owner_int.get()}]
            df = pd.DataFrame.from_dict(data)
            
            price_prediction = lin_reg_model.predict(df)
            print(price_prediction[0])

            ############################# To display the predicted price ####################################
            self.text.set(str(abs(round(price_prediction[0], 2)))+' Lakhs') 

####################################### Reset button to reset the blocks ################################################################################################################

    def reset_data(self):
        self.var_name_str.set("") 
        self.var_current_price.set("") 
        self.var_year.set("Select Year") 
        self.var_fuel_str.set("Select Fuel Type") 
        self.var_transmission_str.set("Select Transmission")
        self.var_seller_str.set("Select Seller Type") 
        self.var_kms_driven.set("") 
        self.var_owner_str.set("Select Owner") 

######################################## Graph button to move to graphs window ###############################################################################################

    def graphs_fun(self):
        self.new_window = Toplevel(
            self.root
        )  # This asks where we want to open our window
        self.app = graphs(self.new_window, self.car_data)

##############################################################################################################################


if __name__ == "__main__":
    root = Tk()
    obj = interface(root)
    root.mainloop()
