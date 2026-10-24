# Niri 输入法配置项

| 文件 | 条目 | 作用 |
| --- | --- | --- |
| `.config/fcitx5/profile` | keyboard-us、rime | 英文键盘和 Rime 输入法 |
| `.local/share/fcitx5/rime/default.custom.yaml` | schema_list | 小鹤双拼优先，保留简体全拼 |
| `double_pinyin_flypy.schema.yaml` | simplification.reset | 1，默认简体 |
| `double_pinyin_flypy.custom.yaml` | schema/name | 双拼（小鹤），状态栏简称“双” |
| `.config/fcitx5/conf/classicui.conf` | Theme、DarkTheme | macOS-dark；候选字体 Sans 12 |
| `.config/autostart/org.fcitx.Fcitx5.desktop` | Exec | 登录后启动 Fcitx5 |
| `.xinputrc` 与 Niri environment | Fcitx 环境变量 | GTK/Qt/XIM 接入 |

配置均在 `dotfile/ubuntu-26.04-niri/home/`。Ctrl+Space 切换输入法，Shift 切换中英文。Rime 的 build、sync、学习词库和 installation.yaml 不上传。

系统需提供明月拼音和笔画词库，部署：

```bash
rime_deployer --build ~/.local/share/fcitx5/rime /usr/share/rime-data ~/.local/share/fcitx5/rime/build
```

Candlelight 主题及 Rime 映射的上游许可见根目录 `licenses/`。
