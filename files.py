import streamlit as st
import pandas as pd
st.subheader("Uploading the CSV File")

df =st.file_uploader('Upload the csv file',type=['csv','xlsx'])
st.table(df)
# if df is not None:
#     st.dataframe(df) E:\COURSES\Data Science\python_practise\data\In-One-Go\streamlit_prac


st.subheader("Load the CSV File")
df2=pd.read_csv("E:\COURSES\Data Science\python_practise\data\In-One-Go\streamlit_prac\Jobs.csv")
st.table(df2)



st.subheader("Dealing with images")
st.image('img.png')

st.subheader("Upload the images")

images=st.file_uploader('Upload the Image',type=['png','jpg'])
if images is not None:
     st.image(images)

st.subheader("Upload the Video")
video_file=st.file_uploader('Upload the video',['mp4','mkv'])
if video_file is not None:
     st.video(video_file)


st.subheader("Upload the audio")
audio_file=st.file_uploader('Upload Audio',['mp3','wav'])
if audio_file is not None:
     st.audio(audio_file.read())