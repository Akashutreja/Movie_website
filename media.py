import webbrowser
class Movie():
	"""This class store movie related information"""
	VALID_STRINGS=["G","R","RG","RG-13"]
	def __init__(self,title,story_line,poster,movie_trailer,review):
		self.title=title
		self.story_line=story_line
		self.trailer_youtube_url=movie_trailer
		self.poster_image_url=poster
		self.review=review

	def show_trailer(self):
		webbrowser.open(self.movie_trailer_url)