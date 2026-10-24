# 壁纸自动取色

当前终端配色由 **DMS 1.6.2 + Matugen 4.2.0** 从壁纸生成。Kitty 的字体、背景不透明度和按键设置独立保存在 `kitty.conf`，配色由其中的 `include dank-theme.conf` 加载。

## 自动生成流程

1. 在 DMS 中选择壁纸；使用视频或 Wallpaper Engine 时，壁纸插件生成一张静态截图。
2. DMS 的动态主题收到壁纸变化，调用 `dms matugen queue`，传入取色图片和当前明暗模式。
3. Matugen 提取 Material 配色，DMS 提供适用于终端的 `dank16` 调色板。
4. Kitty 模板生成 `~/.config/kitty/dank-theme.conf` 和 `dank-tabs.conf`。
5. Kitty 加载生成的颜色。已有窗口可按 `Ctrl+Shift+F5` 重载，新窗口直接使用新配色。

壁纸插件的 `generateStaticWallpaper=true` 已包含在仓库的 `home/.config/DankMaterialShell/plugin_settings.json`。当前两个壁纸插件的这一选项均已开启；DMS 配置中的 `currentThemeName` 和 `currentThemeCategory` 均为 `dynamic`。

## 保存的配置和模板

| 路径 | 作用 |
| --- | --- |
| `home/.config/DankMaterialShell/settings.json` | 动态主题选择和桌面设置 |
| `home/.config/DankMaterialShell/plugin_settings.json` | 动态壁纸截图取色设置 |
| `plugins.json`、`patches/dms-mpvpaper.patch` | 壁纸插件固定提交及本地补丁 |
| `theming/dms/matugen/configs/kitty.toml` | Kitty 模板的输入、输出路径映射 |
| `theming/dms/matugen/templates/kitty.conf` | 背景、前景、光标、选区和 16 色模板 |
| `theming/dms/matugen/templates/kitty-tabs.conf` | 标签栏配色模板 |
| `theming/dms/pipeline.json` | DMS/Matugen 版本、源文件位置与校验值 |
| `home/.config/kitty/dank-theme.conf` | 当前壁纸生成的颜色快照 |

`theming/dms/` 的模板是本机 DMS 内置模板的源码快照，用来保存和核对自动取色逻辑。运行时由安装好的 DMS 使用其内置模板；这些参考文件不由 `restore.py` 写入系统目录。当前机器没有额外的 `~/.config/matugen/config.toml` 覆盖。

模板中的 `SHELL_DIR` 和 `CONFIG_DIR` 由 DMS 在生成时解析；模板还使用 DMS 提供的 `dank16` 变量。因此不要把这些占位路径原样当作独立 Matugen 用户配置执行。

## 在另一台机器恢复

安装兼容版本的 DMS、Matugen 和 Kitty，然后按主 README 恢复配置。启用 DMS 动态主题，并在 DMS 中重新选择本机可用的壁纸。使用动态壁纸时，还需恢复相应壁纸插件和渲染器依赖。

运行 DMS 的环境不要设置 `DMS_DISABLE_MATUGEN=1` 或 `true`，否则自动取色会被禁用。壁纸素材、生成截图缓存和 DMS 启动器搜索历史不打包进仓库。

确认换壁纸后 `~/.config/kitty/dank-theme.conf` 的内容或修改时间已更新，再新开 Kitty 或按 `Ctrl+Shift+F5` 检查颜色。自动取色不会修改 `font_size`、`font_family` 或 `background_opacity`；它们仍由 `kitty.conf` 管理。

以上 DMS 内置模板保留其上游 MIT 许可，见 `licenses/dms-LICENSE`。
