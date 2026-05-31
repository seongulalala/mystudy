# 재귀 CTE (Recursive CTE) 핵심 정리

## 1. 기본 구조

```sql
WITH RECURSIVE CTE_NAME AS (
    -- [앵커] 시작점 정의
    SELECT ...
    FROM 테이블
    WHERE 시작 조건

    UNION ALL

    -- [재귀] 직전 결과를 이용해 다음 단계 탐색
    SELECT ...
    FROM 테이블 AS D
    JOIN CTE_NAME AS P         -- 자기 자신을 JOIN
    ON D.PARENT_ID = P.ID
)
SELECT * FROM CTE_NAME;
```

---

## 2. 두 박스 멘탈 모델

```
┌──────────────────────────────────┐
│ 결과 박스 (Result Box)            │
│ 최종적으로 쌓이는 모든 행          │
└──────────────────────────────────┘
           ↑ 매 라운드 추가

┌──────────────────────────────────┐
│ 작업 박스 (Working Box)           │
│ 직전 라운드 결과만 들어있음         │
│ → 다음 라운드 JOIN의 기준이 됨     │
└──────────────────────────────────┘
```

- 앵커 결과 → 결과 박스에 쌓임, 동시에 작업 박스로 들어감
- 재귀 스텝: 작업 박스 기준으로 JOIN → 새 행을 결과 박스에 추가 + 작업 박스 교체
- 새 행이 없으면 종료

---

## 3. 패턴별 정리

### 패턴 1. 단순 트리 순회 (+ Depth)

**특정 노드에서 하위 전체 탐색**

```sql
RECURSIVE_CTE AS (
    SELECT *, 0 AS DEPTH
    FROM DEPT
    WHERE DEPT_ID = 3              -- 시작점 지정

    UNION ALL

    SELECT D.*, P.DEPTH + 1
    FROM DEPT AS D
    JOIN RECURSIVE_CTE AS P
    ON D.PARENT_DEPT_ID = P.DEPT_ID
)
```

- 앵커의 `WHERE` 조건이 시작점을 결정
- 재귀에서는 조건 없이 자식을 자유롭게 탐색

---

### 패턴 2. 경로 누적 (Path Accumulation)

**루트부터 각 노드까지의 경로 문자열 생성**

```sql
RECURSIVE_CTE AS (
    SELECT *, CAST(DEPT_NAME AS CHAR(1000)) AS PATH
    FROM DEPT
    WHERE PARENT_DEPT_ID IS NULL   -- 루트에서 시작

    UNION ALL

    SELECT D.*, CONCAT(P.PATH, ' > ', D.DEPT_NAME)
    FROM DEPT AS D
    JOIN RECURSIVE_CTE AS P
    ON D.PARENT_DEPT_ID = P.DEPT_ID
)
```

- `CAST(... AS CHAR(1000))`: 문자열 누적 시 타입 안전을 위해 앵커에서 명시
- `CONCAT`으로 경로를 이어붙임

---

### 패턴 3. 다중 시작점 + 집계 (Multi-Start + Aggregate)

**각 부모 노드별로 하위 전체를 집계**

```sql
RECURSIVE_CTE AS (
    -- 앵커: 단과대(depth=1)만 시작점으로 지정
    SELECT *, DEPT_ID AS ROOT_DEPT_ID
    FROM DEPT
    WHERE PARENT_DEPT_ID = 1       -- 대학교의 직속 자식만

    UNION ALL

    SELECT D.*, P.ROOT_DEPT_ID     -- 시작점 ID를 끝까지 전파
    FROM DEPT AS D
    JOIN RECURSIVE_CTE AS P
    ON D.PARENT_DEPT_ID = P.DEPT_ID
)
SELECT ROOT_DEPT_ID, SUM(STUDENT_COUNT)
FROM RECURSIVE_CTE
GROUP BY ROOT_DEPT_ID;
```

**핵심 인사이트:**
- 앵커의 `WHERE` 조건으로 **시작점 범위**를 제한
- `ROOT_DEPT_ID = DEPT_ID`로 자기 자신을 레이블링 → 재귀 내내 전파
- 재귀 스텝에서는 `WHERE` 없이 하위 전체 탐색
- 최종 `GROUP BY ROOT_DEPT_ID`로 단과대별 집계

---

## 4. 자주 하는 실수

### ❌ 재귀에서 값을 누적/변환하면 안 된다

```sql
-- 잘못된 예: D.STUDENT_COUNT + P.STUDENT_COUNT
SELECT D.DEPT_ID, D.STUDENT_COUNT + P.STUDENT_COUNT, ROOT_DEPT_ID
FROM DEPT AS D JOIN RECURSIVE_CTE AS P ...
```

- 하위 노드가 부모를 타고 올라가며 **여러 번 누적**됨
- 올바른 방법: `D.STUDENT_COUNT`만 전달, 마지막에 `SUM()`으로 집계

### ❌ STUDENT_COUNT 0인 행도 SUM에 포함됨

- 중간 노드(국문과, 컴퓨터공학과 등)는 STUDENT_COUNT = 0
- 집계에 영향 없으므로 무시해도 되지만, 필요하면 `WHERE STUDENT_COUNT > 0`으로 필터

---

## 5. 앵커 WHERE 조건의 역할

```
앵커: WHERE PARENT_DEPT_ID = 1
        → 인문대(2), 공과대(3), 경영대(4) 만 시작

재귀: 조건 없음
        → 인문대 → 국문과, 영문과, ...
        → 공과대 → 컴퓨터공학과, 전자공학과, ...
        → (자식 없으면 자동 종료)
```

- **`WHERE` 조건은 앵커에만 적용**된다
- 이후 재귀 스텝은 자식을 조건 없이 자유롭게 탐색
- 앵커에서 박힌 `ROOT_DEPT_ID`가 재귀 내내 그대로 전달됨

---

## 6. 실무 팁

| 상황 | 방법 |
|------|------|
| 문자열 경로 누적 | 앵커에 `CAST(col AS CHAR(1000))` |
| 단과대별 집계 | 앵커에 `ROOT_DEPT_ID = DEPT_ID` |
| 깊이 제한 | 재귀에 `WHERE DEPTH < N` |
| 리프 노드 찾기 | `NOT EXISTS (SELECT 1 FROM T WHERE PARENT_ID = T.ID)` |