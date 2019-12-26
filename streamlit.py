import streamlit as st,pandas as pd,numpy as np,math,matplotlib.pyplot as p,seaborn as sn
st.header('Expression plotter App')
Exp=st.sidebar.selectbox('Select type of expression',('Linear','Quadratic','Cubic','Quartic','Trig','Exponential'))
values=[x for x in range(-10,11)]
values_for_trig_exp=[math.radians(x) for x in range(0,361,10)]
values_exp=[x for x in np.arange(-1,1,0.1)]
if Exp=='Linear':
    st.write('Input values of coefficient')                        
    a=st.number_input('Enter x coefficient')
    b=st.number_input('Enter constant')
    eq=[a*x+b for x in values]
elif Exp=='Quadratic':
    st.write('Input values of coefficient')
    a=st.number_input('Enter x squared coefficient')
    b=st.number_input('Enter x coefficient')
    c=st.number_input('Enter constant')
    eq=[a*x**2-b*x+c for x in values]
elif Exp=='Cubic':
    st.write('Input values of coefficient')
    a=st.number_input('Enter x cube coefficient')
    b=st.number_input('Enter x squared coefficient')
    c=st.number_input('Enter x coefficient')                       
    d=st.number_input('Enter a constant')
    eq=[a*x**3+b*x**2+c*x+d for x in values]
elif Exp=='Quartic':
    st.write('Input values of coefficient')
    a=st.number_input('Enter x quartic coefficient')
    b=st.number_input('Enter x cube coefficient')
    c=st.number_input('Enter x squared coefficient')
    d=st.number_input('Enter x coefficient')
    e=st.number_input('Enter a constant')
    eq=[a*x**4+b*x**3+c*x**2+d*x+e for x in values]
elif Exp=='Trig':
    st.write('Input values of coefficient [bsin(ax)+ccos(ax)+dtan(ax)+e] x in radians')
    a=st.number_input('Enter x coefficient')
    b=st.number_input('Enter sine coefficient')
    c=st.number_input('Enter cosine coefficient')
    d=st.number_input('Enter tangent coefficient')
    e=st.number_input('Enter a constant')
    eq=[b*math.sin(a*x)+c*math.cos(a*x)+d*math.tan(a*x)+e for x in values_for_trig_exp]
else:
    st.write('Input values of coefficient [aexp(bx)+c]')
    a=st.number_input('Enter x coefficient')
    b=st.number_input('Enter exponential coefficient')
    c=st.number_input('Enter a constant')
    eq=[a*math.exp(b*x)+c for x in values_exp]
if Exp=='Trig':    
    df=pd.DataFrame({'x':values_for_trig_exp,'y':eq})
elif Exp=='Exponential':
    df=pd.DataFrame({'x':values_exp,'y':eq})
else:
    df=pd.DataFrame({'x':values,'y':eq})
if st.checkbox("Show/Hide values' ranges"):
    st.write(df,width=100, height=50)
sn.lineplot(df['x'],df['y'])
p.axhline(0)
p.axvline(0)
p.xlabel('values[x]')
p.ylabel('solutions[y]')
st.pyplot()
