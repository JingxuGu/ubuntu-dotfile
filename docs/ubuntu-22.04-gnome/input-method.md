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

## 从 IBus 迁移到 Fcitx5 + Rime

可复用 Niri 方案的小鹤双拼、明月全拼与 Candlelight 主题；本系统使用 GNOME 兼容的 `classicui.conf`。迁移顺序为备份、安装、部署、切换与验证，最后再移除旧输入法。备份应包含 `~/.config/ibus`、`~/.cache/ibus` 中的旧学习数据、输入法相关 GSettings 和已有 Fcitx5 配置，不将这些个人数据提交到仓库。

除了共用包中的 Rime、词库和 GTK/Qt 前端，GNOME 软件列表显式包含 `fcitx5-module-xorg`、`fcitx5-module-wayland`，使用 `--no-install-recommends` 安装时也应包含这两个显示模块。

部署本页列出的配置文件并编译 Rime 后，执行 `im-config -n fcitx5` 选择默认框架。chezmoi 的 GNOME 方案还会部署 `~/.config/environment.d/90-fcitx5.conf`，为后续会话设置 GTK/Qt/XIM 和 Kitty 所需的环境；Niri 方案不会部署这个 GNOME 专用文件。

Kitty 可使用以下启动器立即继承新环境，保持字体、Bash 与毛玻璃设置：

```bash
install -Dm755 dotfile/ubuntu-22.04-gnome/launchers/kitty-fcitx5 ~/.local/bin/kitty
install -Dm644 dotfile/ubuntu-22.04-gnome/launchers/kitty-fcitx5.desktop \
  ~/.local/share/applications/kitty.desktop
update-desktop-database ~/.local/share/applications
```

自定义终端快捷键使用 `~/.local/bin/kitty` 的完整路径。GNOME 输入来源中移除旧 IBus 引擎、保留已有 XKB 键盘；GTK 应用需要时可在 `org.gnome.settings-daemon.plugins.xsettings` 的 `overrides` 中合并 `'Gtk/IMModule': <'fcitx'>`，保留其他已有覆盖项。不要为此重新应用整份桌面快照或清空用户原有快捷键。

注销并重新登录后，按 `Ctrl+Space` 切换输入法，`Shift` 切换中英文；Rime 方案菜单可选择小鹤双拼或明月全拼。小鹤编码 `nihc` 应能选出“你好”。`GLFW_IM_MODULE=ibus` 在这里指兼容协议，不需要继续运行 IBus 服务。

确认新框架可用后，单独选择旧包清理清单，先查看计划：

```bash
cd ansible
ansible-playbook -i localhost, -c local site.yml \
  -e profile=ubuntu-22.04-gnome \
  -e @vars/ubuntu-22.04-fcitx5-cleanup.yml --check --diff --ask-become-pass
# 确认仅移除清单中的旧包后，去掉 --check 执行
```

此清单不默认启用，避免在配置和验证前卸载旧输入法。保留 GNOME 必需的 `libibus-1.0-5` 与 `gir1.2-ibus-1.0`；不运行全局 autoremove。卸载完成后再次打开 Kitty 测试输入。

已在 Ubuntu 22.04.5 / GNOME 42.9 Wayland 上完成上述迁移，使用 Fcitx5 5.0.14、Fcitx5-Rime 5.0.11、Rime 1.7.3，并验证 Kitty 0.21.2 的 `Ctrl+Space` 切换及小鹤编码 `nihc` 实际输出“你好”。

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
