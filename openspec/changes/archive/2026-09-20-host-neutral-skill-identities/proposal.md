## Why

`maya-inspect` 仍引用早期 Codex 专用身份，与当前 `maya-design` 回执和宿主无关的技能发布模式不一致。

## What Changes

- 将当前技能正文中的 Dreamina 3D 与 Maya 公共身份改为宿主无关名称。
- 增加回归测试并发布 patch 版本。

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `host-neutral-skill-identity`: Maya 技能只公开宿主无关的跨插件身份。

## Impact

影响 `maya-inspect`、测试、README 版本与 manifest patch 版本；不改变 Maya 执行行为。
