using System.Globalization;

namespace AutoHotspot;

internal sealed class FileLogger : IAppLogger
{
    private const int RetainedLogCount = 10;
    private readonly string _logPath;

    private FileLogger(string logPath)
    {
        _logPath = logPath;
    }

    public string LogPath => _logPath;

    public static FileLogger Create()
    {
        var logDirectory = Path.Combine(
            Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),
            "AutoHotspot",
            "logs");

        Directory.CreateDirectory(logDirectory);
        DeleteOldLogs(logDirectory);

        var fileName = $"autohotspot-{DateTime.Now:yyyyMMdd-HHmmss-fff}.log";
        return new FileLogger(Path.Combine(logDirectory, fileName));
    }

    public void Info(string message) => Write("INFO", message);

    public void Error(string message) => Write("ERROR", message);

    public void Error(Exception exception) =>
        Write("ERROR", $"{exception.GetType().FullName}: {exception.Message}{Environment.NewLine}{exception.StackTrace}");

    private static void DeleteOldLogs(string logDirectory)
    {
        var oldLogs = new DirectoryInfo(logDirectory)
            .EnumerateFiles("autohotspot-*.log")
            .OrderByDescending(file => file.CreationTimeUtc)
            .Skip(RetainedLogCount - 1);

        foreach (var oldLog in oldLogs)
        {
            try
            {
                oldLog.Delete();
            }
            catch (IOException)
            {
                // A locked log can be retried on the next run.
            }
            catch (UnauthorizedAccessException)
            {
                // Logging must never prevent hotspot startup.
            }
        }
    }

    private void Write(string level, string message)
    {
        var line = string.Create(
            CultureInfo.InvariantCulture,
            $"{DateTimeOffset.Now:O} [{level}] {message}{Environment.NewLine}");

        File.AppendAllText(_logPath, line);
    }
}
