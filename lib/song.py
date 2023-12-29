class Song:
    pass

    count = 0    
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_genre_count(genre)
        Song.add_to_artists(artist)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment
        
    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)
        
    @classmethod
    def add_dict_count(cls, dict_name, key, increment = 1):
        dict_count = cls.genre_count if (dict_name == "genre") else cls.artist_count
        if (dict_count.get(key) == None):
            dict_count[key] = 1
        else:
            dict_count[key] += increment
        
    @classmethod
    def add_to_genre_count(cls, genre, increment = 1):
        cls.add_dict_count("genre", genre, increment)
            
    @classmethod
    def add_to_artist_count(cls, artist, increment = 1):
        cls.add_dict_count("artist", artist, increment)