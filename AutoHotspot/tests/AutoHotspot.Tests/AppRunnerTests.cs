namespace AutoHotspot.Tests;

[TestClass]
public sealed class AppRunnerTests
{
    [TestMethod]
    public async Task RunAsync_RetriesUntilNetworkIsAvailable()
    {
        var session = new FakeSession { State = HotspotState.On };
        var platform = new FakePlatform(null, null, session);
        var delays = 0;
        var runner = CreateRunner(platform, _ =>
        {
            delays++;
            return Task.CompletedTask;
        });

        var result = await runner.RunAsync(statusOnly: false);

        Assert.AreEqual(ExitCode.Success, result);
        Assert.AreEqual(2, delays);
        Assert.AreEqual(0, session.StartCalls);
    }

    [TestMethod]
    public async Task RunAsync_ReturnsNetworkUnavailableAfterRetryLimit()
    {
        var runner = CreateRunner(new FakePlatform(null, null, null));

        var result = await runner.RunAsync(statusOnly: false);

        Assert.AreEqual(ExitCode.NetworkUnavailable, result);
    }

    [TestMethod]
    public async Task RunAsync_DoesNotStartHotspotInStatusOnlyMode()
    {
        var session = new FakeSession { State = HotspotState.Off };
        var runner = CreateRunner(new FakePlatform(session));

        var result = await runner.RunAsync(statusOnly: true);

        Assert.AreEqual(ExitCode.Success, result);
        Assert.AreEqual(0, session.StartCalls);
    }

    [TestMethod]
    public async Task RunAsync_ReturnsStartFailedWhenApiRejectsStart()
    {
        var session = new FakeSession
        {
            State = HotspotState.Off,
            StartResult = new HotspotStartResult(false, "Unknown", "Blocked by policy"),
        };
        var logger = new FakeLogger();
        var runner = CreateRunner(new FakePlatform(session), logger: logger);

        var result = await runner.RunAsync(statusOnly: false);

        Assert.AreEqual(ExitCode.StartFailed, result);
        Assert.AreEqual(1, session.StartCalls);
        Assert.IsTrue(logger.Errors.Any(message => message.Contains("Blocked by policy", StringComparison.Ordinal)));
    }

    private static AppRunner CreateRunner(
        IHotspotPlatform platform,
        Func<TimeSpan, Task>? delay = null,
        FakeLogger? logger = null) =>
        new(
            platform,
            logger ?? new FakeLogger(),
            delay ?? (_ => Task.CompletedTask),
            TimeSpan.FromSeconds(5),
            networkAttempts: 3);

    private sealed class FakePlatform(params IHotspotSession?[] sessions) : IHotspotPlatform
    {
        private readonly Queue<IHotspotSession?> _sessions = new(sessions);

        public IHotspotSession? TryCreateSession() => _sessions.Count == 0 ? null : _sessions.Dequeue();
    }

    private sealed class FakeSession : IHotspotSession
    {
        public string ConnectionName { get; init; } = "Test connection";

        public HotspotState State { get; init; }

        public uint ClientCount => 0;

        public uint MaxClientCount => 8;

        public HotspotStartResult StartResult { get; init; } = new(true, "Success", null);

        public int StartCalls { get; private set; }

        public Task<HotspotStartResult> StartAsync()
        {
            StartCalls++;
            return Task.FromResult(StartResult);
        }
    }

    private sealed class FakeLogger : IAppLogger
    {
        public List<string> Errors { get; } = [];

        public void Info(string message)
        {
        }

        public void Error(string message) => Errors.Add(message);

        public void Error(Exception exception) => Errors.Add(exception.Message);
    }
}
