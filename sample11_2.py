import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

left_column, right_column = st.columns(2)

with left_column:
    btn = left_column.button('右カラムに文字を表示')

with right_column:
    if btn:
        right_column = st.write('左カラムのボタンを押すと右カラムに書き込むことができます。')

expander = st.expander('問い合わせ')
expander.write('問い合わせの回答を書く')

#text = st.text_input('あなたの趣味は何ですか？')
#condition = st.slider('あなたの今の調子は？', 0, 100, 50)

#'あなたの趣味：', text
#'コンディション：', condition
