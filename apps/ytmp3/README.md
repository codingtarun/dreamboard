# YouTube to MP3 Downloader

A simple terminal app to download YouTube videos as **320kbps MP3** files.

## Usage

```bash
cd apps/ytmp3

# Download a video
uv run python ytmp3.py "https://youtube.com/watch?v=..."

# Or run interactively (it will prompt for URL)
uv run python ytmp3.py

# Save to a custom folder
uv run python ytmp3.py "https://youtube.com/watch?v=..." -o /path/to/folder
```

## What it does

- Downloads the best available audio stream from YouTube
- Converts it to **MP3 at 320kbps** using FFmpeg
- Saves the file to your `~/Downloads/` folder (or custom path)
- Embeds thumbnail and metadata into the MP3

## Requirements

- `uv` (already available)
- `ffmpeg` (installed automatically if needed)
- `yt-dlp` (installed in the local venv)
