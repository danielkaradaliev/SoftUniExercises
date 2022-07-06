class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = list()

    def add_album(self, album):
        if album.name in [x.name for x in self.albums]:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        if album_name not in [x.name for x in self.albums]:
            return f"Album {album_name} is not found."

        for index, album in enumerate(self.albums):
            if album.name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                self.albums.pop(index)
                return f"Album {album.name} has been removed."

    def details(self):
        linesep = "\n"
        info = f"Band {self.name}{linesep}" + linesep.join([x.details() for x in self.albums])
        return info
