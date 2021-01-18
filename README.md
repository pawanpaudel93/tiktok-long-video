<h1 align="center">Welcome to tiktok-long-video</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.5.0-blue.svg?cacheSeconds=2592000" />
</p>

A useful package/tool to make webm/mp4 videos greater than 60s in length uploadable to TikTok.

## Installation
```bash
pip install ttlv
```

## Proof

  This video [https://www.tiktok.com/@harrynepal26/video/6917917976008183042](https://www.tiktok.com/@harrynepal26/video/6917917976008183042 "https://www.tiktok.com/@harrynepal26/video/6917917976008183042") is actually 2 Minutes 45 Seconds long.
  You can download this video using [govue-tiktok-downloader](https://github.com/pawanpaudel93/govue-tiktok-downloader "govue-tiktok-downloader") to confirm that video is more than 60 seconds long.

## Usage

To upload longer videos than 60 seconds, first you must have a webm/mp4 video file or you can convert the video to webm/mp4 using online or offline tools and you have to save using below commands and upload via Tiktok web not mobile app.

You can use as cli tool.
For help,
```bash
ttlv -h
```

Input filepath is must and output filepath is optional. For saving tiktok long video,
```bash
ttlv -i "/home/user/Desktop/sample.webm" -o "/home/user/Desktop/sample-ttlv.webm"
```

OR

You can import and use in your programs. 
output_path is optional.
```python
from ttlv import Video

video = Video(input_path="./sample.mp4", output_path="./sample-ttlv.mp4")
video.save()
```

## Author

👤 **Pawan Paudel**

* Github: [@pawanpaudel93](https://github.com/pawanpaudel93)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/pawanpaudel93/tiktok-long-video/issues). 

## Show your support

Give a ⭐️ if this project helped you!

Copyright © 2021 [Pawan Paudel](https://github.com/pawanpaudel93).<br />
