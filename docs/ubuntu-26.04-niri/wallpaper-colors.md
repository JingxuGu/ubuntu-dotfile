# Niri 壁纸自动取色配置项

DMS 1.6.2 与 Matugen 4.2.0 是这份快照记录的版本。动态取色流程：壁纸变化或插件生成静态截图 → DMS 提交 Matugen 队列 → Material / dank16 调色板 → Kitty 配色文件。

| 文件或条目 | 当前值与作用 |
| --- | --- |
| DMS settings.json 的 currentThemeName / currentThemeCategory | dynamic / dynamic |
| plugin_settings.json 的 generateStaticWallpaper | 两个壁纸插件均为 true，生成取色图片 |
| Kitty `include dank-theme.conf` | 读取动态生成颜色 |
| `dotfile/ubuntu-26.04-niri/theming/dms/` | 已安装 DMS 模板、输入输出映射及 pipeline.json 的源码快照 |
| chezmoi 的 create_dank-theme.conf.tmpl 等 | 仅首次缺失时提供颜色种子，不覆盖 DMS 后续生成结果 |
| DMS_DISABLE_MATUGEN | 不应设为 1 或 true，否则禁用取色 |

DMS 模板使用其提供的 dank16 变量及 SHELL_DIR、CONFIG_DIR 占位路径；参考快照不由 restore.py 覆盖系统 DMS 模板，也不直接当作普通 Matugen 用户配置运行。DMS 更新可以更新内置模板。

恢复对应的 DMS 和 Matugen、插件仓库及配置后，在 DMS 中重新选择本机壁纸。插件固定提交与 mpvpaper 补丁在该方案的 `plugins.json` 和 `patches/`。Kirie/Haru 的二进制、代理库和 Wallpaper Engine 素材需要单独准备；包装脚本里的路径和代理端口需适合当前设备。

确认更换壁纸后 `~/.config/kitty/dank-theme.conf` 内容变化，再新开 Kitty 或按 Ctrl+Shift+F5 重载。字体、字号、0.65 不透明度与配色生成相互独立。缓存截图、原始壁纸及 DMS 搜索历史不入库。
