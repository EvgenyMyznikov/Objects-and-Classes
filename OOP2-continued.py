class Track:
    def __init__(self, name='', duration=0):
        self.name = name
        self.duration = duration

    def track_info(self):
        print(self.__str__())

    def __str__(self):
        return (f'{self.name} - {self.duration}')


class Album(Track):
    def __init__(self, band='', name=''):
        self.band = band
        self.name = name
        self.tracks = []

    def album_info(self):
        print(self.__str__())

    def __str__(self):
        for track in self.tracks:
            return self.tracks

    def get_duration(self):
        return sum([track.duration for track in self.tracks])

    def add_track(self, track):
        if not isinstance(track, Track):
            raise NotImplementedError('Can not add this object to track list!')
        self.tracks.append(track)


albums = []
album = Album("Metallica", "...And Justice for All")
album.add_track(Track("The Shortest Straw", 7))
album.add_track(Track("Harvester of Sorrow", 6))
album.add_track(Track("To Live Is to Die", 10))
albums.append(album)

album = Album("Wolfheart", "Winterborn")
album.add_track(Track("The Hunt", 5))
album.add_track(Track("Gale Of Winter", 5))
album.add_track(Track("Ghosts Of Karelia", 5))
albums.append(album)

for album in albums:
    print(f'Album "{album.name}" of band {album.band}:')
    for track in enumerate(album.__str__(), 1):
        print(f'{track[0]}. {track[1]}')
    print(f'Album total length: {album.get_duration()} minutes\n')
