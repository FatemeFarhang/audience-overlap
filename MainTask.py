import os
import random
import collections
from time import sleep
from dotenv import load_dotenv
from igramscraper.instagram import Instagram
load_dotenv()

def get_5_followings(usernames):
    '''This function find 5 followings of each users'''
    instagram = Instagram()
    print(f'[info] - Logging...')
    try:
        instagram.with_credentials(random.choices(os.getenv('USERNAMES').split())[0], os.getenv('PASSWORD'))
        instagram.login()
        print('[info] - Successfully logged in.')
    except:
        instagram.with_credentials(random.choices(os.getenv('USERNAMES').split())[0], os.getenv('PASSWORD'))
        instagram.login()
        print('[info] - Successfully logged in.')

    sleep(4)

    result_files = []
    for username in usernames:
        print(username)
        account = instagram.get_account(username)
        sleep(2)
        followings = instagram.get_following(account.identifier, 5, 5, delayed=True)

        with open(username + '_followings.txt', 'w+', encoding='utf-8') as following_file:
            for following in followings['accounts']:
                following_file.write(following.username + '\n')

        result_files.append(username + '_followings.txt')
    
    check_followings(result_files)


def check_followings(result_files):
    '''This function check followings'''
    print('[info] - Opening result files...')

    followings = []
    for file in result_files:
        with open(file, 'r', encoding='utf-8') as following_file:
            followings_result = following_file.readlines()
            for i in followings_result:
                followings.append(i.replace('\n', ''))
    
    
    mutual_followings = [item for item, count in collections.Counter(followings).items() if count > 1]
    if mutual_followings:
        print(f'Mutual followings : {mutual_followings}')
    else:
        print('There is no mutual following.')

get_5_followings(['vancityraynolds', 'willsmith'])