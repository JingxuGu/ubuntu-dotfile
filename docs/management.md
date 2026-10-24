# 配置管理方式

## 三层职责

| 层 | 维护内容 | 不负责的内容 |
| --- | --- | --- |
| `dotfile/<profile>/` | 原始快照、恢复清单、GNOME GSettings 工具、字体及主题来源 | 不安装系统软件 |
| `chezmoi/` | 主目录文件模板、系统选择、设备参数 | 不运行 apt，不自动修改 GSettings |
| `ansible/` | 软件包存在或移除的声明 | 不覆盖主目录配置，不切换用户默认 Shell |

常规配置变更先更新 chezmoi 模板。需要发布新的原始快照时，重新导出对应的 `dotfile/<profile>/home/` 并更新 `snapshot.json`；不要将缓存、词库或搜索历史导入模板。

## Chezmoi 系统与设备选择

仓库根目录 `.chezmoiroot` 指向 `chezmoi/`。用已有克隆初始化：

```bash
chezmoi --source "$PWD" init
chezmoi edit-config
chezmoi diff
chezmoi apply
```

初始化必须显式选择 `ubuntu-26.04-niri` 或 `ubuntu-22.04-gnome`。同一份源树按 `profile` 选择 `.chezmoitemplates/` 中的方案，并忽略另一个系统专属的目录；没有 `exact_` 或自动删除另一个系统文件的操作。

本机参数保存在 chezmoi 用户配置中，可按实际设备修改：

```toml
[data]
profile = "ubuntu-26.04-niri"
deviceName = "desktop"
fontFamily = "JetBrainsMono Nerd Font Mono"
fontSize = 12.0
opacity = 0.65
monitor = "DP-2"
scale = 1.1
windowRadius = 12
proxyPort = 7897
```

目标主目录从 `.chezmoi.destDir` 自动获取，正常部署默认是当前用户主目录，临时目录验证时则指向测试目录。`monitor`、`scale` 和 `windowRadius` 控制 Niri；字体、字号、透明度适用于两套 Kitty。`proxyPort` 仅用于 Niri 的壁纸包装脚本，不含账户口令。`deviceName` 用作设备标识。

DMS 生成的颜色和布局文件使用 `create_`：首次缺失时提供种子文件，已有文件保留，由 DMS 随壁纸重新生成。这避免重复 `chezmoi apply` 覆盖新取色结果。[chezmoi 属性说明](https://www.chezmoi.io/reference/source-state-attributes/)

## Ansible 软件状态

先进入 `ansible/`，并在目标 Ubuntu 上执行：

```bash
ansible-playbook -i localhost, -c local site.yml \
  -e profile=ubuntu-22.04-gnome --check --diff --ask-become-pass
# 检查结果符合预期后去掉 --check，执行安装/显式移除
```

远程设备可复制 `inventory.example.yml`，修改示例地址、用户名和方案，然后限制目标：

```bash
ansible-playbook -i inventory.yml site.yml --limit gnome-laptop --check --diff --ask-become-pass
```

`common_packages_present` 是共用软件，`desktop_packages_present` 按系统选择，设备可用 `extra_packages_present` 增加软件。`packages_absent` 默认空，只移除明确列出的包，不 purge、不 autoremove、不隐式升级所有软件。执行前校验 Ubuntu 版本，避免把 Niri 的软件列表套到 Jammy。

Ansible 不会自动添加第三方软件源。Niri/DMS/Matugen 需要兼容的已配置软件源；源缺失时先按该方案的软件文档准备。字体、Satty 发布包、GNOME 扩展和壁纸素材属于额外组件，有单独说明；`external_components` 只是记录，不声称由 apt 安装。

## 原始快照恢复与撤销

原有恢复工具移到了各方案目录，默认仅预览：

```bash
python3 dotfile/ubuntu-26.04-niri/restore.py
python3 dotfile/ubuntu-22.04-gnome/restore.py
```

增加 `--apply` 才写入；工具会备份原文件。GNOME 支持 `--gnome` 和 `gnome.py --undo`，详见该方案文档。快照恢复是整套覆盖，日常设备配置优先使用 chezmoi diff/apply。更换账户默认 Shell 仍由用户执行 `chsh -s /usr/bin/zsh`。
