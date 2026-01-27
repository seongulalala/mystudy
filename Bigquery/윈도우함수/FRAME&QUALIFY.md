# FRAME
- 데이터의 범위를 전환하는 방법

## ROWS , RANGE

### ROWS
- 물리적인 행 수를 기준으로 경계를 지정
- 이전 행, 이후 3개의 행

### RANGE
- 논리적인 값의 범위를 기준으로 지정
- 값의 3일 전, 3일 후


## 시작과 끝 명시
- PRECEDING : 현재 행 기준으로 이전 행
- FOLLOWING : 현재 행 기준으로 이후 행

- CURRENT ROW : 현재 행
- UNBOUNDED : 처음부터 또는 끝까지


## 생성법 ROWS/RANGE + BETWEEN + 시작 AND 끝  
`ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING`
> 현재 행 기준 1행 전 + 1행 후

`ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`
> 파티션의 처음부터 현재 행까지

# QUALIFY (조건 설정)
- 윈도우 함수에 대한 조건
- WHERE과 같이 쓸 경우 WHERE 아래에

