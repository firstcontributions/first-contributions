namespace AutoHotspot;

internal sealed class StartupWorkflow(
    AppRunner runner,
    IUserNotifier notifier,
    IAppLogger logger,
    Func<TimeSpan, Task> delay,
    TimeSpan startupDelay)
{
    public async Task<ExitCode> RunAsync()
    {
        logger.Info($"Startup mode detected; waiting {startupDelay.TotalSeconds:0} seconds before starting hotspot.");
        await delay(startupDelay);

        notifier.ShowStarting();

        ExitCode result;
        try
        {
            result = await runner.RunAsync(statusOnly: false);
        }
        catch (Exception exception)
        {
            logger.Error(exception);
            notifier.ShowFailed();
            return ExitCode.UnexpectedError;
        }

        if (result == ExitCode.Success)
        {
            notifier.ShowSucceeded();
        }
        else
        {
            notifier.ShowFailed();
        }

        return result;
    }
}
