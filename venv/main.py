from flask import Flask
import flask
import tweepy
from tweepy import OAuthHandler

app = Flask(__name__)

@app.route('/')
def index():
	return 'Welcome to Elastacloud Nottingham!'
    
    
@app.route('/twitterfeed')
def twitter():
    # Consumer keys and access tokens, used for OAuth  
    consumer_key = 	'MRKUBOetQfebbVoDjNuPEanYs'
    consumer_secret = '1YafSu13K6u62LL1x4VxREqkl2a31nKWv82sXi5EGCWc6L0nHR'
    access_token = '927465007906000896-wRK9cVeT5MqYd8ULeT0sW8wAzcgb54r'
    access_token_secret = 'rbo5OumeuMuHUSLghFXgJrCEswM4D8Rw93o89YiN7bgSR'
      
    # OAuth process, using the keys and tokens  
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
    auth.set_access_token(access_token, access_token_secret)  
      
    # Creation of the actual interface, using authentication  
    api = tweepy.API(auth)  
      
    return flask.render_template('tweets.html', tweets = api.user_timeline(screen_name = 'elastacloud', count = 100, include_rts = True))
    
    
@app.route('/channels')
def channels():
	return 'Welcome to Elastacloud Channels!'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
	
