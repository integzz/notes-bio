# 翻墙经验

翻墙的方法主要有两种，修改 Hosts 文件和 VPN。

## 1. 修改 Hosts 文件

### 1.1. 手动修改

hosts 文件的路径为

- Windows：`C:\Windows\System32\drivers\etc\hosts`
- MacOS：`/private/etc/hosts`
- Linux：`/etc/host`

将 Github 上分享的 [hosts](https://github.com/googlehosts/hosts/blob/master/hosts-files/hosts) 文件下载下来替换上述 hosts 文件。

### 1.2. 自动化脚本

对于 MacOS 用户，可下载 HostsToolforMac。

```bash
brew install hoststool
```

## 2. VPN

### 2.1. 浏览器 VPN

下载火狐浏览器，进入插件商店（add-ins），搜索"VPN"，这里推荐 Hoxx VPN（外加 WebRTC Leaks Shield）。

## 3. 全局代理

代理和 VPN 有一些区别

### 3.1. 酸酸乳（Shadowsocksr，SSR）

免费机场

- [lncn](https://lncn.org)
