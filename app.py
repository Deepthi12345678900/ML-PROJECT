# from flask import Flask, request, jsonify, render_template
# import instaloader
# import tweepy
# import re

# app = Flask(__name__)

# # Configure Twitter API
# API_KEY = 'your_api_key'
# API_SECRET = 'your_api_secret'
# ACCESS_TOKEN = 'your_access_token'
# ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

# # Function to extract data from Instagram profile
# def extract_instagram_profile_data(username):
#     L = instaloader.Instaloader()
#     profile = instaloader.Profile.from_username(L.context, username)
    
#     data = {
#         'followers': profile.followers,
#         'following': profile.followees,
#         'is_private': profile.is_private,
#         'is_verified': profile.is_verified,
#         'post_count': profile.mediacount,
#         'bio': profile.biography,
#         'external_url': profile.external_url
#     }
#     return data

# # Function to extract data from Twitter profile
# def extract_twitter_profile_data(username):
#     try:
#         user = api.get_user(screen_name=username)
#         data = {
#             'followers': user.followers_count,
#             'following': user.friends_count,
#             'bio': user.description,
#             'tweets_count': user.statuses_count,
#             'is_verified': user.verified,
#             'is_private': user.protected,
#         }
#         return data
#     except Exception as e:
#         print(f"Error extracting Twitter data: {e}")
#         return {}

# # Example classifier logic based on followers
# def classify_profile(data):
#     followers = data.get('followers', 0)
#     following = data.get('following', 0)
#     post_count = data.get('post_count', data.get('tweets_count', 0))
#     is_private = data.get('is_private', False)
#     is_verified = data.get('is_verified', False)
    
#     # Influencer
#     if is_verified:
#         return 'influencer'
    
#     if followers > 10000 and post_count > 100:
#         return 'influencer'
    
#     if followers > 1000000:
#         return 'influencer'
    
#     if followers > 1000 and followers / (following + 1) > 2:
#         return 'potential influencer'
    
#     # Regular User
#     if is_private:
#         return 'regular user'
    
#     # Bot Characteristics
#     if followers == 0 and post_count == 0 and following > 100:
#         return 'bot'
    
#     if followers < 100 and following > 1000:
#         return 'bot'
    
#     # Fake Account Characteristics
#     if followers < 100 and post_count < 10 and following > 1000:
#         return 'fake account'
    
#     if followers < 100 and post_count < 10 and following < 100:
#         return 'fake account'
    
#     if 'spammer' in data and data['spammer']:
#         return 'spammer'
    
#     return 'regular user'


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/classify', methods=['POST'])
# def classify_user():
#     profile_url = request.form.get('profile_url')
    
#     if not profile_url:
#         return jsonify({'error': 'No profile URL provided'}), 400
    
#     try:
#         if 'instagram.com' in profile_url:
#             username = profile_url.rstrip('/').split('/')[-1]
#             profile_data = extract_instagram_profile_data(username)
#         elif 'twitter.com' in profile_url:
#             username = profile_url.rstrip('/').split('/')[-1]
#             profile_data = extract_twitter_profile_data(username)
#         else:
#             return jsonify({'error': 'Unsupported social media platform'}), 400
        
#         if not profile_data:
#             return jsonify({'error': 'Could not extract profile data'}), 500
        
#         category = classify_profile(profile_data)
#         return render_template('result.html', category=category, profile_data=profile_data)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

