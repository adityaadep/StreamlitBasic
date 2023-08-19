import streamlit as st


st.title('Hello world')

st.header('Header')

st.subheader('Sub-Header')

st.text('This is Text')

st.markdown('# H1')
st.markdown('## H2')
st.markdown('### H3')
st.markdown('#### H4')
st.markdown('##### H5')
st.markdown('###### H6')


st.success("This is Success")
st.info('This is info command')
st.warning('This is warning')
st.error("This is error")



exp=ZeroDivisionError('Division with zero is not possible')
st.exception(exp)
#st.exception(ZeroDivisionError('Division with zero is not possible'))

#if you want to know about any function
st.help(ZeroDivisionError)


st.write('1+2+6')
st.write(1+2+6)

st.code('x=10\n'
        'for i in range(x):\n'
        'print(x)')


st.checkbox('Male')
#st.checkbox('Female')

if(st.checkbox('Female')):
    st.write('You are Female')
else:
    st.write('You are Male')





radiobutton=st.radio('Select One:',('Male','Female','Other'))

if(radiobutton=='Male'):
    st.write('You are Male')
elif(radiobutton=='Female'):
    st.write('You are Female')
else:
    st.write('You are other')


st.subheader('select box')

select_box=st.selectbox('Data Science:',['Python','ML','Tableau','Deep Learning'])
st.write('You have selected ',select_box)


st.subheader('Multi-select box')

multi_select_box=st.multiselect('Data Science:',['Python','ML','Tableau','Deep Learning'])
st.write('You have selected ',len(multi_select_box),multi_select_box)

#st.button("Button")

if(st.button("Click me")):
    st.write('You have clicked the button')

st.subheader('Slider')

slider=st.slider('select the volume',1,10,step=1)
st.write('You slider has value',slider)


st.subheader('Take USer Text input')

name=st.text_input("Enter your name")

st.write("Hi",name)


username=st.text_input("Username")
password=st.text_input("Password",type="password")

st.subheader("TextArea")
textarea=st.text_area("Please write something about yourself")
st.write(textarea)


st.subheader("Number Input")
st.number_input("Select Age",18,100)

st.subheader("Date Input")
st.date_input("Select Date")

st.subheader("Time Input")
st.time_input("Select Time")
