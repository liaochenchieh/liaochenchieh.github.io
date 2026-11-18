"""Refresh publication HTML from JSON; serving the site needs no build."""
from pathlib import Path
import html,json,re
ROOT=Path(__file__).resolve().parents[1]/'public'
def render(p):
 esc=html.escape
 authors=esc(p['authors']).replace('Chen-Chieh Liao','<strong>Chen-Chieh Liao</strong>').replace('廖振傑','<strong>廖振傑</strong>')
 links=''.join(f'<a href="{esc(url)}">{esc(label)} ↗</a>' for label,url in p['links'])
 award=f'<div class="award">{esc(p["award"])}</div>' if p.get('award') else ''
 equal='<p class="authors">∗ Equal contribution</p>' if p['id']==7 else ''
 return f'''<article class="paper" id="paper-{p['id']}" data-year="{p['year']}" data-topic="{esc(p['topic'])}" data-category="{esc(p['category'])}">
<div class="paper-thumb"><img src="{esc(p['image'])}" alt="Research figure: {esc(p['title'])}" loading="lazy" width="200" height="150"></div>
<div class="paper-body"><div class="meta">{esc(p['venue'])} · {p['year']} · {esc(p['category'])}</div><h3>{esc(p['title'])}</h3>{award}<p class="authors">{authors}</p>{equal}<div class="paper-links">{links}</div></div></article>'''
def main():
 papers=json.loads((ROOT/'data/publications.json').read_text())
 assert len({p['id'] for p in papers})==len(papers),'Duplicate publication IDs'
 s=(ROOT/'index.html').read_text()
 replacement='<!-- publications:start -->\n'+'\n'.join(render(p) for p in sorted(papers,key=lambda p:(-p['year'],p['id'])))+'\n<!-- publications:end -->'
 s,n=re.subn(r'<!-- publications:start -->.*?<!-- publications:end -->',lambda m:replacement,s,flags=re.S)
 assert n==1,'Expected one publication list'
 s,n=re.subn(r'(<p id="result-count"[^>]*>).*?(</p>)',lambda m:m[1]+f'{len(papers)} research entries'+m[2],s,count=1)
 assert n==1
 (ROOT/'index.html').write_text(s)
 print(f'Updated {len(papers)} publication entries.')
if __name__=='__main__':main()
