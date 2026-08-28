# 栩婷的工作台 · PM 成长知识库

> 一个 **纯前端、零构建** 的个人产品经理成长工作台：把面试经验、方法论、AI Native 实践沉淀成可检索的知识库，按「公司 + 岗位」分类，支持组合筛选。

## 🚀 直接访问（点击即进入工作台）

👉 **https://zxt1223.github.io/pm-growth-workspace/**

（GitHub Pages 自动部署，仓库根目录 `index.html` 即应用本体，无需 `npm install` / 构建。）

## 📦 这是什么

- **形态**：单文件 `index.html` 应用（数据内联，打开即用）。
- **定位**：PM 面试 / 方法论 / AI Native 产品实践的个人知识库。
- **筛选维度**：`公司（字节 / 腾讯 / 美团 / 阿里 …）` × `岗位 / 主题（经验贴 / 面试 / 产品方法论 / AI Native …）`，支持「只看某公司 / 只看某岗位 / 某公司某岗位」组合。

## 🗂 内容结构

| 维度 | 覆盖 |
|---|---|
| 公司 | 字节跳动、腾讯、美团、阿里 |
| 主题 | 经验贴、面试、产品方法论、AI Native 产品方法论 |
| 形态 | 经验沉淀、面经、方法论知识贴、思维训练题 |

最新提交示例：`AI Native 产品 vs 传统 AI+产品方法论` 知识贴、`字节跳动 AI 产品经理面试经验贴（已 offer）` 等。

## 🛠 本地运行 / 部署

```bash
# 1. 克隆
git clone https://github.com/zxt1223/pm-growth-workspace.git
cd pm-growth-workspace

# 2. 本地预览（任选其一）
#    - 直接用浏览器打开 index.html
#    - 或起一个静态服务
python -m http.server 8000   # 然后访问 http://localhost:8000
```

部署：推送到 `main` 分支后，GitHub Pages 自动更新，无需额外构建步骤。

## ⚠️ 维护约定

- **只增不删**：迭代时仅做优化，不删除已有经验贴 / 数据。
- 新增内容请按「公司 + 岗位 / 主题」归类，确保筛选器可命中。

## 📄 仓库文件

| 文件 | 说明 |
|---|---|
| `index.html` | 工作台主应用（知识库本体） |
| `design-prototypes.html` | 设计原型参考 |
| `ui-design-prompt.md` | UI 设计提示词 |

---

仓库地址：https://github.com/zxt1223/pm-growth-workspace
