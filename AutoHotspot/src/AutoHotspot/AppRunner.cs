namespace AutoHotspot;

internal sealed class AppRunner(
    IHotspotPlatform platform,
    IAppLogger logger,
    Func<TimeSpan, Task> delay,
    TimeSpan networkRetryInterval,
    int networkAttempts)
{
    public async Task<ExitCode> RunAsync(bool statusOnly)
    {
        IHotspotSession? session = null;

        for (var attempt = 1; attempt <= networkAttempts; attempt++)
        {
            try
            {
                session = platform.TryCreateSession();
            }
            catch (Exception exception)
            {
                logger.Error($"Could not create the tethering manager: {exception.Message}");
                return ExitCode.ManagerUnavailable;
            }

            if (session is not null)
            {
                break;
            }

            if (attempt < networkAttempts)
            {
                logger.Info($"Internet connection profile is not ready; retrying in {networkRetryInterval.TotalSeconds:0} seconds.");
                await delay(networkRetryInterval);
            }
        }

        if (session is null)
        {
            logger.Error("No Internet connection profile became available before the retry limit.");
            return ExitCode.NetworkUnavailable;
        }

        logger.Info($"Using Internet connection profile: {session.ConnectionName}");
        logger.Info($"Current hotspot state: {session.State}; clients: {session.ClientCount}/{session.MaxClientCount}");

        if (statusOnly)
        {
            logger.Info("Status-only check completed.");
            return ExitCode.Success;
        }

        if (session.State == HotspotState.On)
        {
            logger.Info("Hotspot is already on.");
            return ExitCode.Success;
        }

        logger.Info("Starting hotspot.");
        var result = await session.StartAsync();
        if (!result.Succeeded)
        {
            logger.Error($"Hotspot start failed. Status: {result.Status}; message: {result.ErrorMessage}");
            return ExitCode.StartFailed;
        }

        logger.Info("Hotspot started successfully.");
        return ExitCode.Success;
    }
}
