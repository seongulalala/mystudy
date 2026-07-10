# BeautifulSoup + CSS 선택자 핵심 정리

## 1. `select()`와 `select_one()` 차이

| 코드 | 의미 | 결과 |
| --- | --- | --- |
| `select()` | 조건에 맞는 요소를 여러 개 가져옴 | 리스트 |
| `select_one()` | 조건에 맞는 요소 중 첫 번째 하나만 가져옴 | 태그 1개 |

```python
products = soup.select(".product")      # 상품 박스 여러 개
title = soup.select_one(".name")        # 첫 번째 상품명 하나
```

---

## 2. 큰 박스를 먼저 잡고 그 안에서 찾기

크롤링에서 가장 중요한 구조는 아래와 같다.

```python
products = soup.select(".product")

for product in products:
    name = product.select_one(".name").text
    price = product.select_one(".price").text
    link = product.select_one(".detail-link")["href"]

    print(name, price, link)
```

흐름은 다음과 같다.

```text
전체 HTML
→ 상품 박스 여러 개 선택
→ 상품 박스 하나씩 반복
→ 그 안에서 이름, 가격, 링크 선택
```

---

## 3. `soup.select()`와 `product.select_one()` 차이

| 코드 | 의미 |
| --- | --- |
| `soup.select(".name")` | 전체 HTML에서 `.name` 전부 찾기 |
| `product.select_one(".name")` | 현재 상품 박스 안에서 `.name` 하나 찾기 |

예를 들어 `.name`이 상품명에도 있고 공지사항에도 있으면:

```python
soup.select(".name")
```

이 코드는 공지사항까지 잡을 수 있다.

그래서 상품 정보만 뽑을 때는 보통 아래처럼 상품 박스 기준으로 접근한다.

```python
products = soup.select(".product")

for product in products:
    name = product.select_one(".name").text
```

---

## 4. 자주 쓰는 CSS 선택자

| 선택자 | 의미 |
| --- | --- |
| `.product` | class가 product인 요소 |
| `.name` | class가 name인 요소 |
| `#shop` | id가 shop인 요소 |
| `#shop .name` | shop 안에 있는 name 요소 |
| `.product.best` | product와 best 클래스를 둘 다 가진 요소 |
| `.product.soldout` | product와 soldout 클래스를 둘 다 가진 요소 |
| `a.detail-link` | a 태그이면서 class가 detail-link인 요소 |
| `img.thumb` | img 태그이면서 class가 thumb인 요소 |

---

## 5. class가 여러 개인 경우

```html
<div class="product best">
```

이건 class가 2개인 것이다.

```text
product
best
```

그래서 아래 선택자에 모두 잡힌다.

```python
soup.select(".product")
soup.select(".best")
soup.select(".product.best")
```

주의할 점은 아래 차이다.

| 선택자 | 의미 |
| --- | --- |
| `.product.best` | 같은 태그에 product와 best가 둘 다 있음 |
| `.product .best` | product 안에 있는 best 자식 요소 |

---

## 6. `.text`와 `["속성명"]`

| 가져오려는 것 | 코드 |
| --- | --- |
| 화면에 보이는 글자 | `.text` |
| 링크 주소 | `["href"]` |
| 이미지 주소 | `["src"]` |

```python
name = product.select_one(".name").text
link = product.select_one(".detail-link")["href"]
img = product.select_one(".thumb")["src"]
```

---
## 7. 크롤링 기본 패턴

아래 구조를 가장 먼저 익히면 된다.

```python
items = soup.select("반복되는 큰 박스")

for item in items:
    title = item.select_one("제목 선택자").text
    price = item.select_one("가격 선택자").text
    link = item.select_one("링크 선택자")["href"]

    print(title, price, link)
```

이번 실습 기준으로는 아래 코드가 핵심이다.

```python
products = soup.select(".product")

for product in products:
    name = product.select_one(".name").text
    brand = product.select_one(".brand").text
    price = product.select_one(".price").text
    link = product.select_one(".detail-link")["href"]
    img = product.select_one(".thumb")["src"]

    print(name, "/", brand, "/", price, "/", link, "/", img)
```

---

## 8. 한 줄 요약

```text
큰 박스 여러 개를 select()로 잡고,
for문으로 하나씩 꺼낸 뒤,
각 박스 안에서 select_one()으로 필요한 값만 뽑는다.
```