
import requests
import json
import webbrowser

class Media:

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", json=None):
        if json:
            if 'trackName' in json:
                self.title = json['trackName']
            else:
                self.title = json['collectionName']
        else:
            self.title = title
        self.author = json['artistName'] if json and json.get('artistName') else author
        self.release_year = json['releaseDate'][0:4] if json and json.get('releaseDate') else release_year
        self.url = json['collectionViewUrl'] if json and json.get('collectionViewUrl') else url

    def info(self):
        return f"{self.title} by {self.author} ({self.release_year})"

    def length(self):
        return 0

class Song(Media):

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", album="No Album", genre="No Genre", track_length=0, json=None):
        super().__init__(title, author, release_year, url, json)
        self.album = json['collectionName'] if json and json.get('collectionName') else album
        self.genre = json['primaryGenreName'] if json and json.get('primaryGenreName') else genre
        self.track_length = json['trackTimeMillis'] if json and json.get('trackTimeMillis') else track_length

    def info(self):
        return f"{Media.info(self)} [{self.genre}]"

    def length(self):
        return round(self.track_length / 1000)

class Movie(Media):

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", rating="No Rating", movie_length=0, json=None):
        super().__init__(title, author, release_year, url, json)
        self.rating = json['contentAdvisoryRating'] if json and json.get('contentAdvisoryRating') else rating
        self.movie_length = json['trackTimeMillis'] if json and json.get('trackTimeMillis') else movie_length

    def info(self):
        return f"{Media.info(self)} [{self.rating}]"

    def length(self):
        return round(self.movie_length / 60000)

# part 3: a function that can fatch data form the API and returns different result object lists
def get_info(json_info):
    songs = []
    movies = []
    others = []
    for item in json_info:
        if item.get('kind') == 'song':
            songs.append(Song(json=item))
        elif item.get('kind') == 'feature_movie':
            movies.append(Movie(json=item))
        else:
            others.append(Media(json=item))
    return songs, movies, others


# part 4: interactive command line and data processing
# a function that process the user input query and returns the clean data presented to the user in dictionary form
def process_data(query):
    baseurl = "https://itunes.apple.com/search?"
    parameter_dictionary = {'term': query}
    response = requests.get(baseurl, parameter_dictionary)
    json_info = json.loads(response.text)['results']
    songs, movies, others = get_info(json_info)
    return print_results(songs, movies, others)

# a finction that can use the object list produced by get_info function and print the simplified info to users
# it returns a dictionary with the index of each result as the key and the object as the value
def print_results(songs, movies, others):
    clean_data_dict = {}
    print('\nSONGS')
    for idx, song in enumerate(songs):
        print(f"{idx + 1} {song.info()}")
        clean_data_dict[idx + 1] = song
    song_list_length = len(songs)
    print('\nMOVIES')
    for idx, movie in enumerate(movies):
        print(f"{idx + song_list_length + 1} {movie.info()}")
        clean_data_dict[idx + song_list_length + 1] = movie
    song_and_movie_list_length = song_list_length + len(movies)
    print('\nOTHER MEDIA')
    for idx, other in enumerate(others):
        print(f"{song_and_movie_list_length + idx + 1} {other.info()}")
        clean_data_dict[song_and_movie_list_length + idx + 1] = other
    return clean_data_dict

if __name__ == "__main__":

    first_query = input('Enter a search term, or "exit" to quit: ')
    if first_query == 'exit':
        print('\nBye!')
        quit()
    else:
        clean_dict = process_data(first_query)
    while True:
        user_input = input('\nEnter a number for more info, or another search term, or exit: ')
        if user_input.isnumeric() and int(user_input) in clean_dict:
            this_url = clean_dict.get(int(user_input)).url
            print(f"Launching\n{this_url}\nin web browser...")
            wb = webbrowser.get('chrome')
            wb.open(this_url)
        elif user_input == 'exit':
            print('\nBye!')
            break
        else:
            clean_dict = process_data(user_input)