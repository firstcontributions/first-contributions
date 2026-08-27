param(
    [switch]$SkipTests,
    [switch]$SkipInstaller
)

$ErrorActionPreference = 'Stop'
$projectRoot = $PSScriptRoot
$solution = Join-Path $projectRoot 'AutoHotspot.slnx'
$project = Join-Path $projectRoot 'src\AutoHotspot\AutoHotspot.csproj'
$publishDirectory = Join-Path $projectRoot 'artifacts\publish\win-x64'

dotnet build $solution --configuration Release
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

if (-not $SkipTests) {
    dotnet test $solution --configuration Release --no-build
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

dotnet publish $project `
    --configuration Release `
    --runtime win-x64 `
    --self-contained true `
    --output $publishDirectory
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

if (-not $SkipInstaller) {
    $isccCommand = Get-Command 'ISCC.exe' -ErrorAction SilentlyContinue
    $isccCandidates = @(
        if ($isccCommand) { $isccCommand.Source }
        if (${env:ProgramFiles(x86)}) { Join-Path ${env:ProgramFiles(x86)} 'Inno Setup 6\ISCC.exe' }
        if ($env:LOCALAPPDATA) { Join-Path $env:LOCALAPPDATA 'Programs\Inno Setup 6\ISCC.exe' }
    )
    $iscc = $isccCandidates | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
    if (-not $iscc) {
        throw 'Inno Setup 6 was not found. Install it before building the installer.'
    }

    & $iscc (Join-Path $projectRoot 'installer\installer.iss')
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
