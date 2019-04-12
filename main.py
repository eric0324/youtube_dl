# -*- coding: UTF-8 -*-
from argparse import ArgumentParser
import subprocess
import youtube_dl


def DownloadMP3(url, file_name):
    ydl_opts = {
    'outtmpl': 'output/'+file_name+'.webm',
    'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    subprocess.call(["play", "output/"+file_name+".mp3"])

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-url", help="Input youtubeurl")
    parser.add_argument("-fname", help="Input file name")
    args = parser.parse_args()

    DownloadMP3(args.url, args.fname)
