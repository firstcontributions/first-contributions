using Windows.Networking.Connectivity;
using Windows.Networking.NetworkOperators;

namespace AutoHotspot;

internal enum HotspotState
{
    Off,
    On,
    InTransition,
    Unknown,
}

internal sealed record HotspotStartResult(bool Succeeded, string Status, string? ErrorMessage);

internal interface IHotspotSession
{
    string ConnectionName { get; }

    HotspotState State { get; }

    uint ClientCount { get; }

    uint MaxClientCount { get; }

    Task<HotspotStartResult> StartAsync();
}

internal interface IHotspotPlatform
{
    IHotspotSession? TryCreateSession();
}

internal sealed class WindowsHotspotPlatform : IHotspotPlatform
{
    public IHotspotSession? TryCreateSession()
    {
        var profile = NetworkInformation.GetInternetConnectionProfile();
        return profile is null ? null : new WindowsHotspotSession(profile);
    }

    private sealed class WindowsHotspotSession : IHotspotSession
    {
        private readonly NetworkOperatorTetheringManager _manager;

        public WindowsHotspotSession(ConnectionProfile profile)
        {
            ConnectionName = profile.ProfileName;
            _manager = NetworkOperatorTetheringManager.CreateFromConnectionProfile(profile);
        }

        public string ConnectionName { get; }

        public HotspotState State => _manager.TetheringOperationalState switch
        {
            TetheringOperationalState.Off => HotspotState.Off,
            TetheringOperationalState.On => HotspotState.On,
            TetheringOperationalState.InTransition => HotspotState.InTransition,
            _ => HotspotState.Unknown,
        };

        public uint ClientCount => _manager.ClientCount;

        public uint MaxClientCount => _manager.MaxClientCount;

        public async Task<HotspotStartResult> StartAsync()
        {
            var result = await _manager.StartTetheringAsync();
            return new HotspotStartResult(
                result.Status == TetheringOperationStatus.Success,
                result.Status.ToString(),
                result.AdditionalErrorMessage);
        }
    }
}
