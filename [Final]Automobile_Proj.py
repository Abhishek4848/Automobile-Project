from time import sleep
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import time
df=pd.read_csv("C:\\Abhi\\python\\Automobile_proj\\Automobile_data.csv")
text="**************************Welcome**************************"
for i in range(len(text)):
        print (text[i],sep=' ',end=' ',flush=True),sleep(0.01)
print ("\n")
print ("1.>Print the first and last five rows from the dataset")
print ("2.>Replace all column values which contain ‘?’ and n.a with NaN.")
print ("3.>Print most expensive car’s company name and price and show it using line graph")
print ("4.>Print all  the details of the particular car manufacturer.")
print ("5.>Find the total number of cars manufactured by each company and show it using line graph.")
print ("6.>Find the average mileage of each car making company")
print ("7.>Create two data frames using the following two Dicts, Concatenate those two data frames and create a key for each data frame.")
print ("8.>Create two data frames using the following two Dicts, Merge two data frames, and append second data frame as a new column to the first data frame.")
print ("9.>Exit")
print ("*"*116)

def progress():
	toolbar_width = 115

	sys.stdout.write("[%s]" % ("-" * toolbar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width+1))

	for i in range(toolbar_width):
	    time.sleep(0.01)
	    sys.stdout.write("#")
	    sys.stdout.flush()
	
	sys.stdout.write("]\n")

def print_dat():
        print("THE FIRST 5 ROWS IN THE DATASET ARE:")
        print(df.head(5))
        print ("-"*116)
        print("THE LAST 5 ROWS IN THE DATASET ARE:")
        print(df.tail(5))
        print ("-"*116)

def replace():
        print("To replace '?' and 'n.a' with 'NaN' ")
        df.replace(to_replace =["?", "n.a"],value ="NaN")
        print(df)
        print ("-"*116)


def expensive():
        print("The most expensive car is:")
        exp= df [['company','price']][df.price==df['price'].max()]
        print(exp)
        df.plot(kind='line',x='company',y='price', color='red')
        plt.title('GRAPH:Company vs Price')
        plt.xlabel('Company')
        plt.ylabel('Price')
        plt.show()
        print ("-"*116)

def car_det():
        car_Manufacturers = df.groupby('company')
        c=input ("Enter name of the car=")
        print ("The details of "+c+" are:")
        print(car_Manufacturers.get_group(c))
        print ("-"*116)

def no_cars():
        print("Total number of cars manufactured by each company is:")
        print("Car Name\tNo. of units manufactured")
        no=df['company'].value_counts()
        print(no)
        df.groupby('company')['price'].nunique().plot(kind='line')
        plt.title('GRAPH:Number of Cars Manufactured by each Company')
        plt.xlabel('Company')
        plt.ylabel('No. of Cars')
        plt.show()
        print ("-"*116)
    
def mileage():
        print("AVERAGE MILEAGE OF EACH CAR MAKING COMPANY:")
        print('CAR NAME   AVERAGE MILEAGE')
        mn=df.groupby('company')['average-mileage'].mean()
        print(mn)
        print("-"*116)

def concatenate():
        GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
        gc=pd.DataFrame(data=GermanCars)
        japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
        jc=pd.DataFrame(data=japaneseCars)
        gcjc=pd.concat([gc,jc],keys=["Germany", "Japan"])
        print(gcjc)
        print ("-"*116)

def merge():
        Car_Price = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}

        car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

        cp=pd.DataFrame(data=Car_Price)
        ch=pd.DataFrame(data=car_Horsepower)
        cpch=pd.merge(cp,ch,on='Company')
        print(cpch)
        print ("-"*116)
q=False
while(q!=True):
        try:
                ch=int(input("Enter your choice:"))
                if ch==1:
                        progress()
                        print_dat()
                        q=True
                if ch==2:
                        progress()
                        replace()
                        q=True
                if ch==3:
                        progress()
                        expensive()
                        q=True
                if ch==4:
                        progress()
                        car_det()
                        q=True
                if ch==5:
                        progress()
                        no_cars()
                        q=True
                if ch==6:
                        progress()
                        mileage()
                        q=True
                if ch==7:
                        progress()
                        concatenate()
                        q=True
                if ch==8:
                        progress()
                        merge()
                        q=True
                if ch==9:
                        nam="=+=+=+=+=+=+=+=+=+=+=+=+THANK YOU !!!=+=+=+=+=+=+=+=+=+=+=+= \nProject done by: \n>>Abhishek V"
                        for j in range(len(nam)):
                                print (nam[j],sep=' ',end=' ',flush=True),sleep(0.25)
                        print("\n")
                        break
                else:
                        q=False
        except ValueError:
                continue
                
        



