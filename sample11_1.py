import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.sidebar.write('サイドバー')
text = st.sidebar.text_input('あなたの趣味は何ですか？')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味：', text
'コンディション：', condition
