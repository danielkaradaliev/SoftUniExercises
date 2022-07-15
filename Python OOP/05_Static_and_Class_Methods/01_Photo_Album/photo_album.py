class PhotoAlbum():
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [list() for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls((photos_count // 4) + int(bool(photos_count % 4)))

    def add_photo(self, label: str):
        for index, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(page)}"
        else:
            return "No more free slots"

    def display(self):
        linesep = "\n"
        page_separation = "-" * 11
        result = page_separation + linesep
        for page in self.photos:
            result += " ".join(["[]" for _ in range(len(page))]) + linesep + page_separation + linesep

        return result


def main():
    album = PhotoAlbum(2)

    print(album.add_photo("baby"))
    print(album.add_photo("first grade"))
    print(album.add_photo("eight grade"))
    print(album.add_photo("party with friends"))
    print(album.photos)
    print(album.add_photo("prom"))
    print(album.add_photo("wedding"))

    print(album.display())


if __name__ == "__main__":
    main()
