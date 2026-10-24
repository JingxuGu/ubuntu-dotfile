# Ubuntu 22.04 软件包状态

声明入口：`ansible/vars/ubuntu-22.04-gnome.yml`。共用包在 packages role 的 defaults 中。

| 类型 | 内容 |
| --- | --- |
| 共用 apt 软件 | Kitty、Zsh、Git、Python/GI、Fcitx5/Rime、Noto 字体等 |
| GNOME apt 软件 | GNOME Shell、Control Center、Ubuntu Dock、扩展首选项、Yaru、GTK2 输入法前端 |
| 可选上游软件 | Starship、Fastfetch、Nerd Font、GNOME 42 兼容的 Blur my Shell v47 |

目标使用标准 Ubuntu Desktop 的 GNOME 会话。先启用 Jammy 的 universe 软件源，再运行 Ansible --check。Ubuntu 22.04 官方仓库没有 Starship/Fastfetch；按上游发布说明安装支持 Jammy 的版本，Shell 对缺少这些组件有保护。没有管理其他桌面的软件包状态，不会自动卸载已存在的 Niri。

常用验证：`zsh -n ~/.zshrc`、`fc-match 'JetBrainsMono Nerd Font Mono'`、Fcitx5 的 Rime 重新部署，以及在 GNOME 会话中预览 gnome.py。未经目标 GNOME 42 的实际验证，不把当前 Niri 机器上的渲染测试当作 GNOME 验证。
