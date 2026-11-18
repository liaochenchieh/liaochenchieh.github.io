"""Generate the static Japanese homepage from the English page and translations."""
from pathlib import Path
import re,html,json
ROOT=Path(__file__).resolve().parents[1]/'public'
def main():
 s=(ROOT/'index.html').read_text();t=json.loads((ROOT/'data/ja.json').read_text())
 # Keep filter values language-independent while translating their visible labels.
 s=re.sub(r'<option>([^<]+)</option>',lambda m:'<option value="'+html.escape(html.unescape(m[1]),quote=True)+'">'+m[1]+'</option>',s)
 def translate(m):
  raw=html.unescape(m[1]);key=raw.strip();v=t.get(key)
  if not key:return '>'+m[1]+'<'
  if v is None:
   v=key
   for en,ja in t.items():
    if ' · '+en in v:v=v.replace(' · '+en,' · '+ja)
   v=re.sub(r'(\d+) research entries',r'研究業績：\1件',v)
  return '>'+raw[:len(raw)-len(raw.lstrip())]+html.escape(v,quote=False)+raw[len(raw.rstrip()):]+'<'
 s=re.sub(r'>([^<>]+)<',translate,s)
 bio=(ROOT/'data/intro-ja.html').read_text()
 s,n=re.subn(r'<div class="bio">.*?</div>\s*<div class="news">',lambda m:bio+'<div class="news">',s,count=1,flags=re.S);assert n==1
 s=s.replace('<html lang="en">','<html lang="ja">')
 s=s.replace('Jacky Liao | Chen-Chieh Liao — Academic Homepage','廖振傑（Jacky Liao） — 研究者ホームページ').replace('Jacky Liao — Academic Homepage','廖振傑（Jacky Liao） — 研究者ホームページ')
 s=s.replace('Jacky (Chen-Chieh) Liao researches AI, XR, human movement, and skill acquisition. Explore publications, projects, honors, and research funding.','廖振傑（Jacky Liao）の研究者ホームページ。AI・XR、人の動作、技能獲得支援に関する研究、論文、経歴、受賞を紹介します。')
 s=s.replace('rel="canonical" href="https://liaochenchieh.github.io/"','rel="canonical" href="https://liaochenchieh.github.io/jp.html"').replace('property="og:url" content="https://liaochenchieh.github.io/"','property="og:url" content="https://liaochenchieh.github.io/jp.html"')
 s=s.replace('hreflang="en" aria-current="page"','hreflang="en"').replace('href="/jp.html" lang="ja" hreflang="ja"','href="/jp.html" lang="ja" hreflang="ja" aria-current="page"')
 s=s.replace('aria-label="Main navigation"','aria-label="メインナビゲーション"').replace('aria-label="Language"','aria-label="言語切り替え"').replace('placeholder="Title, author, or keyword"','placeholder="論文名・著者・キーワード"')
 s=s.replace('Research figure:','研究図：').replace(' research figure"','の研究図"')
 s=s.replace(' and <a href="#project-7">',' と <a href="#project-7">').replace(' accepted to ECCV 2026.',' がECCV 2026に採択されました。').replace(' accepted to NeurIPS 2025.',' がNeurIPS 2025に採択されました。')
 s=s.replace('Started a <a href="#funding">JSPS KAKENHI Early-Career Scientists project</a> on motion style transfer for sports skill acquisition.','動作スタイル転移によるスポーツ技能獲得支援をテーマとする<a href="#funding">科研費・若手研究</a>を開始しました。')
 s=s.replace('Two CHI Best Paper Honorable Mentions','CHIで2件の優秀論文賞を受賞')
 s='\n'.join(line.rstrip() for line in s.splitlines())+'\n'
 (ROOT/'jp.html').write_text(s)
 print('Updated Japanese homepage.')
if __name__=='__main__':main()
