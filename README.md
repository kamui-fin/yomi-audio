# Yomichan Audio Server

Although Yomichan does support custom audio URLs, it doesn't solve the problem of using a local directory.
Instead of having to mess with nginx configs, with yomi-audio, you can easily start an audio server and
pass it to Yomichan to pull pronunciation directly from your local filesystem.

The directories passed into the CLI are sorted in ascending order by name. This can be leveraged to prioritize results from directories that contain higher quality audio.

## Installation

```
git clone https://github.com/kamui-fin/yomi-audio
cd yomi-audio
pip install -r requirements.txt
```

## CLI

TBD...
