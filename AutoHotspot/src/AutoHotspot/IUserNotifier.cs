namespace AutoHotspot;

internal interface IUserNotifier
{
    void ShowStarting();

    void ShowSucceeded();

    void ShowFailed();
}
