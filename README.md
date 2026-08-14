[ This project is currently not working. ]

# YouTube Subtitle Downloader

This program downloads subtitles from YouTube videos using the `youtube_transcript_api` and `pytube` packages.

## Installation

One way or another, you will and a python3 environment with the following dependencies:

- `youtube_transcript_api`
- `pytube`

You may do it manually, or use the refered `venvutils` git submodule. For the latter, check its documentation.

## Usage

```
./yt-sub.py [<video_id>] [<language_code>]
```

`<video_id>` is the YouTube video ID, not the full link. Omit it and be prompted.
`<language_code>` with the desired subtitle language code. Omit it and the script will prompt list the available options.

## Warnings

This code uses an undocumented part of the YouTube API, which is called by the YouTube web-client. So there is no guarantee that it won't stop working tomorrow, if they change how things work. I will however do my best to make things working again as soon as possible if that happens. So if it stops working, let me know!

## Author

This program was created by Flávio Carrara (fde-capu) flavio@carrara.us.

## Copyright and License

Copyright (c) 2023 Flávio Carrara. All rights reserved.

This software is licensed under a custom license that allows for free use, modification, and distribution for non-commercial purposes. For commercial use, a separate license must be obtained. Contact the author for more information on obtaining a commercial license.
