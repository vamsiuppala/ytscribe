import pytube as pt
import whisper
import os
import re
import ssl

def replace_special_chars(text):
    # Define the pattern to match special characters and spaces
    pattern = r'[^a-zA-Z0-9]+'
    # Replace the matched pattern with underscores
    replaced_text = re.sub(pattern, '_', text)
    return replaced_text


ssl._create_default_https_context = ssl._create_unverified_context

model = whisper.load_model('base')

def download_video_and_transcribe(video_url, directory, output_filename = 'title'):
    
    # create the directory
    os.makedirs(directory, exist_ok=True)

    # define video
    yt = pt.YouTube(video_url)
    # get title
    title_name = (replace_special_chars(yt.title))
    
    if output_filename == 'title':
        video_name = title_name
    else:
        video_name = output_filename
    
    # download video
    stream = yt.streams.filter(only_audio=True)[0]
    stream.download(filename = directory + '/' + video_name + '.wav')

    # transcribe video
    result = model.transcribe(directory + '/' + video_name + '.wav')

    # Open a text file and write transcription in it
    with open(directory + '/' + video_name + '.txt', 'w') as file:
        # Write some text to the file
        file.write(result['text'])
        file.close()

    # delete video file
    if os.path.exists(directory + '/' + video_name + '.wav'):
        os.remove(directory + '/' + video_name + '.wav')
