# -*- coding: utf-8 -*-
import re, shutil

PMREPO = r"C:/Users/Lenovo/WorkBuddy/2026-08-24-07-22-42/.workbuddy/pmrepo/reports/2027秋招快消全清单_年包排名.html"
SRC    = r"C:/Users/Lenovo/WorkBuddy/2026-08-19-17-13-08/reports/2027秋招快消全清单_年包排名.html"

with open(PMREPO, encoding="utf-8") as f:
    html = f.read()

# ---------- 1) Main table: delete expired rows, renumber, update deadlines ----------
idx = html.find('data-page-node-id="mergeTable"')
seg = html[idx:]
mt = re.search(r'<tbody>(.*?)</tbody>', seg, re.S)
inner = mt.group(1)
s0 = idx + mt.start()
e0 = idx + mt.end()

rows = re.findall(r'<tr>(.*?)</tr>', inner, re.S)

DELETE = ['玛氏','乐高','元气森林','科蒂','泡泡玛特','蒙牛','格力','农夫山泉',
          '百胜','星巴克','蓝月亮','名创优品','爱茉莉','喜茶','Moody','金佰利',
          'UR','来伊份','奈雪']

def comp_name(row):
    td = re.search(r'<td data-label="公司">(.*?)</td>', row, re.S).group(1)
    b = re.search(r'<b>(.*?)</b>', td, re.S)
    return b.group(1) if b else td

kept = [r for r in rows if not any(k in comp_name(r) for k in DELETE)]

UPDATES = {
  '默克':   ('11月中（2026-09起滚动，多数岗位11月中前截止）', '在招 · 11月中'),
  '可口可乐':('滚动至 2027-05-31（部分瓶装厂）', '在招 · 长期滚动'),
  '雀巢':   ('11月30日（Moka 通道）', '在招 · 11月30日'),
  'LVMH':   ('滚动至 2027-01（HORIZONS 项目）', '在招 · 滚动'),
  '耐克':   ('本科 10/18–11/1，硕士 11/30–12/7', '在招 · 硕士11月底'),
  '汉高':   ('10月31日（网申停止）', '在招 · 10月31日'),
  '达能':   ('10月31日（9/7–10/31）', '在招 · 10月31日'),
  '百威':   ('10月31日（10月底）', '在招 · 10月31日'),
  '亿滋':   ('11月30日', '在招 · 11月30日'),
  'SHEIN':  ('招满即止（2026/9–2027/6 滚动）', '在招 · 长期滚动'),
  '优衣库': ('10月31日（秋招批次）/ UMC 长期至2027/8/21', '在招 · UMC长期'),
  '资生堂': ('10月（建议官网核实）', '在招 · 待核实'),
  '费列罗': ('10月（建议官网核实）', '在招 · 待核实'),
  '拜尔斯道夫':('10月（建议官网核实）', '在招 · 待核实'),
  '青岛啤酒': ('10月（建议官网核实）', '在招 · 待核实'),
  '卡夫亨氏': ('10月（建议官网核实）', '在招 · 待核实'),
  '帝亚吉欧': ('官网未公布（滚动）', '在招 · 待核实'),
}

def set_cells(row, deadline, status):
    row = re.sub(r'<td data-label="网申截止">.*?</td>',
                 f'<td data-label="网申截止">{deadline}</td>', row, count=1)
    row = re.sub(r'<td style="font-size:12px" data-label="网申状态">.*?</td>',
                 f'<td style="font-size:12px" data-label="网申状态">{status}</td>', row, count=1)
    return row

new_rows = []
for i, r in enumerate(kept, 1):
    name = comp_name(r)
    r = re.sub(r'<td class="rk" data-label="#">\d+</td>',
               f'<td class="rk" data-label="#">{i}</td>', r, count=1)
    for k,(d,s) in UPDATES.items():
        if k in name:
            r = set_cells(r, d, s); break
    new_rows.append(r)

new_tbody = '<tbody>\n      ' + '\n      '.join(new_rows) + '\n    </tbody>'
html = html[:s0] + new_tbody + html[e0:]
print("kept rows:", len(kept))

