# Local Network Media Browser

**Status:** raw
**Spark:** 🔥🔥🔥🔥
**Created:** 2026-05-16
**Last Updated:** 2026-05-16
**Tags:** mobile-app, media-browser, local-network, file-sharing, cross-platform, smb, nas, photos

## The Spark
A mobile app that allows browsing local network shared HDDs — whether from Linux, Windows, or macOS — and allows viewing images and other media directly from local network drives. No cloud, no uploads, just pure local network discovery and streaming.

## Details
- Cross-platform network discovery (SMB/CIFS, AFP, NFS, DLNA/UPnP where possible)
- Browse shared folders from Windows, Linux (Samba), and macOS machines on the same Wi-Fi/LAN
- View images, play videos, and possibly stream audio from network shares
- No server-side software required — connects using standard protocols
- Potential support for NAS devices (Synology, QNAP, etc.) that expose standard shares
- Could include offline caching / favorites for frequently accessed folders

## Why It Excites Me
- Keeps personal media local and private — no cloud dependency
- Many people have old hard drives or PCs sharing files on their home network with no good mobile interface
- Unified experience across heterogeneous home networks (mixed OS environments)

## Potential Obstacles
- Protocol fragmentation: SMB versions, authentication methods, macOS AFP vs SMB
- iOS sandboxing and networking restrictions (local network permission prompts)
- Android storage access framework limitations on newer versions
- Video codec support on mobile for direct streaming without transcoding
- Security concerns with older SMB versions on home networks
- Discovery reliability across different routers/network configs

## Next Steps
- Research existing apps in this space (VLC network browsing, FileBrowser, etc.)
- Validate protocol support on iOS/Android native APIs
- Design the smallest experiment: a proof-of-concept that can list SMB shares from a mobile device

## Related Ideas
- [None yet]

## Notes Log
- 2026-05-16 — Idea captured.
