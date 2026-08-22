# 明亮风 SaaS 中后台 / Admin Dashboard 设计 Prompt

> 适用工具：Midjourney / v0 / Stitch / Claude Artifacts / Cursor 等任何前端生成工具
> 来源：基于 4 张参考图（Nexus 仪表盘、CrowdPass 票务、Konoom Locations、Zendenta 牙科 Staff List）提炼的统一设计语言

---

## 1. 整体氛围与背景
- 整体置于一张**浅紫蓝冷色渐变**背景上：`#EEF1FF → #F5F7FF → #FAFAFE`，从左上到右下。
- 主区域是一张**白色大圆角面板**（圆角 24px，柔和多重阴影：`0 20px 60px -20px rgba(95,108,255,.18), 0 8px 24px -8px rgba(95,108,255,.10)`），整张面板悬浮在背景上，四周留出 80–120px padding。
- 信息密度适中、留白充足；禁止出现纯黑底或高饱和大色块。
- 圆角统一 Token：`sm=8px / md=12px / lg=16px / xl=24px / pill=999px`。

## 2. 字体
- 全局：`"Inter", "PingFang SC", system-ui, sans-serif`。
- 标题：字重 700，字号 28–32px；副标题字重 400，14–16px，色 `#6B7280`。
- 指标数字：字重 700，36–48px，tabular-nums。
- 表内文本 14px；表头小写字 12px，字重 500，色 `#6B7280`，uppercase，letter-spacing 0.04em。

## 3. 配色系统
- 主色（品牌蓝紫）：`#4F6BFF`，hover `#3D57E6`，浅色面 `#E8EDFF`。
- 文字：`primary #1A2233 / secondary #6B7280 / muted #9CA3AF / onBrand #FFFFFF`。
- 状态：`success #16A34A / successBg #E7F8EF`、`danger #DC2626 / dangerBg #FEE7E7`、`warn #F59E0B / warnBg #FFF6E0`、`info #2563EB / infoBg #E8F0FE`。
- 图表：`#4F6BFF / #8C9EFF / #B8C2FF / #16A34A / #F59E0B / #DC2626 / #9CA3AF`。

## 4. 左侧导航栏（240px）
- 宽度 240px，纯白，右侧 1px 分割线 `#EEF0F5`，无圆角外框。
- 顶部 Logo 区：高 72px，左对齐 logo icon + 品牌名（色 `#1A2233`，字重 700）。
- 紧接**用户卡**：`48px` 圆形头像 + 主名 + 副角色两行，左 padding 16，hover 时整张卡变 `#F4F6FF`。
- 菜单分组：
  - 选中态：**整行 pill 胶囊背景 `#EEF1FF`** + 主色文字 + 主色实心 icon；非选中态文字色 `#374151`，icon 线性描边。
  - 图标统一用 20px 线性图标（Lucide / Phosphor 风格），1.75px stroke。
  - 组与组之间用 6px gap + 8px 大写小字分组标题色 `#9CA3AF`（例：`CLINIC` / `FINANCE` / `PHYSICAL ASSET`）。
- 最底部 `Log out` 与上面的菜单隔一道 1px 分隔线，置灰。

## 5. 顶部条（Header Bar，64px）
- 高度 64px，纯白，底部 1px 分割线。
- 左：当前页大标题 `Hello, Rayan!` + 一行小副标题 `Here's your analytic detail`。
- 中（可选）：圆角 12px 搜索框，宽 480px，icon 14px、占位文 `Search here…`，focus 时 2px 主色 ring。
- 右：一排 40×40 icon button（主题切换、消息气泡、铃铛 with 小红点）+ 圆形头像（紧贴通知铃铛）。
- 右侧第二批：下拉筛选 `Month ▾` + 主按钮 `Export ▾`（实心 `#4F6BFF`，white text，14px，圆角 10px，左侧 download icon）。

## 6. KPI / 指标卡（核心）
- 卡宽自适应网格（4 列各占 1/4），卡体高 132px 左右，padding 20。
- 头部：`标题（小写 14px #6B7280）` 左侧 + `⋯` 24×24 icon button 右侧。
- 主体：大数字（36–44px #1A2233 tabular）+ 紧贴一行的变化徽章：`↗ +20.1%`（绿）/ `↘ -10%`（红）/ `+2,123 today`（灰小字）。
- 底部右侧：`View Report →` 14px 主色文字按钮。
- **可叠加迷你图**：卡片右上角嵌入 80×32 sparkline 折线图，深浅蓝色渐变填充，发卡圆点强调末尾。
- 整张卡 hover：阴影加深，过渡 200ms ease-out。

