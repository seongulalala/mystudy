# BeautifulSoup 기본 구문 정리

## 핵심 구문

| 목적           | 구문                         | 예시                                 |
| ------------ | -------------------------- | ---------------------------------- |
| 태그명으로 찾기     | `soup.select_one("태그명")`   | `soup.select_one("h1")`            |
| class로 찾기    | `soup.select_one(".클래스명")` | `soup.select_one(".price")`        |
| id로 찾기       | `soup.select_one("#아이디명")` | `soup.select_one("#main")`         |
| 텍스트 가져오기     | `태그.text`                  | `soup.select_one(".price").text`   |
| 링크 가져오기     | `태그["속성명"]`                | `soup.select_one(".link")["href"]` |
| 부모 안에서 자식 찾기 | `부모.select_one("자식선택자")`   | `product.select_one(".title")`     |

---

## 예시 HTML

```html
<div id="main">
  <h1 class="title">크롤링 연습</h1>
  <span class="price">15,000원</span>
  <a href="/product/100" class="link">상세보기</a>
</div>
```

---

## 예시 코드

```python
from bs4 import BeautifulSoup

html = """
<div id="main">
  <h1 class="title">크롤링 연습</h1>
  <span class="price">15,000원</span>
  <a href="/product/100" class="link">상세보기</a>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

title = soup.select_one("h1").text
price = soup.select_one(".price").text
link = soup.select_one(".link")["href"]

print(title)
print(price)
print(link)
```

---

## 실행 결과

```text
크롤링 연습
15,000원
/product/100
```

---

## 부모 요소를 먼저 잡는 방식

```python
product = soup.select_one("#main")

title = product.select_one(".title").text
price = product.select_one(".price").text
link = product.select_one(".link")["href"]

print(title)
print(price)
print(link)
```

| 코드                                    | 의미                            |
| ------------------------------------- | ----------------------------- |
| `product = soup.select_one("#main")`  | `id="main"`인 큰 부모 요소를 먼저 찾음   |
| `product.select_one(".title")`        | 부모 요소 안에서 제목 찾기               |
| `product.select_one(".price")`        | 부모 요소 안에서 가격 찾기               |
| `product.select_one(".link")["href"]` | 부모 요소 안에서 링크의 `href` 속성값 가져오기 |

---

## 한 줄 정리

`select_one()`으로 원하는 요소를 찾고, 화면에 보이는 글자는 `.text`, 태그 안의 속성값은 `["속성명"]`으로 가져온다.
