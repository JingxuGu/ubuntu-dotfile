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

## 保留 IBus 时的 Kitty 中文输入

GNOME 默认 IBus 拼音可继续使用，不需要迁移至 Fcitx5。Kitty 0.21.2 在 X11/XWayland 下需要在启动进程前设置 `GLFW_IM_MODULE=ibus`，否则输入法服务即使正常运行，Kitty 也不会建立 IBus 输入连接。`kitty.conf` 中的 `env` 用于子进程，不能替代该启动环境变量。[Kitty 官方说明](https://sw.kovidgoyal.net/kitty/glossary/#envvar-GLFW_IM_MODULE)

可先从支持中文的终端启动验证：

```bash
GLFW_IM_MODULE=ibus /usr/bin/kitty
```

永久设置提供独立启动器，不改动输入法来源、切换快捷键、Bash 或终端外观。在仓库根目录执行；已有同名文件时先备份：

```bash
install -Dm755 dotfile/ubuntu-22.04-gnome/launchers/kitty-ibus ~/.local/bin/kitty
install -Dm644 dotfile/ubuntu-22.04-gnome/launchers/kitty-ibus.desktop \
  ~/.local/share/applications/kitty.desktop
update-desktop-database ~/.local/share/applications
```

命令行需保证 `~/.local/bin` 位于 `/usr/bin` 之前；`Super+T` 等自定义快捷键的命令应使用启动器的完整路径（例如 `/home/你的用户名/.local/bin/kitty`）。应用菜单由用户级 `kitty.desktop` 显式设置变量，不依赖桌面进程的 PATH。

从应用菜单或快捷键重新打开 Kitty 后测试拼音选词；已打开的进程需要保留工作并另开窗口，重载配色无法重新初始化输入法连接。不要在这个旧版本里将 `ibus address` 输出直接写入 `IBUS_ADDRESS`：Kitty 0.21 的实现将该变量当作地址文件路径，通常应让它自动读取 `~/.config/ibus/bus/`。

本机在 GNOME 42 Wayland + Kitty XWayland 下验证：键入 `ni` 并按空格，终端实际收到“你”，调试日志显示 `Connected to IBUS daemon` 和 `CommitText`。
