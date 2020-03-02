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

youtube_search('livecoding')

/*
Video 0: George Hotz | Programming | Livecoding SLAM | twitchslam | Part1
Video 1: Joel Grus - Livecoding Madness - Let's Build a Deep Learning Library
Video 2: Sam Aaron live coding an ambient electro set w/ Sonic Pi
Video 3: 12 Hour Coding Livestream - Creating an Online Game with Python
Video 4: Live-Coding – programming masterly music  | Juan Romero & Patrick Borgeat | TEDxKIT
Video 5: DOMMUNE Tokyo - live coding performances - algorave tokyo x yorkshire
Video 6: Live Stream: TidalCycles Livecoding Improv
Video 7: George Hotz | Programming | twitchchess | a simple neural chess AI | Part1
Video 8: Live Coding with AWS: Dockerizing a Web App - Part 1
Video 9: Taller de LiveCoding
*/
