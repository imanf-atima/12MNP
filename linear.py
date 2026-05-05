import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv("data.csv")
X=df[['HouseStudied']]
Y=df['ExamScore']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,Y_train)
st.tilte("Exam Score Predictor")
st.write("Enter hours studied to predict exam score")
