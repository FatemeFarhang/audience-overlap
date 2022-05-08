import os
import random
import collections
from webbrowser import get
from dotenv import load_dotenv
from instagramy import InstagramUser
load_dotenv()

username = 'nike'
# Get random session id from .env file
session_id = random.choices(os.getenv('session_ids').split())[0]

# Try 3 times to connect to the account
try:
    user = InstagramUser(username, sessionid=session_id, from_cache=True)
except KeyError:
    session_id = random.choices(os.getenv('session_ids').split())[0]
    user = InstagramUser(username, sessionid=session_id, from_cache=True)
finally:
    session_id = random.choices(os.getenv('session_ids').split())[0]
    user = InstagramUser(username, sessionid=session_id, from_cache=True)


def find_unique_follower_ratio():
    pass


def get_average_comments_and_likes(): 
    '''This function return average number of received comments and likes in last 10 posts'''
    posts = user.posts[-10:]
    likes_count = []
    comments_count = []

    for post in posts:
        likes_count.append(int(post.likes))
        comments_count.append(int(post.comments))

    print(sum(likes_count) / 10)
    print(sum(comments_count) / 10)


def get_most_frequent_locations():
    '''This function return most frequent locations of the posts in last 20 posts'''
    posts = user.posts[-20:]
    locations = []

    for post in posts:
        if post.location:
            locations.append(post.location['name'])

    frequent_locations = [item for item, count in collections.Counter(locations).items() if count > 1]
    if frequent_locations:
        return frequent_locations
    else:
        return f'No frequent location detected in last 20 posts'


def get_best_3_posts_on_comments_likes():
    '''This function return best 3 posts on received comments and likes in last 30 posts'''
    posts = user.posts[-30:]
    best_3_posts_comments = []
    best_3_posts_likes = []
    likes = []
    comments = []

    # Append post likes into likse list
    for post in posts:
        likes.append(post.likes)
    
    # Append post comments into comments list
    for post_2 in posts:
        comments.append(post_2.comments)

    for post_3 in posts:
        # Append best posts on likes into best_3_posts_likes list based on last 3 
        # sorted values in likes list (3 best posts on likes)
        for best_likes in sorted(likes)[-3:]:
            if post_3.likes == best_likes:
                best_3_posts_likes.append(post_3)
        
        # Append best posts on comments into best_3_posts_comments list based on last 3 
        # sorted values in comments list (3 best posts on comments)
        for best_comments in sorted(comments)[-3:]:
            if post_3.comments == best_comments:
                best_3_posts_comments.append(post_3)

    return best_3_posts_comments, best_3_posts_likes