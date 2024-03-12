### Transcribe YouTube video
Has code to transcribe any YouTube video

### Certificate issues
If you run into ssl certification troubles, this command helped

``` python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```