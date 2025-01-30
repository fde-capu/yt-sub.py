#!/bin/env python3
"""
╔═════════════════════════════╗
║ YouTube Subtitle Downloader ║
║ Author: fde-capu            ║
║ Email: flavio@carrara.us    ║
║ Date: 5/13/2023             ║
╚═════════════════════════════╝
"""
import sys
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import urllib.parse

# Prompt the user for the video id or use the first argument
if len(sys.argv) > 1:
    video_id = sys.argv[1]
else:
    video_id = input("Enter the video id: ")
video_id = urllib.parse.quote(video_id)

# Fetch the video title and author information
video_url = f'https://www.youtube.com/watch?v={video_id}'
yt = YouTube(video_url)
video_title = yt.title
author_name = yt.author

# Display the author name and video title
print(f"{author_name}\n{video_title}")

# Retrieve the available transcripts
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

# List available subtitle languages
transcripts = list(transcript_list)
for i, transcript in enumerate(transcripts):
    print(f"{i + 1}. {transcript.language} ({transcript.language_code})")

# Prompt the user to choose a language or use the second argument
if len(sys.argv) > 2:
    chosen_language = sys.argv[2]
else:
    user_input = int(input("-> "))
    chosen_language = transcripts[user_input - 1].language_code

# Download the subtitle for the chosen language
subtitle = YouTubeTranscriptApi.get_transcript(video_id, languages=[chosen_language])

# Save the subtitle to a file
filename = f"{author_name.replace(' ', '_')}_{video_title[:20].replace(' ', '_')}_{chosen_language}.txt"
with open(filename, "w") as f:
    for line in subtitle:
        f.write(f"{line['text']}\n")

print(f"Subtitle saved to: {filename}.")
