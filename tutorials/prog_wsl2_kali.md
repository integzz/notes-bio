# 搭建 WSL2 下的 Kali 环境

Windows 开启了 WSL2 的支持后，便被追捧为最佳 Linux 发行版。其实际性能究竟如何，我们可以通过 Kali Linux 进行一下体验。话不多说，下面开始配置。

## 1. 安装 WSL2

### 1.1. 开启虚拟机功能

在控制面板 -> 程序和功能 -> Windows 功能窗口中勾选适用于 Linux 的 Windows 子系统 功能，点击确定，并按照提示重启电脑。

![WSL2](images/wsl2/wsl2.png)

或以管理员身份在命令行键入

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

### 1.2. 安装发行版

在 Windows 应用商店搜索 WSL ，选择自己想要的 Linux 发行版，点击下载安装即可。这里选择的是 Kali。

![Kali](images/wsl2/app.png)

### 1.3. 升级

由于版本问题，好多人的的子系统还停留在 WSL，而不是 WSL2，由于后者实质上是一个虚拟机。故要启动虚拟化：

```powershell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl -l # 查看 WSL 列表
wsl --set-version kali-linux 2
```

中间需要下载一个 [WSL2-kernel](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

若之前没有用过 WSL，则首先需要安装 Windows 10 的 WSL 功能：

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

这部分详情见 [WSL2](https://docs.microsoft.com/en-us/windows/wsl/wsl2-kernel)

## 2. Kali

### 2.1. 升级

安装完成后，在 Kali Linux 下，输入如下命令，安装默认工具集

```bash
sudo apt update && sudo apt upgrade
sudo apt install -y kali-linux-default
```

![Kali](images/wsl2/kali.png)

当然你也可以选择安装完整工具集

```bash
sudo apt install -y kali-linux-large
```

### 2.2. GUI

当然为了更好的体验 Kali，我们可以安装官方推荐的 GUI —— Win-KeX。输入如下命令，进行安装。

```bash
sudo apt install -y kali-win-kex
```

安装完毕后，可使用如下命令启动

```bash
# 启动
cd ~
kex
# 关闭
kex stop
# 窗口模式
kex --win -s
```

![Kex](images/wsl2/kex.png)

Win-KeX 还提供了无缝模式

```bash
# 无缝模式
kex --sl -s
```

![Kex2](images/wsl2/kex_seamless.png)

### 2.3. Terminal 整合

当然，像上面那样启动还是不大方便。我们可以在 Windows Terminal 的配置中，加入一下内容，将 Kali 和 Win-KeX 整合进 Terminal。

```json
{
  "list": [
    {
      "guid": "{46ca431a-3a87-5fb3-83cd-11ececc031d2}",
      "hidden": false,
      "name": "Kali",
      "icon": "file:///c:/users/ci/pictures/icons/kali.png",
      "source": "Windows.Terminal.Wsl"
    },
    {
      "guid": "{55ca431a-3a87-5fb3-83cd-11ececc031d2}",
      "hidden": false,
      "name": "KaTex",
      "icon": "file:///c:/users/ci/pictures/icons/kali.png",
      // 窗口模式启动
      "commandline": "wsl -d kali-linux kex --wtstart -s"
    }
  ]
}
```

![Terminal](images/wsl2/kali_terminal.png)

## 3. WSL2 优化

### 3.1. 压缩

随着使用时间的延长，WSL2 占用的硬盘空间会越来越多，这个时候就需要对其文件进行压缩。方法如下

```powershell
wsl --shutdown
# open window Diskpart
diskpart
select vdisk file="C:\Users\Ci\AppData\Local\Packages\KaliLinux.54290C8133FEE_ey8k8hqnwqnmg\LocalState\ext4.vhdx"
# select vdisk  file="C:\Users\Ci\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\LocalState\ext4.vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
```

### 3.2. 内存

当然，WSL2 也会带来内存占用的问题，可以打开 `~/.wslconfig` ，进行如下设置

```powershell
[wsl2]
memory=4GB
swap=0
```

### 3.3. Bugs

The attempted operation is not supported for the type of object referenced.

```powershell
sudo netsh winsock reset
```
