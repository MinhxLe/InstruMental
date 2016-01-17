from pytube import YouTube
# not necessary, just for demo purposes.
from pprint import pprint
class MusicScraper:
    sadSongs = [{"title": "Yiruma - River Flows In You", "url": "https://www.youtube.com/watch?v=XsTjI75uEUQ"},
                {"title": "Bearface - Hotline Bling", "url": "https://www.youtube.com/watch?v=bb3oqArH0G4"},
                {"title": "First Love - Joe Hisaishi", "url": "https://www.youtube.com/watch?v=iJavCNjXgsI"},
                {"title": "A Good One - After The Rain", "url": "https://www.youtube.com/watch?v=hiqCQarvZUM"},
                {"title": "NAK X Elyon Beats - 23 Prayers", "url": "https://www.youtube.com/watch?v=PK1z5uc_21o"},
                {"title": "NAK x Wy-i Night Sky", "url": "https://www.youtube.com/watch?v=SN76eL5S8W0"},
                {"title": "Alina Baraz & Galimatias - Urban Flora EP", "url": "https://www.youtube.com/watch?v=7nB4hLP5yKM"},
                {"title": "Michl - Kill Our Way To Heaven", "url": "https://www.youtube.com/watch?v=zAPhp9LYq44"}]

    happySongs = [{"title": "RL Grime - Core", "url": "https://www.youtube.com/watch?v=04ufimjXEbA"},
                {"title": "Bro Safari - The Drop", "url": "https://www.youtube.com/watch?v=XxGmgmelZV0"},
                {"title": "Keys N Krates - Dreamyness", "url": "https://www.youtube.com/watch?v=mPV3-DKiCME"},
                {"title": "Lil' Wayne - A Milli (K Theory Remix)", "url": "https://www.youtube.com/watch?v=xlDLd8MBkeE"},
                {"title": "Kaytranada - Killa Cats", "url": "https://www.youtube.com/watch?v=9406dsecgBA"},
                {"title": "Psychic Type - Victory Road", "url": "https://www.youtube.com/watch?v=bE8sjRUjiUI"},
                {"title": "Fifth Harmony - Worth It ft. Kid Ink", "url": "https://www.youtube.com/watch?v=YBHQbu5rbdQ"}]

    def loadTube(self, link):
        '''
        :param link: string representing https:// link
        :return: YouTube
        '''
        yt = YouTube(link)
        return yt

    def download(self, yt, fileName):
        # You can also filter the criteria by filetype.
        try:
            pprint(yt.filter('mp4')[-1])
        except IndexError: # file type does not exist for download
            return
        try:
            video = yt.get('mp4', '360p')
            video.download(fileName)
        except:
            pass


