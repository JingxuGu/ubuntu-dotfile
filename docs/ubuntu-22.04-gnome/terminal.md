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
