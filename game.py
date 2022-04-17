class Game:
    def __init__(self, name="No Name",summary="No Summary", id=0,rating = 0, release_year = "No Release Year",generes ='No genre',metacritic = None, json = None):
        if(json is None):
            self.name=name
            self.genres = genres
            self.release_year=release_year
            self.id=id
            self.metacritic=metacritic
            self.rating = rating
            self.summary = summary
        else:
            self.name = json["name"]
            try:
                self.summary = json['summary']
            except:
                self.summary = "No Summary"
            try:
                self.genres = json['genres']
            except:
                self.genres = []
            try:
                self.rating = json['total_rating']
            except:
                self.rating = 0
            if self.genres == []:
                self.genres = 'N/A'
            try:
                self.release_year=json["released"][:4]
            except:
                try:
                    self.release_year=json["release_dates"][:4]
                except:
                    self.release_year=None
            self.id = json['id']
            try:
                self.metacritic=json['metacritic']
            except:
                self.metacritic = None
            if self.metacritic == None:
                self.metacritic = 'N/A'