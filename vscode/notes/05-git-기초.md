# Git 기초

## Git 작업 흐름

```text
파일 수정
→ git status
→ git diff
→ git add
→ git diff --staged
→ git commit
→ git push
```

- Working Directory: 현재 수정 중인 파일
- Staging Area: 다음 커밋에 포함할 변경사항
- Commit: 변경사항을 하나의 버전으로 저장

## 상태 확인

```bash
git status
```

- 변경된 파일과 Staging 상태 확인

```bash
git status --short
```

- 상태를 짧게 확인
- `M`: 수정된 파일
- `??`: 아직 Git이 추적하지 않는 파일
- 출력이 없으면 변경사항 없음

```bash
git rev-parse --show-toplevel
```

- 현재 Git 저장소의 최상위 폴더 확인

## 변경 내용 확인

```bash
git diff
```

- 아직 `git add`하지 않은 변경 내용 확인
- 새로 생성된 Untracked 파일은 기본적으로 표시되지 않음

```bash
git diff --staged
```

- Staging Area에 올라간 변경 내용 확인

```bash
git diff --staged --stat
```

- Staging된 파일과 변경량만 간단하게 확인

Diff 표시:
- `-`: 이전 버전에서 제거된 줄
- `+`: 새 버전에 추가된 줄
- 공백: 변경되지 않은 줄
- `q`: diff 화면 종료

## Staging

```bash
git add .
```

- 현재 폴더와 하위 폴더의 변경사항을 Staging Area에 추가
- 실행 위치에 따라 포함되는 파일 범위가 달라짐

```bash
git restore --staged 파일명
```

- 파일을 Staging Area에서만 제거
- 실제 수정 내용은 유지

## Commit과 Push

```bash
git commit -m "커밋 메시지"
```

- Staging된 변경사항을 하나의 버전으로 저장
- 커밋 메시지는 변경 내용을 알 수 있게 작성

```bash
git push origin master
```

- 로컬에서 커밋한 기록을 원격 저장소에 업로드
- Staging만 된 파일은 push되지 않음

## 변경 취소

```bash
git restore 파일명
```

- 아직 commit하지 않은 파일의 수정 내용을 마지막 커밋 상태로 되돌림

```text
git restore 파일
→ 실제 수정 내용 취소

git restore --staged 파일
→ Staging에서만 제거
→ 수정 내용은 유지
```

## .gitignore

- Git에서 추적하지 않을 파일이나 폴더 지정
- 데이터 파일, 환경설정 파일 등을 커밋에서 제외할 때 사용

```gitignore
*.csv
```

- 하위 폴더를 포함한 CSV 파일 제외

## 경로 주의

명령어의 파일 경로는 현재 터미널 위치를 기준으로 작성함.

```text
현재 위치: mystudy/vscode

bike-demand/src/hello.py         → 정상
vscode/bike-demand/src/hello.py  → vscode가 중복됨
```