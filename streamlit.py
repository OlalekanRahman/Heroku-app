import time,streamlit as st,pandas as pd,numpy as np,math,matplotlib.pyplot as p,seaborn as sn
st.title('Expression plotter App')
st.markdown('**This app is a tool for demonstrating how changing variable coefficients transforms graphical facades of mathematical expressions. it is prepared for school students and adults not in the mathematical knows')
Exp=st.sidebar.selectbox('Select Type of Function',('','Linear','Quadratic','Cubic','Quartic','Trig','Exponential'))
def graph_axis_range():
    st.write('Input x-axis value range')
    x_min_value=st.number_input('Enter min value for x-axis')
    x_max_value=st.number_input('Enter max value for x-axis')
    x_axis_step=st.number_input('Enter step in  x-axis values',value=0.01)
    return np.arange(x_min_value,x_max_value,x_axis_step)
if Exp=='':
    st.write('*Select a function to view') 
elif Exp=='Linear':
    values=graph_axis_range()
    st.write('Input values of coefficient')                        
    a=st.number_input('Enter x coefficient')
    b=st.number_input('Enter constant')
    eq=[a*x+b for x in values]
elif Exp=='Quadratic':
    values=graph_axis_range()
    st.write('Input values of coefficient')
    a=st.number_input('Enter x squared coefficient')
    b=st.number_input('Enter x coefficient')
    c=st.number_input('Enter constant')
    eq=[a*x**2-b*x+c for x in values]
elif Exp=='Cubic':
    values=graph_axis_range()
    st.write('Input values of coefficient')
    a=st.number_input('Enter x cube coefficient')
    b=st.number_input('Enter x squared coefficient')
    c=st.number_input('Enter x coefficient')                       
    d=st.number_input('Enter a constant')
    eq=[a*x**3+b*x**2+c*x+d for x in values]
elif Exp=='Quartic':
    values=graph_axis_range()
    st.write('Input values of coefficient')
    a=st.number_input('Enter x quartic coefficient')
    b=st.number_input('Enter x cube coefficient')
    c=st.number_input('Enter x squared coefficient')
    d=st.number_input('Enter x coefficient')
    e=st.number_input('Enter a constant')
    eq=[a*x**4+b*x**3+c*x**2+d*x+e for x in values]
elif Exp=='Trig':
    values=graph_axis_range()
    st.write('Input values of coefficient [bsin(ax)+ccos(ax)+dtan(ax)+e], x in degrees')
    a=st.number_input('Enter x coefficient')
    b=st.number_input('Enter sine coefficient')
    c=st.number_input('Enter cosine coefficient')
    d=st.number_input('Enter tangent coefficient')
    e=st.number_input('Enter a constant')
    eq=[b*math.sin(a*x)+c*math.cos(a*x)+d*math.tan(a*x)+e for x in [math.radians(x) for x in values]]
else:
    values=graph_axis_range()
    st.write('Input values of coefficient [aexp(bx)+c]')
    a=st.number_input('Enter exponential[exp] coefficient')
    b=st.number_input('Enter x coefficient')
    c=st.number_input('Enter a constant')
    eq=[a*(math.exp(b*x))+c for x in values]
def table():
    if st.checkbox("Show/Hide values' ranges"):
        return st.dataframe(df)

if Exp=='':
    pass
elif Exp=='Trig':    
    df=pd.DataFrame({'x':values,'y':eq})
    table()
elif Exp=='Exponential':
    df=pd.DataFrame({'x':values,'y':eq})
    table()
else:
    df=pd.DataFrame({'x':values,'y':eq})
    table()
if Exp=='':
    pass
else:
    sn.lineplot(df['x'],df['y'])
    p.axhline(0)
    p.axvline(0)
    p.xlabel('values[x]')
    p.ylabel('solutions[y]')
    st.pyplot()
