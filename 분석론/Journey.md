# 🗺 사용자 여정 분석 (User Journey Analysis)

## 1. 개요

- 사용자가 서비스를 이용하는 동안 어떤 **행동 순서**를 거쳤는지 추적·분석하는 기법
- 단순히 퍼널 단계를 밟는 것에 그치지 않고, **비선형적 흐름**이나 **반복 행동**, **전환 루트 다양성**까지 파악할 수 있음
- 복잡한 사용자 행동을 시퀀스 형태로 이해함으로써 **UX 개선**, **이탈 지점 분석**, **리마케팅 전략 수립**에 활용

---

## 2. 분석 절차

1. **이벤트 로그 확보**  
   - 시간 순으로 정렬된 사용자 이벤트 로그 수집 (`user_id`, `event_name`, `event_time` 등)

2. **세션 정의**  
   - 사용자 ID 및 시간 간격을 기준으로 하나의 세션 단위를 구분  
   *(예: 30분 이상 비활성 시 새로운 세션으로 간주)*

3. **행동 시퀀스 생성**  
   - 세션별로 사용자의 행동을 순서대로 나열하여 시퀀스 분석에 활용

4. **시각화 및 분석**  
   - Sankey Diagram, Transition Matrix, 패턴 빈도 분석 등으로 행동 흐름 파악

---

## 3. 분석 예시

### 🧪 1. 시퀀스 데이터 생성
```python
import pandas as pd

# 이벤트 로그 불러오기
df = pd.read_csv("user_journey_log.csv")

# 이벤트 시간 기준 정렬
df = df.sort_values(by=['user_id', 'event_time'])

# 사용자별 시퀀스 생성
user_sequences = df.groupby('user_id')['event_name'].apply(list).reset_index()
user_sequences.columns = ['user_id', 'event_sequence']

# 예시 출력
user_sequences.head()
```

### 2. 전이행렬 만들기
```py
from collections import Counter
import pandas as pd

# 모든 transition 쌍 추출
all_transitions = []

for sequence in user_sequences['event_sequence']:
    transitions = zip(sequence[:-1], sequence[1:])
    all_transitions.extend(transitions)

# transition 빈도수 계산
transition_counts = Counter(all_transitions)

# DataFrame으로 변환
transition_df = pd.DataFrame(transition_counts.items(), columns=['transition', 'count'])
transition_df[['from', 'to']] = pd.DataFrame(transition_df['transition'].tolist(), index=transition_df.index)
transition_df.drop('transition', axis=1, inplace=True)

transition_df.head()
```

### 3. Sankey 다이어그램 시각화
```py
import plotly.graph_objects as go

# 고유 단계 추출 및 인덱싱
labels = list(set(transition_df['from']) | set(transition_df['to']))
label_to_index = {label: i for i, label in enumerate(labels)}

# source, target, value 생성
sources = transition_df['from'].map(label_to_index)
targets = transition_df['to'].map(label_to_index)
values = transition_df['count']

# Sankey 생성
fig = go.Figure(data=[go.Sankey(
    node=dict(label=labels, pad=15, thickness=20),
    link=dict(source=sources, target=targets, value=values)
)])
fig.show()
```

## 4. 활용 예시
| 활용 분야      | 설명                            |
| ---------- | ----------------------------- |
| UX 개선      | 사용자가 반복하거나 돌아가는 흐름 파악 → UI 개선 |
| 마케팅 최적화    | 전환률이 높은 여정 루트 중심으로 타겟팅 전략 설정  |
| 제품 기획      | 주요 기능 흐름 파악 및 우선순위 설정         |
| A/B 테스트 분석 | 그룹별 행동 흐름 차이 비교로 전략적 판단 가능    |

---

## ✅ 요약

- 사용자 여정 분석은 퍼널 분석보다 더 다양한 루트와 행동 흐름을 포착할 수 있음
- UX, 마케팅, 제품 전략 등 다양한 영역에 인사이트 제공
- Sankey Diagram을 활용하면 행동 흐름을 직관적으로 파악 가능
