class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.songs = [x for x in args]
        self.published = False

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song.name in [x.name for x in self.songs]:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if song_name not in [x.name for x in self.songs]:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        for index, song in enumerate(self.songs):
            if song.name == song_name:
                self.songs.pop(index)
                return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return "Album {name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        linesep = "\n"
        info = f"Album {self.name}{linesep}" + linesep.join([f"== {song.get_info()}" for song in self.songs])
        return info
