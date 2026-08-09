# Git 기초

## 핵심 흐름

```text
파일 수정
→ git status
→ git diff
→ git add
→ git commit
→ git push
```

- Working Directory: 현재 수정 중인 파일
- Staging Area: 다음 커밋에 포함할 변경사항
- Commit: 변경사항을 하나의 버전으로 저장

## 핵심 명령어

```bash
git status
```
- 현재 Git 상태 확인

```bash
git diff
```
- `git add` 전 변경 내용 확인

```bash
git add .
```
- 현재 폴더와 하위 폴더의 변경사항을 Staging

```bash
git diff --staged
```
- 커밋될 변경 내용 확인

```bash
git commit -m "커밋 메시지"
```
- Staging된 변경사항을 버전으로 저장

```bash
git push origin master
```
- 커밋을 원격 저장소에 업로드

## 변경 취소

```bash
git restore 파일명
```
- 실제 파일의 수정 내용 취소

```bash
git restore --staged 파일명
```
- Staging에서만 제거
- 실제 수정 내용은 유지

## .gitignore

- Git에서 추적하지 않을 파일이나 폴더 지정

```gitignore
*.csv
```

- CSV 파일을 Git에서 제외

## 경로 주의

- 파일 경로는 현재 터미널 위치를 기준으로 작성
- `git add .`도 현재 폴더와 하위 폴더만 대상으로 함