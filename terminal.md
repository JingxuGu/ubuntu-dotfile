# Kitty 和 Zsh 终端配置

2026 年 10 月 25 日核对的终端配置。实际配置保存在 `home/`，终端文件清单记录于 `snapshot.json` 的 `terminal_files`；字体信息保存在 `fonts/jetbrains-mono.json`。

## 配置文件

| 文件 | 内容 |
| --- | --- |
| `home/.zshrc` | 原生 Zsh 补全、历史记录、PATH、Fastfetch 和 Starship 初始化 |
| `home/.zprofile`、`.profile`、`.bashrc` | 登录环境和 Bash 兼容配置 |
| `home/.config/starship.toml` | 目录、Git 分支及状态、Python 虚拟环境、Conda、耗时和 SSH 主机名 |
| `home/.config/fastfetch/config.jsonc` | 系统信息、Nerd Font 图标、淡蓝紫色标签和对齐分隔符 |
| `home/.config/fastfetch/ubuntu-ascii.txt` | 纯 ASCII Ubuntu 标志，无图片协议依赖 |
| `home/.config/kitty/kitty.conf` | 字体、透明度、padding、Wayland、真彩色和默认 Shell |
| `home/.config/kitty/dank-theme.conf` | 当前 DMS 动态配色快照，已由 Kitty 引入 |
| `home/.config/kitty/dank-tabs.conf` | DMS 生成的标签栏配置快照，当前主配置没有引入 |
| `home/.config/niri/config.kdl` | 含 Kitty 圆角和模糊规则的完整 Niri 桌面配置 |

## 字体

当前字体为 **JetBrainsMono Nerd Font Mono**，上游 JetBrains Mono 版本为 **2.304**，Nerd Fonts 发布版本为 **3.5.1**。仓库记录了本机安装的 16 个字体文件的 SHA-256，字体文件本身不打包进配置仓库。

[下载对应字体包](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.5.1/JetBrainsMono.tar.xz)，将其中 `JetBrainsMonoNerdFontMono-*.ttf` 安装到 `~/.local/share/fonts/JetBrainsMonoNerdFont/`，然后运行：

```bash
fc-cache -f
fc-match 'JetBrainsMono Nerd Font Mono'
```

Kitty 使用 12 号字体，粗体、斜体及粗斜体由字体系统匹配。Nerd Font 图标用于 Fastfetch 系统信息项。

## 透明背景和窗口效果

Kitty 中的主要设置：

```conf
font_family JetBrainsMono Nerd Font Mono
font_size 12.0
background_opacity 0.65
background_blur 0
window_padding_width 8
hide_window_decorations yes
linux_display_server wayland
```

`background_opacity 0.65` 表示背景 65% 不透明。文字维持正常清晰度。模糊由 Niri 的 Kitty 规则实现：

```kdl
window-rule {
    match app-id="^kitty$"
    opacity 1.0
    draw-border-with-background false
    geometry-corner-radius 12
    clip-to-geometry true
    background-effect {
        blur true
        xray true
    }
}
```

`xray true` 使毛玻璃透出模糊后的壁纸。将这段规则合并到另一台机器的现有 Niri 配置时，先检查是否已经存在 Kitty 规则，避免重复。

## Shell 和系统信息

Kitty 明确运行 `/usr/bin/zsh -l`。Zsh 使用原生补全和历史记录，没有 Oh My Zsh 等框架；已有环境配置保留。Starship 使用简洁的单行提示符，命令超过 2 秒才显示耗时，SSH 主机名仅在远程会话中出现。

Fastfetch 仅在连接终端的交互式 Zsh 启动时执行，输出 Ubuntu ASCII 标志和系统信息，不显示底部色块。使用 ` > ` 分隔标签与数值。

## 恢复和验证

依赖：Kitty、Zsh、Starship、Fastfetch、上述字体，以及需要背景模糊时的 Niri 26.04 或更新版本。恢复工具的完整操作见主 README；`restore.py` 会恢复整个桌面快照，默认仅预览，使用 `--apply` 才写入并备份旧文件。只迁移终端时，可按本页文件清单复制相应配置，并将 `/home/grainrain` 路径调整为目标用户主目录。

检查配置和效果：

```bash
zsh -n ~/.zshrc
zsh --version
starship --version
fastfetch
fc-match 'JetBrainsMono Nerd Font Mono'
niri validate
```

新开 Kitty 窗口即可查看字体和 0.65 透明度。DMS 换壁纸后会重新生成配色文件；已有 Kitty 可用 `Ctrl+Shift+F5` 重载配色。透明度调整后重新开窗生效。

## 壁纸自动配色

当前采用 DMS 动态主题与 Matugen 自动从壁纸取色，`dank-theme.conf` 是生成结果，不是固定主题。动态主题设置、生成模板和依赖版本见 [壁纸自动取色说明](theming/README.md) 和 `theming/dms/pipeline.json`。无需用另一个主题工具覆盖 Kitty 配色。
