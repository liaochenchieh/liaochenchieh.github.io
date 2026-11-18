"""Validate homepage assets, anchors, publication coverage, and retained routes."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import json
ROOT=Path(__file__).resolve().parents[1]/'public'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=[];self.papers=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.append(a['id'])
  if 'paper' in a.get('class','').split():self.papers+=1
  self.refs.extend(a[k] for k in ('src','href') if k in a)
s=(ROOT/'index.html').read_text();page=Page();page.feed(s)
assert not any(x in s for x in ['{{','{%','¥','CHF ']),'Unrendered template or money amount'
assert len(page.ids)==len(set(page.ids)),'Duplicate HTML IDs'
assert page.papers==len(json.loads((ROOT/'data/publications.json').read_text()))
missing=[]
for ref in page.refs:
 u=urlparse(ref)
 if u.scheme or u.netloc:continue
 if not u.path:
  if u.fragment and u.fragment not in page.ids:missing.append(ref)
 else:
  p=ROOT/unquote(u.path.lstrip('/'))
  if not p.is_file() and not (p/'index.html').is_file():missing.append(ref)
assert not missing,f'Missing assets or targets: {missing}'
for path in ['.nojekyll','projects/motion-style-slider/index.html','jp.html','assets/pdf/CV.pdf']:
 assert (ROOT/path).is_file(),path
print(f'PASS: {page.papers} publications; local links/assets, anchors, and retained routes verified.')
