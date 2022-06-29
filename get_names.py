import tweepy
from os import listdir
import utils
api = utils.Auth()


ids = listdir("ids")
names = utils.GetNames(api, ids)

f = open("names.txt", "w")

for i, n in zip(ids, names):
    f.write("{},{}\n".format(i, n))

f.close()