# ---------- 2) Header h1 + tags ----------
html = html.replace(
    '2027 届秋招 · 快消全清单（72 家）适配岗位 + 年包排名',
    '2027 届秋招 · 快消在招清单（剩 20 家 · 截至 10-23）适配岗位 + 年包排名')
html = html.replace('已核实：宝洁 / 联合利华 / 欧莱雅 / 玛氏 / 高露洁',
                    '已复核：嘉士伯 / 迪卡侬 / 默克 / 可口可乐 / 达能 / 汉高（2026-10-23）')
html = html.replace('其余为同类节奏估算',
                    '其余 10 家为官网/往年节奏估算，投递前请官网确认')
html = html.replace('更新于 2026-10-04 · 年包已按你的岗位拆解',
                    '复核于 2026-10-23 · 年包已按你的岗位拆解')

# ---------- 3) line 182 keep-count note ----------
html = html.replace('共保留 39 家。',
                    '共保留 20 家（截至 2026-10-23 仍在招）。')
html = html.replace('本表已合并原「四、全部公司投递入口+岗位匹配度」与「六、岗位年包拆解」三张大表为一；',
                    '本表已合并原「四、全部公司投递入口+岗位匹配度」与「六、岗位年包拆解」三张大表为一；并按 2026-10-23 复核，删除了已结束校招的公司（见下方「已截止」清单）；')

# ---------- 4) Urgency table (基准日 + rows) ----------
html = html.replace('二、⚠️ 当前可投·按截止紧迫度（基准日 2026-10-19）',
                    '二、⚠️ 当前可投·按截止紧迫度（基准日 2026-10-23）')

