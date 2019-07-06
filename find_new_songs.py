import requests, json, os.path

songList = []

def get_json_data(url):
    data = requests.get(url)
    return data.json()

def add_songs(musicData):
    for songData in enumerate(musicData):
        song = ("{} - {}".format(songData[1]['artist'],
                                 songData[1]['title']).lower())
        songList.append(song)

def get_songs(fileName):
    songsDict = {}

    # Create file if it doesn't exist yet.
    if (not os.path.isfile(fileName)):
        fh = open(fileName, 'w')
        fh.close()

    with open(fileName, 'r+') as songsFile:
        songsFile.seek(0)
        for song in songsFile:
            song = song.strip()
            songsDict[song] = song

    return songsDict

def write_new_songs(oldSongsDict, newSongsDict):
    with open('new_songs.txt', 'a+') as newSongsFile:
        for song in songList:
            if song not in oldSongsDict and song not in newSongsDict:
                newSongsFile.write("{}\n".format(song))

url = 'https://nowplaying.bbgi.com/WRBQFM/list?limit=100&offset=0'
musicData = get_json_data(url)

add_songs(musicData)

oldSongsDict = get_songs('song_list.txt')
newSongsDict = get_songs('new_songs.txt')

write_new_songs(oldSongsDict, newSongsDict)
