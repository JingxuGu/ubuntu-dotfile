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

工具保留其他扩展清单，只追加目标扩展。Wayland 首次安装后注销再登录，让 GNOME Shell 发现扩展。`gnome-extensions info blur-my-shell@aunetx` 可查看状态。上面的历史配置关闭应用窗口模糊；Kitty 可另行应用下面的配置。

## Kitty 窗口背景模糊

配置位置：`dotfile/ubuntu-22.04-gnome/gnome/kitty-blur.json`。适用于 Ubuntu 22.04、GNOME 42、Blur my Shell v47 与 Kitty 0.21 的 X11/XWayland 窗口。它只管理扩展的应用窗口模糊选项及启用状态，不修改主题、Dock、Shell、输入法或快捷键。

| applications 配置项 | 值及作用 |
| --- | --- |
| blur / customize | true / true，启用独立参数 |
| sigma / brightness | 30 / 1.0，模糊半径与亮度 |
| enable-all / whitelist | false / `['kitty', 'Kitty']`，只匹配 Kitty 窗口类别 |
| opacity | 255，不额外降低窗口内容不透明度，文字保持清晰 |
| blur-on-overview | false，概览中不额外强制显示应用窗口 |

Kitty 自己的 `background_opacity` 必须小于 1，当前配置为 0.65。扩展模糊背景，Kitty 负责背景透明度；仅降低整个窗口的不透明度会让文字一起变淡。

在仓库根目录、当前 GNOME 桌面用户下执行，不加 sudo：

```bash
# 先确认 State: ENABLED、Version: 47
gnome-extensions info blur-my-shell@aunetx

# 预览，再应用；原值会自动备份
/usr/bin/python3 dotfile/ubuntu-22.04-gnome/gnome.py \
  --config dotfile/ubuntu-22.04-gnome/gnome/kitty-blur.json
/usr/bin/python3 dotfile/ubuntu-22.04-gnome/gnome.py \
  --config dotfile/ubuntu-22.04-gnome/gnome/kitty-blur.json --apply
```

然后打开新的 Kitty 窗口，在有图案的壁纸或其他窗口前确认背景被模糊且文字清晰。白名单会替换此前的应用白名单；有其他需要模糊的应用时，先将它们的窗口类别加入配置。不要使用 `enable-all=true` 为所有应用添加透明效果。

已在 Ubuntu 22.04.5、GNOME 42.9 Wayland、Kitty 0.21.2 和 Blur my Shell v47 上验证设置持久化、`WM_CLASS=kitty` 匹配及扩展的实际模糊执行日志。备份、撤销、重复应用及输入法快捷键保留由内存 GSettings 测试覆盖。

如果重新应用上面的 `blur-my-shell.json`，应用模糊会被关闭，需要最后再应用 `kitty-blur.json`。原始快照与整套恢复流程保留原有行为，不会自动启用此选项。

撤销时使用应用命令输出的备份路径，先预览，再加 `--apply`：

```bash
/usr/bin/python3 dotfile/ubuntu-22.04-gnome/gnome.py \
  --undo ~/.local/state/ubuntu-dotfile-backups/<时间>/gnome-settings.json
```