urg_rows = '''
      <tr><td data-label="公司"><b>强生 J&amp;J</b></td><td data-label="截止"><span class="urgent2">10月31日 24:00</span></td><td data-label="还剩">剩约8天</td><td data-label="适配岗位">管培：市场/销售/供应链</td><td data-label="行动">尽快投（已核实·进行中）</td></tr>
      <tr><td data-label="公司"><b>达能 Danone</b></td><td data-label="截止"><span class="urgent2">10月31日</span></td><td data-label="还剩">剩约8天</td><td data-label="适配岗位">管培：市场/销售/供应链</td><td data-label="行动">尽快投（已核实·进行中）</td></tr>
      <tr><td data-label="公司"><b>百威 Budweiser</b></td><td data-label="截止"><span class="urgent2">10月31日（10月底）</span></td><td data-label="还剩">剩约8天</td><td data-label="适配岗位">管培：销售/市场</td><td data-label="行动">尽快投（已核实·进行中）</td></tr>
      <tr><td data-label="公司"><b>嘉士伯 Carlsberg</b></td><td data-label="截止"><span class="urgent2">10月31日 18:00</span></td><td data-label="还剩">剩约8天</td><td data-label="适配岗位">职能管培·市场（广州）/ 商务管培</td><td data-label="行动">尽快投（已核实·年包20–23w+）</td></tr>
      <tr><td data-label="公司"><b>汉高 Henkel</b></td><td data-label="截止"><span class="urgent2">10月31日</span></td><td data-label="还剩">剩约8天</td><td data-label="适配岗位">管培：市场/销售/供应链（含施华蔻）</td><td data-label="行动">尽快投（已核实）</td></tr>
      <tr><td data-label="公司"><b>优衣库 UMC</b></td><td data-label="截止">2027年8月21日</td><td data-label="还剩">长期</td><td data-label="适配岗位">零售运营 / 电商 / 商品</td><td data-label="行动">长期项目，早投占位（已核实）</td></tr>
      <tr><td data-label="公司"><b>SHEIN</b></td><td data-label="截止">招满即止</td><td data-label="还剩">长期滚动</td><td data-label="适配岗位">电商运营 / 数据分析 / 品类</td><td data-label="行动">随时可投（已核实）</td></tr>
      <tr><td data-label="公司"><b>资生堂 Shiseido</b></td><td data-label="截止">10月（待核实）</td><td data-label="还剩">待确认</td><td data-label="适配岗位">管培：市场/电商/数字营销</td><td data-label="行动">先官网确认再投</td></tr>
      <tr><td data-label="公司"><b>费列罗 Ferrero</b></td><td data-label="截止">10月（待核实）</td><td data-label="还剩">待确认</td><td data-label="适配岗位">管培：市场/销售</td><td data-label="行动">先官网确认再投</td></tr>
      <tr><td data-label="公司"><b>拜尔斯道夫 Nivea</b></td><td data-label="截止">10月（待核实）</td><td data-label="还剩">待确认</td><td data-label="适配岗位">管培：市场/销售</td><td data-label="行动">先官网确认再投</td></tr>
      <tr><td data-label="公司"><b>青岛啤酒</b></td><td data-label="截止">10月（待核实）</td><td data-label="还剩">待确认</td><td data-label="适配岗位">管培：市场/电商</td><td data-label="行动">先官网确认再投</td></tr>
      <tr><td data-label="公司"><b>卡夫亨氏 / 中粮</b></td><td data-label="截止">10月（待核实）</td><td data-label="还剩">待确认</td><td data-label="适配岗位">管培：市场/供应链</td><td data-label="行动">先官网确认再投</td></tr>
      <tr><td data-label="公司"><b>帝亚吉欧 DIAGEO</b></td><td data-label="截止">官网未公布</td><td data-label="还剩">待确认</td><td data-label="适配岗位">管培：市场/品牌</td><td data-label="行动">先官网确认再投</td></tr>
      <tr><td data-label="公司"><b>默克 Merck</b></td><td data-label="截止">11月中</td><td data-label="还剩">剩约23天</td><td data-label="适配岗位">管培：市场/供应链/商业分析</td><td data-label="行动">本月内投</td></tr>
      <tr><td data-label="公司"><b>雀巢 Nestlé</b></td><td data-label="截止">11月30日</td><td data-label="还剩">剩约38天</td><td data-label="适配岗位">管培：销售/市场/供应链</td><td data-label="行动">本月内投（Moka）</td></tr>
      <tr><td data-label="公司"><b>亿滋 Mondelēz</b></td><td data-label="截止">11月30日</td><td data-label="还剩">剩约38天</td><td data-label="适配岗位">管培：市场/销售/品类</td><td data-label="行动">本月内投（已核实）</td></tr>
      <tr><td data-label="公司"><b>迪卡侬 Decathlon</b></td><td data-label="截止">11月30日</td><td data-label="还剩">剩约38天</td><td data-label="适配岗位">线上运营/电商/全渠道零售</td><td data-label="行动">本月内投（已核实）</td></tr>
      <tr><td data-label="公司"><b>耐克 Nike</b></td><td data-label="截止">硕士 11月底</td><td data-label="还剩">剩约38天</td><td data-label="适配岗位">管培：零售/数字电商/市场</td><td data-label="行动">硕士岗可投</td></tr>
      <tr><td data-label="公司"><b>LVMH</b></td><td data-label="截止">滚动至 2027/1</td><td data-label="还剩">长期</td><td data-label="适配岗位">管培：市场/品类/零售/电商</td><td data-label="行动">随时可投</td></tr>
      <tr><td data-label="公司"><b>可口可乐 Coca-Cola</b></td><td data-label="截止">滚动至 2027/5</td><td data-label="还剩">长期</td><td data-label="适配岗位">管培：销售发展/市场/供应链</td><td data-label="行动">随时可投</td></tr>
'''
html = re.sub(r'<tbody data-page-node-id="Kv96sDnwNMLU8t1Z7QIaDc">.*?</tbody>',
              '<tbody data-page-node-id="Kv96sDnwNMLU8t1Z7QIaDc">' + urg_rows + '      </tbody>',
              html, count=1, flags=re.S)

# ---------- 5) 已截止 note ----------
old_note = ('⚠️ 已截止不可投（均已联网核实，且已按要求从主表删除）：宝洁 9/28、阿迪达斯 9/30'
            '（大陆管培）、欧莱雅 10/8、高露洁 10/8、雅诗兰黛 10/8、联合利华 10/12、百事 10/18 24:00。'
            '可关注补录 / 春招或社招通道。')
