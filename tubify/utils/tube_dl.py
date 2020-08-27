from __future__ import unicode_literals
import youtube_dl
import os


'''
    class to download youtube to audio
'''


class Tubedl(object):
    def __init__(self):
        self.SAVE_PATH = os.path.join(os.getcwd(), 'songs')
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320'
            }],
            'outtmpl': self.SAVE_PATH + '/%(id)s.%(ext)s'
        }

    def get_audio(self, urls, dbx, dbx_path):
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            urllist = urls.split(',')[0]
            # ydl.download(urllist)
            try:
                info_dict = ydl.extract_info(urllist, download=True)
                video_id = info_dict.get('id', None)

                # dbx object to send to dbx
                fname = video_id+".mp3"
                local_file = self.SAVE_PATH+"/"+fname
                dbx.send_to_dbx(local_file, dbx_path+fname)
            except:
                pass
