# Yomichan Audio Server

Although Yomichan does support custom audio URLs, it doesn't solve the problem of using a local directory.
Instead of having to mess with nginx configs, with yomi-audio, you can easily start an audio server and
pass it to Yomichan to pull pronunciation directly from your local filesystem.

## Setup

Python and pip are required to run the server. Clone the repository and install the necessary dependencies:

```
git clone https://github.com/kamui-fin/yomi-audio && cd yomi-audio
pip install -r requirements.txt
```

### Running locally

The script offers a CLI that customizes the behavior of the server and starts it. The main required option is `-d` or `--directories` to specify the location of one or more directories containing the audio files. For example:

```
python app.py -d /home/user/audio_bank
```

### Sorting

By default, the original order in which they were specified is retained without any sorting.

With the `-s` flag, the directories passed in are sorted in ascending order by name. This can be leveraged to prioritize results from directories that contain higher quality audio.

### Pattern matching

The default pattern for matching audio files is `{term}.mp3`.
Obviously, this may not suffice depending on the naming scheme.
As a result, there are two different ways to customize the way the _correct_ file is found.

With both ways, the `term` and `reading` must be surrounded by `{}` as a template literal, where they will be later replaced during matching.

One way is to use `-p` to directly match using a completely static/pre-defined naming pattern. This can be useful if the underlying naming scheme of the directory does not vary. For example, if all the files are named like `pronunciation_喜欢.mp3`, you can simply use the static pattern `pronunciation_{term}.mp3`.

The other way with `-g` utilizes powerful [glob](<https://en.wikipedia.org/wiki/Glob_(programming)>) functionality. An example would be `???{term}???.mp3` to match `{term}` with 3 leading and trailing characters.

## Connecting to Yomichan

Once you have the server running, open Yomichan settings. Click "Configure audio playback sources" under the Audio section and add the following custom URL:

```
http://localhost:5000/?expression={term}&reading={reading}
```