## 7. 图表区
- **柱状图（Revenue）**：圆角 8px 的柱子，主蓝+浅蓝双系列；最右一根略深（强调当月），底部 x 轴小字月份标签，图例 `● Profit / ● Loss` 居右上。
- **环形图（Traffic Channel）**：双环，外环分段彩色，中心显示大数字 `1.05` + 副字 `Average range`；外侧发卡标注百分比 `11% / 24% / 39%`。
- **状态环（Status Attendees）**：外圈刻度线形式 `1042` + 中间 `1042 Total Status Attendees`，下方 `832 ↗ 79%` + `210 ↗ 21%` 双小指标。
- 所有图表统一 16px 圆角面板，padding 20–24，无轴线，**只有浅灰虚线 gridline** `#F1F3F9` 横向。

## 8. 列表 / 表格
- 表格卡：白底 + 1px `#EEF0F5` 边框 + 16px 圆角。
- 顶部工具条：左侧大标题，右侧一排图标按钮 + 主按钮（`+ Add Location`）：
  - 图标按钮：`Search / Columns / Density / Filter / Export`，统一 36×36 圆角 10px `#F4F6FF` hover `#E8EDFF`，icon 16px。
  - 主按钮右对齐实心蓝紫。
- 选中状态条：选中后顶部出现浅蓝高亮提示条 `1 Attendees Selected` + 多动作小按钮组（邮件、打印、放大、刷新、撤销）+ 右侧 `Check In` 蓝按钮 + `Delete` 红字按钮。
- 列头：可排序字段右侧 8px caret 大小标，上下箭头，hover 高亮行。
- 行：
  - 复选框列 32px 宽。
  - **「双行单元格」**：圆形 32px 头像 + 主名（粗） + 邮箱（次灰 13px）。
  - 状态胶囊：`Member` 绿、`Signed Up` 蓝、`New Customer` 黄、`Verified` 绿、`Replication Needed` 红、`Code Suspended` 红，全部为 `padding 2 10 / font 12 / radius 999`。
  - 进度：圆点 + 百分比 `60%`，以纯文字 + 竖条图示呈现，避免彩色干扰。
  - 金额右对齐，tabular-nums，色 `#1A2233`。
- 行 hover 整行变 `#F8FAFF`，左侧 3px 主色边条。
- 底部：左侧 `Showing 12 of 150`，右侧 `Prev / 1 / 2 / 3 / … / Next` 分页。

## 9. 浏览器外壳装饰（可选）
- 若要画 Dribbble 风样板图，可在外层套一个 macOS 浏览器壳：顶部 36px 白条 + `🔴 🟡 🟢` 圆点 + `< / >` 导航键 + 中间地址栏（`⬤ crowpass.com/attendance`）+ 右侧刷新、分享、`+`、双窗口键。
- 整张图外缘 24px 圆角，深阴影贴地。

## 10. 微交互
- hover：阴影/底色 200ms `ease-out`。
- 数字变化：用 `tabular-nums`，避免抖动。
- 加载：所有指标卡圆角 8px 浅灰 `#F1F3F9` shimmer 骨架占位。
- 空状态：插画 + `No data yet` 居中。

## 11. 交付物要求（v0 / Cursor / Claude Artifacts）
- 单页 React/Vue/HTML+CSS 皆可，**禁止引入 chart.js / echarts 等重型库**；图表用纯 SVG 写。
- 提供 4 个并排场景演示：
  1. **Dashboard**（带 KPI+柱图+环形图+Recent Activity）
  2. **Events 列表**（带日历/状态环）
  3. **Locations 表格**（带搜索+列控制+分页+状态胶囊）
  4. **Staff List 表格**（带头像双行+工作日圆点组+服务胶囊）
- 全站 CSS 变量集中在 `:root`，命名与上文 Token 对齐。
- 不需要暗色模式首版；预留 `prefers-color-scheme` 切换 hook 即可。

## 12. 一句话精简版（贴进 v0 / Stitch 输入框）
> Modern light-themed SaaS admin dashboard with a 240px left sidebar (linear icons + pill highlight), 24px-radius white floating panel on a soft lavender→white gradient, Inter font, primary `#4F6BFF`. Top bar: big title + centered search + icon buttons + avatar + `Month` selector + blue `Export` button. KPI cards: 4-column grid with large tabular numbers, green↑ / red↓ trend chips, mini sparkline top-right, `View Report →` link. Charts: rounded bar chart, donut with center metric, status ring. Data table: white card, icon toolbar (Search/Columns/Density/Filter/Export) + `Add` primary button, selection banner, dual-line cell with 32px avatar + email, status pills (Member/Signed Up/Verified/…), zebra-hover rows, pagination. Soft multi-shadow, generous whitespace, 12–24px corner radius system, no dark mode.

---

*附：本工作台「设计参考」面板已内置这 4 个场景的可交互预览（点击在面板内打开 `design-prototypes.html`），并复用以上设计 Token。*
