<h1 align="center">Welcome to tiktok-long-video</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
</p>

A useful package/tool to make webm videos greater than 60s in length uploadable to TikTok.

## Usage

You can use as cli tool.
For help,
```python
tlv -h
```

Input filepath is must and output filepath is optional. For saving tiktok long video,
```python
tlv -i "/home/user/Desktop/sample.webm" -o "/home/user/Desktop/sample-tlv.webm"
```

OR

You can import and use in your programs. 
output_path is optional.
```python
from tlv import Video

video = Video(input_path="./sample.webm", output_path="./sample-tlv.webm")
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