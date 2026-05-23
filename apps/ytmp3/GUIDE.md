# YouTube to MP3 Downloader — Step-by-Step Guide

Follow these steps to download any YouTube video as a high-quality MP3 file.

---

## Step 1: Open Your Terminal

Open a terminal and navigate to the app folder:

```bash
cd apps/ytmp3
```

---

## Step 2: Run the Downloader

### Option A — Pass the YouTube URL directly

```bash
uv run python ytmp3.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Replace `VIDEO_ID` with the actual ID from the YouTube link.

### Option B — Run interactively (it will ask for the URL)

```bash
uv run python ytmp3.py
```

Then paste the YouTube URL when prompted:

```
🔗 Enter YouTube video URL: https://www.youtube.com/watch?v=VIDEO_ID
```

---

## Step 3: Wait for the Download

The app will:
1. Fetch the best audio stream from YouTube
2. Convert it to **MP3 at 320kbps**
3. Save it to your **Downloads** folder

You'll see progress in the terminal. When done, you'll see:

```
✅ Done! Saved: Song Title.mp3
```

---

## Step 4: Find Your File

Open your **Downloads** folder to find the MP3:

```bash
open ~/Downloads
```

Or on Linux:

```bash
xdg-open ~/Downloads
```

---

## Optional: Download to a Different Folder

Use the `-o` flag to choose a custom save location:

```bash
uv run python ytmp3.py "URL" -o /path/to/your/folder
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `yt-dlp not found` | Run `uv pip install yt-dlp` inside the `apps/ytmp3` folder |
| `ffmpeg not found` | Install it with `sudo apt install ffmpeg` (Linux) or `brew install ffmpeg` (Mac) |
| Download fails | Check your internet connection and make sure the video URL is valid |

---

## Quick Reference

| What you want | Command |
|---------------|---------|
| Download with URL | `uv run python ytmp3.py "URL"` |
| Interactive mode | `uv run python ytmp3.py` |
| Custom output folder | `uv run python ytmp3.py "URL" -o /path/to/folder` |
| Show help | `uv run python ytmp3.py --help` |
