#!/usr/bin/env python3
"""전 페이지 상단 메뉴를 IA 기반 링크 구조로 교체 (idempotent)"""
import re, glob, os

BASE = "/Users/skyim/Library/CloudStorage/Dropbox/Claude Code/butler-lifting-layouts"

HEADER = '''<header class="gnb">
<style>
.gnb{position:sticky;top:0;z-index:80;/*lang 기준*/ background:#FBFAF8;border-bottom:1px solid rgba(112,112,112,0.45);font-family:'Noto Sans','Noto Sans KR',sans-serif;}
.gnb .gwrap{display:flex;align-items:center;justify-content:flex-start;height:60px;max-width:none;margin:0;padding:0 30px;gap:0;}
.gnb .glogo{display:flex;align-items:center;text-decoration:none;}
.gnb .glogo img{height:22px;width:auto;display:block;}
.gnb nav.gnav{display:flex;gap:0;margin-left:auto;font-size:13px;font-weight:400;letter-spacing:0.03em;text-transform:uppercase;color:#333;}
.gnb .nv{position:relative;padding:0 17px;}
.gnb .nv > a{color:#333;text-decoration:none;padding:20px 0;display:inline-block;}
.gnb .nv > a:hover{color:#111;}
.gnb .nv-t{color:#333;cursor:default;padding:20px 0;display:inline-block;}
.gnb .dp{position:absolute;top:100%;left:50%;transform:translateX(-50%);text-transform:none;background:#FBFAF8;border:1px solid #ECECEC;box-shadow:0 10px 28px rgba(0,0,0,0.07);border-radius:0;padding:8px 0;display:none;min-width:158px;z-index:120;}
.gnb .nv:hover .dp{display:block;}
.gnb .dp a{display:block;padding:8px 20px;font-size:12.5px;font-weight:400;color:#555;text-decoration:none;white-space:nowrap;text-align:left;}
.gnb .dp a:hover{color:#111;background:#F4F4F4;}
.gnb .gglobe{position:relative;margin-left:17px;display:flex;align-items:center;}
.gnb .gglobe-btn{display:flex;align-items:center;justify-content:center;padding:20px 0;background:none;border:none;outline:none;cursor:pointer;color:#333;}
.gnb .gglobe-btn:focus,.gnb .gglobe-btn:focus-visible{outline:none;}
.gnb .gglobe .gdp{position:absolute;top:100%;right:0;background:#FBFAF8;border:1px solid #EBEBEB;box-shadow:0 10px 24px rgba(0,0,0,0.07);min-width:92px;padding:6px 0;display:none;z-index:130;}
.gnb .gglobe:hover .gdp,.gnb .gglobe.open .gdp{display:block;}
.gnb .gglobe .gdp a{display:block;padding:7px 18px;font-size:12px;letter-spacing:0.06em;color:#555;text-decoration:none;text-align:right;}
.gnb .gglobe .gdp a:hover{color:#111;background:#F4F4F4;}
.gnb .gglobe .gdp a.on{color:#111;font-weight:600;}
.gnb .gmenu-btn{display:none;margin-left:auto;width:40px;height:40px;position:relative;background:none;border:none;cursor:pointer;}
.gnb .gmenu-btn i{position:absolute;left:9px;right:9px;height:1.5px;background:#111;transition:transform .3s ease,opacity .3s ease;}
.gnb .gmenu-btn i:nth-child(1){top:14px;} .gnb .gmenu-btn i:nth-child(2){top:20px;} .gnb .gmenu-btn i:nth-child(3){top:26px;}
body.gm-open .gmenu-btn i:nth-child(1){transform:translateY(6px) rotate(45deg);}
body.gm-open .gmenu-btn i:nth-child(2){opacity:0;}
body.gm-open .gmenu-btn i:nth-child(3){transform:translateY(-6px) rotate(-45deg);}
.gnb-mobile{position:fixed;inset:0;z-index:190;background:#FBFAF8;padding:84px 28px 120px;overflow-y:auto;display:none;}
body.gm-open .gnb-mobile{display:block;}
body.gm-open{overflow:hidden;}
.gnb-mobile .gm-grp{border-bottom:1px solid #E3E3E3;padding:18px 0;}
.gnb-mobile .gm-solo{border-bottom:none;padding:1.5px 0;}
.gnb-mobile .gm-grp:not(.gm-solo) + .gm-solo{padding-top:18px;}
.gnb-mobile .gm-t{font-size:15px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;color:#111;}
.gnb-mobile .gm-sub{margin-top:12px;display:grid;grid-template-columns:1fr 1fr;gap:10px 14px;}
.gnb-mobile .gm-sub a{font-size:14px;color:#555;text-decoration:none;}
.gnb-mobile .gm-lang{display:flex;justify-content:flex-start;gap:16px;margin-top:30px;padding-bottom:24px;font-size:12px;letter-spacing:0.1em;color:#b0b0b0;}
.gnb-mobile .gm-lang a{color:#8a8a8a;text-decoration:none;}
.gnb-mobile .gm-lang a.on{color:#111;font-weight:600;}
@media(max-width:1024px){ .gnb nav.gnav{display:none;} .gnb .gglobe{display:none;} .gnb .gmenu-btn{display:block;} }
@media(min-width:1025px){ .gnb-mobile{display:none !important;} }
</style>
<div class="gwrap">
  <a href="index.html" class="glogo"><img src="img/00_home/logo_h_dark.png" alt="Butler Clinic"></a>
  <nav class="gnav">
    <div class="nv"><a href="about-brand-story-full.html">Butler Clinic</a>
      <div class="dp">
        <a href="about-brand-story-full.html">브랜딩 스토리</a>
        <a href="about-doctors-full.html">의료진 소개</a>
        <a href="about-equipment-full.html">보유장비·의약품</a>
        <a href="about-tour-full.html">둘러보기</a>
        <a href="about-location-full.html">오시는 길</a>
      </div>
    </div>
    <div class="nv"><a href="surgery-eye-open.html">Surgery</a>
      <div class="dp">
        <a href="surgery-eye-open.html">눈 수술</a>
        <a href="surgery-face-open.html">안면부 수술</a>
        <a href="surgery-forehead-open.html">이마 수술</a>
      </div>
    </div>
    <div class="nv"><a href="sub-open.html">Skin Care</a>
      <div class="dp">
        <a href="skincare-thread-lifting-open.html">실 리프팅</a>
        <a href="sub-open.html">레이저 리프팅</a>
        <a href="skincare-botox-filler-open.html">보톡스·필러</a>
        <a href="skincare-skin-booster-open.html">스킨부스터</a>
        <a href="skincare-regenerative-cell-open.html">재생세포</a>
        <a href="skincare-hyperbaric-oxygen-open.html">고압산소치료</a>
      </div>
    </div>
    <div class="nv"><span class="nv-t">Doctor's Column</span></div>
    <div class="nv"><span class="nv-t">Before / After</span></div>
    <div class="nv"><span class="nv-t">Promotion</span></div>
  </nav>
  <div class="gglobe">
    <button class="gglobe-btn" type="button" aria-label="언어 선택"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.7 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.7-3.8-9s1.3-6.4 3.8-9z"/></svg></button>
    <div class="gdp"><a href="#" class="on">Korea</a><a href="#">English</a><a href="#">China</a><a href="#">Japan</a></div>
  </div>
  <button class="gmenu-btn" aria-label="메뉴 열기"><i></i><i></i><i></i></button>
</div>
<div class="gnb-mobile">
  <div class="gm-grp"><span class="gm-t">Butler Clinic</span>
    <div class="gm-sub">
      <a href="about-brand-story-full.html">브랜딩 스토리</a>
      <a href="about-doctors-full.html">의료진 소개</a>
      <a href="about-equipment-full.html">보유장비·의약품</a>
      <a href="about-tour-full.html">둘러보기</a>
      <a href="about-location-full.html">오시는 길</a>
    </div>
  </div>
  <div class="gm-grp"><span class="gm-t">Surgery</span>
    <div class="gm-sub">
      <a href="surgery-eye-open.html">눈 수술</a>
      <a href="surgery-face-open.html">안면부 수술</a>
      <a href="surgery-forehead-open.html">이마 수술</a>
    </div>
  </div>
  <div class="gm-grp"><span class="gm-t">Skin Care</span>
    <div class="gm-sub">
      <a href="skincare-thread-lifting-open.html">실 리프팅</a>
      <a href="sub-open.html">레이저 리프팅</a>
      <a href="skincare-botox-filler-open.html">보톡스·필러</a>
      <a href="skincare-skin-booster-open.html">스킨부스터</a>
      <a href="skincare-regenerative-cell-open.html">재생세포</a>
      <a href="skincare-hyperbaric-oxygen-open.html">고압산소치료</a>
    </div>
  </div>
  <div class="gm-grp gm-solo"><span class="gm-t nv-t">Doctor's Column</span></div>
  <div class="gm-grp gm-solo"><span class="gm-t nv-t">Before / After</span></div>
  <div class="gm-grp gm-solo"><span class="gm-t nv-t">Promotion</span></div>
  <div class="gm-lang"><a href="#" class="on">KR</a><a href="#">EN</a><a href="#">CH</a><a href="#">JP</a></div>
</div>
<script>
(function(){
  var btn = document.querySelector('.gnb .gmenu-btn');
  if (btn) btn.addEventListener('click', function(){ document.body.classList.toggle('gm-open'); });
  var gb = document.querySelector('.gnb .gglobe');
  if (gb) {
    gb.querySelector('.gglobe-btn').addEventListener('click', function(e){ e.stopPropagation(); gb.classList.toggle('open'); });
    document.addEventListener('click', function(){ gb.classList.remove('open'); });
  }
  document.querySelectorAll('.nv-t').forEach(function(el){
    el.style.cursor = 'pointer';
    el.addEventListener('click', function(){ alert('준비중 입니다'); });
  });
})();
</script>
</header>'''

files = sorted(glob.glob(os.path.join(BASE, "*.html")))
for f in files:
    src = open(f, encoding="utf-8").read()
    pat = re.compile(r'<header class="gnb">[\s\S]*?</header>')
    if pat.search(src):
        new = pat.sub(lambda m: HEADER, src, count=1)
        action = "교체"
    else:
        m = re.search(r'<body[^>]*>\n?', src)
        if not m:
            print(os.path.basename(f), ": body 태그 없음 — 건너뜀"); continue
        new = src[:m.end()] + "\n" + HEADER + "\n" + src[m.end():]
        action = "삽입"
    open(f, "w", encoding="utf-8").write(new)
    print(os.path.basename(f), ":", action)
