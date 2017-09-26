import webbrowser

class Movie():
    """Initalize a movie class with title, image, and youtube trailer URL
     Example:
     a_movie = media.Movie('Movie Title',
                            'Full URL to movie image',
                            'Full URL to trailer on YouTube')
    """

    def __init__(self, title, poster_image, trailer_video):
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_video