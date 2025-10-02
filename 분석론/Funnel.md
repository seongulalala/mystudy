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
    # --- 데이터 설정 ---
    
    # (Y축): 퍼널의 각 단계.
    y = funnel_df['stage'],
    #(X축): 각 단계의 값
    x = funnel_df['user_count'],

)
```
**추가작업**
```py
    # --- 텍스트 정보 설정 ---
    
    # 텍스트 위치
    textposition = "inside",  
    #'inside'는 막대 안
    #'outside'는 바깥쪽을 의미

    # 표시할 텍스트 정보
    textinfo = "value+percent initial+percent previous", 
    #'value'(실제 값), 'percent initial'(첫 단계 대비), 'percent previous'(이전 단계 대비)


    # 각 막대(marker)의 스타일을 설정
    marker = {
        "color": ["#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F"], # 각 막대의 색상을 리스트로 순서대로 지정
        "line": { # 막대의 테두리 선 스타일을 설정
            "width": 1,
            "color": "#333333"
        }
    },
    
    # 각 단계를 연결하는 선(connector)의 스타일을 설정
    connector = {
        "line": { # 선의 색상, 종류('dot', 'solid' 등), 굵기를 지정
            "color": "gray",
            "dash": "dot",
            "width": 2
        }
    }
))
```


