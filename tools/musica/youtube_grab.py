from __future__ import unicode_literals
import youtube_dl, requests, threading
from youtube_search import YoutubeSearch
def youtube_download(link,name='youtube_last'):
    ydl_opts = {
    'outtmpl': f'{FOXDOT_LOOP}/{name}.mp3',
   # 'outtmpl': f'{name}.mp3',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': False
}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
# youtube_download(['https://www.youtube.com/watch?v=BaW_jenozKc'],name='pruebita')
def youtube_search(terms, max_results=10):
    content = YoutubeSearch(terms, max_results=max_results).to_dict()
    for each in content:
        titulo = each['title']
        print(f'Video {content.index(each)}: {titulo}')
    return(content)
def youtube_getlink(term,number):
    content = youtube_search(term)
    link = content[number]['link']
    full_link = f'https://youtube.com{link}'
    print(full_link)
    return full_link
def youtube_grab(term, number,name='youtube_last'):
    link = youtube_getlink(term, number)
    try:
        youtube_download(link,name=name)
        print('Finalizo la descarga')
    except:
        print('Error: fijate si el archivo ya existe.')
        print('No se descargo el sonido.')
def yt_grab(term,number,name='youtube_last'):
    t = threading.Thread(target=youtube_grab, args=(term, number), kwargs={'name': name})
    t.start()
    
# SEARCH

youtube_search('a la grande le puse cuca')

"""
>>youtube_search('a la grande le puse cuca')
Video 0: A la grande le puse cuca- Los Simpsons latino
Video 1: A la grande le puse cuca [Los Simpson - Latino]
Video 2: los simpson-a la grande le puse cuca(parte 1 y 2)
Video 3: A La Grande Le Puse Cuca - Los Simpson Latino
Video 4: Marge contra el Monorriel (Parte 1/5) Los Simpson
"""

youtube_getlink('livecoding',0)

"""
>>youtube_getlink('livecoding',0)
https://youtube.com/watch?v=7Hlb8YX2-W8
"""

yt_grab('a la grande le puse cuca',0,name='grande_cuca')
#Starts a thread to download the sample. It saves it in the _loop_ folder so that it can be used ASAP.
p1 >> loop('grande_cuca',P[:50])


