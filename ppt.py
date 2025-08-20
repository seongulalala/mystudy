import matplotlib.pyplot as plt
from matplotlib import rcParams

# 한글 폰트 설정
rcParams['font.family'] = 'Malgun Gothic'  # 또는 'NanumGothic'
rcParams['axes.unicode_minus'] = False

slides = {
    "나의 능력 & 경험": """📌 자격증
- 빅데이터분석기사
- ADsP
- SQLD
- 컴활 1급

📌 전공
- 상명대 경영학부
- 빅데이터애널리틱스 복수 전공

📌 강점
- 데이터 분석 역량
- AI & 머신러닝 지식
- 마케팅 관점에서 문제를 보는 시각

📌 단점
- 리더 역할을 좋아하지 않음
- (대신 보조·서포트 역할에 강점, 분석·아이디어 보강에 자신 있음)""",

    "프로젝트 목표": """- 포트폴리오에 활용 가능한 수준의 프로젝트 완성
- 수업에서 배운 내용을 활용
- 필요하다면 개인 능력에 따른 알파 추가""",

    "팀원에게 바라는 점": """- 회의 시 서로의 의견 존중
- 배우지 않은 내용도 추가할 수는 있지만,
  배운 내용을 메인으로 프로젝트를 진행하고 싶음"""
}

for i, (title, content) in enumerate(slides.items(), start=1):
    plt.figure(figsize=(10, 6))
    plt.axis("off")
    plt.text(0.5, 0.92, title, ha="center", va="top", fontsize=22, weight="bold")
    plt.text(0.05, 0.8, content, ha="left", va="top", fontsize=16, wrap=True)
    plt.savefig(f"slide_{i}_kor.png", bbox_inches="tight")
    plt.close()
