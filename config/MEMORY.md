# User-Level Memory

## 跨项目偏好

### AI 产物存放路径（强制）
- **所有 AI 生成的 SVG/HTML/PDF 产物必须写入 `~/.workbuddy/ai-artifacts/`**
- 不要写入工作区临时目录，统一归档到此路径
- 产物按主题分子目录存放
- **该目录已是 git repo，托管在 GitHub**
- 每次操作前必须 `git pull` 刷新；有冲突时需用户介入解决
- 每次操作后必须 `git add && git commit && git push` 推送到远端

### 图表绘制偏好
- 默认使用 baoyu-diagram 技能
- 浅色主题（白底 + 彩色节点 + 清晰边框）
- 对称布局、准确箭头

### 沟通风格
- 简洁直接，厌恶废话
- 高度结构化输出（表格、对比分析）
- 偏好渐进式修改，反对完全重写
