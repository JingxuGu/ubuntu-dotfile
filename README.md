# Ubuntu 桌面配置

所有受维护的系统方案都放在 `main` 的目录中，Git 分支用于开发变更，不再用于区分 Ubuntu 版本。

| 系统方案 | 配置快照 | 配置项条目 |
| --- | --- | --- |
| Ubuntu 26.04 + Niri + DMS | [dotfile/ubuntu-26.04-niri](dotfile/ubuntu-26.04-niri) | [文档](docs/ubuntu-26.04-niri/README.md) |
| Ubuntu 22.04 + GNOME 42 | [dotfile/ubuntu-22.04-gnome](dotfile/ubuntu-22.04-gnome) | [文档](docs/ubuntu-22.04-gnome/README.md) |

Niri 方案来自 Ubuntu 26.04.1 的实际快照；GNOME 方案是原 `ubuntu-22.04-gnome` 分支的适配模板。两者的来源提交记录于 [systems.json](systems.json)。

## 目录职责

```text
.
├── dotfile/                 # 两套原始文件、恢复工具和资源清单
│   ├── ubuntu-26.04-niri/
│   └── ubuntu-22.04-gnome/
├── chezmoi/                 # 两套配置的可部署模板和设备参数
├── ansible/                 # 按系统方案维护软件包 installed/absent 状态
├── docs/                    # Markdown 配置项、使用流程和迁移说明
│   ├── ubuntu-26.04-niri/
│   └── ubuntu-22.04-gnome/
├── licenses/                # 上游许可
└── tests/                   # 结构、渲染和迁移验证
```

## 使用流程

1. 用 Ansible 检查并准备对应系统的软件包。
2. 用 chezmoi 选择系统方案，设置当前设备的显示器、缩放、字体和透明度。
3. 查看 `chezmoi diff` 后应用。GNOME 的 GSettings 由单独的备份工具预览和应用。

```bash
git clone https://github.com/JingxuGu/ubuntu-dotfile.git
cd ubuntu-dotfile

# 软件状态：先检查，不执行安装；Niri 需先配置兼容的软件源
cd ansible
ansible-playbook -i localhost, -c local site.yml \
  -e profile=ubuntu-26.04-niri --check --diff --ask-become-pass
cd ..

# init 会询问选择哪一套系统；不会自动 apply
chezmoi --source "$PWD" init
chezmoi diff
chezmoi apply
```

GNOME 机器将 Ansible 的 `profile` 改为 `ubuntu-22.04-gnome`，chezmoi 中也选择同一方案。不要对同一目标同时应用两个方案。

设备变量与软件源前提见 [管理方式](docs/management.md)，完整配置目录见 [文档索引](docs/README.md)。旧分支只保留为历史参考，日常更新集中在 `main`；本次迁移提交同时包含两个来源分支的历史。

字体包、软件二进制、壁纸素材、历史记录、凭据和输入法学习词库不在仓库中。当前桌面的配置不会因仓库重排自动改变。
