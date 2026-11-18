const rows=[...document.querySelectorAll('#paper-list .paper')];
const fields=['search','year','topic','category'].map(id=>document.getElementById(id));
const japanese=document.documentElement.lang==='ja';
function filter(){
 const [q,y,t,c]=fields.map(x=>x.value.trim().toLowerCase());let n=0;
 for(const r of rows){r.hidden=!(r.textContent.toLowerCase().includes(q)&&(!y||r.dataset.year===y)&&(!t||r.dataset.topic.toLowerCase()===t)&&(!c||r.dataset.category.toLowerCase()===c));if(!r.hidden)n++;}
 document.getElementById('result-count').textContent=japanese?`研究業績：${n}件`:`${n} research ${n===1?'entry':'entries'}`;
 document.getElementById('empty').hidden=n>0;
}
fields.forEach(f=>f.addEventListener(f.id==='search'?'input':'change',filter));
function languageLinks(){for(const link of document.querySelectorAll('.language-switch a')){const url=new URL(link.href);url.hash=location.hash;link.href=url.href;}}
window.addEventListener('hashchange',languageLinks);languageLinks();
