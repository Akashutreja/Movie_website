import webbrowser


class Movie():
    """This class store movie related information"""

    def __init__(self, title, story_line, poster, movie_trailer, review):
        """this function will be called when a movie object is created
        keyword argument:
        self -- as a reference which called the constructor
        title -- a movie title
        story_line -- a movie story line
        poster -- a movie poster
        trailer -- a movie trailer
        review -- a movie review
        """
        self.title = title
        self.story_line = story_line
        self.trailer_youtube_url = movie_trailer
        self.poster_image_url = poster
        self.review = review

    def show_trailer(self):
        """ this function will open specific trailer
        a movie"""
        webbrowser.open(self.movie_trailer_url)
