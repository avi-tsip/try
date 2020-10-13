import requests
import json
import unittest
from datetime import datetime, timedelta

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
now = datetime.now()
format = "%Y-%m-%d"
end_date = now.strftime(format) 
delta = datetime.now() - timedelta(days=7)
start_date = delta.strftime(format)

update_movies_list = []
response = requests.get('https://api.themoviedb.org/3/movie/489326/images?api_key=cc9771a7d70090169469155420aac01e')
update_movies_response = json.loads(response.text)
print(update_movies_response['posters'])
print(response.status_code)
      
