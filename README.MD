# WeChatFerry
一个玩微信的工具。更多介绍见：[WeChatFerry: 一个玩微信的工具](https://mp.weixin.qq.com/s/CGLfSaNDy8MyuyPWGjGJ7w)。

<details><summary><font color="#FF0000" size="5">免责声明【必读】</font></summary>

本工具仅供学习和技术研究使用，不得用于任何商业或非法行为，否则后果自负。

本工具的作者不对本工具的安全性、完整性、可靠性、有效性、正确性或适用性做任何明示或暗示的保证，也不对本工具的使用或滥用造成的任何直接或间接的损失、责任、索赔、要求或诉讼承担任何责任。

本工具的作者保留随时修改、更新、删除或终止本工具的权利，无需事先通知或承担任何义务。

本工具的使用者应遵守相关法律法规，尊重微信的版权和隐私，不得侵犯微信或其他第三方的合法权益，不得从事任何违法或不道德的行为。

本工具的使用者在下载、安装、运行或使用本工具时，即表示已阅读并同意本免责声明。如有异议，请立即停止使用本工具，并删除所有相关文件。

</details>

|[📖 Python 文档](https://wechatferry.readthedocs.io/)|[📺 Python 视频教程](https://mp.weixin.qq.com/s/APdjGyZ2hllXxyG_sNCfXQ)|[🙋 FAQ](https://mp.weixin.qq.com/s/WOw26mKJG8Nq55cT6iG-yA)|
|:-:|:-:|:-:|

👉 [WeChatRobot🤖](https://github.com/lich0821/WeChatRobot)，一个基于 WeChatFerry 的 Python 机器人框架。

<details><summary>点击查看功能清单</summary>

* 检查登录状态
* 获取登录账号的 wxid
* 获取消息类型
* 获取所有联系人
* 获取所有好友
* 获取数据库
* 获取某数据库下的表
* 获取用户信息
* 发送文本消息（可 @）
* 发送图片
* 发送文件
* 允许接收消息
* 停止接收消息
* 执行 SQL 查询
* 接受好友申请
* 添加群成员
* 删除群成员
* 解密图片
* 获取朋友圈消息
* 保存图片
* 保存语音
* 发送卡片消息
* 拍一拍群友
* 邀请群成员
* 图片 OCR
* 转发消息
* 撤回消息
* 获取登录二维码
* 娱乐五子棋
* 计算好友之间的亲密度
* 获取天气情况并按时通知
* 查看新闻和知乎热榜

</details>

<details><summary>点击查看支持的客户端</summary>

* Go
* HTTP (Go, Rust)
* Java
* Node.js
* Python
* Rust
</details>



## 快速开始
### Python
[![PyPi](https://img.shields.io/pypi/v/wcferry.svg)](https://pypi.python.org/pypi/wcferry) [![Downloads](https://static.pepy.tech/badge/wcferry)](https://pypi.python.org/pypi/wcferry) [![Documentation Status](https://readthedocs.org/projects/wechatferry/badge/?version=latest)](https://wechatferry.readthedocs.io/zh/latest/?badge=latest)

* 安装
```sh
pip install --upgrade wcferry
```

* 参考框架：[🤖WeChatRobot](https://github.com/lich0821/WeChatRobot)

### HTTP
#### [wcfrust](https://github.com/lich0821/wcf-client-rust)（基于 Rust）
开箱即用：[快速开始](https://github.com/lich0821/wcf-client-rust?tab=readme-ov-file#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)。

#### GoHttp（基于 Go）
参考 [GoHttp README.MD](clients/gohttp/README.md)


其余客户端，可下载 [最新发布的版本](https://github.com/lich0821/WeChatFerry/releases/latest)，根据技术栈，选择客户端，将相应 `dll` 和 `exe` 文件放到对应位置。

### Go
参考 [Go README.MD](clients/go/README.md)

### Java
参考 [Java README.MD](clients/java/README.MD)

### Node.js
参考 [Node.js README.MD](https://github.com/stkevintan/node-wcferry/blob/main/README.md)

### Rust
参考 [Rust README.MD](clients/rust/README.MD)



### 安装开发环境
<details><summary>点击查看</summary>

#### 安装 vcpkg
* 安装，参考[Vcpkg: 总览](https://github.com/microsoft/vcpkg/blob/master/README_zh_CN.md)。
```sh
cd C:\Tools
git clone https://github.com/microsoft/vcpkg
.\vcpkg\bootstrap-vcpkg.bat
```

* 添加全局配置：
环境变量增加 `vcpkg` 所在路径（本文为：`C:\Tools\vcpkg`）。

#### 安装相关组件
```sh
vcpkg install protobuf[zlib]:x86-windows-static
vcpkg install spdlog:x86-windows-static
vcpkg install nng:x86-windows-static
vcpkg install magic-enum:x86-windows-static
vcpkg integrate install
```

安装完毕后，需要配置 protoc 的环境变量，并确保在命令行下可用，protoc 的路径在 `<vcpkg_install_path>\installed\x86-windows-static\tools\protobuf`

#### 安装 VS2019

#### 安装 Python3

通过微软商店或者 python.org 自行下载均可，注意配置好环境变量，确保 `python3` 在命令行下可用

</details>

### 编译
使用 VS2019 打开工程，编译即可。

**注**：如果遇到执行 `protoc` 时的 9009 错误，检查是否是 python3 环境有问题，或者 protoc 命令的环境变量配置不正确。

### 运行
运行 `wcf.exe` 启动
```sh
wcf.exe --help
```

## 项目结构
```sh
WeChatFerry
├── LICENSE                 # LICENSE
├── README.MD               # 说明
├── WeChatFerry
│   ├── WeChatFerry.sln     # VS2019 工程文件
│   ├── rpc                 # RPC 模块
│   ├── sdk                 # 注入及启动模块
│   ├── spy                 # 核心功能实现模块
│   └── wcf                 # 命令行版启动器
├── assets
│   ├── QR.jpeg             # 二维码，测试用图
│   ├── TEQuant.jpg         # 二维码，测试用图
│   └── demo.gif            # 示例动图
├── clients
│   ├── go                  # Go 客户端
│   ├── gohttp              # HTTP 客户端
│   ├── http                # HTTP 客户端
│   ├── java                # Java 客户端
│   ├── node                # Node.js 客户端  
│   ├── pyauto              # 群友封装的客户端
│   ├── python              # Python 客户端
│   └── rust                # Rust 客户端
└── docs                    # 文档

```

<details><summary>点击查看</summary>

### go
Go 客户端。

### gohttp
HTTP 客户端，二进制发布无依赖

### http
HTTP 客户端。

### node
Node.js 客户端.

### java
Java 客户端。

### python
Python 客户端。

### rpc
RPC 的通信部分和序列化 / 反序列化部分。

### rust
Rust 客户端。

### sdk
负责将 `spy` 注入微信进程，并启动 RPC 服务。

### spy
间谍模块，注入到微信中，通过 RPC 做消息转发工作。

### wcf
命令行版启动器，调用 `sdk` 将 `spy` 注入微信。其他客户端可通过 RPC 连接到 `spy` 进行消息传递。默认监听的地址为 `tcp://0.0.0.0:10086` 和 `tcp://0.0.0.0:10087`。一般情况不需要显式运行，各客户端自动调用。

</details>


