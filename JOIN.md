## JOIN의 기본

INNER JOIN : A,B 둘 다 매칭되는 데이터

OUTER JOIN : 
    
    LEFT JOIN : 왼쪽은 무조건 유지 오른쪽에서 못 찾은 것은 NULL / 

    RIGHT HOIN 

    CROSS JOIN : 모든 조합 EX) A =5개 컬럼, B = 10개 컬럼 > 50개 컬럼

    FULL OUTER JOIN : MYSQL에는 없음  

## 팁

### WHERE VS ON
**(1) : A는 전부 남고 B는 조건에 맞는 것만 붙는다 > 없으면 NULL**
```SQL
-- (1) 조건을 ON에 넣는 경우
SELECT ...
FROM A
LEFT JOIN B
    ON A.id = B.a_id
   AND B.status = 'Y';
```

**(2) : 결과적으로 INNER JOIN처럼 되어버림**
```SQL
-- (2) 조건을 WHERE에 넣는 경우
SELECT ...
FROM A
LEFT JOIN B
    ON A.id = B.a_id
WHERE B.status = 'Y';
```

### COUNT(*) VS COUNT(컬럼)
```SQL
COUNT(*)      -- NULL이어도 카운트
COUNT(b.id)   -- NULL이 아닌 경우만 카운트
```

