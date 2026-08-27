# AutoHotspot

AutoHotspot 是一个 Windows 后台程序，在当前用户登录后自动开启 Windows 移动热点。程序使用 WinRT `NetworkOperatorTetheringManager`，无窗口运行，并把执行结果写入当前用户的本地日志目录。

## 系统要求

- Windows 10 2004（build 19041）或更高版本
- x64 处理器
- 支持 Windows 移动热点的无线网卡和驱动
- 已在 Windows 设置中配置过移动热点名称、密码和频段
- 企业策略未禁用移动热点

发布程序为 self-contained 多文件应用，安装包会部署全部运行依赖，目标电脑无需预装 .NET 或 Windows App SDK Runtime。

## 安装

运行：

```text
artifacts\installer\AutoHotspot-Setup-1.1.0-win-x64.exe
```

安装器不需要管理员权限，默认安装到：

```text
%LocalAppData%\Programs\AutoHotspot
```

安装器会在当前用户启动目录创建 `AutoHotspot.lnk`。用户登录后，Windows Shell 通过该快捷方式以 `--startup` 参数运行程序。

## 运行行为

- 登录启动模式先等待约 30 秒，减少登录初期网络和系统服务尚未就绪的影响。
- 等待结束后发送“热点正在自启动”系统通知。
- 每 5 秒检查一次 Internet Connection Profile，最多尝试 13 次，覆盖约 60 秒。
- 热点已经开启时直接成功退出。
- 热点关闭时调用 WinRT API 开启热点，并检查操作结果。
- 成功后发送“热点自启动完成”通知，失败后发送“热点自启动失败”通知。
- 通知发送失败只写日志，不会阻止热点操作。
- 同一用户已有实例运行时，新实例返回 `40`，避免重复操作。
- 所有自动执行均无窗口，不阻塞用户登录。

只检查状态而不启动热点：

```powershell
AutoHotspot.exe --status-only
```

模拟完整登录启动流程：

```powershell
AutoHotspot.exe --startup
```

## 日志

日志目录：

```text
%LocalAppData%\AutoHotspot\logs
```

最多保留最近 10 个日志文件。日志包含版本、连接名称、热点状态、客户端数量和 API 错误，但不记录热点密码或用户凭据。

## 退出码

| 退出码 | 含义 |
|---|---|
| `0` | 成功、热点已经开启或只读状态检查完成 |
| `10` | 等待结束后仍没有 Internet Connection Profile |
| `20` | 无法创建热点管理器 |
| `30` | Windows 拒绝或未能启动热点 |
| `40` | 当前用户已有 AutoHotspot 实例运行 |
| `100` | 未预期异常 |

## 开发构建

要求：

- .NET SDK 10.0.302 或兼容的更新 Feature Band
- Inno Setup 6，仅在生成安装包时需要

完整构建、测试、发布和安装包生成：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\build.ps1
```

只生成程序，不生成安装包：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\build.ps1 -SkipInstaller
```

独立运行测试：

```powershell
dotnet test .\AutoHotspot.slnx --configuration Release
```

## 项目结构

| 路径 | 内容 |
|---|---|
| `src/AutoHotspot` | 后台程序和 Windows WinRT 适配层 |
| `tests/AutoHotspot.Tests` | 不操作真实热点的核心流程测试 |
| `installer/installer.iss` | Inno Setup 用户级安装脚本 |
| `artifacts/publish/win-x64` | self-contained 发布文件 |
| `artifacts/installer` | 最终安装包 |
| `测试报告.md` | 当前环境的验证记录和剩余测试项 |

## 限制

- 当前只构建和验证 `win-x64`。
- 自动运行依赖用户登录和 Windows Shell，不支持无人登录时启动。
- 首版不修改热点名称、密码或频段。
- VPN、多 Internet Profile、Windows 10 实机和企业策略环境仍需分别验证。
