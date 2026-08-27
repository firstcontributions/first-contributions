namespace AutoHotspot;

internal enum ExitCode
{
    Success = 0,
    NetworkUnavailable = 10,
    ManagerUnavailable = 20,
    StartFailed = 30,
    AlreadyRunning = 40,
    UnexpectedError = 100,
}
