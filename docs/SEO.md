# 버틀러 클리닉 — SEO 구성 제안 (2026-07-22)

> ## ⚑ 확정 로드맵 (2026-07-22 사용자 확정 — 사이트 마무리까지 유지)
> 1. **지금(프론트)**: 구조 SEO를 페이지 생성 규칙에 내장. **외관 무손상 원칙** — 보이는 디자인은 픽셀 단위로 유지 (태그/속성/보이지 않는 층만 변경).
> 2. **정적 오픈**: 최소 메타(title·description·OG) 하드코딩 + robots/sitemap 정적 버전 → **SEO 먼저 적용 후 노출**. 색인 자산을 쌓기 시작.
> 3. **정식 오픈(WP)**: 도메인·URL(IA 슬러그) 유지로 **정적 기간 SEO 점수를 그대로 승계**. 메타는 Yoast SEO 필드로 이관, sitemap·다국어·소유확인 전부 플러그인/옵션 관리. ⚠ 이관 중 "검색엔진 차단" 켰다면 오픈 때 해제 — 체크리스트 1번.
> 4. 히어로 영상(18.7MB) 최적화는 별도 진행 예정 (현 단계 생략 — 사용자 결정).
>
> **파일 버전 규칙**: `{페이지}-open.html` = 정적 오픈용(스위처·숨김 변형 없음, 크롤 대상) / `{페이지}-full.html` = 정식 작업본(스위처 유지) / 배포 시 open 버전을 IA 슬러그 폴더에 `index.html`로 복사.

> 에이전트 2기가 index.html(메인)·sub.html(서브 와이어프레임)을 분석한 결과 기반.
> 백엔드는 추후 워드프레스로 이관 예정 → §3에 WP 옵션/플러그인에서 지정할 값 별도 정리.

---

## 0. 현재 진단 요약

### index.html (메인)
| 항목 | 상태 |
|---|---|
| title / meta description | 있음 (title 32자로 짧음 — 지역·시술 키워드 여지) |
| OG / Twitter Card / canonical / robots meta | **전부 없음** |
| 구조화 데이터(JSON-LD) | **없음** (주소·전화 원자료는 푸터에 있으나 마크업 안 됨) |
| 헤딩 | h1 영문뿐("Butler plastic surgery…"), 유일한 h2가 숨김 변형 안 → 기본 뷰 h1→h3 건너뜀 |
| 이미지 | 18개 중 lazy loading 0, width/height 13개 누락(CLS), 전부 JPG, 낱장 250KB~1.5MB |
| **hero_01.mp4 = 18.7MB** | autoplay라 기본 숨김이어도 프리페치 위험 — 최대 성능 리스크 |
| 내부 링크 | 12개 전부 `#consult` 단일 앵커 수렴, 타 페이지 링크 0 |
| 시맨틱 | header/nav/main 없음. b06 링크가 font-size:0 + aria-hidden 조합(클로킹성) |
| 개발 잔재 | A/B/C 시안 스위처(tx-switch) 잔존, 섹션2 변형 중복 텍스트 |

### sub.html (서브 — 9개 시술 페이지의 템플릿)
| 항목 | 상태 |
|---|---|
| title | "레이저리프팅 — 레이아웃 시안 (HANEUL Design System)" — **시안 문구 그대로** |
| meta description / OG / canonical / robots | **전부 없음** |
| 구조화 데이터 | 없음 — FAQ 5문답 있는데 FAQPage 스키마 없음 |
| 중복 콘텐츠 | **h2의 64%, 전체 텍스트의 60~70%가 숨김 변형 중복** (E 5벌·F 3벌·lay1/lay2 이중) |
| 중복 id | `id="secG"` 4회 — HTML 위반 + 기본(lay2)에서 대상이 display:none이라 "전후사진 보기" 무효 |
| 브랜드 잔재 | 로고 alt "SNOW CLINIC YEO-SU", nav "여수 스노우", 푸터 "여수스노우 구조 카피" |
| 성능 | 인라인 CSS 93KB, lazy loading·srcset·WebP 없음 |
| 의료광고 | 전후사진 고지문 있음(양호) / 심의필 번호·실제 사업자 정보 없음(푸터 플레이스홀더) |

---

## 1. 오픈 전 필수 (정적 단계에서 지금 추가)

