import streamlit as st
import numpy as np
import pandas as pd

st.title("Foram Khuthiya")
st.write("MSc DSAI")
st.header("Python")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.caption("Caption trial")
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))
st.table(df)
data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(data)

col1, col2 = st.columns(2)

with col1:
    st.header('Initials')
    st.image('images/fk.png', width=300)
with col2:
    st.header('Python')
    st.image('images/python.png', width=300)
