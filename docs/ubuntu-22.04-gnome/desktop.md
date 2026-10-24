# GNOME 桌面与毛玻璃配置项

配置位置：`dotfile/ubuntu-22.04-gnome/gnome/settings.json`。工具 `gnome.py` 按类型和值范围检查 schema，缺少可选 Dock schema 时跳过。

| 配置项 | 当前值及作用 |
| --- | --- |
| org.gnome.desktop.interface.color-scheme | prefer-dark |
| gtk-theme / icon-theme / cursor-theme | Yaru-dark / Yaru-dark / Yaru |
| clock-format / clock-show-weekday | 24h / true |
| show-battery-percentage | true |
| enable-hot-corners | false |
| org.gnome.mutter.dynamic-workspaces | true |
| edge-tiling | true |
| Dash to Dock dock-position / extend-height | BOTTOM / false |
| dash-max-icon-size | 40 |
| dock-fixed / intellihide | false / true |
| show-trash | false |
| Super+T | 追加 Kitty 自定义快捷键，保留其他自定义绑定 |
| Super / Super+Space / Super+S | GNOME 概览和搜索 |
| Super+Q / Alt+F4 | 关闭窗口 |
| Super+Up / Super+Down | 最大化 / 取消最大化 |

## Blur my Shell

可选扩展 Blur my Shell 的 GNOME 42 兼容版本为 v47、version_tag 42627。单独的效果配置位于 `gnome/blur-my-shell.json`，不会重新应用基本主题或快捷键。

| 配置项 | 值 |
| --- | --- |
| panel.blur / customize | true / true |
| panel.sigma / brightness | 30 / 0.8 |
| panel.static-blur / override-background | true / true |
| panel.unblur-in-overview | true，避免重复模糊 |
| overview.blur / customize | true / true |
| overview.sigma / brightness | 40 / 0.65 |
| appfolder、applications、dash-to-dock、screenshot、lockscreen、window-list blur | false |

安装和应用：

```bash
curl -fL 'https://extensions.gnome.org/download-extension/blur-my-shell@aunetx.shell-extension.zip?version_tag=42627' \
  -o /tmp/blur-my-shell-v47.zip
gnome-extensions install /tmp/blur-my-shell-v47.zip
/usr/bin/python3 dotfile/ubuntu-22.04-gnome/gnome.py \
  --config dotfile/ubuntu-22.04-gnome/gnome/blur-my-shell.json
# 检查预览后添加 --apply
```

工具保留其他扩展清单，只追加目标扩展。Wayland 首次安装后注销再登录，让 GNOME Shell 发现扩展。`gnome-extensions info blur-my-shell@aunetx` 可查看状态。原分支没有启用应用窗口模糊，因此不宣称 Kitty 在 GNOME 上具备 Niri 的背景模糊。
