using System.Reflection;
namespace AutoHotspot;

internal static class Program
{
    static Program()
    {
        Environment.SetEnvironmentVariable(
            "MICROSOFT_WINDOWSAPPRUNTIME_BASE_DIRECTORY",
            AppContext.BaseDirectory);
    }

    private static readonly TimeSpan NetworkRetryInterval = TimeSpan.FromSeconds(5);
    private static readonly TimeSpan NetworkWaitTimeout = TimeSpan.FromSeconds(60);
    private static readonly TimeSpan StartupDelay = TimeSpan.FromSeconds(30);

    [STAThread]
    private static async Task<int> Main(string[] args)
    {
        FileLogger? logger = null;

        try
        {
            logger = FileLogger.Create();
            logger.Info($"AutoHotspot {GetVersion()} started. Arguments: {FormatArguments(args)}");

            using var mutex = new Mutex(true, "AutoHotspot.CurrentUser", out var ownsMutex);
            if (!ownsMutex)
            {
                logger.Info("Another AutoHotspot instance is already running.");
                return (int)ExitCode.AlreadyRunning;
            }

            var statusOnly = args.Any(argument =>
                string.Equals(argument, "--status-only", StringComparison.OrdinalIgnoreCase));
            var startupMode = args.Any(argument =>
                string.Equals(argument, "--startup", StringComparison.OrdinalIgnoreCase));

            var networkAttempts = (int)(NetworkWaitTimeout / NetworkRetryInterval) + 1;
            var runner = new AppRunner(
                new WindowsHotspotPlatform(),
                logger,
                Task.Delay,
                NetworkRetryInterval,
                networkAttempts);

            if (startupMode)
            {
                using var notifier = new WindowsUserNotifier(logger);
                var workflow = new StartupWorkflow(runner, notifier, logger, Task.Delay, StartupDelay);
                return (int)await workflow.RunAsync();
            }

            return (int)await runner.RunAsync(statusOnly);
        }
        catch (Exception exception)
        {
            if (logger is not null)
            {
                try
                {
                    logger.Error(exception);
                }
                catch
                {
                    // There is no UI fallback because scheduled execution must stay silent.
                }
            }

            return (int)ExitCode.UnexpectedError;
        }
    }

    private static string FormatArguments(string[] args) =>
        args.Length == 0 ? "<none>" : string.Join(' ', args.Select(argument => $"\"{argument.Replace("\"", "\\\"")}\""));

    private static string GetVersion() =>
        Assembly.GetExecutingAssembly().GetName().Version?.ToString() ?? "unknown";
}
