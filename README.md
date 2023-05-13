# YouTube Subtitle Downloader

This program downloads subtitles from YouTube videos using the `youtube_transcript_api` and `pytube` packages.

## Installation

1. Install the required packages using the following command:

pip install youtube_transcript_api pytube

## Usage

Run the script with the following command:

python yt-sub.py [<video_id>] [<language_code>]

Replace `<video_id>` with the YouTube video ID and `<language_code>` with the desired subtitle language code (optional).

If you omit the `<video_id>` argument, the script will prompt you for it.

If you omit the `<language_code>` argument, the script will list the available subtitle languages and prompt you to choose one.

## Example

python3 yt-sub.py PELnMfcYUj0 en

This will download the English subtitles for the video with ID `PELnMfcYUj0`.

## Warnings

This code uses an undocumented part of the YouTube API, which is called by the YouTube web-client. So there is no guarantee that it won't stop working tomorrow, if they change how things work. I will however do my best to make things working again as soon as possible if that happens. So if it stops working, let me know!

## Author

This program was created by Flávio Carrara (fde-capu) flavio@carrara.us.

## Copyright and License

Copyright (c) 2023 Your Name. All rights reserved.

This software is licensed under a custom license that allows for free use, modification, and distribution for non-commercial purposes. For commercial use, a separate license must be obtained. Contact the author for more information on obtaining a commercial license.
