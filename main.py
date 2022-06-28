import datetime
from pytube import YouTube
from pathlib import Path

def on_complete(stream, filepath):
    print('Download Complete')
    print(filepath)

def on_progress(stream, chunk, bytes_remaining):
    progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100), 2)}%'
    print(progress_string)
  
def convert(n):
    return str(datetime.timedelta(seconds = n))

link = input('YouTube link: ')
video_object = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)

# Video Information
print(f'Title:  {video_object.title}')
print(f'Length: {convert(video_object.length)}')
print('Views:  {:,}'.format(video_object.views))
print(f'Author: {video_object.author}')

# Download
print('Download: (B)est | (W)orst | (A)udio')
download_choice = input()
downloads_path = str(Path.home() / "Downloads")

match download_choice.upper():
    case 'B':
        video_object.streams.get_highest_resolution().download(downloads_path)
    case 'W':
        video_object.streams.get_lowest_resolution().download(downloads_path)
    case 'A':
        video_object.streams.get_audio_only().download(downloads_path)

input('Press ENTER to exit: ')