#!/usr/bin/env python3
import re

with open('福建省校招情报专刊_2026-05-09.md','r',encoding='utf-8') as f:
    md = f.read()

html = md

# Headers
for i in range(6,0,-1):
    pat = '^' + '#'*i + r' (.+)$'
    rep = '<h%d>\\1</h%d>' % (i,i)
    html = re.sub(pat, rep, html, flags=re.MULTILINE)

# Bold **text**
html = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', html)
# Italic *text*
html = re.sub(r'\*(.+?)\*', r'<i>\1</i>', html)
# Links [text](url)
html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html)
# Code `text`
html = re.sub(r'`(.+?)`', r'<code>\1</code>', html)
# Blockquote
html = re.sub(r'^\u003e (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)

# Tables: find table blocks
def convert_table(text):
    lines = [l for l in text.split('\n') if l.strip().startswith('|')]
    if len(lines) < 2:
        return text
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if cells and all('-' in c and set(c) <= set('|-: ') for c in cells):
            continue  # separator line
        if cells:
            rows.append(cells)
    if not rows:
        return text
    # First row is header
    out = '<table>\n<thead>\n<tr>' + ''.join('<th>%s</th>' % c for c in rows[0]) + '</tr>\n</thead>\n<tbody>\n'
    for row in rows[1:]:
        out += '<tr>' + ''.join('<td>%s</td>' % c for c in row) + '</tr>\n'
    out += '</tbody>\n</table>'
    # Replace the original table block in text
    return out

# Simple table detection: lines starting with |
table_blocks = re.split(r'(\n\|[^\n]+\n\|[-|\s:]+\n(?:\|[^\n]+\n)*)', html)
new_parts = []
for part in table_blocks:
    if part.strip().startswith('|') and '\n|' in part:
        new_parts.append(convert_table(part))
    else:
        new_parts.append(part)
html = ''.join(new_parts)

# Lists
lines = html.split('\n')
new_lines = []
in_ul = False
in_ol = False
for line in lines:
    s = line.strip()
    if s.startswith('- ') or s.startswith('* '):
        if not in_ul:
            new_lines.append('<ul>')
            in_ul = True
        content = s[2:]
        new_lines.append('<li>%s</li>' % content)
    elif re.match(r'^\d+\.\s', s):
        if not in_ol:
            new_lines.append('<ol>')
            in_ol = True
        content = re.sub(r'^\d+\.\s', '', s)
        new_lines.append('<li>%s</li>' % content)
    else:
        if in_ul:
            new_lines.append('</ul>')
            in_ul = False
        if in_ol:
            new_lines.append('</ol>')
            in_ol = False
        new_lines.append(line)
if in_ul:
    new_lines.append('</ul>')
if in_ol:
    new_lines.append('</ol>')
html = '\n'.join(new_lines)

# Paragraphs for remaining text
lines = html.split('\n')
new_lines = []
for line in lines:
    stripped = line.strip()
    if stripped and not stripped.startswith('<') and not stripped.startswith('---') and not stripped.startswith('#'):
        new_lines.append('<p>%s</p>' % stripped)
    else:
        new_lines.append(line)
html = '\n'.join(new_lines)

html = html.replace('---', '<hr>')

full_html = '''<!DOCTYPE html>
<html><head><meta charset=utf-8>
<style>
@page { size: A4; margin: 15mm; }
body { font-family: 'Noto Sans CJK SC','WenQuanYi Micro Hei','Microsoft YaHei',sans-serif; font-size: 10pt; line-height: 1.6; color: #333; }
h1 { color: #e94560; font-size: 20pt; border-bottom: 3px solid #e94560; padding-bottom: 8px; }
h2 { color: #16213e; font-size: 14pt; border-bottom: 2px solid #e94560; padding-bottom: 6px; margin-top: 24px; }
h3 { color: #333; font-size: 12pt; margin-top: 18px; }
table { border-collapse: collapse; width: 100%; font-size: 8.5pt; margin: 12px 0; page-break-inside: avoid; }
th, td { border: 1px solid #ccc; padding: 5px 6px; text-align: left; vertical-align: top; }
th { background: #1a1a2e; color: #fff; font-weight: 600; }
tr:nth-child(even) { background: #f8f9fa; }
blockquote { border-left: 4px solid #e94560; margin: 12px 0; padding: 8px 12px; background: #fff5f5; color: #555; }
a { color: #e94560; text-decoration: none; }
code { background: #f0f0f0; padding: 2px 4px; border-radius: 3px; font-size: 9pt; }
ul, ol { margin: 8px 0; padding-left: 24px; }
li { margin: 4px 0; }
p { margin: 8px 0; }
small { font-size: 8pt; color: #888; }
</style></head><body>''' + html + '''</body></html>'''

with open('福建省校招情报专刊_2026-05-09.html','w',encoding='utf-8') as f:
    f.write(full_html)
print('HTML generated')
