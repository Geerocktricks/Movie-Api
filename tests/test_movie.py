import unittest
from app.models import Movie

movie=Movie

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_movie = movie(1234,'Python Must Be Crazy','A thrilling new Python Series','/khsjha27hbs',8.5,129993)
        print(self.new_movie)

    def test_instance(self):    
        self.assertTrue(isinstance(self.new_movie,movie))
        
# if__name__='__main__'
