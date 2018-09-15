""" Clean 縦書き on a Kindle 4 from AZW3 files (b/c using custom CSS in Calibre
    fails and TXT export turns ルビ into normal text).

    - export w/ Calibre as HTMLZ
    - unpack
    - run this script on index.html
    - convert to pdf w/ http://a2k.aill.org/text.html
"""

import sys
import re
from bs4 import BeautifulSoup

def aozora_fmt(ruby_elem):
    """ https://www.aozora.gr.jp/annotation/etc.html#ruby
    """

    hani_ptrn = re.compile('([^>]+)(?=<rt>)')
    s = str(ruby_elem)
    s = re.sub(hani_ptrn, r'｜\1', s)
    s = s.replace('<rt>', '《')
    s = s.replace('</rt>', '》')
    s = s.replace('<ruby>', '')
    s = s.replace('</ruby>', '')
    # U+5C5B -> U+5C4F b/c a2k.aill.org/text.html eats U+5C5B
    s = s.replace('屛', '屏')

    return s

if len(sys.argv) < 2:
    print('Usage: python3 html2txt_ruby.py <input_file>')
    sys.exit()

with open(sys.argv[1]) as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')
for r in soup('ruby'):
    r.replace_with(aozora_fmt(r))

text = soup.get_text()

with open('out.txt', 'w') as f:
    f.write(text)
