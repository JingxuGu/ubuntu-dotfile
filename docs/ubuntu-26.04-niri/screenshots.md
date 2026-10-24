# Niri 截图配置项

| 按键或配置 | 功能 |
| --- | --- |
| F1 | slurp 选区、grim 截图、Satty 标注 |
| Super+Print | 全屏截图并打开 Satty |
| Super+Shift+Print | Niri 当前窗口截图并打开 Satty |
| Ctrl+Print / Alt+Print | Niri 原生全屏 / 窗口截图 |
| Satty Enter | 保存、复制并退出 |
| Satty Escape | 取消并退出 |

脚本为 `dotfile/ubuntu-26.04-niri/home/.local/bin/screenshot`，编辑器设置在同目录树的 `.config/satty/config.toml`，图片保存至 `~/Pictures/Screenshots/`。

截图脚本在父进程持有 flock 锁；启动 Satty 时关闭子进程的文件描述符 9，避免 wl-copy 在后台继承锁导致后续 F1 失效。Niri 窗口截图异步写入，脚本等待完整 PNG 后才打开编辑器。

Satty 0.22.0 的安装脚本保存在 `.local/bin/install-screenshot-tools`，下载 x86_64 发布包并验证 SHA-256。编辑器二进制和截图内容不入库。
