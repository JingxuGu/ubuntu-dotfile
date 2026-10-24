# 仓库验证

结构迁移只在仓库、临时主目录和 GSettings 内存后端验证，不把另一套系统的配置应用到当前桌面。

```bash
# 来源快照完整性、临时目录恢复、chezmoi 两系统渲染及设备差异
CHEZMOI="$(command -v chezmoi)" python3 -m unittest discover -s tests -v

# 保留的 GNOME 备份/撤销与恢复测试，使用内存 GSettings
GSETTINGS_BACKEND=memory /usr/bin/python3 -m unittest discover \\
  -s dotfile/ubuntu-22.04-gnome/tests -v

cd ansible
ansible-playbook -i localhost, -c local site.yml \\
  -e profile=ubuntu-26.04-niri --syntax-check
ansible-playbook -i localhost, -c local site.yml \\
  -e profile=ubuntu-22.04-gnome --syntax-check
```

chezmoi 渲染测试在没有安装 chezmoi 时会跳过；应提供真实二进制来完成验证。测试检查系统之间的隔离、设备参数替换、重新初始化参数保留、自动取色文件的 create-only 行为，以及迁移文件与原始提交逐字节一致。

GNOME 使用当前机器可用的 schema 做类型与备份/撤销测试，这不等于对 Ubuntu 22.04 GNOME 42 的实际窗口、扩展渲染和输入法体验验证。Ansible 只做语法检查；实际软件源和安装状态需在目标系统先运行 --check。
