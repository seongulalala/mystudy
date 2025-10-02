# 1. 퍼널분석 개요
* 사용자가 도달하기까지 거치는 일련의 단계들을 시각화하고 분석하는 기법
* 사용자가 어디서 많이 이탈하는지 즉 , **병목현상**이 어디서 발생하는지 파악하는데 사용  

<br>

# 2. 분석절차
1. 퍼널 단계 정의
   - 사용자의 행동을 몇 가지 단계로 구분

2. 단계별 사용자수 계산

3. 시각화

<br>  

# 3. 분석방법
## 1. 데이터 준비
```python
import pandas as pd
import numpy as np

raw_df = pd.read_csv('funnel_raw_df.csv')
```

## 2. 퍼널 단계별 집계
```python
# 퍼널 순서 정의
funnel_order = ['visit','view_item','add_to_cart','begin_checkout','purchase']

# 퍼널별 (고유한) 고객 수 집계

raw_df['event_name'].value_counts()
# > ★☆순서대로 안 나옴★☆ 

#순서대로 나오게 정렬
funnel_df = raw_df.groupby('event_name')['user_id'].nunique().reindex(funnel_order).reset_index()

#퍼널 열 이름 변경
funnel_df.columns = ['stage', 'user_count']

```

## 3. 시각화
**필수**
```py
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = funnel_df['stage'],  # 각 단계 이름
    x = funnel_df['user_count']  # 각 단계별 사용자 수
))
fig.show()

```
**추가작업**
```py
fig = go.Figure(go.Funnel(
    y = funnel_df['stage'],
    x = funnel_df['user_count'],
    
    # 텍스트 위치: 막대 안에 텍스트 표시
    textposition = "inside",
    
    # 표시할 정보: 값, 초기 대비 %, 이전 단계 대비 %
    textinfo = "value+percent initial+percent previous",

    # 막대 색상 및 테두리
    marker = {
        "color": ["#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F"],
        "line": {
            "width": 1,
            "color": "#333333"
        }
    },

    # 단계 연결선 스타일
    connector = {
        "line": {
            "color": "gray",
            "dash": "dot",
            "width": 2
        }
    }
))
fig.show()

```


