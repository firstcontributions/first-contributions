namespace AutoHotspot;

internal interface IAppLogger
{
    void Info(string message);

    void Error(string message);

    void Error(Exception exception);
}
