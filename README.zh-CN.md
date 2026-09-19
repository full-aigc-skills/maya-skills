# maya-skills

**Maya AIGC 技能** — 诊断/检查/Playblast 导出预览/工作流路由。本包包含 **4 个技能**。

当前版本：`v1.0.1`。全部技能包含渐进式 references 与可执行场景示例，确定性 TRACE 基分均为 `4.65`。

## 📦 安装

```bash
npx skills add full-aigc-skills/maya-skills
```

## 🎯 技能列表 (4)

| 技能 | 描述 |
|------|------|
| `maya-diagnose` | 诊断 Maya 插件失败：分类 MAYA_NOT_FOUND / MODULE_ERROR / SYNTAX / RUNTIME |
| `maya-inspect` | 只读检查已授权 Maya 场景，生成包含摄像机/回放/当前形状的场景回执 |
| `maya-export-preview` | 从授权 Maya 场景导出 Playblast 预览，含编解码器/帧率/尺寸/SHA-256 |
| `maya-use` | 路由器：把请求分发到最窄的 Maya 工作流 |

## 🤖 支持的智能体

Claude Code / Codex / Cursor / OpenCode / Gemini CLI / GitHub Copilot / Windsurf 等。

## 📄 License

Apache 2.0

## ✅ 发布门禁

```bash
python3 scripts/lint_skills.py
python3 scripts/generate_quality_resources.py
python3 scripts/trace_gate.py --evaluator <trace_evaluate.py> --threshold 4.5
```

完整结果见 [TRACE_EVALUATION.md](TRACE_EVALUATION.md)。
