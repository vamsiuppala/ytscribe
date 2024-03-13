# ytscribe

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A simple library that allows you to transcribe any single person YouTube video into a text file using OpenAI's Whisper module. 

## Setup
1. Clone this library and cd into the ytscribe folder:
```
git clone https://github.com/vamsiuppala/ytscribe.git
cd ytscribe
```

2. Install dependencies
```
pip install -r requirements.txt
```
### From PIP
You can also install the library from pip
```
pip install ytscribe
```

## Transcribe YouTube video
### Step 1. Get the link to the YouTube video you're interested in
1. This package has one main module that takes YouTube link and simply transcribes it.
2. Pick a video that only has a single speaker since Whisper doesn't differentiate between multiple speakers
3. As an example, let's pick one of MKBHD's videos from [AutoFocus](https://www.youtube.com/@AutoFocus) - https://www.youtube.com/watch?v=CRhjL9X2yKA

### Step 2. Pass on the YouTube video link
```python

video_url = "https://www.youtube.com/watch?v=CRhjL9X2yKA"
directory = "files"
from ytscribe import transcribe

# transcribe
transcribe.download_video_and_transcribe(video_url, directory, output_filename = 'title', whisper_model = 'base')

```
The above bit should create a folder called ``files`` and add the transcribed YouTube video as a txt file. 

## Speed
On my 16GB M1 Pro Macbook Pro, a 20 minute video took around 2 minutes to get downloaded and transcribed

## Certificate issues
If you run into ssl certification troubles, this command helped me

``` python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```
