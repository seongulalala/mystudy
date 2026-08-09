# Git 상태 확인

## 핵심 명령어

```bash
git status
```

- 현재 브랜치와 파일 상태 확인
- Git 작업 전후 가장 먼저 확인

```bash
git status --short
```

- 변경 상태를 짧게 확인
- `M`: 수정된 파일
- `??`: 새로 생긴 Untracked 파일
- 출력이 없으면 변경사항 없음

```bash
git diff
```

- 아직 `git add`하지 않은 변경 내용 확인

```bash
git diff --staged
```

- `git add`한 뒤 커밋될 변경 내용 확인

```bash
git diff --staged --stat
```

- Staging된 파일과 변경량만 간단하게 확인

```bash
git log --oneline -5
```

- 최근 커밋 5개 확인

```bash
git rev-parse --show-toplevel
```

- 현재 Git 저장소의 최상위 폴더 확인

## 상태에 따른 다음 작업

```text
파일 수정
→ git status
→ git diff
→ git add
→ git diff --staged
→ git commit
→ git push
```

변경을 취소하려면:

```bash
git restore 파일명
```

Staging에서만 빼려면:

```bash
git restore --staged 파일명
```

## git status 문구 요약

```text
ahead by N commits
→ 로컬 commit N개가 아직 원격에 없음
→ git push

Changes to be committed
→ git add 완료
→ git commit

Changes not staged for commit
→ 기존 파일 수정 후 add 안 함
→ git add 또는 git restore

Untracked files
→ 새 파일을 Git이 아직 추적하지 않음
→ git add 여부 결정

nothing to commit, working tree clean
→ 로컬 변경사항 없음
```