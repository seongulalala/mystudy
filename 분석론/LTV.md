# 1. LTV 단순 계산
``` 
LTV = ARPU(고객당 평균 수익) x LifeTime(고객 생애 기간)
```
- `ARPU = 특정기간 총매출 / 해당 기간 황성 사용자 수`
- `LifeTime = 1 / Churn Rate (고객 이탈률)`  
  
  즉 ,

  $
  LTV = \frac{ARPU\ (\text{고객당 평균 수익})} {ChurnRate\ (\text{고객 이탈률})}  
  $  
  
# 2 . LTV 심화 계산
## 1. 데이터 불러오기
```python
!pip install lifetimes

import pandas as pd
from lifetimes import BetaGeoFitter, GammaGammaFitter
from lifetimes.utils import summary_data_from_transcation_data

transactions_df = pd.read_csv()
```

## 2. 데이터 준비하기  
``` python
# 기존 df를 LTV를 구하는데 적합하도록 수정(요약)
summary = summary_data_from_transation_data(
    transactions_df,
    customer_id_col = 'cusomer_id',
    datetime_col = 'transaction_date',
    montary_value_col = 'monetary_value',
    observation_period_end = '2025-08-05'
)
```
* 좌변 = 고정
* 우변 = transations_df의 필드명
* 마지막 = 분석 기준 시점

## 3. 분석 진행
### 1. bgf모델 선언  (미래 구매 횟수 예측 모델)
```python
# 모델 불러오기
bgf = BataGeoFitter(penalizer_coef = 0.001) 

# 모델 적합하기(fit하기)
bgf.fit(summary['frequency'],summary['recency'],summary['T'])
# 요약했던 df의 frequency, recency, T 순서로 입력
```

### 2. Gamma-Gamma모델 (평균 구매액 예측)
```python
# 모델에 조건주기(fequncy가 1 이상)
summary_gg = summary[summary['frequency']>0]
# 모델 불러오기
ggf = GammaGammaFitter(penalizer_coef = 0.001)
# 모델 적합하기
ggf.fit(summary_gg['frequency'],summary_gg['monetary_value'])
```

### 3. LTV계산하기
- bgf = 미래 구매횟수 예측
- ggf = 평균 구매금액 예측

```python
ltv = ggf.customer_lifetime_value(
    bgf,
    summary['frequency'],
    summary['recency'],
    summary['T'],
    summary['monetary_value'],
    time = 12,
    freq = 'D',
    discount_rate = 0.01
)
```
- time = LTV를 예측할 미래 기간
- freq = 입력 데이터의 단위가 '일'로 요약
- discount_rate = 0.01 = 월간 할인율(미래가치를 현재 가치로 환산)
