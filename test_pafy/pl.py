import sys
import os

import pafy

early_py_version = sys.version_info[:2] < (2, 7)


def download(video, audio=False, stream=None):
    """ Download a video. """

    if not stream and not audio:
        stream = video.getbest(preftype="mp4")

    if not stream and audio:
        stream = video.getbestaudio()

    print stream.extension

    size = stream.get_filesize()
    dl_str = "-Downloading '{0}' [{1:,} Bytes]"

    if early_py_version:
        dl_str = "-Downloading '{0}' [{1} Bytes]"

    #xprint(dl_str.format(stream.filename, size))
    #xprint("-Quality: %s; Format: %s" % (stream.quality, stream.extension))
    stream.download(quiet=False, filepath="tracks/")
    #xprint("\nDone")
    print("done")




def fetchPlaylistAndDownload(playlistID):


    playlist = pafy.get_playlist(playlistID)


    for item in playlist['items']:
        meta = item['playlist_meta']
        title = meta['title']
        added = meta['added']
        #print meta
        #print item['pafy'].videoid
        print title
        #print "\n\n"
        download(item['pafy'], audio=False)
        #print(title + ' was published on ' + added)
        print("")


def fetchOneSongAndDownload(songID):
    vid = pafy.new(songID)
    #print vid.keywords
    download(vid, audio=True)



if __name__ == '__main__':
    fetchPlaylistAndDownload("RDFZu097wb8wU")

    #fetchOneSongAndDownload("SmM0653YvXU")
