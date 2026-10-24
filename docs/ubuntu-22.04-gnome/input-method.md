# GNOME 输入法配置项

| 文件或设置 | 作用 |
| --- | --- |
| .xinputrc | im-config 选择 Fcitx5 |
| org.fcitx.Fcitx5.desktop | GNOME 登录后自动启动 Fcitx5 |
| .config/fcitx5/profile | keyboard-us 与 Rime |
| Rime default.custom.yaml | 小鹤双拼优先，保留简体全拼 |
| 小鹤 schema 与 custom.yaml | 键位、默认简体和显示名称 |
| classicui.conf / macOS-dark | Candlelight 候选主题 |
| Ctrl+Space | Fcitx5 中英文切换 |
| GNOME switch-input-source | 清空系统 Super+Space 切换，交由概览使用 |

文件在 `dotfile/ubuntu-22.04-gnome/home/`。输入法恢复后注销并重新登录，在 Fcitx5 菜单重新部署 Rime，或运行：

```bash
mkdir -p ~/.local/share/fcitx5/rime/build
rime_deployer --build ~/.local/share/fcitx5/rime \
  /usr/share/rime-data ~/.local/share/fcitx5/rime/build
```

Kitty 使用 X11/XWayland 以兼容 Jammy 输入法。GNOME 原生 Wayland 程序和 Shell 候选窗仍可能需要额外适配，必要时使用 Ubuntu on Xorg。不会复制 Niri 专属环境配置到 GNOME。
