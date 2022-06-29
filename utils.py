import os
import tweepy
from tweepy import OAuthHandler


def Auth():
    consumer_key = 'nWFOYiDwURNw8hvety2UXgxg9'
    consumer_secret = 'trb3NETdthh6Ymr4SkH7F8g1Rqhm4HBFCgSKdeBstAPv36L0QK'
    access_token = '871120857577525248-uToYqbCL9u29x99OsAMYH93FnzpSZnw'
    access_secret = 'MApnpeCpYOXHTTN9ZJidly9O1CLUriN0yPTTl5gAVsk2H'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    return tweepy.API(auth, wait_on_rate_limit=True)


def BuildDict():
    f = open("names.txt", 'r')
    lines = f.readlines()
    f.close()

    d = {"807332651782774785": "paleshadow7"}
    for line in lines:
        ID, name = line.strip().split(',')
        d[ID] = name

    return d


def GetNames(api, ids):
    return [user.screen_name for user in api.lookup_users(user_ids=ids)]


def WriteFollowerIDs(api, user_id):
    fName = "ids/{}".format(user_id)
    if os.path.isfile(fName):
        print("File already exists for {}".format(user_id))
        return False

    ids = []
    for page in tweepy.Cursor(api.followers_ids, id=user_id).pages():
        ids.extend(page)

    ids = [str(i) for i in ids]
    f = open(fName, "w")
    f.write('\n'.join(ids))
    f.close()

    return True


def Reload(api, user_id):
    fName = "ids/{}".format(user_id)

    ids = []
    for page in tweepy.Cursor(api.followers_ids, id=user_id).pages(300):
        ids.extend(page)

    print("Finished Reading")
    ids = [str(i) for i in ids]
    f = open(fName, "w")
    f.write('\n'.join(ids))
    f.close()
    print("Finished Writing")

    return True


def SortCentrality(c_dict):
    return sorted(c_dict, key=c_dict.get, reverse=True)


def WriteCentrality(f, s_dict, c_dict):
    for u in s_dict:
        f.write("{}, {}\n".format(u, c_dict[u]))
