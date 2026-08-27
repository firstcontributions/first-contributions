using Microsoft.Windows.AppNotifications;
using Microsoft.Windows.AppNotifications.Builder;

namespace AutoHotspot;

internal sealed class WindowsUserNotifier(IAppLogger logger) : IUserNotifier, IDisposable
{
    private bool _registered;

    public void ShowStarting() => Show("热点正在自启动", "AutoHotspot 正在开启 Windows 移动热点。");

    public void ShowSucceeded() => Show("热点自启动完成", "Windows 移动热点已成功开启。");

    public void ShowFailed() => Show("热点自启动失败", "未能开启 Windows 移动热点，请查看 AutoHotspot 日志。");

    public void Dispose()
    {
        if (!_registered)
        {
            return;
        }

        try
        {
            AppNotificationManager.Default.Unregister();
        }
        catch (Exception exception)
        {
            logger.Error($"Could not unregister app notifications: {exception.Message}");
        }
    }

    private void Show(string title, string message)
    {
        try
        {
            EnsureRegistered();
            var notification = new AppNotificationBuilder()
                .AddText(title)
                .AddText(message)
                .BuildNotification();

            AppNotificationManager.Default.Show(notification);
            logger.Info($"Notification sent: {title}");
        }
        catch (Exception exception)
        {
            logger.Error($"Could not send notification '{title}': {exception.Message}");
        }
    }

    private void EnsureRegistered()
    {
        if (_registered)
        {
            return;
        }

        AppNotificationManager.Default.Register();
        _registered = true;
    }
}
