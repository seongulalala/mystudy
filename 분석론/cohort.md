# 📆 코호트 분석 (Cohort Analysis)

## 1. 개요

- **코호트 분석**은 공통된 속성을 가진 사용자 집단(코호트)의 행동을 시간 흐름에 따라 분석하는 기법
- 주로 신규 유입 고객이 **시간이 지남에 따라 얼마나 유지(retention)되는지**를 파악할 때 사용
- 마케팅, 유저 리텐션, 서비스 개선 등 **고객 생애주기 관리**에 매우 유용

---

## 2. 분석 절차

1. **코호트 기준 정의**  
   - 사용자를 그룹핑할 기준 설정 (예: 최초 가입일, 첫 구매일 등)

2. **행동 지표 선택**  
   - 유저의 특정 행동(예: 로그인, 구매 등)을 리텐션으로 정의

3. **코호트 테이블 생성**  
   - 코호트별로 시간 흐름에 따른 행동 비율을 집계

4. **시각화 및 해석**  
   - 리텐션 매트릭스, 히트맵 등을 통해 코호트별 유지율 비교

---

## 3. 예제: 가입일 기준 주차별 리텐션 분석

### 1️⃣ 데이터 준비

```python
import pandas as pd

# 데이터 불러오기 (예: user_id, signup_date, activity_date)
df = pd.read_csv("user_activity_log.csv", parse_dates=['signup_date', 'activity_date'])

# 주 단위로 변환
df['signup_week'] = df['signup_date'].dt.to_period('W').apply(lambda r: r.start_time)
df['activity_week'] = df['activity_date'].dt.to_period('W').apply(lambda r: r.start_time)
```

### 2️⃣ 코호트와 경과 주차 계산
```py
# 코호트별 경과 주차
df['cohort_index'] = ((df['activity_week'] - df['signup_week']) / pd.Timedelta(weeks=1)).astype(int)
```
### 3️⃣ 코호트 테이블 생성 (리텐션 수치)
```py
# 고유 유저 수 집계
cohort_data = df.groupby(['signup_week', 'cohort_index'])['user_id'].nunique().reset_index()

# 피벗 테이블 생성
cohort_pivot = cohort_data.pivot(index='signup_week', columns='cohort_index', values='user_id')

# 첫 주 유저 수 기준 비율 계산
cohort_size = cohort_pivot.iloc[:, 0]
retention = cohort_pivot.divide(cohort_size, axis=0)
retention = retention.round(3)

retention.head()
```

### 4️⃣ 시각화 (히트맵)
```py
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
sns.heatmap(retention, annot=True, fmt='.0%', cmap="YlGnBu")
plt.title('Cohort Analysis: Weekly Retention')
plt.xlabel('Cohort Index (Weeks Since Signup)')
plt.ylabel('Signup Week')
plt.show()
```

## 4. 활용
| 활용 분야       | 설명                                    |
| ----------- | ------------------------------------- |
| 유저 리텐션 분석   | 고객 유입 시점별로 얼마나 남아 있는지 분석해 이탈 시점 파악    |
| 마케팅 캠페인 비교  | 특정 캠페인 기간에 유입된 유저의 리텐션이 높은지/낮은지 비교 가능 |
| 제품 기능 효과 측정 | 새로운 기능 도입 이후 유입된 코호트의 리텐션 변화 분석       |
| 구독 서비스 분석   | 결제 시점 기준으로 N주 뒤 갱신율 측정 (결제 기반 코호트)    |
