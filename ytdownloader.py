import pytube

class YTDownloader():

    def getResolutions(self, streams):
        res = []
        """for stream in streams:
            if ("progressive="True"") in str(stream):
                try:
                    resolution = str(stream).split("res="")[1].split("p"")[0]
                    if resolution not in res:
                        res.append(resolution)
                except:
                    continue
        res = [int(x) for x in res]
        res.sort()"""
        return res

    def getItagByResolution(self, streams,resolution):
        for stream in streams:
            pass

    def __init__(self, url):
        video = pytube.YouTube(url)
        print(video.streams.filter(file_extension="mp4"))
     