### 1-1. 페이지별 메타 세트 (전 페이지 공통 템플릿)
```html
<title>{페이지명} | 버틀러클리닉 성형외과</title>  <!-- 서브: 레이저 리프팅 | 버틀러클리닉 -->
<meta name="description" content="{페이지별 요약 70~110자, 시술·지역 키워드 포함}">
<meta name="robots" content="index,follow">
<link rel="canonical" href="https://도메인{IA.md 슬러그}">
<meta property="og:type" content="website">
<meta property="og:title" content="…">
<meta property="og:description" content="…">
<meta property="og:image" content="https://도메인/img/og-default.jpg">  <!-- 1200×630 제작 필요 -->
<meta property="og:url" content="…">
<meta name="twitter:card" content="summary_large_image">
```
- 카카오톡/문자 공유가 많은 한국 특성상 **og:image가 실질 체감 1순위**.

### 1-2. 구조화 데이터 (JSON-LD)
- **전 페이지 공통**: `MedicalClinic` (name, address, telephone, openingHours, geo, sameAs) — 푸터 실제 정보 확정 후.
- **서브(시술) 페이지**: `MedicalWebPage` + `MedicalProcedure`(시술별) + `FAQPage`(기존 5문답 그대로) + `BreadcrumbList`(IA 2단 구조).
- **메인**: `Organization` + `WebSite`.

### 1-3. 오픈용 빌드 정리 (스위처·중복 제거)
작업용 파일과 배포용 파일을 분리한다. **작업 파일은 그대로 두고**, 오픈 직전:
1. 확정 변형(active)만 남기고 비활성 `.variant`·`lay1-only`(또는 lay2-only) 블록 삭제 → 중복 콘텐츠 60~70% 해소
2. `.sec-chip`·`.lay-chip`·`tx-switch` 등 개발 스위처 UI/JS 제거
3. `id="secG"` 중복 해소 (활성 변형에만 부여)
4. 여수스노우 잔재 전면 교체 (로고 alt, nav 문구, 푸터)
5. title/description을 실제 페이지명으로

### 1-4. 헤딩·시맨틱 정리
- 메인 h1에 한국어 핵심 키워드 포함 (예: `버틀러 성형외과 — 에이지 매니지먼트 클리닉`; 영문 워드마크는 시각 요소로 유지하고 sr 텍스트 분리 가능)
- 기본 뷰에서 h1→h2→h3 위계 성립하도록 (숨김 변형 의존 금지). "Featured Operation" 등 p로 마크업된 시각적 헤딩 → h2 전환
- `<main>` 랜드마크 추가, 메인에 `<nav>` (IA 슬러그 기반 실제 링크)
- b06 `font-size:0` + `aria-hidden` 조합 → sr-only 패턴으로 교체 (클로킹 오해 방지)

