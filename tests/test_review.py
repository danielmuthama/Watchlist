import unittest
from app.models import Movie

class Review:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()
    @classmethod
    def get_reviews(cls,movie_id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == movie_id:
                response.append(review)

        return response

