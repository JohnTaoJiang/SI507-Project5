import unittest
from SI507project5_code import *

class Test_data_from_API(unittest.TestCase):

    def setUp(self):
        self.cache_file = open("cache_contents.json", "r")
        self.cache_json = self.cache_file.read()
        self.cache_dict = json.loads(self.cache_json)
        
        self.quote_request_url = "https://api.tumblr.com/v2/blog/derekg.org/posts/quote"
        self.quote_params = {}
        self.quote_colnames = ["id", "post_url", "date", "summary"]
        self.quote_ident = create_request_identifier(self.quote_request_url, self.quote_params)
        self.quote_cache = get_from_cache(self.quote_ident, self.cache_dict)
        self.quote_posts_res = self.quote_cache['response']['posts']
        self.quote_csvfile = open("quote_posts.csv", "r", encoding = 'utf-8')

        self.tagged_request_url = "https://api.tumblr.com/v2/tagged"
        self.tagged_params = {'tag': 'gif'}
        self.tagged_colnames = ["blog_name", "post_url", "tags", "summary"]
        self.tagged_ident = create_request_identifier(self.tagged_request_url, self.tagged_params)
        self.tagged_cache = get_from_cache(self.tagged_ident, self.cache_dict)
        self.tagged_posts_res = self.tagged_cache['response']
        self.tagged_csvfile = open("tagged_posts.csv", "r", encoding = 'utf-8')

    def test_cache_data_types(self):
        self.assertTrue(isinstance(self.quote_cache, dict))
        self.assertTrue(isinstance(self.quote_posts_res, list))
        self.assertTrue(isinstance(self.tagged_cache, dict))
        self.assertTrue(isinstance(self.tagged_posts_res, list))

    def test_cache_data_keys(self):
        for col in self.quote_colnames:
            self.assertTrue(col in self.quote_posts_res[0])
        for col in self.tagged_colnames:
            self.assertTrue(col in self.tagged_posts_res[0])

    def test_csv_cols(self):
        quote_header = self.quote_csvfile.readline()
        quote_header = quote_header.replace('\n', '')
        quote_csv_cols = quote_header.split(',')
        self.assertTrue(quote_csv_cols == self.quote_colnames)
        
        tagged_header = self.tagged_csvfile.readline()
        tagged_header=  tagged_header.replace('\n', '')
        tagged_csv_cols = tagged_header.split(',')
        self.assertTrue(tagged_csv_cols == self.tagged_colnames)
        
    def test_csv_len(self):
        quote_csv_contents = self.quote_csvfile.readlines()
        self.assertTrue(len(quote_csv_contents) >= 20)
        tagged_csv_contents = self.tagged_csvfile.readlines()
        self.assertTrue(len(tagged_csv_contents) >= 20)

    def tearDown(self):
        self.cache_file.close()
        self.quote_csvfile.close()
        self.tagged_csvfile.close()












if __name__ == "__main__":
    unittest.main(verbosity=2)
