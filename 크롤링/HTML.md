# HTML표준

# HTML 구조 정리


## 1. HTML 문서의 기본 구조 (트리 구조)

HTML은 **부모-자식(Parent-Child)** 관계로 이루어진 트리 구조다.

```html
<html>                  ← 최상위 Parent (start tag)
  <body>                ← html의 child
    <a href="http://naver.com">네이버</a>   ← body의 child
    <table>                                 ← body의 child → 동시에 tr의 parent
      <tr>                                  ← table의 child → 동시에 td의 parent
        <td> ... </td>
      </tr>
      <tr> ... </tr>
    </table>
  </body>
</html>                 ← end tag
```

> 하나의 요소가 **parent이면서 동시에 child**일 수 있다.
> 예: `<table>`은 `<body>`의 child이면서 `<tr>`의 parent

---

## 2. 태그의 구성 요소

### 시작 태그(Start Tag) & 종료 태그(End Tag)
### 속성(Attribute)

시작 태그 안에 `속성 = "값"` 형태로 작성한다.

```html
<a href="http://naver.com">
    ^^^^   ^^^^^^^^^^^^^^^^^^
    속성명       속성값
```

---

## 3. 요소(Element)의 종류

### 일반 요소 (쌍 태그로 구성)

시작 태그 + 내용 + 종료 태그로 구성된다.

```html
<p>텍스트 내용</p>
<a href="...">링크 텍스트</a>
```

### 단독 요소 (Self-Closing Tag)


종료 태그 없이 단독으로 사용된다.

```html
<hr />    ← 수평선
<br />    ← 줄바꿈
<img />   ← 이미지
```

---

## 4. Child 요소의 두 가지 유형

태그 안에 들어갈 수 있는 자식(child)은 크게 **두 종류**다.

| 유형 | 설명 | 예시 |
|------|------|------|
| **텍스트(Text)** | 문자열(String) 그 자체 | `네이버`, `안녕하세요` |
| **요소(태그)** | 또 다른 HTML 태그 | `<tr>`, `<td>`, `<a>` 등 |

```html
<!-- text가 child인 경우 -->
<a href="http://naver.com">네이버</a>
                            ^^^^^^ → 텍스트(String)

<!-- 요소(태그)가 child인 경우 -->
<table>
  <tr> ... </tr>   → 요소(태그)가 child
</table>
```

---

## 5. 핵심 요약
  1. HTML 문서는 여러 요소(Element)로 구성되어 있다

  2. 각 요소는 시작 태그(start tag)로 시작하고 종료 태그(end tag)로 끝난다

  3. 시작 태그에는 속성(Attribute)이 붙을 수 있다

  4. 시작 태그와 종료 태그 사이에는 텍스트 또는 다른 요소(child)가 들어갈 수 있다

  5. 하나의 요소가 child이면서 동시에 다른 요소의 parent가 될 수 있다
    → ex) <table>은 <body>의 child이면서 <tr>의 parent


## 6. 핵심 요약2
1. HTML은 시작태그, 속성, 내용 , 종료태그로 구성된다
2. 시작 태그에는 속성이 있을 수도 있고 없을 수도 있다
3. 내용에는 텍스트나 다른 요소(child)가 있을 수도 있고 없을 수도 있다
