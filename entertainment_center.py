import fresh_tamatoes
from media import Movie
bhaubali=Movie("Bahubali","A story of mahendra bhaubali",r"http://moviecorner.in/wp-content/uploads/2017/02/Bhaubali-2.jpg",r"https://www.youtube.com/watch?v=qD-6d8Wo3do")
poc=Movie("pirates of caribbean","A story of a caribbean",r"https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-nie8b7_49ceb417.jpeg?region=0,0,300,450",r"https://www.youtube.com/watch?v=lsJ58L3u8qw")
#print(bhaubali.story_line)
#bhaubali.show_trailer()
#poc.show_trailer()
hindi_medium=Movie("Hindi Medium","A story of a poor guy",r"https://upload.wikimedia.org/wikipedia/en/d/db/Hindi_Medium_Poster.jpg",r"https://www.youtube.com/watch?v=GjkFr48jk68")
Got=Movie("Game of Thrones","A story of a kingdom",r"http://media.moddb.com/images/members/1/123/122021/profile/c9lzmv4d3mgzpnyntz7s.jpg",r"https://www.youtube.com/watch?v=rbNWMGecNcM")
#movies_list=[bhaubali,poc,hindi_medium,Got]
#fresh_tamatoes.open_movies_page(movies_list)
#print(Movie.VALID_STRINGS)
print(Movie.__doc__)
print(Movie.__name__)
print(Movie.__module__)