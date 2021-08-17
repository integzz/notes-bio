# 搭建 Python 轻量级编写环境

Windows 下的 Python 环境经常会给人带来一系列的困扰，如，时隐时现的各种因为环境变量导致的奇怪报错，Conda 库更新不到最新的版本，还有诸如 xgboost 等库压根儿就不提供 Win 版等。现在，WSL2（Windows Subsystem Linux 2）的出现，让我们有了一种新的选择。WSL2 是一个 Windows 的内置虚拟机，可运行 Linux 环境，一旦有了 Linux 环境，后面的配置不必多说。

下面仅以 Miniconda 的安装为例，分享一下我自己关于 WSL2 配置的一些经验。

## 1. 安装 WSL2

### 1.1. 开启虚拟机功能

在控制面板 -> 程序和功能 -> Windows 功能窗口中勾选适用于 Linux 的 Windows 子系统 功能，点击确定，并按照提示重启电脑。

![WSL2](images/wsl2/wsl2.png)

或以管理员身份在命令行键入

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

### 1.2. 安装发行版

在 Windows 应用商店搜索 WSL ，选择自己想要的 Linux 发行版，点击下载安装即可。这里选择的是 Ubuntu 20.04。

![Ubuntu](images//wsl2/app.png)

### 1.3. 升级

由于版本问题，好多人的的子系统还停留在 WSL，而不是 WSL2，由于后者实质上是一个虚拟机。故要启动虚拟化：

```powershell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl -l # 查看 WSL 列表
wsl --set-version Ubuntu-20.04 2
```

中间需要下载一个 [WSL2-kernel](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

若之前没有用过 WSL，则首先需要安装 Windows 10 的 WSL 功能：

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

这部分详情见 [WSL2](https://docs.microsoft.com/en-us/windows/wsl/wsl2-kernel)

## 2. Ubuntu

### 2.1. 版本

安装完成后，使用微软自家的 Windows-Terminal 打开一个 Ubuntu 标签，待其初始化完成。通过如下命令查看版本

```powershell
wsl -l -v
```

![WSL2 version](images/wsl2/version.png)

设置 WSL2 为默认版本

```powershell
wsl --set-default-version 2
```

卸载

```powershell
wslconfig /u Ubuntu-20.04
```

### 2.2. 初始化

输入以下命令，为 root 用户设置密码。

```bash
sudo passwd root
```

当然，你也可使用如下命令，创建新用户

```bash
sudo adduser username
```

![Terminal](images/terminal/zsh.png)

### 2.3. 软件源

打开 `sources.list`：

```bash
sudo vi /etc/apt/sources.list
```

更改软件源：

```bash
deb https://http.kali.org/kali kali-rolling main non-free contrib
deb https://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib

deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
```

更新：

```bash
sudo apt update && sudo apt update -y && sudo apt upgrade -y
# 清理缓存
sudo apt -y clean && sudo apt -y autoclean && sudo apt -y autoremove
```

### 2.4. 网络

Powershell 中，管理员执行如下命令

```powershell
New-NetFirewallRule -DisplayName "WSL" -Direction Inbound  -InterfaceAlias "vEthernet (WSL)"  -Action Allow
```

```bash
ip route | grep default | awk '{print $3}'
sudo vi /etc/wsl.conf
[network]
generateResolvConf = false
sudo vi /etc/resolv.conf
nameserver 8.8.8.8
```

### 2.5. 工具链

为了更方便地使用 Linux，墙裂建议安装 Zsh

同时，也推荐安装 Homebrew，相关文章为

此处仅是建议，若觉得 Homebrew 对 Linux 来说纯属鸡肋，权当我没说。

### 2.6. 删除多余的包

```bash
sudo apt remove --purge python3
```

## 3. 安装 Miniconda

### 3.1. 下载安装

```bash
# 下载
wget -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
# 安装
bash Miniconda3-latest-Linux-x86_64.sh
```

### 3.2. 添加镜像

```bash
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/pytorch
```

有关 Conda 的具体使用，这里不再赘述。

## 4. 安装 JupyterLab

第一步非常简单，命令如下

```bash
conda install -c conda-forge jupyterlab
```

关键是第二步，让 JupyterLab 自动打开宿主浏览器。打开配置文件 `jupyter_notebook_config.py` 。

```bash
vi ~/.jupyter/jupyter_notebook_config.py
```

若没有，由如下命令生成

```bash
jupyter notebook --generate-config
```

修改下面这如下一行

```bash
c.NotebookApp.use_redirect_file = False
```

退回到主界面，在 `~/.bashrc` 或 `~/.zshrc` 文件末尾添加，指定默认浏览器地址，其中， `/mnt/` 之后的部分是你默认浏览器的在 Windows 上的地址

```bash
export BROWSER="/mnt/c/scoop/apps/firefox/current/firefox.exe"
# 或
export BROWSER="/mnt/c/'program files (x86)'/microsoft/edge/application/msedge.exe"
```

使用 `source` 刷新后，就可愉快地使用 Linux 版的 Python 了。

![jupyterLab](images/jupyter/python.png)

## 5. 沙雕版 GUI

### 5.1. VcXsrv 的安装和配置

这里，我们选择最省心的 VcXsrv，其下载链接为 [VcXsrv](https://sourceforge.net/projects/vcxsrv/)

也可通过包管理器安装

```powershell
scoop install vcxsrv
```

安装完毕之后打开防火墙配置，勾选所有的 Xserver 连接。

![Fire Wall](images/wsl2/vcxsrv.png)

启动开始菜单中的 XLaunch，使用默认的 `One large window` 和 `Start no client` ，在 Extra settings 中勾选第三项

![XLaunch](images/wsl2/vcxsrv2.png)

最后，完成配置

### 5.2. xfce4 的安装和配置

进入 WSL2，安装 xfce4

```bash
sudo apt install xfce4
```

打开 `/etc/resolve.conf` ，添加如下语句

```bash
[network]
generateResolvConf = false
```

在 Powershell 中，查询本地 IP

```powershell
ipconfig
```

![ipconfig](images/wsl2/ipconfig.png)

回到 WSL2，将如下语句，添加至 `~/.bashrc` 或 `~/.zshrc` 末尾

```bash
export DISPLAY=$(awk '/nameserver / {print $2; exit}' /etc/resolv.conf 2>/dev/null):0
export LIBGL_ALWAYS_INDIRECT=1
```

### 5.3. 启动 GUI

重启 bash 或 zsh

```bash
# source ~/.bashrc
# source ~/.zshrc
```

保持 XLaunch 开启，启动 xfce4

```bash
startxfce4
```

![GUI](images/wsl2/gui.png)
