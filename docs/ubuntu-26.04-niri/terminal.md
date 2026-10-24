# Niri 终端与字体配置项

快照根目录：`dotfile/ubuntu-26.04-niri/home/`。

| 文件 | 配置项 | 当前值及作用 |
| --- | --- | --- |
| `.config/kitty/kitty.conf` | font_family | JetBrainsMono Nerd Font Mono |
| 同上 | font_size | 12，chezmoi 的 fontSize 可按设备修改 |
| 同上 | background_opacity | 0.65，只让背景半透明 |
| 同上 | background_blur | 0，模糊由 Niri 提供 |
| 同上 | window_padding_width | 8 点 |
| 同上 | hide_window_decorations | yes |
| 同上 | linux_display_server | wayland，Kitty 原生 GPU 渲染 |
| 同上 | term / COLORTERM | xterm-kitty / truecolor |
| 同上 | shell | /usr/bin/zsh -l |
| 同上 | include | dank-theme.conf，读取 DMS 动态配色；dank-tabs.conf 当前没有引入 |
| `.zshrc` | compinit、历史记录 | 原生补全、10000 条历史、保留已有 PATH 和 Fastfetch |
| `.config/starship.toml` | format | 目录、Git、Python/Conda、耗时、SSH 主机、提示符 |
| 同上 | cmd_duration.min_time | 2000 毫秒 |
| `.config/fastfetch/config.jsonc` | logo | ubuntu-ascii.txt，纯 ASCII Ubuntu 标志 |
| 同上 | separator / key.width | ` > ` / 13，图标与标签对齐；无底部色块 |

字体上游 JetBrains Mono 2.304、Nerd Fonts 3.5.1，16 个字体文件的 SHA-256 与下载地址保存在 `dotfile/ubuntu-26.04-niri/fonts/jetbrains-mono.json`。字体包不入库。安装后执行 `fc-cache -f`、`fc-match 'JetBrainsMono Nerd Font Mono'`。

验证：`zsh -n ~/.zshrc`、`starship --version`、`fastfetch`。字体或透明度调整后重新打开 Kitty；配色可用 Ctrl+Shift+F5 重载。
