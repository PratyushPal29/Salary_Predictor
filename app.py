import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

data = pd.read_csv("public//salary1.csv")

st.title("Salary Prediction")

nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])

if nav == "Home":
    st.image("public//Salary_home.jpg")
    if st.checkbox("Show table"):
        st.table(data)

    if st.checkbox("Graph"):
        val = st.slider("Filter data using years of experience",0,10)
        data = data.loc[data["experience"]>=val]
        plt.figure(figsize=(10,5))
        plt.scatter(data["experience"],data["salary"])
        plt.ylim(0)
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot()

if nav == "Prediction":
    st.header("Know your Salary")
    val = st.number_input("Enter your experience",0.00,10.00,step=0.01)
    grad = st.selectbox(
        'Graduate in:',
        ('B.Tech', 'M.Tech')
    )
    field = st.selectbox(
        'Field:',
        ('Engineer',
         'Manufacturing',
        'Construction',
        'Machinery',
        'IT Service',
        'Consultancy',
        'Automobile',
        'Power',
        'Electronics',
        'Mining',
        'Electrical',
        'Chemical',
        'Software Products',
        'Fashion & Textile',
        'Aerospace',
        'Food Processing',
        'Marine',
        'Printing & Packaging',
        'Biotechnology',
        'Railways',
        'Agriculture')
    )

    data = data.loc[data["field"]==field]
    x = np.array(data["experience"]).reshape(-1,1)
    lr = LinearRegression()
    lr.fit(x,np.array(data["salary"]))
    val = np.array(val).reshape(-1,1)
    pred = lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your predicted salary {round(pred,2)} LPA")
if nav == "Contribute":
    st.header("Contribute to our dataset")
    ex = st.number_input("Enter your Experience",0.0,20.0,step = 0.001)
    sal = st.number_input("Enter your Salary",0.00,10.00,step = 0.001)
    fld = st.selectbox(
        'Field:',
        ('Manufacturing',
        'Construction',
        'Machinery',
        'IT Service',
        'Consultancy',
        'Automobile',
        'Power',
        'Electronics',
        'Mining',
        'Electrical',
        'Chemical',
        'Software Products',
        'Fashion & Textile',
        'Aerospace',
        'Food Processing',
        'Marine',
        'Printing & Packaging',
        'Biotechnology',
        'Railways',
        'Agriculture')
    )
    if st.button("submit"):
        to_add = {"Experience":[ex],"Salary":[sal],"Field":[fld]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("public//Salary1.csv",mode='a',header = False,index= False)
        st.success("Submitted")