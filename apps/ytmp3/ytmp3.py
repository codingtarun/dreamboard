#!/usr/bin/env python3
"""
YouTube to MP3 Downloader
Downloads YouTube videos as 320kbps MP3 files to ~/Downloads/
"""

import os
import sys
import argparse

try:
    from yt_dlp import YoutubeDL
except ImportError:
    print("Error: yt-dlp is not installed.")
    print("Install it with: uv pip install yt-dlp")
    sys.exit(1)


def get_downloads_folder():
    """Return the user's Downloads folder path."""
    home = os.path.expanduser("~")
    downloads = os.path.join(home, "Downloads")
    os.makedirs(downloads, exist_ok=True)
    return downloads


def download_mp3(url, output_dir=None):
    """Download a YouTube video as MP3 at 320kbps."""
    if output_dir is None:
        output_dir = get_downloads_folder()

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],
        "embed_thumbnail": True,
        "addmetadata": True,
        "quiet": False,
        "no_warnings": False,
    }

    print(f"\n🎵 Downloading: {url}")
    print(f"📁 Saving to: {output_dir}")
    print("⏳ This may take a moment...\n")

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get("title", "Unknown")
        print(f"\n✅ Done! Saved: {title}.mp3")
        return True


def main():
    parser = argparse.ArgumentParser(
        description="Download YouTube videos as 320kbps MP3 files"
    )
    parser.add_argument("url", nargs="?", help="YouTube video URL")
    parser.add_argument(
        "-o", "--output", help="Output directory (default: ~/Downloads)"
    )
    args = parser.parse_args()

    url = args.url
    if not url:
        url = input("🔗 Enter YouTube video URL: ").strip()

    if not url:
        print("Error: No URL provided.")
        sys.exit(1)

    try:
        download_mp3(url, output_dir=args.output)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
