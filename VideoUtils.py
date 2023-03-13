import pytube
import os
from moviepy.editor import *
import imagesize


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

    def cut_video(self, old_filename, new_filename, start, end):
        video = VideoFileClip(old_filename).subclip(start, end)
        video.write_videofile(new_filename)

    def set_audio(self, audio_clip_title, video_clip_title,new_filename):
        videoclip = VideoFileClip(video_clip_title)
        audioclip = AudioFileClip(audio_clip_title)
        
        new_videoclip = videoclip.set_audio(audioclip)
        new_videoclip.write_videofile(new_filename)
    
    def finalize_video(self,images_path, list_talk_duration, audio_clip_title, video_clip_title,new_filename):
        videoclip = VideoFileClip(video_clip_title)
        video_width,video_height = (videoclip.w,videoclip.h)
        audioclip = AudioFileClip(audio_clip_title)
        new_videoclip = videoclip.set_audio(audioclip)

        final_video_array = [new_videoclip]
        time_stamp = 0
        for _tuple in list_talk_duration:
            name, time = _tuple
            image = images_path+name+".png"
            image_width, image_height = imagesize.get(image)
            xpos=0.3
            if name == "Trump":
                xpos=0.6
            final_video_array.append(ImageClip(image).set_start(time_stamp).set_duration(time).set_pos(((xpos*video_width)-(image_width/2),video_height-image_height)))
            time_stamp += time
        	
        new_videoclip = CompositeVideoClip(final_video_array)

        new_videoclip.write_videofile(new_filename)

