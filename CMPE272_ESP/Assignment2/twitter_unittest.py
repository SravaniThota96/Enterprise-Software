import unittest
from unittest.mock import patch
from FlaskTweetBot import home, app, deleteTweet, createTweet, searchTweet

class TwitterTests(unittest.TestCase):
    
    #testcase1 : to check if home page is rendered
    @patch("FlaskTweetBot.render_template")
    def test_homePageUnitTest_returnval(self, mock_render_template):
        mock_render_template.return_value = "Test"
        ret = home()
        self.assertEqual(ret, "Test")

    #testcase2 : to check if render template is called with home.html
    @patch("FlaskTweetBot.render_template")
    def test_homePageUnitTest_servehomepage(self, mock_render_template):
        mock_render_template.return_value = "Test"
        home()
        mock_render_template.assert_called_with('home.html',posts=[], text = "Technovators Tweet Bot")
    
    #testcase3 : to check if render template is called with home.html
    @patch("FlaskTweetBot.render_template")
    def test_homePageUnitTest_servehomepage_success(self, mock_render_template):
        mock_render_template.return_value = "Test"
        home("Successful")
        mock_render_template.assert_called_with('home.html',posts=[], text = "Tweet successful")
    
    #testcase4 : to check if render template is called with home.html
    @patch("FlaskTweetBot.render_template")
    def test_homePageUnitTest_servehomepage_delete(self, mock_render_template):
        mock_render_template.return_value = "Test"
        home("Deleted")
        mock_render_template.assert_called_with('home.html',posts=[], text = "Tweet deleted")

    #testcase5 : to check if delete api is called with the correct tweet id and return to home page
    @patch("FlaskTweetBot.DeleteForm")
    @patch("FlaskTweetBot.oauth.delete")
    @patch("FlaskTweetBot.redirect")
    @patch("FlaskTweetBot.url_for")
    def test_deleteTweetTest_twitter_api_call(self, mock_url_for, mock_redirect, mock_oauth_delete, mock_deleteTweet):
        mock_delete = mock_deleteTweet()
        
        mock_delete.validate_on_submit.return_value = True
        mock_delete.deleteTweetId.data = "1234"

        mock_url_for.return_value = "/home"
        mock_oauth_delete.return_value = None
        mock_redirect.return_value = "home-page"

        ret = deleteTweet()
        self.assertEqual(ret, "home-page")
        mock_oauth_delete.assert_called_with("https://api.twitter.com/2/tweets/1234")

    #testcase6 : to check if render template in deletetweet function is called with delete.html
    @patch("FlaskTweetBot.DeleteForm")
    @patch("FlaskTweetBot.render_template")
    def test_deleteTweet_displayPage(self, mock_render_template, mock_deleteTweet):
        mock_delete = mock_deleteTweet()
        mock_delete.validate_on_submit.return_value = False
        mock_render_template.return_value = "delete-page"

        ret = deleteTweet()
        self.assertEqual(ret, "delete-page")
        mock_render_template.assert_called_with('delete.html',title = "delete", form = mock_delete)
    
    #testcase7 : to check if render template in createtweet function is called with create.html
    @patch("FlaskTweetBot.CreateTweet")
    @patch("FlaskTweetBot.render_template")
    def test_createTweet_displayPage(self, mock_render_template, mock_createtweet):
        mock_create = mock_createtweet()
        mock_create.validate_on_submit.return_value = False
        mock_render_template.return_value = "create-page"

        ret = createTweet()
        self.assertEqual(ret, "create-page")
        mock_render_template.assert_called_with('create.html',title = "create", form = mock_create, text="Tweet created")

    #testcase8 : to check if create api is called with the correct tweet content and return to home page
    @patch("FlaskTweetBot.CreateTweet")
    @patch("FlaskTweetBot.oauth.post")
    @patch("FlaskTweetBot.redirect")
    @patch("FlaskTweetBot.url_for")
    def test_createTweetTest_twitter_api_call(self, mock_url_for, mock_redirect, mock_oauth_post, mock_createtweet):
        mock_create = mock_createtweet()
        
        mock_create.validate_on_submit.return_value = True
        mock_create.tweet.data = "MockTweetData"

        mock_url_for.return_value = "/home"
        mock_oauth_post.return_value = None
        mock_redirect.return_value = "home-page"

        ret = createTweet()
        self.assertEqual(ret, "home-page")
        mock_oauth_post.assert_called_with("https://api.twitter.com/2/tweets",json={"text": "MockTweetData"})

    #testcase9 : to check if render template in searchtweet function is called with search.html
    @patch("FlaskTweetBot.SearchForm")
    @patch("FlaskTweetBot.render_template")
    def test_searchTweet_displayPage(self, mock_render_template, mock_searchtweet):
        mock_search = mock_searchtweet()
        mock_search.validate_on_submit.return_value = False
        mock_render_template.return_value = "search-page"

        ret = searchTweet()
        self.assertEqual(ret, "search-page")
        mock_render_template.assert_called_with('search.html',title = "search", form = mock_search, posts=[])
    

if __name__ == '__main__':
    unittest.main()