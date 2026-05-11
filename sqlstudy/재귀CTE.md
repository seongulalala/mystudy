```SQL
WITH RECURSIVE 이름 AS (
    -- 앵커: 시작값 정의
    SELECT 시작값
    
    UNION ALL
    
    -- 재귀: 이전 결과를 받아서 다음 값 만들기
    SELECT 다음값
    FROM 이름
    WHERE 종료_조건
)
SELECT * FROM 이름
```

```SQL
## 1~10을 출력
WITH RECURSIVE BASE AS
(
    SELECT 1 AS NUMBER
    UNION ALL
    
    SELECT NUMBER +1
    FROM BASE
    WHERE NUMBER < 10
)

SELECT * FROM BASE
결과 = NUMBER = 1 ~ 10

---
## 1~20까지의 짝수만 출력
 WITH RECURSIVE BASE AS(
     SELECT 2 AS NUMBER
    
     UNION ALL
     SELECT NUMBER + 2
     FROM BASE 
     WHERE NUMBER <20
)

SELECT * FROM BASE
---
## 구구단 2단
WITH RECURSIVE BASE AS(
    SELECT 
        2 AS DAN, 
        1 AS NUM, 
        2 AS RESULT
    
    UNION ALL
    
    SELECT 
        DAN, 
        NUM + 1,
        RESULT + 2
    FROM BASE 
    WHERE NUM < 9
)


SELECT * FROM BASE
```

응용
```SQL
WITH RECURSIVE 
    EMPLOYEES (EMP_ID, EMP_NAME, MANAGER_ID) AS (
        SELECT 1, '김대표', NULL UNION ALL
        SELECT 2, '이부장', 1    UNION ALL
        SELECT 3, '박부장', 1    UNION ALL
        SELECT 4, '최과장', 2    UNION ALL
        SELECT 5, '정과장', 2    UNION ALL
        SELECT 6, '한대리', 4    UNION ALL
        SELECT 7, '윤대리', 5    UNION ALL
        SELECT 8, '송사원', 6
    ),
    SUBORDINATES AS (
        SELECT *
        FROM EMPLOYEES
        WHERE EMP_ID = 2

        UNION ALL

        SELECT E.EMP_ID, E.EMP_NAME, E.MANAGER_ID
        FROM EMPLOYEES AS E
        JOIN SUBORDINATES AS S
          ON E.MANAGER_ID = S.EMP_ID
    )
SELECT EMP_ID, EMP_NAME 
FROM SUBORDINATES
WHERE EMP_ID <> 2;
```

## 팁
내가 만든 CTE와 기존 테이블을 연결하는 것  
처음엔 내가 만든 CTE > UNION ALL 기존 테이블과 CTE를 연결

CTE는 작업 상자
 - 계속 반복되는 작업을 함
 - 마지막 SELECT에 쓰는 CTE는 결과 상자의 역할

## 재귀 CTE 팁

### 구조
- WITH RECURSIVE 한 번만 사용
- 앵커 + UNION ALL + 재귀 (한 세트)
- 앵커: 시작점 (출발 행)
- 재귀: 이전 결과를 받아 다음 행을 만드는 부분

### 핵심 동작
재귀 부분에서 "내가 만들고 있는 CTE 자기 자신"을
"기존 테이블"과 JOIN해서 한 단계 더 확장한다.
```
  FROM 기존_테이블 AS E
  JOIN 내_CTE      AS C
    ON E.???? = C.????
```
### 방향에 따른 JOIN 조건
- 자식 방향 (위에서 아래로): E.PARENT_ID = C.ID
- 부모 방향 (아래에서 위로): E.ID = C.PARENT_ID

### 컬럼 규칙
- 앵커와 재귀의 SELECT 컬럼 개수/순서/타입이 일치해야 함
- 재귀에서 만드는 한 행은 결국 "테이블의 한 행과 같은 형태"

### 종료
- WHERE 조건으로 멈추거나 (숫자 생성: WHERE NUMBER < 10)
- 새 행이 안 나올 때 자동 종료 (트리 탐색)


응용2
```SQL


```
응용3
```SQL
WITH RECURSIVE
    CATEGORIES (CATEGORY_ID, CATEGORY_NAME, PARENT_ID) AS (
        SELECT 1,  '전체',         NULL UNION ALL
        SELECT 2,  '의류',         1    UNION ALL
        SELECT 3,  '전자제품',     1    UNION ALL
        SELECT 4,  '식품',         1    UNION ALL
        SELECT 5,  '남성의류',     2    UNION ALL
        SELECT 6,  '여성의류',     2    UNION ALL
        SELECT 7,  '노트북',       3    UNION ALL
        SELECT 8,  '스마트폰',     3    UNION ALL
        SELECT 9,  '셔츠',         5    UNION ALL
        SELECT 10, '바지',         5    UNION ALL
        SELECT 11, '원피스',       6    UNION ALL
        SELECT 12, '게이밍노트북', 7    UNION ALL
        SELECT 13, '사무용노트북', 7
    ),
PT3 AS(
    SELECT * , CATEGORY_NAME AS PATH
    FROM CATEGORIES
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    SELECT C.CATEGORY_ID, C.CATEGORY_NAME, C.PARENT_ID, CONCAT(P.PATH,'>',C.CATEGORY_NAME)
    FROM CATEGORIES AS C
    JOIN PT3 AS P
    ON P.CATEGORY_ID = C.PARENT_ID
)
    
    
SELECT * FROM PT3

```