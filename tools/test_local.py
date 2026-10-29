"""Standard-library checks. Run: python tools/test_local.py"""
from pathlib import Path
from html.parser import HTMLParser
import json
root=Path(__file__).resolve().parents[1]
class Parser(HTMLParser):
    def __init__(self): super().__init__();self.ids=set()
    def handle_starttag(self,tag,attrs):
        values=dict(attrs)
        if 'id' in values:self.ids.add(values['id'])
p=Parser();p.feed((root/'index.html').read_text(encoding='utf-8'))
required={'intervalTab','stopwatchTab','clock','startBtn','resetBtn','swClock','swStart','templateSelect','saveTemplate','rounds','work','rest','prepare'}
assert required <= p.ids,required-p.ids
for filename in ['index.html','styles.css','app.js','service-worker.js','manifest.webmanifest','assets/icon.svg']:
    assert (root/filename).is_file(),filename
assert json.loads((root/'manifest.webmanifest').read_text(encoding='utf-8'))['display']=='standalone'
print('PASS: 필요한 파일, 화면 요소, PWA manifest 확인 완료')
