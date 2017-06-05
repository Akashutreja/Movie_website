import fresh_tamatoes
from media import Movie

# bhaubali is instance of movie class.
bhaubali = Movie("Bahubali",
                 "A story of mahendra bhaubali",
                 "images/2.jpg",
                 "https://www.youtube.com/watch?v=qD-6d8Wo3do",
                 "It's awesome")

# poc is instance of movie class
poc = Movie("pirates of caribbean",
            "A story of a caribbean",
            "images/1.jpg",
            "https://www.youtube.com/watch?v=lsJ58L3u8qw",
            "one time watch")
# hindi_medium is instance of movie class
hindi_medium = Movie("Hindi Medium", "A story of a poor guy",
                     "/images/4.jpg",
                     "https://www.youtube.com/watch?v=GjkFr48jk68",
                     "can guess concept by title")

# Got is instance of movie class
Got = Movie("Game of Thrones", "A story of a kingdom",
            "imgaes/3.jpg",
            "https://www.youtube.com/watch?v=rbNWMGecNcM", "it's thrilling")
# movie_list will contain all movies objects
movies_list = [bhaubali, poc, hindi_medium, Got]
# fresh_tamatoes's function open_movie_page will open our website
fresh_tamatoes.open_movies_page(movies_list)
