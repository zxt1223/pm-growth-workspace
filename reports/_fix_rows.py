# -*- coding: utf-8 -*-
import re

PMREPO = r"C:/Users/Lenovo/WorkBuddy/2026-08-24-07-22-42/.workbuddy/pmrepo/reports/2027秋招快消全清单_年包排名.html"
SRC    = r"C:/Users/Leno/WorkBuddy/2026-08-19-17-13-08/reports/2027秋招快消全清单_年包排名.html"

with open(PMREPO, encoding="utf-8") as f:
    html = f.read()

# locate main table tbody (the one right after mergeTable)
idx = html.find('data-page-node-id="mergeTable"')
seg = html[idx:]
mt = re.search(r'<tbody>(.*?)</tbody>', seg, re.S)
inner_span_start = idx + mt.start() + len('<tbody>')
inner_span_end   = idx + mt.start() + len('<tbody>') + len(mt.group(1))
inner = mt.group(1)

lines = inner.split('\n')
new_lines = []
wrapped = 0
for ln in lines:
    if re.match(r'^\s*<td class="rk"', ln):
        # line currently: "      <td ...> ... </td>"  -> wrap in <tr>...</tr>
        body = ln.lstrip()
        indent = ln[:len(ln)-len(body)]
        new_lines.append(indent + '<tr>' + body + '</tr>')
        wrapped += 1
    else:
        new_lines.append(ln)

new_inner = '\n'.join(new_lines)
html = html[:inner_span_start] + new_inner + html[inner_span_end:]

print("wrapped rows:", wrapped)

# sanity: ensure there are now 20 <tr> with rk
print("rk rows:", html.count('<tr><td class="rk"') + html.count('<tr>\n      <td class="rk"'))

with open(PMREPO, "w", encoding="utf-8") as f:
    f.write(html)
print("pmrepo written")
