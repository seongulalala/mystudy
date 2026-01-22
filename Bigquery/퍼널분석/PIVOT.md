# 축을 중심으로 회전하는 PIVIOT

## PIVIOT방법
MAX,IF,GROUP BY를 사용

```
SELECT
 student,
 MAX(IF(subject='수학',score,NULL)) as 수학
 MAX(IF(subject='영어',score,NULL)) as 영어
 MAX(IF(subject='과학',score,NULL)) as 과학
FROM 테이블
GROUP BY student
```

