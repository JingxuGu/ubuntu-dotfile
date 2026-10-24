# Ubuntu 22.04 与 GNOME

本方案面向 Ubuntu 22.04 LTS、GNOME 42、Mutter 和 Ubuntu Dock，完整保留原 `ubuntu-22.04-gnome` 分支的配置、GSettings 备份撤销工具及测试。它是适配模板，不是对当前 Niri 机器的配置采集。

- [桌面、Dock 与扩展](desktop.md)
- [终端与字体](terminal.md)
- [输入法](input-method.md)
- [截图](screenshots.md)
- [软件包状态](packages.md)

主目录文件由 chezmoi 选择 `ubuntu-22.04-gnome` 后部署。GNOME 设置单独预览并应用：

```bash
/usr/bin/python3 dotfile/ubuntu-22.04-gnome/gnome.py
/usr/bin/python3 dotfile/ubuntu-22.04-gnome/gnome.py --apply
```

也保留整套快照恢复：

```bash
/usr/bin/python3 dotfile/ubuntu-22.04-gnome/restore.py --gnome
/usr/bin/python3 dotfile/ubuntu-22.04-gnome/restore.py --apply --gnome
```

在目标用户的 GNOME 桌面会话中运行，不加 sudo；需要 python3-gi。工具先验证 schema/键/范围，再备份修改项。撤销先预览，再添加 --apply：

```bash
/usr/bin/python3 dotfile/ubuntu-22.04-gnome/gnome.py --undo \
  ~/.local/state/ubuntu-dotfile-backups/<时间>/gnome-settings.json
```

迁移源码及已有测试位于 `dotfile/ubuntu-22.04-gnome/`，本次仓库重构不会自动执行桌面设置命令。
