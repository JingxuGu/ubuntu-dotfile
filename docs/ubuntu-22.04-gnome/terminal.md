# GNOME 终端与字体配置项

快照根目录：`dotfile/ubuntu-22.04-gnome/home/`。

| 文件 | 配置项 | 当前值及作用 |
| --- | --- | --- |
| .config/kitty/kitty.conf | font_family / font_size | JetBrainsMono Nerd Font Mono / 12 |
| 同上 | background_opacity | 0.65 |
| 同上 | window_padding_width | 8 点 |
| 同上 | linux_display_server | x11，兼容 Jammy Kitty 0.21 与 Fcitx5；Wayland 会话下使用 XWayland |
| 同上 | hide_window_decorations | no，保留 GNOME 窗口装饰 |
| 同上 | include | colors.conf，固定配色，不依赖 DMS |
| 同上 | shell | /usr/bin/zsh -l |
| .zshrc / .config/starship.toml | 初始化与提示符 | 原生补全、历史、目录/Git/Python/Conda/耗时；缺少 Starship 时可启动普通 Shell |
| .config/fastfetch/config.jsonc | logo、模块 | ASCII Ubuntu 标志、Nerd Font 图标、对齐分隔符 |

Nerd Font 从上游发布页安装到 ~/.local/share/fonts，执行 fc-cache -f。字体选择、字号和透明度可通过 chezmoi 的本机数据调整。Starship/Fastfetch 是可选上游软件，不把它们当作 Jammy 官方 apt 包。

本方案不使用 Niri layer/window-rule、DMS 动态主题、Fuzzel 或 Satty。Kitty 的透明度不自动带来窗口背景模糊。修改字体和透明度后重新开窗确认。

## Kitty 毛玻璃背景

GNOME 42 可使用已安装并启用的 Blur my Shell v47 为 Kitty 添加背景模糊，具体步骤见[桌面配置](desktop.md#kitty-窗口背景模糊)。保留 `background_opacity 0.65` 和 `linux_display_server x11`；扩展使用 `opacity=255` 保持窗口内容不额外变淡。无需修改当前 Bash、字体、输入法或输入法快捷键。

窗口类别必须与扩展白名单一致，普通 Kitty 使用 `kitty`，配置也兼容 `Kitty`。使用 `kitty --class 自定义名称` 的窗口需要将该类别加入白名单。可用 `xprop WM_CLASS` 后点击 Kitty 查询。
