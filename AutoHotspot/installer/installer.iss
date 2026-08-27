#define AppName "AutoHotspot"
#define AppVersion "1.1.0"
#define AppPublisher "AutoHotspot"
#define AppExeName "AutoHotspot.exe"

[Setup]
AppId={{5A12A3A7-D787-4A43-970E-D71B0251B772}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher={#AppPublisher}
DefaultDirName={localappdata}\Programs\{#AppName}
DefaultGroupName={#AppName}
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
OutputDir=..\artifacts\installer
OutputBaseFilename=AutoHotspot-Setup-{#AppVersion}-win-x64
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
UninstallDisplayIcon={app}\{#AppExeName}
CloseApplications=yes
RestartApplications=no

[Files]
Source: "..\artifacts\publish\win-x64\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\卸载 {#AppName}"; Filename: "{uninstallexe}"
Name: "{userstartup}\{#AppName}"; Filename: "{app}\{#AppExeName}"; Parameters: "--startup"; WorkingDir: "{app}"; Comment: "登录后延时开启 Windows 移动热点"

[Run]
Filename: "{app}\{#AppExeName}"; Parameters: "--status-only"; Description: "验证移动热点访问"; StatusMsg: "正在验证移动热点访问..."; Flags: runhidden waituntilterminated postinstall skipifsilent runasoriginaluser
