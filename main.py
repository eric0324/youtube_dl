from argparse import ArgumentParser

import youtube_dl

ydl_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}]
}


def DownloadMP3(url):		
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])	

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-url", help="Input youtubeurl")
    args = parser.parse_args()

    DownloadMP3(args.url)
