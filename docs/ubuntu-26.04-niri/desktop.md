# Niri 桌面与 Fuzzel 配置项

快照根目录：`dotfile/ubuntu-26.04-niri/home/`。

| 配置位置 | 条目 | 当前值及作用 |
| --- | --- | --- |
| `.config/niri/config.kdl` | `layout.gaps` | 8，窗口间距 |
| 同上 | DP-2 `scale` | 1.1，110% 缩放；chezmoi 可按设备设置 monitor/scale |
| 同上 | Kitty `geometry-corner-radius` | 12；`clip-to-geometry true` 裁剪窗口 |
| 同上 | Kitty `opacity` | 1.0，保持文字清晰；背景透明度由 Kitty 控制 |
| 同上 | Kitty `background-effect` | blur=true、xray=true，显示模糊壁纸 |
| 同上 | 快捷键 | Super+T 启动 Kitty；Super+Space 启动 Fuzzel |
| `.config/fuzzel/fuzzel.ini` | background | `24242bbf`，约 75% 不透明深色背景 |
| 同上 | border.radius | 20 像素圆角，细边框与居中布局 |
| Niri launcher layer-rule | blur、xray | true、false，模糊启动器下方的内容；保留阴影 |

Niri 的 `dms/` 子目录为 DMS 生成文件；当前主配置是否引用它们以 `include` 为准，保存这些文件不等于自动启用所有 DMS 布局。快照保留现有 `waybar` 启动项，DMS 软件和会话服务单独管理。

验证：`niri validate`、`fuzzel --check-config`。Niri 配置自动重载，Fuzzel 下次启动读取配置。
