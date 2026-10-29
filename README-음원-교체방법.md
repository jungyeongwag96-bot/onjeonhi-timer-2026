# 온전히 타이머 V4 실제 녹음 음원 적용

이 프로젝트는 기존 V4 디자인/인터벌/스톱워치/PWA 구조를 그대로 유지하고, **복싱벨·심판 휘슬·응원 나팔 3가지**만 실제 MP3를 재생하도록 고쳤습니다.

**주의: 이 ZIP에는 저작권 확인이 완료된 녹음 MP3 파일이 포함되어 있지 않습니다.** 먼저 아래 페이지에서 음원을 직접 들어보고 내려받아야 합니다. (임의 음원 배포나 잘못된 사용권 주장을 피하기 위함)

## 1. 음원 선택 및 다운로드

- 복싱벨: https://pixabay.com/sound-effects/boxing-bell-1-232450/
- 심판 휘슬: https://pixabay.com/sound-effects/film-special-effects-referee-whistle-coach-whistle-sports-whistle-291815/
- 응원 나팔: https://pixabay.com/sound-effects/film-special-effects-air-horn-sound-effect-372453/

각 사이트에서 다운로드 후 실제 소리를 들어보세요. 원본이 여러 번 울리거나 긴 파일이면 무료 오디오 편집기에서 원하는 **첫 울림 1회**만 잘라 내세요. 파일에 있는 소리를 한 번만 재생하도록 코드가 구성되어 있지만, 파일 안에 여러 소리가 들어 있으면 모두 들립니다.

Pixabay Content License는 일반적으로 상업적 프로젝트 내 사용을 허용하지만 원본 음원을 독립 상품처럼 재배포하는 것은 제한합니다. 사이트별 최신 이용약관과 출처를 검토하고 사용 근거를 보관하세요.

## 2. 이름 변경 후 폴더에 넣기

파일이름을 정확히 다음으로 지정합니다.

```
onjeonhi-timer/
  index.html
  service-worker.js
  manifest.webmanifest
  assets/...
  sounds/
    boxing-bell.mp3
    referee-whistle.mp3
    cheer-horn.mp3
```

## 3. GitHub 갱신

현재 GitHub 저장소 `onjeonhi-timer-2026`의 루트에 `index.html`, `service-worker.js`, `sounds` 폴더 안의 MP3 파일까지 업로드합니다. GitHub 웹 UI에서 폴더를 끌어다 놓거나 `sounds/boxing-bell.mp3` 경로로 업로드합니다. 변경 내용을 commit하면 Cloudflare Pages가 새 버전을 자동 배포합니다.

## 4. 갤럭시 PWA 테스트

Cloudflare 배포 완료 후 브라우저에서 사이트를 열고 **사운드 설정 → 복싱벨 → 소리 미리듣기**를 누르세요. 다른 2개도 확인하세요. 홈 화면 설치본에서 이전 버전이 나온다면 앱을 완전히 종료하고 온라인에서 다시 열어 캐시를 갱신하세요. 계속 오류가 나면 브라우저 사이트 데이터를 확인하세요 (로컬에 저장된 타이머/기록이 삭제될 수 있으니 주의).

### 주의사항

- 이 버전은 녹음 MP3가 없으면 합성음을 대신 재생하지 않습니다. 즉, 음원을 업로드하기 전 해당 3개 선택지는 무음입니다.
- 기존의 맑은 벨, 디지털 비프, 부드러운 차임과 카운트다운 비프는 합성 방식을 유지합니다.
- 모바일 브라우저는 화면 잠금이나 백그라운드에서 소리 재생을 제한할 수 있습니다.
- 공개 저장소에 업로드한 음원은 누구나 내려받을 수 있습니다. 사용 권한을 확인해야 합니다.
