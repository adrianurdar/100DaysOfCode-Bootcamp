from bs4 import BeautifulSoup
import requests

SITE_LINK = "https://www.empireonline.com/movies/features/best-movies-2/"

res = requests.get(url=SITE_LINK)
webpage = res.text

soup = BeautifulSoup(webpage, "html.parser")

movie_tags = soup.find_all("h3", "title")
movie_titles = [movie_tag.get_text() for movie_tag in movie_tags]
movie_titles.reverse()
movie_titles[0] = f"1) {movie_titles[0]}"
print(movie_titles)

with open("movies.txt", "w") as file:
    for movie_title in movie_titles:
        file.write(f"{movie_title}\n")