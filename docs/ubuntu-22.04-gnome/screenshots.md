# GNOME 截图配置项

配置位置：`dotfile/ubuntu-22.04-gnome/gnome/settings.json` 的 org.gnome.shell.keybindings。

| 快捷键 | 设置与功能 |
| --- | --- |
| F1 / Print | show-screenshot-ui，GNOME 42 原生截图/录屏界面 |
| Shift+Print / Ctrl+Print | screenshot，直接全屏截图 |
| Alt+Print | screenshot-window，直接当前窗口截图 |

原生界面支持区域、窗口、全屏和录屏；截图保存至图片目录下的 Screenshots 并复制到剪贴板。需要绘图标注时另用图片编辑器，本方案没有安装 Niri 的截图脚本、grim/slurp 或 Satty。

通过 gnome.py 预览并应用设置。设置修改前的 GSettings 值会保存到用户状态目录，以便 --undo 撤销。
