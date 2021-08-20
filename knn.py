"""
This project is created by NAMAN MADHARIA

Dataset Source: kaggle.com
"""
#-----------------------------Importing libraries-----------------------
import tkinter

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.cm import rainbow


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier 


#-----------------Takinf inputs Fn-----------------
def takeInput():
    inputValues = []

    bmiValues = []
    
    weight1=int(weight.get())
    height1=int(height.get())
#---------conversions---------------------
    age1 = ((int(age.get()) - 29)  / (77-29 ))
    print(age1)
    trestbps1 = ((int(rbp.get()) - 94)/(200-94))
    chol1 = ((int (serumChol.get()) - 126)/(564-126))
    thalach1 = ((int(thalach.get()) - 71)/(202-71))
    oldpeak1 = (int(oldpeak.get())/ (6.2))
    


    bmiValues.append(name.get())
    bmiValues.append(weight1)
    bmiValues.append(height1)

    inputValues.append(age1)
    inputValues.append(sex.get())
    inputValues.append(chestPain.get())
    inputValues.append(trestbps1)
    inputValues.append(chol1)
    inputValues.append(FBS.get())
    inputValues.append(ECG.get())
    inputValues.append(thalach1)
    inputValues.append(trestbps1)
    inputValues.append(oldpeak1)
    inputValues.append(slope.get())
    inputValues.append(ca.get())
    inputValues.append(thal.get()) 
    
    print(inputValues)
    print(" name weight height", bmiValues)

    print("\n") 
    final_Result = knn_classifier.predict([inputValues])
    print(final_Result)
    

    #-----------------------BMI calc-------------------------

    bmi = bmiValues[1]/((bmiValues[2]/100)**2)
    out=""
    if (bmi < 18.5):
        out="underweight"
 
    elif ( bmi >= 18.5 and bmi < 24.9):
        out="healthy"
 
    elif ( bmi >= 24.9 and bmi < 30):
        out="overweight"
 
    elif ( bmi >=30):
        out="suffering from Obesity"

    print("bmi and out :",bmi,out)

#------------------Second Window config tkinter
    substituteWindow = tkinter.Tk()
    substituteWindow.geometry('640x480-15-200')
    substituteWindow.title("PREDICTION")
    substituteWindow.configure(bg='#006064')    

    substituteWindow.columnconfigure(0, weight=2)
    substituteWindow.columnconfigure(1, weight=1)
    substituteWindow.columnconfigure(2, weight=2)
    substituteWindow.columnconfigure(3, weight=2)
    
    substituteWindow.rowconfigure(0, weight=1)
    substituteWindow.rowconfigure(1, weight=10)
    substituteWindow.rowconfigure(2, weight=10)
    substituteWindow.rowconfigure(3, weight=1)
    substituteWindow.rowconfigure(4, weight=1)
    substituteWindow.rowconfigure(5, weight=1)
    substituteWindow.rowconfigure(6, weight=1)
    
    if final_Result[0] == 1:
        label1 = tkinter.Label(substituteWindow, text="HEART DISEASE DETECTED !!!!!", font=('Times', -35), fg='red')
        label1.grid(row=1, column=1, columnspan=6)
        label2 = tkinter.Label(substituteWindow, text="Dear "+str(bmiValues[0])+" PLEASE VISIT NEAREST CARDIOLOGIST AT THE EARLIEST", font=('Times', -20), fg='red')
        label2.grid(row=2, column=1, columnspan=6)
        label3 = tkinter.Label(substituteWindow, text = "Your BMI is "+str(bmi)+"% and you are  "+out, font=('Times', -20))
        label3.grid(row=3, column = 2)
        
    else: 
        label1 = tkinter.Label(substituteWindow, text="NO DETECTIOIN OF HEART DISEASES", font=('Times', -35) )
        label1.grid(row=1, column=1, columnspan=6)
        label2 = tkinter.Label(substituteWindow, text="Dear "+str(bmiValues[0]), font=('Times', -30))
        label2.grid(row=2, column=1, columnspan=6)
        label3 = tkinter.Label(substituteWindow, text = "Your BMI is "+str(bmi)+"% and you are  "+out, font=('Times', -20))
        label3.grid(row=3, column = 1)
        
    substituteWindow.mainloop()
        
#------------------------------------Readig dataset------------------
heart = pd.read_csv("heart_disease.csv")

#using min max scaler
min_max = MinMaxScaler()
columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
heart[columns_to_scale ] = min_max.fit_transform(heart[columns_to_scale])
y = heart['target']
X = heart.drop(['target'], axis = 1)

#training and testing of datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)
# heart = pd.get_dummies(heart, columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'])




# print(len(X_train))
# len(X_test)


#---------------------knn classifier-----------------------
knn_classifier = KNeighborsClassifier(n_neighbors = 4)
knn_classifier.fit(X_train, y_train)

 


#-----------------------starting main window of tkinter---------------------
mainWindow = tkinter.Tk()
mainWindow.geometry('640x480-15-200')
mainWindow['padx']=20
mainWindow.title("HEART DISEASE PREDICTION")
mainWindow.configure(bg='#006064') # hash49B

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=2)
mainWindow.rowconfigure(0, weight=0)
mainWindow.rowconfigure(1, weight=0)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)
mainWindow.rowconfigure(6, weight=1)
mainWindow.rowconfigure(7, weight=1)
mainWindow.rowconfigure(8, weight=1)
mainWindow.rowconfigure(9, weight=1)
mainWindow.rowconfigure(10, weight=10)