new_note = ('⚠️ 已截止 / 已删除（截至 2026-10-23，已从主表移除）：'
            '宝洁 9/28、阿迪达斯 9/30、欧莱雅 10/8、高露洁 10/8、雅诗兰黛 10/8、联合利华 10/12、百事 10/18；'
            '本次复核新增——玛氏 10月中、乐高 10月中、元气森林 10月中、科蒂 10/21、爱茉莉 10/20、'
            '泡泡玛特 10月中、百胜 10月中、金佰利 10月中、蒙牛/伊利 10月中、格力 10月、农夫山泉 10月、'
            '星巴克 10月、蓝月亮/花西子 10月、名创优品 10月、喜茶 10月、Moody/卡士/娃哈哈 10月、'
            'UR/CK/李锦记等 10月中、来伊份组 10月中、奈雪 10月。可关注补录 / 春招或社招通道。')
html = html.replace(old_note, new_note)

# ---------- 6) comparison table: remove expired 科蒂 / 爱茉莉 rows ----------
html = re.sub(r'\s*<tr><td data-label="公司"><b>科蒂 Coty</b>.*?</tr>', '', html, flags=re.S)
html = re.sub(r'\s*<tr><td data-label="公司"><b>爱茉莉太平洋</b>.*?</tr>', '', html, flags=re.S)
# fix 汉高 date in comparison
html = html.replace('<b>汉高（含施华蔻）</b> 10/30', '<b>汉高（含施华蔻）</b> 10/31')
# update comparison note
html = html.replace(
    '嘉士伯/迪卡侬/百事/阿迪达斯有官方或高校就业网信源；科蒂/汉高/爱茉莉太平洋的截止日暂以图源为准（标"待核"），投递前以官网为准。',
    '嘉士伯/迪卡侬有官方或高校就业网信源；汉高的截止日暂以图源为准（标"待核"），投递前以官网为准。科蒂（10/21）、爱茉莉太平洋（10/20）已截止、已从表删除。')

# ---------- 7) decision advice bullets (avoid pointing to closed cos) ----------
html = html.replace(
    '<b data-page-node-id="3zNtjCwC6ap8nGt6DD3mgy">第一梯队优先抢：</b>欧莱雅（10.8）+ 高露洁（10.8）+ 联合利华（10.12）——截止最近、你的「市场/电商/消费者洞察」画像最吃得开，且年包 15–28 万。',
    '<b data-page-node-id="3zNtjCwC6ap8nGt6DD3mgy">当前最紧迫（10/31 前）：</b>强生 / 达能 / 百威 / 嘉士伯（广州岗·年包20–23w+）/ 汉高——均已核实 10月31日前后截止，且你的「市场/电商/消费者洞察」画像吃得开，今天起优先投。')
html = html.replace(
    '<b data-page-node-id="jL46Bp8p6A67vCjWL3D24W">你的最优性价比组合：</b>欧莱雅（电商/市场管培，28万上限）+ 联合利华 CMI（消费者洞察岗，几乎为你定制）+ 高露洁市场部。三家的流程互不冲突，可同时推进到面试。',
    '<b data-page-node-id="jL46Bp8p6A67vCjWL3D24W">你的最优性价比组合：</b>嘉士伯·职能管培市场（广州✓·年包20–23w+）+ 迪卡侬·线上运营/电商（WLB标杆·上海广州深圳）+ 达能/强生市场岗。三家流程互不冲突，可同时推进。')

# ---------- 8) footer ----------
html = html.replace(
    '数据整理于 2026-10-03｜2026-10-04 补充：全部 72 家投递入口',
    '数据整理于 2026-10-03｜2026-10-04 补充：全部 72 家投递入口｜2026-10-23 复核：删除已结束校招公司，仅保留仍在招的 20 家')

with open(PMREPO, "w", encoding="utf-8") as f:
    f.write(html)

# sync source copy
shutil.copy2(PMREPO, SRC)
print("written + synced")
