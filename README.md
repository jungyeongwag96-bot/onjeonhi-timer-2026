# 온전히 · 타이머 (독립형 PWA)

ChatGPT Sites와 독립적으로 작동하는 HTML/CSS/JavaScript 정적 웹앱입니다. Python은 로컬 서버·검증에만 필요하고 실제 방문자에게 Python 서버는 필요하지 않습니다.

## 기능
- 인터벌: 준비·운동·휴식, 라운드 수, 라운드 이름, 시작/종료 알림음
- 브라우저 오디오 생성 사운드(벨/휘슬/나팔/기본음), 음량, 한국어 라운드 번호 음성(브라우저 지원 시)
- 일시정지/계속/초기화, 진행 상황, 가로 화면 반응형
- 템플릿 최대 30개, 로컬 브라우저 저장
- 스톱워치, 랩 기록, CSV 다운로드
- PWA 설치 지원(브라우저별 차이), 서비스 워커 오프라인 캐시

## Windows에서 실행
1. 이 ZIP 파일의 압축을 풀어 `onjeonhi-timer` 폴더를 만듭니다.
2. 해당 폴더 빈 공간에서 Shift+마우스 우클릭 → 터미널/PowerShell 열기.
3. `python --version`을 실행합니다. 설치되어 있지 않다면 https://www.python.org/downloads/ 에서 설치하세요.
4. `python -m http.server 8000` 실행 (`python`이 안 되면 `py -m http.server 8000`).
5. Chrome/Edge에서 `http://localhost:8000` 열기.
6. 종료할 때 터미널에서 Ctrl+C.
7. 추가 점검: `python tools/test_local.py`

## Cloudflare Pages 무료 배포 (GitHub 없이 시작)
1. https://dash.cloudflare.com/ 에 가입/로그인.
2. Workers & Pages → Create application → Pages → Drag and drop 방식의 Direct Upload 선택 (화면 문구는 바뀔 수 있음).
3. 압축 해제한 `onjeonhi-timer` **폴더 자체** 또는 배포용 ZIP을 끌어 놓습니다. 업로드 결과의 최상위에 `index.html`이 있어야 합니다.
4. 프로젝트 이름 입력(예: `onjeonhi-timer-2026`) → Deploy site.
5. 발급된 `https://[프로젝트명].pages.dev` 주소로 접속한 뒤 모바일/PC 테스트.
6. 수정했으면 다시 파일 업로드로 재배포합니다.

공식 가이드: https://developers.cloudflare.com/pages/get-started/direct-upload/

**중요:** Direct Upload로 생성한 프로젝트는 나중에 같은 프로젝트를 Git 자동 배포 방식으로 전환할 수 없습니다. 자동 배포가 필요하면 처음부터 Git integration 방식으로 새 프로젝트를 만드세요.

## GitHub 자동 배포 (대안)
1. GitHub에 새 저장소를 만들고 이 폴더 안의 파일을 최상위에 업로드.
2. Cloudflare Pages → Connect to Git → 저장소 선택.
3. Framework preset: None, Build command: `exit 0`, Build output directory: `.`.
4. 배포 후 GitHub 파일 수정/푸시 시 자동 재배포.

가이드: https://developers.cloudflare.com/pages/get-started/git-integration/

## 알려진 제약과 수익화 전 체크
- 원본 ChatGPT Sites의 소스에 접근할 수 없으므로 **대화에 나온 요구사항을 기반으로 재구현한 버전**입니다. 원본과 픽셀 단위 동일함을 보장하지 않습니다.
- 사운드는 외부 음원 복제본이 아닌 Web Audio API 생성음입니다. 이전에 지정했던 특정 복싱벨/휘슬 파일을 그대로 넣으려면 그 음원의 **상업적 이용·재배포 권한**을 확인해야 합니다.
- 브라우저의 음성 합성은 기기별 지원과 발음/볼륨이 다르며, 무음·절전·백그라운드에서는 알림/타이머 갱신이 지연될 수 있습니다.
- 설정 및 템플릿은 localStorage에만 남습니다. 브라우저 데이터 삭제, 다른 기기와의 동기화는 지원하지 않습니다.
- PRO 결제·로그인·광고·통계는 아직 구현되지 않았습니다. 결제 검증·이용권 권한은 반드시 신뢰할 수 있는 서버에서 구현해야 합니다.
- 광고·결제 도입 전 개인정보 처리방침, 동의 관리, 사이트 약관, 사업·세무·겸업 문제를 검토하세요.
- 광고가 실시간 타이머 화면을 가리지 않도록 운동 종료·설정 화면 위주로 설계하세요.

## 프로젝트 구성
```
onjeonhi-timer/
  index.html           # 화면
  styles.css           # 보라/노랑 반응형 디자인
  app.js               # 인터벌·스톱워치·설정·사운드
  manifest.webmanifest # PWA 설정
  service-worker.js    # 오프라인 캐시
  assets/icon.svg      # 아이콘
  tools/test_local.py  # Python 점검
  README.md            # 본 문서
```
