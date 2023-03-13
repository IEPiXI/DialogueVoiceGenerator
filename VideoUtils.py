import pytube
from moviepy.editor import *

class YTDownloader():

    def __init__(self, url, resolution):
        self.video_streams = pytube.YouTube(url).streams
        self.resolution = resolution
        self.filtered_stream = self.filter_stream()
        self.title = "".join(x for x in self.filtered_stream.title if x.isalnum())
        self.fps = self.filtered_stream.fps

    def filter_stream(self):
        filtered_stream = self.video_streams.filter(file_extension="mp4").filter(resolution=self.resolution)[0]
        return filtered_stream
    
    def download(self):
        self.filtered_stream.download(filename=self.title+".mp4")

class VideoEditHelper():

    def cut_video(self,title,fps,start,end):
        video = VideoFileClip(f"{title}.mp4").subclip(start,end)
        video.write_videofile(f"{title}_cut.mp4",fps=fps)