### 1-5. 내부 링크 아키텍처
- 헤더 nav의 `href="#"` 더미들을 IA.md 슬러그로 연결 (`/skincare/laser-lifting` 등)
- 메인 featured 카드 6개 → 해당 시술 서브페이지로 (현재 전부 #consult)
- 서브 → 메인/형제 시술 페이지 상호 링크 (히어로 탭 활용)

### 1-6. 성능 (Core Web Vitals)
- **hero_01.mp4 18.7MB → 3~5MB 이하 재인코딩** (H.264 CRF 28 내외, 해상도 1920 상한) + `poster` 지정 + `preload="none"`(비활성 변형)
- 이미지 일괄 WebP 변환 + 원본 JPG 폴백 (`<picture>`), 낱장 200KB 이하 목표
- 첫 화면 밖 `<img>` 전부 `loading="lazy"` + `width`/`height` 명시 (CLS 방지)
- Pretendard CDN에 preconnect 추가, Noto Sans weight 5종 → 실사용 3종(300/400/700)으로 축소

### 1-7. 사이트 기반 파일
- `robots.txt` (오픈 전까지 Disallow, 오픈 시 해제 + Sitemap 경로)
- `sitemap.xml` (IA.md 24페이지 기준 — WP 이관 후엔 플러그인 자동화로 대체)
- 파비콘 세트: favicon.ico + apple-touch-icon(180×180) + theme-color

### 1-8. 의료광고 준수 (한국 필수)
- 의료광고 사전심의필 번호 표기 (전후사진·이벤트 노출 페이지)
- 푸터 실제 정보: 의료기관명·대표자·사업자등록번호·주소·연락처 (현재 000 플레이스홀더)
- 전후사진 고지문 유지 (이미 있음 — 양호)
- 비급여 진료비용 고지 페이지(`/pricing`) — 의료법상 고지 의무

---

## 2. 오픈 시점에 할 일 (검색엔진 등록)
| 채널 | 작업 |
|---|---|
| **네이버 서치어드바이저** | 사이트 등록 + 소유확인 meta + sitemap 제출 — **한국 의원은 네이버가 1순위** |
| Google Search Console | 소유확인 + sitemap 제출 |
| 네이버 스마트플레이스 / Google 비즈니스 프로필 | 지역(로컬) 검색 — 진료시간·사진·리뷰 관리 |
| Bing 웹마스터 | 선택 |

---

## 3. 워드프레스 이관 시 지정할 값 (화면에 안 보이지만 반드시 설정)

### 3-1. WP 코어 설정
| 위치 | 값 | 비고 |
|---|---|---|
| 설정 > 일반 | 사이트 제목 = `버틀러클리닉 성형외과`, 태그라인 = 브랜드 카피 | title 템플릿 변수로 쓰임 |
| 설정 > 일반 | WordPress/사이트 주소 = `https://` + www 유무 통일 | canonical의 뿌리 |
| 설정 > 고유주소 | **"글 이름"** + 페이지는 부모/자식 계층으로 IA 슬러그 재현 | `/about/brand-story` = about 페이지의 자식 |
| **설정 > 읽기** | **"검색엔진이 이 사이트를 검색하는 것을 차단" — 개발 중 ON, 오픈 때 OFF** | 잊으면 색인 전체 차단되는 최다 사고 지점 |
| 설정 > 토론 | 댓글·핑백 OFF | 의원 사이트에 불필요, 스팸 방지 |
| 설정 > 개인정보 | 개인정보처리방침 페이지 지정 (`/privacy`) | |

### 3-2. SEO 플러그인 (Yoast SEO 또는 RankMath 중 1개)
- 페이지별 meta title/description/OG/canonical → §1-1에서 정한 값을 그대로 입력 (프론트에 하드코딩했던 것을 플러그인 필드로 이관)
- title 템플릿: `%page% | %sitename%`
- sitemap.xml 자동 생성 (정적 sitemap 대체)
- Breadcrumb 출력 + BreadcrumbList 스키마
- 아카이브류 noindex: 작성자 아카이브, 날짜 아카이브, 태그 (저품질 색인 방지)
- 소유확인 코드 입력란: 네이버·구글 verification meta 여기서 관리

### 3-3. 스키마/콘텐츠 구조
- MedicalClinic JSON-LD: 테마 header.php 또는 스키마 플러그인으로 전역 출력
- Doctor's Column → **글(post) + 카테고리 2개**(성형 클리닉 / 클리닉 칼럼)로 설계, 나머지는 전부 고정 페이지
- FAQ 블록: RankMath/Yoast FAQ 블록 사용 시 FAQPage 스키마 자동화

### 3-4. 미디어·성능
- 업로드 규칙: 파일명 키워드화(`laser-lifting-ulthera.jpg`), alt 필수 입력 (미디어 라이브러리에서 관리)
- 이미지 최적화 플러그인 (WebP 자동 변환): Imagify / EWWW 등
- 캐시 플러그인 (WP Rocket / LiteSpeed Cache) — WP 5.5+는 loading="lazy" 자동
- `큰 이미지 임계값`(기본 2560px) 유지 — 원본 대형 업로드 자동 리사이즈

### 3-5. 다국어 (IA의 GLOBAL — KR/EN/CH/JP)
- Polylang 또는 WPML: 언어 프리픽스 `/en` `/zh` `/ja`, **hreflang 자동 출력**
- 기본 언어 ko는 프리픽스 없음 (IA.md 규칙과 일치)
- 번역 전 단계에서는 언어 메뉴 비노출 권장 (빈 번역 페이지 색인 방지)

### 3-6. 보안/기타
- XML-RPC 비활성, wp-admin 접근 제한 (SEO 직접 항목은 아니나 해킹 시 스팸 색인 리스크)
- 리다이렉트 관리: 정적 → WP 이관 시 URL이 IA 슬러그와 동일하면 리다이렉트 불필요 (지금 IA 슬러그로 통일해두는 것의 이점)

---

## 4. 우선순위

1. **[즉시]** 메타 세트 템플릿 + og:image 제작 + 파비콘 세트 — 전 페이지 공통 뼈대
2. **[즉시]** hero_01.mp4 압축, 이미지 lazy/width/height — 성능 최대 리스크
3. **[페이지 제작하며]** JSON-LD(FAQPage·MedicalProcedure·BreadcrumbList), 헤딩 위계, 내부 링크
4. **[오픈 직전]** 스위처·중복 변형 제거 빌드, 여수스노우 잔재 교체, 푸터 실제 정보, robots/sitemap, 심의필 번호
5. **[오픈 시]** 네이버 서치어드바이저·GSC 등록, 스마트플레이스/비즈니스 프로필
6. **[WP 이관 시]** §3 전체 — 특히 읽기 설정 차단 해제, 고유주소 IA 일치, SEO 플러그인 필드 이관
