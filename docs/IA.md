# 버틀러 클리닉 — 사이트 IA (Information Architecture)

> 2026-07-22 확정. 페이지 생성 시 이 문서의 슬러그·영문 페이지명을 기준으로 한다.
> 로컬 정적 작업 시 슬러그 경로 그대로 폴더를 만들고 `index.html`을 둔다.
> (예: `/skincare/laser-lifting` → `skincare/laser-lifting/index.html`)

## 구조 요약

```
HOME (/)
├─ BUTLER CLINIC (/about)
├─ Surgery (/surgery)
├─ Skin Care (/skincare)
├─ Doctor's Column (/column)
├─ Before / After (/before-after)
└─ Promotion (/promotion)
푸터: GLOBAL(언어) · 비급여 · 개인정보 취급방침
```

## 전체 페이지 리스트

| 대메뉴 | 소메뉴(국문) | 영문 페이지명 | 슬러그 | 콘텐츠 원본 |
|---|---|---|---|---|
| HOME | — | Home | `/` | — |
| BUTLER CLINIC | (대메뉴) | Butler Clinic | `/about` | — |
| BUTLER CLINIC | 브랜딩 스토리 | Brand Story | `/about/brand-story` | `../소개페이지/01_브랜딩스토리.txt` |
| BUTLER CLINIC | 의료진 소개 | Medical Team | `/about/doctors` | `../소개페이지/02_의료진 소개.txt` |
| BUTLER CLINIC | 보유장비 / 의약품 | Equipment & Medications | `/about/equipment` | `../소개페이지/03_보유장비 : 의약품 .txt` |
| BUTLER CLINIC | 둘러보기 | Clinic Tour | `/about/tour` | `../소개페이지/04_둘러보기.txt` |
| BUTLER CLINIC | 오시는 길 | Location | `/about/location` | `../소개페이지/05_오시는 길.txt` |
| Surgery | (대메뉴) | Surgery | `/surgery` | — |
| Surgery | 눈 수술 | Eye Surgery | `/surgery/eye` | 기획안 0301 |
| Surgery | 안면부 수술 | Facial Surgery | `/surgery/face` | 기획안 0302 |
| Surgery | 이마 수술 | Forehead Surgery | `/surgery/forehead` | 기획안 0303 |
| Skin Care | (대메뉴) | Skin Care | `/skincare` | — |
| Skin Care | 실 리프팅 | Thread Lifting | `/skincare/thread-lifting` | 기획안 0401 |
| Skin Care | 레이저 리프팅 | Laser Lifting | `/skincare/laser-lifting` | 기획안 0402 ← **현재 와이어프레임(sub-open/sub-full.html)** |
| Skin Care | 보톡스 / 필러 | Botox & Filler | `/skincare/botox-filler` | 기획안 0403 |
| Skin Care | 스킨부스터 | Skin Booster | `/skincare/skin-booster` | 기획안 0404 |
| Skin Care | 재생세포 | Regenerative Cell Therapy | `/skincare/regenerative-cell` | 기획안 0405 |
| Skin Care | 고압산소치료 | Hyperbaric Oxygen Therapy | `/skincare/hyperbaric-oxygen` | 기획안 0406 |
| Doctor's Column | (대메뉴) | Doctor's Column | `/column` | — |
| Doctor's Column | 성형 클리닉 | Plastic Surgery | `/column/plastic-surgery` | — |
| Doctor's Column | 클리닉 칼럼 | Clinic Column | `/column/clinic` | — |
| Before / After | (대메뉴) | Before & After | `/before-after` | — |
| Before / After | 성형 수술 | Surgery | `/before-after/surgery` | — |
| Before / After | 스킨 케어 | Skin Care | `/before-after/skincare` | — |
| Promotion | (단독) | Promotion | `/promotion` | — |

## 유틸리티 (푸터)

| 항목 | 영문 페이지명 | 슬러그 |
|---|---|---|
| GLOBAL — KR/EN/CH/JP | Language | 언어 프리픽스 `/en` `/zh` `/ja` (기본 ko는 프리픽스 없음) |
| 비급여 | Non-Covered Pricing | `/pricing` |
| 개인정보 취급방침 | Privacy Policy | `/privacy` |

## 이미지 폴더 규칙 (2026-07-22)

`img/` 하위에 대메뉴 번호 프리픽스 + 슬러그 폴더로 이미지를 관리한다. 소메뉴는 하위 폴더.

```
img/00_home/                  # 홈
img/01_about/{brand-story, doctors, equipment, tour, location}
img/02_surgery/{eye, face, forehead}
img/03_skincare/{thread-lifting, laser-lifting, botox-filler, skin-booster, regenerative-cell, hyperbaric-oxygen}
img/04_column/
img/05_before-after/{surgery, skincare}
img/06_promotion/
```
- img/ 루트에 남아 있는 기존 파일들은 현 페이지(index·sub)가 참조 중인 임시본 — 실이미지 확보 시 위 폴더로 이동하며 경로 교체.

## 규칙

- 슬러그: 소문자, 하이픈 구분, 대메뉴/소메뉴 2단 구조.
- IA 원본 다이어그램의 "KE"는 KR 오타로 간주 → 표준 언어코드(en/zh/ja) 사용.
- 비급여(`/pricing`)는 의료광고 규정상 노출 의무 페이지.
- 시술 서브페이지(Surgery·Skin Care 9종)는 `sub-open.html`(정적 오픈)·`sub-full.html`(정식) 공용 와이어프레임에서 파생 제작 (PLAN.md 로드맵 참조).
- 기획안 엑셀 위치: `~/Library/CloudStorage/Dropbox/#. Work/#. 버틀러🦋/초고/`
