import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

'''
## チェックボックス
'''
st.write('チェックボックスにチェックが入っていればイメージを表示')

if st.checkbox('イメージを表示'):
    img = Image.open('Slime.png')
    st.image(img, caption='スライム')

'''
## セレクトボックス
'''

option = st.selectbox(
    'あなたが好きな数字は何ですか？',
    list(range(1, 11))
)

'あなたの好きな数字は', option, 'です。'

'''
## テキスト入力
'''
text = st.text_input('あなたの趣味は何ですか？')
'あなたの趣味：', text

'''
## スライダー
'''
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition
 
