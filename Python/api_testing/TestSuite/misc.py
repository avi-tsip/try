import requests
import json
import unittest
from datetime import datetime, timedelta
import urllib
from urllib.error import HTTPError

# movies_list = []
# page_count = 10
# movie_total_count = 1
# while (len(movies_list) <= 49):
#     response = requests.get(r'https://api.themoviedb.org/3/movie/changes?api_key=cc9771a7d70090169469155420aac01e&page=' + str(page_count))
#     json_response = json.loads(response.text)
#     json_of_movies = (json_response['results'])
#     for movie in json_of_movies:
#         if (movie_total_count <= 50):
#             movies_list.append(movie)
#             movie_total_count += 1
#     page_count +=1
# print(movies_list[0])

# now = datetime.now()
# format = "%Y-%m-%d"
# end_date = now.strftime(format)
# delta = datetime.now() - timedelta(days=7)
# start_date = delta.strftime(format)

# update_movies_list = []
# response = requests.get('https://api.themoviedb.org/3/movie/489326/images?api_key=cc9771a7d70090169469155420aac01e')
# update_movies_response = json.loads(response.text)
# print(update_movies_response['posters'])
# print(response.status_code)

base_url = r'https://image.tmdb.org/t/p/original'
image_count = 0
index = 0
while (index <= 49):
    movie_id = popular_movies_list[index]['id']
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/images?api_key=cc9771a7d70090169469155420aac01e')
    assertEqual(response.status_code, 200)
    images_response = json.loads(response.text)
    path_of_images = images_response['posters'][image_count]['file_path']
    while (image_count <= 9 or image_count <= len(images_response['posters']) - 1):
        try:
            urllib.request.urlretrieve(base_url + path_of_images)
        except HTTPError:
            print(f'could not download {path_of_images} image')
        image_count += 1
    index += 1
    image_count = 0
