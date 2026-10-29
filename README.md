# 온전히 타이머 — 원본 화면 기반 복원 V3

HTML/CSS/JavaScript 정적 PWA. ChatGPT Sites와 별도이며 Cloudflare Pages에서 실행됩니다.

## 설치·배포 (GitHub 초보자용)
1. ZIP 압축을 풉니다. 폴더 안의 `index.html`, `styles.css`, `app.js`, `service-worker.js`, `manifest.webmanifest`, `assets/`를 확인합니다.
2. GitHub `onjeonhi-timer-2026` 저장소 → Code → Add file → Upload files에서 **폴더 안의 파일/폴더를** 업로드합니다. `index.html`이 저장소 최상단에 있어야 합니다.
3. 기존 파일과 같은 이름이면 덮어쓰고, 아래쪽 `Commit changes`를 누릅니다. 파일을 각각 GitHub에서 열어 연필 아이콘으로 수정해도 됩니다.
4. Cloudflare Pages가 GitHub `main`에 연결됐다면 자동 재배포됩니다. `https://onjeonhi-timer-2026.pages.dev/`에서 확인합니다. 반영이 늦으면 Cloudflare Deployments 탭에서 상태를 확인하거나 브라우저 새로고침을 합니다.
5. 아직 GitHub와 연결되지 않았다면 Cloudflare → Workers & Pages → Create → Pages → Git 저장소 연결에서 저장소를 선택합니다. 정적 사이트이므로 프레임워크 없음, 출력 경로 `.`를 사용합니다.

## PC에서 확인하기
`index.html`을 직접 열면 일반 UI는 보이지만 PWA 캐시는 작동하지 않을 수 있습니다. Python 설치되어 있다면 **테스트할 때만** 프로젝트 폴더에서 `python -m http.server 8000` 입력 후 `http://localhost:8000`을 엽니다. Python 없이도 Cloudflare에 업로드하면 됩니다.

## 현재 구현
- 원본 사진에 맞춘 노란 인터벌·보라 스톱워치 화면, 전체화면, 반응형 가로 모드
- 템플릿 생성·편집·선택·삭제 / 라운드·사이클·준비·휴식 설정
- 인터벌 단계 변경, 시작·일시정지, 건너뛰기, 소리와 음성 안내 설정
- 스톱워치 실행·중지 시 기록 자동 저장, 최근 100회/최고 기록/최근 5회 평균
- localStorage(저장 기록은 브라우저·기기별로 분리), PWA 오프라인 캐시

## 중요한 차이 및 테스트 사항
- 실제 복싱벨·휘슬 음원은 제공되지 않았으므로 **합성 사운드**입니다. 외부 음원을 무단 배포하지 않습니다.
- 백그라운드에서 브라우저가 오디오와 음성합성을 제한할 수 있습니다. 타이밍은 `performance.now()` 기준으로 보정하지만 알림이 항상 정확히 들리는 것은 아닙니다.
- 전체화면은 모바일 브라우저별 지원 여부가 다릅니다.
- 설치용 아이콘은 SVG입니다. 일부 플랫폼에서 PWA 설치 지원을 높이려면 192/512px PNG 아이콘을 추가하세요.
- 광고·결제 기능과 계정 동기화는 들어 있지 않습니다.

## 소리 테스트
첫 시작 버튼을 누른 뒤 기기 음량을 올리고, 사운드 설정 → 소리 미리듣기를 누릅니다. 진동은 지원 기기만 작동합니다.
