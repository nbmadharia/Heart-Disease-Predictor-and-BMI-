# Heart Disease Predictor and BMI

## Introduction
About 1 in 16 women age 20 and older (6.2%) have coronary heart disease, the most common type of heart disease:4
About 1 in 16 white women (6.1%), black women (6.5%), and Hispanic women (6%)
About 1 in 30 Asian women (3.2%)

The number of people affected by heart disease increases with age in both men and women. About four out of five people who die of coronary heart 
disease are 65 or older. Because heart disease becomes more common as you age, it's important to have regular checkups and watch your heart disease 
risk factors. But it is not possible to monitor everyone everytime. What if you can predict your own heart disease by providing basic details about yourself.

This project is based on how common the heart disease is and predict by entering the data related to your body. Also It has been noticed that obese people 
will more likely to have heart diseases. So, I have added that attribute also. It is based on KNN classifier model. Where we already have the correct output 
and set of features associated with that output. Used an algorithm and try to train them with the existing data and then try to predict the output of new data 
with only features associated with them. KNN tries to find similarities between predictors and values that are within the dataset.

## Model Accuracy 88%

## About Dataset: (source: https://www.kaggle.com/ronitf/heart-disease-uci)
We have many columns like: 
Age : Age of the patient
Sex : Sex of the patient (0 for female and 1 for male)
exang: exercise induced angina (1 = yes; 0 = no)
ca: number of major vessels (0-3)
cp : Chest Pain type chest pain type
Value 1: typical angina
Value 2: atypical angina
Value 3: non-anginal pain
Value 4: asymptomatic
trtbps : resting blood pressure (in mm Hg)
chol : cholestoral in mg/dl fetched via BMI sensor
fbs : (if fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
rest_ecg : resting electrocardiographic results
Value 0: normal
Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
Value 2: showing probable or definite left ventricular hypertrophy by Estes’ criteria
thalach: maximum heart rate achieved

Name: Name of the patient
Weight: weight of the patient in kgs
Height: height of the patient in cm

output: 0 = less chances of heart attack 
output: 1 = more chances of heart attack
bmi value in %

## As obesity also leads to many heart diseases 
## BMI values: 
- 18.4 or less - Underweight
- 18.5 to 24.9 - Healthy or Normal Weight
- 25 to 29.9 - Overweight
- 30-34.9 - Obesity class 1
- 35 or more - Obesity class 2 and 3

# FUTURE SCOPE:
As the time was very less so I was able to implement this much of part only but it can be scaled up to a big and real-time project with more utilities and functionalities:
## Mental health as a major problem
As you grow old you get more tension, stress and many more things. The most common mental and neurological disorders in this age group are dementia and depression, which affect approximately 5% and 7% of the world's older population, respectively.
To solve this we can use OPENCV library to perform real time image processing and it can determine whether the person is suffering from any mental illness or not. If it finds out then it will automatically inform his/her family members.

## Other utilities that can be added
1. We can use similar model to predict strokes
2. We can use google api to recommend nearest hospitals or doctors.
3. As data is the new fuel, we can store and manage all the inputs given into the google sheets directly using the program. By this we will be having a good amount of data to use it further for other projects or to improve the model accuracy.


![alt text](https://ibb.co/2NB2V19)