label1 = tkinter.Label(mainWindow, text="Enter all your details", font=('Impact', -25),bg='#006064' )
label1.grid(row=1, column=0, columnspan=6)


#-------------------------Input boxes----------------------

ageFrame = tkinter.LabelFrame(mainWindow, text="Age(in years)")
ageFrame.grid(row=3, column=0)
ageFrame.config(font=("Courier", -15))
age= tkinter.Entry(ageFrame)
age.grid(row=2, column=2, sticky='nw')

sexFrame = tkinter.LabelFrame(mainWindow, text="Sex(0-female,1-male)")
sexFrame.grid(row=3, column=1)
sexFrame.config(font=("Courier", -15))
sex= tkinter.Entry(sexFrame)
sex.grid(row=2, column=2, sticky='nw')

chestPainFrame = tkinter.LabelFrame(mainWindow, text="CP (0/1/2/3/4)")
chestPainFrame.grid(row=3, column=2)
chestPainFrame.config(font=("Courier", -15))
chestPain= tkinter.Entry(chestPainFrame)
chestPain.grid(row=2, column=2, sticky='nw')


rbpFrame = tkinter.LabelFrame(mainWindow, text="RBP (94-200)")
rbpFrame.grid(row=4, column=0)
rbpFrame.config(font=("Courier", -15))
rbp= tkinter.Entry(rbpFrame)
rbp.grid(row=2, column=2, sticky='nw')

serumCholFrame = tkinter.LabelFrame(mainWindow, text="Serum Chol")
serumCholFrame.grid(row=4, column=1)
serumCholFrame.config(font=("Courier", -15))
serumChol = tkinter.Entry(serumCholFrame)
serumChol.grid(row=2, column=2, sticky='n')

FBSFrame = tkinter.LabelFrame(mainWindow, text="Fasting BP(0-4)")
FBSFrame.grid(row=4, column=2)
FBSFrame.config(font=("Courier", -15))
FBS= tkinter.Entry(FBSFrame)
FBS.grid(row=2, column=2, sticky='nw')

ECGFrame = tkinter.LabelFrame(mainWindow, text="ECG (0/1/2)")
ECGFrame.grid(row=5, column=0)
ECGFrame.config(font=("Courier", -15))
ECG = tkinter.Entry(ECGFrame)
ECG.grid(row=2, column=2, sticky='nw')


thalachFrame = tkinter.LabelFrame(mainWindow, text="thalach(71-202)")
thalachFrame.grid(row=5, column=1)
thalachFrame.config(font=("Courier", -15))
thalach = tkinter.Entry(thalachFrame)
thalach.grid(row=2, column=2, sticky='nw')

exangFrame = tkinter.LabelFrame(mainWindow, text="exAngina(0/1)")
exangFrame.grid(row=5, column=2)
exangFrame.config(font=("Courier", -15))
exang = tkinter.Entry(exangFrame)
exang.grid(row=2, column=2, sticky='nw')


oldpeakFrame = tkinter.LabelFrame(mainWindow, text="Old Peak(int(0-6))")
oldpeakFrame.grid(row=6, column=0)
oldpeakFrame.config(font=("Courier", -15))
oldpeak = tkinter.Entry(oldpeakFrame)
oldpeak.grid(row=2, column=2, sticky='nw')
  
slopeFrame = tkinter.LabelFrame(mainWindow, text="Slope(0/1/2)")
slopeFrame.grid(row=6, column=1)
slopeFrame.config(font=("Courier", -15))
slope = tkinter.Entry(slopeFrame)
slope.grid(row=2, column=2, sticky='nw')

caFrame = tkinter.LabelFrame(mainWindow, text=" C. A (0/1/2/3)")
caFrame.grid(row=6, column=2)
caFrame.config(font=("Courier", -15))
ca = tkinter.Entry(caFrame)
ca.grid(row=2, column=2, sticky='nw')


thalFrame = tkinter.LabelFrame(mainWindow, text=" THAL(0/1/2/3)")
thalFrame.grid(row=7, column=1)
thalFrame.config(font=("Courier", -15))
thal = tkinter.Entry(thalFrame)
thal.grid(row=2, column=2, sticky='nw')

#---------------------------------BMI-----------------------------
nameFrame = tkinter.LabelFrame(mainWindow, text=" Full Name ")
nameFrame.grid(row=8, column=1)
nameFrame.config(font=("Courier", -15))
name = tkinter.Entry(nameFrame)
name.grid(row=2, column=2, sticky='nw')

wFrame = tkinter.LabelFrame(mainWindow, text=" Weight in kgs ")
wFrame.grid(row=7, column=0)
wFrame.config(font=("Courier", -15))
weight = tkinter.Entry(wFrame)
weight.grid(row=2, column=2, sticky='nw')

hFrame = tkinter.LabelFrame(mainWindow, text=" Height in cms ")
hFrame.grid(row=7, column=2)
hFrame.config(font=("Courier", -15))
height = tkinter.Entry(hFrame)
height.grid(row=2, column=2, sticky='nw')


#------------------------Button setup--------------------------------------
analyseButton = tkinter.Button(mainWindow, text="  PROCEED   ", font=('Impact', -30),command=takeInput,bg='red')
analyseButton.grid(row=10, column=0, columnspan=5)



mainWindow.mainloop()


