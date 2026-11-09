"""Build en/index.html (insovio.com/en/) from index.html.

The page itself is the same; the script in index.html switches to English when the path is /en/.
This copy only changes what has to differ before the script runs: root-relative asset paths,
<html lang>, and the head tags that link previews and search engines read.
Run after every change to index.html:  python3 tools/build_en.py
"""
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
s = (root / 'index.html').read_text(encoding='utf-8')


def sub_once(pattern, repl, text):
    out, n = re.subn(pattern, repl, text, count=1)
    assert n == 1, pattern
    return out


TITLE = 'INSOVIO · Microbiome-based human optimization'
DESC = ('INSOVIO: microbiome-based human optimization. Measure, nourish, track. '
        'Pre-registration is open for the GastroSens sensory experience.')
OG_DESC = ('Half of our body isn’t us. INSOVIO measures your own data, adds the missing ingredient '
           'through delicious real food and tracks the effect.')

s = sub_once(r'<html lang="tr">', '<html lang="en">', s)
s = sub_once(r'<title>[^<]*</title>', f'<title>{TITLE}</title>', s)
s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{DESC}">', s)
s = re.sub(r'(<meta name="description" content="[^"]*">\n?)(?=[\s\S]*<meta name="description")', '', s)
s = sub_once(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="https://insovio.com/en/">', s)
s = sub_once(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="https://insovio.com/en/">', s)
s = sub_once(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{TITLE}">', s)
s = sub_once(r'<meta property="og:description" content="[^"]*">',
             f'<meta property="og:description" content="{OG_DESC}">\n<meta property="og:locale" content="en_GB">', s)
# assets live at the site root
s = re.sub(r'(["\'])img/', r'\1/img/', s)

out = root / 'en' / 'index.html'
out.parent.mkdir(exist_ok=True)
out.write_text(s, encoding='utf-8')
print('wrote', out.relative_to(root))
