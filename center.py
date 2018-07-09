import media
import fresh_tomatoes

#declares new instances of the movie class and sets their peramiters 
TheMatrix = media.Movie("The Matrix",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/"
                        "The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
                        "https://www.youtube.com/watch?v=Q8g9zL-JL8E")
Harmony = media.Movie("Harmony",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/"
                      "Harmony_%282015_film%29_poster.jpeg"
                      "/220px-Harmony_%282015_film%29_poster.jpeg",
                      "https://www.youtube.com/watch?v=9zsdRecN4PI")
TheLastSamurai = media.Movie("The Last Samurai",
                             "https://upload.wikimedia.org"
                             "/wikipedia/en/thumb/c/c6/"
                             "The_Last_Samurai.jpg/220px-The_Last_Samurai.jpg",
                             "https://www.youtube.com/watch?v=T50_qHEOahQ")

# declares a list of movie objects
movies = [TheMatrix, Harmony, TheLastSamurai]
# calls the open_movie_page method
# from the fresh tomatoes class to create our web page
fresh_tomatoes.open_movies_page(movies)
