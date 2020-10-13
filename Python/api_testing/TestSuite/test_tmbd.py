import requests
import json
import unittest
from datetime import datetime, timedelta
import urllib
from urllib.error import HTTPError

class ApiTestCase(unittest.TestCase):

    def setUp(self):
        ''' This methods creates the artifacts needed for the rest of the tests
            Since there is a limit for 20 results per page, we need to iterate over 3 pages and create a list of the first movies'''
        self.popular_movies_list = []
        page_count = 1
        movie_total_count = 1
        while (len(self.popular_movies_list) <= 49):
            response = requests.get(r'https://api.themoviedb.org/3/movie/popular?api_key=cc9771a7d70090169469155420aac01e&page=' + str(page_count)) 
            popular_response = json.loads(response.text)
            json_of_popular_movies = (popular_response['results'])
            for movie in json_of_popular_movies:
                if (movie_total_count <= 50):
                    self.popular_movies_list.append(movie)
                    movie_total_count += 1
            page_count +=1
        # Setting up the datetime variables
        now = datetime.now()
        format = "%Y-%m-%d"
        self.end_date = now.strftime(format) 
        delta = datetime.now() - timedelta(days=7)
        self.start_date = delta.strftime(format)
        # Create a list of movie id's that were updated in the last 7 days
        self.update_movies_list = []
        response = requests.get(f'https://api.themoviedb.org/3/movie/changes?api_key=cc9771a7d70090169469155420aac01e&page=1&start_date={self.start_date}&end_date={self.end_date}')
        update_movies_response = json.loads(response.text)
        json_of_updated_movies = update_movies_response['results']
        for movie in json_of_updated_movies: 
            self.update_movies_list.append(movie['id'])



    def test_key_type(self):
        ''' In this test I am iterating over the list of movies dicts and checking each key's type is correct '''
        index = 0
        while (index <= 49):
            self.assertEqual(type(self.popular_movies_list[index]['popularity']), float)
            self.assertEqual(type(self.popular_movies_list[index]['vote_count']), int)
            self.assertEqual(type(self.popular_movies_list[index]['video']), bool)
            self.assertTrue(type(self.popular_movies_list[index]['poster_path']), str or None)
            self.assertEqual(type(self.popular_movies_list[index]['id']), int)
            self.assertEqual(type(self.popular_movies_list[index]['adult']), bool)
            self.assertTrue(type(self.popular_movies_list[index]['backdrop_path']), str or None)
            self.assertEqual(type(self.popular_movies_list[index]['original_language']), str)
            self.assertEqual(type(self.popular_movies_list[index]['original_title']), str)
            self.assertEqual(type(self.popular_movies_list[index]['genre_ids']), list)
            self.assertEqual(type(self.popular_movies_list[index]['title']), str)
            self.assertTrue(type(self.popular_movies_list[index]['vote_average']), float or int)
            self.assertEqual(type(self.popular_movies_list[index]['overview']), str)
            self.assertEqual(type(self.popular_movies_list[index]['release_date']), str)
            index += 1

    def test_updated_images(self):
        # iterating with each of the popular movie id over the list of updated movies and looking for match
        index = 0
        while (index <= 49):
            try:
                self.assertIn(self.popular_movies_list[index]['id'], self.update_movies_list)
            except AssertionError:
                print(str(self.popular_movies_list[index]['id']) + ' is not found in the list of updated movies')
            index += 1

    def test_existing_movies(self):
        ''' For each movie id int the 50 most popular movies, we will call the images api and see if they have and image
            if they image exist the test passes and we will only download ten images and verify that they were downloaded successfully '''
        base_url = r'https://image.tmdb.org/t/p/original'
        image_count = 0
        index = 0
        while (index <= 49):
            movie_id = self.popular_movies_list[index]['id']
            response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/images?api_key=cc9771a7d70090169469155420aac01e')
            self.assertEqual(response.status_code, 200)
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
            
if __name__ == '__main__':
    unittest.main()