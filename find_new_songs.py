import requests, json, os.path

songList = []

def get_json_list(url):
    data = requests.get(url)
    return data.json()

def add_songs(songDataList):
    for songDataTuple in enumerate(songDataList):
        song = ("{} - {}".format(songDataTuple[1]['artist'],
                                 songDataTuple[1]['title']).lower())
        songList.append(song)

def get_songs(fileName):
    songsDict = {}

    if (not os.path.isfile(fileName)): # create file if it doesn't exist yet
        fh = open(fileName, 'w')
        fh.close()

    with open(fileName, 'r+') as songsFile:
        songsFile.seek(0)
        for song in songsFile:
            song = song.strip()
            songsDict[song] = song

    return songsDict

def write_new_songs(oldSongsDict, newSongsDict):
    with open('newsongs.txt', 'a+') as newSongsFile:
        for song in songList:
            if song not in oldSongsDict and song not in newSongsDict:
                newSongsFile.write("{}\n".format(song))

url = 'https://nowplaying.bbgi.com/WRBQFM/list?limit=100&offset=0'
songDataList = get_json_list(url)

add_songs(songDataList)

oldSongsDict = get_songs('songlist.txt')
newSongsDict = get_songs('newsongs.txt')

write_new_songs(oldSongsDict, newSongsDict)
