import unittest
from methods import Token, Restricted


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()

    def test_generate_token(self):
        self.assertEqual('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w', self.convert.generate_token("admin","secret"))
        self.assertEqual('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiZWRpdG9yIn0.C01pddxYdEY0qum6u_jlQYx3QWpf5NwXJtMq1yoWhc0', self.convert.generate_token("noadmin","noPow3r"))
        self.assertEqual('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoidmlld2VyIn0._k6kmfmdOoKWWMT4qk9nFTz-7k-X_0UdS8tByaCaye8', self.convert.generate_token("bob","thisIsNotAPasswordBob"))


    def test_access_data(self):
        self.assertEqual('You are under protected data', self.validate.access_data('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI'))
        self.assertEqual('You are under protected data', self.validate.access_data('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiZWRpdG9yIn0.C01pddxYdEY0qum6u_jlQYx3QWpf5NwXJtMq1yoWhc0'))
        self.assertEqual('You are under protected data', self.validate.access_data('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoidmlld2VyIn0._k6kmfmdOoKWWMT4qk9nFTz-7k-X_0UdS8tByaCaye8'))

if __name__ == '__main__':
    unittest.main()
