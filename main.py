import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.write('writeでデータフレームを表示')
st.write(df)

st.write('dataframeでデータフレームを表示')
st.dataframe(df, width=200, height=200)

st.write('データフレームの最大値をハイライト表示')
st.dataframe(df.style.highlight_max(axis=0))

st.write('tableでデータフレームを表示（staticな表を作成）')
st.table(df.style.highlight_max(axis=0))

st.write('マジックコマンドで文字サイズやPythonコードを記述できる')
'''
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

'''

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.write('折れ線グラフ')
st.line_chart(df2)

st.write('面チャート')
st.area_chart(df2)

st.write('棒グラフ')
st.bar_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.dataframe(df3)
st.write('マップにプロットする')
st.map(df3)

st.write('イメージを表示')
img = Image.open('Slime.png')
st.image(img, caption='スライム')