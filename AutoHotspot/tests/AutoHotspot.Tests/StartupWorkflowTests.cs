namespace AutoHotspot.Tests;

[TestClass]
public sealed class StartupWorkflowTests
{
    [TestMethod]
    public async Task RunAsync_DelaysThenSendsStartingAndSuccessNotifications()
    {
        var events = new List<string>();
        var notifier = new FakeNotifier(events);
        var runner = CreateRunner(HotspotState.On);
        var workflow = new StartupWorkflow(
            runner,
            notifier,
            new FakeLogger(),
            duration =>
            {
                events.Add($"delay:{duration.TotalSeconds:0}");
                return Task.CompletedTask;
            },
            TimeSpan.FromSeconds(30));

        var result = await workflow.RunAsync();

        Assert.AreEqual(ExitCode.Success, result);
        CollectionAssert.AreEqual(
            new[] { "delay:30", "starting", "succeeded" },
            events);
    }

    [TestMethod]
    public async Task RunAsync_SendsFailureNotificationWhenHotspotStartFails()
    {
        var events = new List<string>();
        var notifier = new FakeNotifier(events);
        var runner = CreateRunner(
            HotspotState.Off,
            new HotspotStartResult(false, "Unknown", "Test failure"));
        var workflow = new StartupWorkflow(
            runner,
            notifier,
            new FakeLogger(),
            _ => Task.CompletedTask,
            TimeSpan.FromSeconds(30));

        var result = await workflow.RunAsync();

        Assert.AreEqual(ExitCode.StartFailed, result);
        CollectionAssert.AreEqual(new[] { "starting", "failed" }, events);
    }

    private static AppRunner CreateRunner(
        HotspotState state,
        HotspotStartResult? startResult = null) =>
        new(
            new FakePlatform(new FakeSession(state, startResult)),
            new FakeLogger(),
            _ => Task.CompletedTask,
            TimeSpan.Zero,
            networkAttempts: 1);

    private sealed class FakeNotifier(List<string> events) : IUserNotifier
    {
        public void ShowStarting() => events.Add("starting");

        public void ShowSucceeded() => events.Add("succeeded");

        public void ShowFailed() => events.Add("failed");
    }

    private sealed class FakePlatform(IHotspotSession session) : IHotspotPlatform
    {
        public IHotspotSession? TryCreateSession() => session;
    }

    private sealed class FakeSession(
        HotspotState state,
        HotspotStartResult? startResult) : IHotspotSession
    {
        public string ConnectionName => "Test connection";

        public HotspotState State => state;

        public uint ClientCount => 0;

        public uint MaxClientCount => 8;

        public Task<HotspotStartResult> StartAsync() =>
            Task.FromResult(startResult ?? new HotspotStartResult(true, "Success", null));
    }

    private sealed class FakeLogger : IAppLogger
    {
        public void Info(string message)
        {
        }

        public void Error(string message)
        {
        }

        public void Error(Exception exception)
        {
        }
    }
}