"""from flask import Flask, request, jsonify, render_template
import instaloader
import tweepy
import re

app = Flask(__name__)

# Configure Twitter (X) API
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Function to extract data from Instagram profile
def extract_instagram_profile_data(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    
    data = {
        'followers': profile.followers,
        'following': profile.followees,
        'is_private': profile.is_private,
        'is_verified': profile.is_verified,
        'post_count': profile.mediacount,
        'bio': profile.biography,
        'external_url': profile.external_url
    }
    return data

# Function to extract data from Twitter (X) profile
def extract_twitter_profile_data(username):
    try:
        print(f"Attempting to extract data for Twitter username: {username}")  # Debugging print
        user = api.get_user(screen_name=username)
        data = {
            'followers': user.followers_count,
            'following': user.friends_count,
            'bio': user.description,
            'tweets_count': user.statuses_count,
            'is_verified': user.verified,
            'is_private': user.protected,
        }
        print(f"Extracted data: {data}")  # Debugging print
        return data
    except Exception as e:
        print(f"Error extracting Twitter data: {e}")  # Debugging print
        return {}

# Example classifier logic based on followers
def classify_profile(data):
    followers = data.get('followers', 0)
    following = data.get('following', 0)
    post_count = data.get('post_count', data.get('tweets_count', 0))
    is_private = data.get('is_private', False)
    is_verified = data.get('is_verified', False)
    
    # Influencer
    if is_verified:
        return 'influencer'
    
    if followers > 10000 and post_count > 100:
        return 'influencer'
    
    if followers > 1000000:
        return 'influencer'
    
    if followers > 1000 and followers / (following + 1) > 2:
        return 'potential influencer'
    
    # Regular User
    if is_private:
        return 'regular user'
    
    # Bot Characteristics
    if followers == 0 and post_count == 0 and following > 100:
        return 'bot'
    
    if followers < 100 and following > 1000:
        return 'bot'
    
    # Fake Account Characteristics
    if followers < 100 and post_count < 10 and following > 1000:
        return 'fake account'
    
    if followers < 100 and post_count < 10 and following < 100:
        return 'fake account'
    
    if 'spammer' in data and data['spammer']:
        return 'spammer'
    
    return 'regular user'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_user():
    profile_url = request.form.get('profile_url')
    
    if not profile_url:
        return jsonify({'error': 'No profile URL provided'}), 400
    
    try:
        if 'instagram.com' in profile_url:
            username = re.search(r'instagram.com/([^/?]+)', profile_url).group(1)
            profile_data = extract_instagram_profile_data(username)
        elif 'twitter.com' in profile_url or 'x.com' in profile_url:
            username = re.search(r'(twitter.com|x.com)/([^/?]+)', profile_url).group(2)
            print(f"Extracted username from URL: {username}")  # Debugging print
            profile_data = extract_twitter_profile_data(username)
        else:
            return jsonify({'error': 'Unsupported social media platform'}), 400
        
        if not profile_data:
            return jsonify({'error': 'Could not extract profile data'}), 500
        
        category = classify_profile(profile_data)
        return render_template('result.html', category=category, profile_data=profile_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
"""

# app.py

from flask import Flask, request, jsonify, render_template
import instaloader
import tweepy
import re
import numpy as np
from tensorflow.keras.models import load_model
import joblib

app = Flask(__name__)

# Load the trained CNN model and scaler
model = load_model('models/cnn_model.h5')
scaler = joblib.load('models/scaler.pkl')

# Configure Twitter (X) API
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Function to extract data from Instagram profile
def extract_instagram_profile_data(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    
    data = {
        'followers': profile.followers,
        'following': profile.followees,
        'is_private': profile.is_private,
        'is_verified': profile.is_verified,
        'post_count': profile.mediacount,
        'bio': profile.biography,
        'external_url': profile.external_url
    }
    return data

# Function to extract data from Twitter (X) profile
def extract_twitter_profile_data(username):
    try:
        user = api.get_user(screen_name=username)
        data = {
            'followers': user.followers_count,
            'following': user.friends_count,
            'bio': user.description,
            'tweets_count': user.statuses_count,
            'is_verified': user.verified,
            'is_private': user.protected,
        }
        return data
    except tweepy.errors.NotFound:
        print(f"User {username} not found.")
    except tweepy.errors.TooManyRequests:
        print(f"Rate limit exceeded for Twitter API.")
    except Exception as e:
        print(f"Error extracting Twitter data: {e}")
    return {}

# Prepare input data for model prediction
def prepare_data_for_prediction(profile_data):
    features = np.array([
        profile_data.get('followers', 0),
        profile_data.get('following', 0),
        0.5,  # Placeholder for engagement_rate; replace with actual calculation
        0,  # Placeholder for is_promotional; replace with actual extraction if needed
        1,  # Placeholder for post_frequency; replace with actual extraction if needed
        0  # Placeholder for sentiment; replace with actual sentiment score calculation
    ])
    features_scaled = scaler.transform([features])
    features_scaled = features_scaled.reshape(features_scaled.shape[0], features_scaled.shape[1], 1)  # Reshape for CNN
    return features_scaled

# Predict the category using the CNN model
def classify_profile_cnn(data):
    prepared_data = prepare_data_for_prediction(data)
    prediction = model.predict(prepared_data)
    category = np.argmax(prediction, axis=1)
    categories = ['regular user', 'bot', 'influencer', 'fake account', 'spammer', 'potential influencer']  # Adjust based on your actual labels
    return categories[category[0]]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_user():
    profile_url = request.form.get('profile_url')
    
    if not profile_url:
        return jsonify({'error': 'No profile URL provided'}), 400
    
    try:
        if 'instagram.com' in profile_url:
            username = re.search(r'instagram.com/([^/?]+)', profile_url).group(1)
            profile_data = extract_instagram_profile_data(username)
        elif 'twitter.com' in profile_url or 'x.com' in profile_url:
            username = re.search(r'(twitter.com|x.com)/([^/?]+)', profile_url).group(2)
            profile_data = extract_twitter_profile_data(username)
        else:
            return jsonify({'error': 'Unsupported social media platform'}), 400
        
        if not profile_data:
            return jsonify({'error': 'Could not extract profile data'}), 500
        
        category = classify_profile_cnn(profile_data)
        return render_template('result.html', category=category, profile_data=profile_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if _name_ == '_main_':
    app.run(debug=True)