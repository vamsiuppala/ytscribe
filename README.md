# ytscribe

## Transcribe YouTube video
Has code to transcribe YouTube file into a txt file

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

## Certificate issues
If you run into ssl certification troubles, this command helped

``` python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```
