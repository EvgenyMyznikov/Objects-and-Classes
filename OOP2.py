class Album(Track):
    def __init__(self, band, album, track_list):
        self.band = band
        self.album = album
        self.track_list = track_list

        album_1 = Album("Metallica", "...And Justice for All", track_list)
        album_2 = Album("Wolfheart", "Winterborn", track_list)
        album_1.track_list = [{"The Shortest Straw": 7}, {"Harvester of Sorrow": 6}, {"To Live Is to Die": 10}]
        album_2.track_list = [{"The Hunt": 5}, {"Gale Of Winter": 5}, {"Ghosts Of Karelia": 5}]

    def get_tracks(self, track_list):
        for i in track_list:
            for track_name, track_duration in i.items():
                print(f'{track_name} - {track_duration}')
                return f'{track_name} - {track_duration}'

    def add_track(self, track_list):
        new_track = ""
        new_duration = 0
        track_list.append([new_track, new_duration])
        return "new track"

    def get_duration(self, track_list):
        sum_track_duration = 0
        for elem in track_list:
            for track_name, track_duration in elem.items():
                sum_track_duration += track_duration
                print(sum_track_duration)
        return sum_track_duration

