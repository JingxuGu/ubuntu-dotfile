# Ubuntu 26.04 软件包状态

声明入口：`ansible/vars/ubuntu-26.04-niri.yml`，共用包在 `ansible/roles/packages/defaults/main.yml`。

| 类型 | 软件 |
| --- | --- |
| 共用 apt 软件 | Kitty、Zsh、Fcitx5/Rime、Noto 字体、Git、Python 等 |
| Niri apt 软件 | niri、dms、matugen、fuzzel、fastfetch、starship、grim、slurp、wl-clipboard、Satty 运行库 |
| 上游发布与资源 | Nerd Font、Satty、壁纸插件、Kirie/Haru、Wallpaper Engine 素材 |

原机器的 niri/Matugen 来自 `ppa:avengemedia/danklinux`，DMS 来自 `ppa:avengemedia/dms`。迁移前确认目标 Ubuntu 26.04 的相应来源可用并已配置，Ansible 不会替你信任或添加这些源。状态使用 present，复用当前可用版本，不强制全量升级到最新；如需固定软件版本，显式将包名写为 name=version。

Ansible 的 --check 不会安装包。原始快照里的安装脚本仅用于明确选择的额外组件，不会在 chezmoi apply 时自动执行。
