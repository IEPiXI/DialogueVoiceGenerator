import pytube
import os
from moviepy.editor import *

class YTDownloader():

    def __init__(self, url, resolution):
        self.video_streams = pytube.YouTube(url).streams
        self.resolution = resolution
        self.filtered_stream = self.filter_stream()
        self.filename = "".join(x for x in self.filtered_stream.title if x.isalnum()) + ".mp4"
        self.fps = self.filtered_stream.fps

    def filter_stream(self):
        filtered_stream = self.video_streams.filter(file_extension="mp4").filter(resolution=self.resolution)[0]
        return filtered_stream
    
    def download(self):
        if not os.path.exists(self.filename):
            self.filtered_stream.download(filename=self.filename)

class VideoEditHelper():

    def cut_video(self, old_filename, new_filename, fps, start, end):
        video = VideoFileClip(old_filename).subclip(start, end)
        video.write_videofile(new_filename, fps=fps)

    def set_audio(self, audio_clip_title, video_clip_title):
        videoclip = VideoFileClip(video_clip_title)
        audioclip = AudioFileClip(audio_clip_title)
        videoclip.set_audio(audioclip)