import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

st.subheader('Plots.py')





st.subheader('Line chart')
chart_data=pd.DataFrame(np.random.rand(20,3),columns=['Line-1','Line-2','Line-3'])
st.line_chart(chart_data)


st.subheader('Area Chart')
st.area_chart(chart_data)



st.subheader('Bar Chart')
st.bar_chart(chart_data)


st.header('Visualization with Matplotlib and Seaborn')

st.subheader('Loading the csv File')
df=pd.read_csv('iris.csv')
st.dataframe(df)

st.subheader('Distribution plot with Matplot lib')
fig=plt.figure(figsize=(15,8))
df['species'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Distribution plot with Seaborn lib')
fig2=plt.figure(figsize=(15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig2)


st.header('Multiple Graphs')

col1, col2 = st.columns(2)
with col1:
    col1.header('KDE = False')
    fig1 = plt.figure(figsize = (5,5))
    sns.distplot(df['sepal_length'], kde = False)
    st.pyplot(fig1)
with col2:
    col2.header('KDE = True')
    fig2=plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'], kde = True)
    st.pyplot(fig2)

st.header('Changing the Styles')
col1 ,col2=st.columns(2)
with col1:
    fig1=plt.figure(figsize=(5,5))
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['sepal_length'],hist=False)
    st.pyplot(fig1)
with col2:
    fig2=plt.figure(figsize=(5,5))
    sns.set_theme(context='poster',style='darkgrid')
    sns.distplot(df['sepal_length'],hist=True)
    st.pyplot(fig2)




st.header('Exploring Different Graphs')

st.subheader('1.Scatter Plot')
fig,ax=plt.subplots(figsize=(18,5))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader('2.Count Plot')
fig=plt.figure(figsize=(5,5))
sns.countplot(data=df,x='species')
st.pyplot(fig)

st.subheader('3. Box Plot')
fig=plt.figure(figsize=(18,7))
sns.boxplot(data=df,x='species',y='petal_length')
st.pyplot(fig)


st.subheader('4. Violin-Plot')
fig = plt.figure(figsize = (15,8))
sns.violinplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(fig)
