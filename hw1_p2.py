import pandas as pd  #padas is used for csv math
import os #os used for genrerating flexible filepath

direc = os.path.dirname(os.path.abspath(__file__)) #find directory

df = pd.read_csv(direc+"/data.csv", names = ['data']) #open csv

mean = round(df['data'].mean(),2) #rounded mean
var = round(df['data'].var(),2)   #rounded variance

dataList = [mean, var]  #list of data

print(dataList)