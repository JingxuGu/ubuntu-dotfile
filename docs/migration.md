# 从版本分支迁移到目录

`main` 是唯一维护入口。系统版本通过 `dotfile/` 的目录和 chezmoi/Ansible 的 `profile` 区分；功能修改才使用开发分支。

| 原位置 | 新位置 |
| --- | --- |
| main 的 `home/`、`snapshot.json`、`restore.py` | `dotfile/ubuntu-26.04-niri/` |
| main 的 `fonts/`、`patches/`、`plugins.json`、`theming/dms/` | `dotfile/ubuntu-26.04-niri/` 内的同名路径 |
| `ubuntu-22.04-gnome` 分支全部配置、GNOME 工具和测试 | `dotfile/ubuntu-22.04-gnome/` |
| 原 README、终端和自动取色说明 | 根 README 与 `docs/<profile>/` 的配置项条目 |

来源提交记录在 `systems.json`。Niri 来源 `01a067dc7679ccb35bde7ca487d2d3c03577fdb5`，GNOME 来源 `af9db74845e5f49ee949db45bbb41a3de1b997e9`。原始配置字节保留，原有许可证统一放在 `licenses/`。迁移提交同时引用两个分支的提交历史，不重写既有历史。

旧 GNOME 分支保留作历史参考，不再作为另一个受维护的版本入口。仓库重排、模板渲染和验证只在仓库或临时目录完成，不对当前桌面执行 Ansible 安装或 chezmoi apply。
