# 打造 MacOS/Linux 优雅终端

## 1. Zsh

Zsh 是公认的终极 Shell，其因强大的补全功能、高度的可定制性以及良好的扩展性，被众多开发者极力推崇。

如今，因为 WSL 的出现，Windows 的用户也可享用这一福利了。

推荐使用 Homebrew 安装，详见 [cmd_homebrew]。

```bash
# 安装 Zsh
brew install zsh
```

### 1.1. 主题

Starship 是由 Rust 编写的跨平台命令行主题，简单、高效、容易配置。

```bash
brew install starship
```

### 1.2. 配置

打开`~/.zshrc`，添加：

```bash
# 导入 bash 配置
source ~/.bash_profile
# linux
# source ~/.bashrc

# 别名
alias ua="unalias"
alias py="python"
alias man="tldr"
alias bat="cat"
alias find="fd"

# 引入环境变量
export PATH = "/usr/local/share/npm/bin:$PATH"
export PATH = "/usr/local/opt/ruby/bin:$PATH"
export PATH = "/usr/local/opt/sqlite/bin:$PATH"
```

## 2. Zsh 扩展

Zsh 有很好的扩展性，这里推荐 3 个最常用的扩展

- zsh-autosuggestions（补全提示）
- zsh-syntax-highlighting（高亮）
- zsh-completions（补全）

### 2.1. 安装

首先安装链接扩展

```bash
brew install zsh-autosuggestions zsh-syntax-highlighting zsh-completions
```

也可以选择源码安装

```bash
# zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
# zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
# zsh-completions
git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/plugins/zsh-completions
```

### 2.2. 整合

在 `~/.zshrc` 中添加：

```bash
plugins=(zsh-autosuggestions zsh-syntax-highlighting zsh-completions)

source /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

autoload -U compinit && compinit
```

### 2.3. 大小写敏感

```bash
echo "set completion-ignore-case On" >> ~/.inputrc
```
