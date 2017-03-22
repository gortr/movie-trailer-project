import fresh_tomatoes
import movie_media


# This is an instance. Movie seclection #1
krampus = movie_media.Movie(
	"Krampus",
	"Storyline",
	"https://upload.wikimedia.org/wikipedia/en/1/1e/Krampus_poster.jpg",
	"https://www.youtube.com/watch?v=h6cVyoMH4QE")

print(krampus.storyline)

jurassic_world = movie_media.Movie(
	"Jurassic World",
	"Storyline",
	"https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg",
	"https://www.youtube.com/watch?v=RFinNxS5KN4")

print(jurassic_world.storyline)

deadpool = movie_media.Movie(
	"Deadpool",
	"Storline",
	"https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
	"https://www.youtube.com/watch?v=9vN6DHB6bJc")

print(deadpool.storyline)

scott_pilgrim = movie_media.Movie(
	"Scott Pilgrim vs. the World",
	"Storyline",
	"https://upload.wikimedia.org/wikipedia/en/1/14/Scott_Pilgrim_vs._the_World_teaser.jpg", # noqa
	"https://www.youtube.com/watch?v=O_RrNCqCIPE")

print(scott_pilgrim.storyline)

interstellar = movie_media.Movie(
	"Interstellar",
	"Storyline",
	"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
	"https://www.youtube.com/watch?v=0vxOhd4qlnA")

print(interstellar.storyline)

prometheus = movie_media.Movie(
	"Prometheus",
	"Storyline",
	"https://upload.wikimedia.org/wikipedia/en/a/a3/Prometheusposterfixed.jpg",
	"https://www.youtube.com/watch?v=sftuxbvGwiU")

print(prometheus.storyline)

john_wick = movie_media.Movie(
	"John Wick",
	"A retired assassain brought back in the game for revenge",
	"https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
	"https://www.youtube.com/watch?v=2AUmvWm5ZDQ")

print(john_wick.storyline)

# Array to store the above movies info.
movies = [krampus, jurassic_world, deadpool, scott_pilgrim, interstellar, prometheus, john_wick]
# Array above then gets used as input for the below function.
fresh_tomatoes.open_movies_page(movies)