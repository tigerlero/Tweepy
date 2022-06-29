import time
import tweepy
import utils
api = utils.Auth()



f = open("save.txt", "r")
lines = f.readlines()
f.close()

followers = [x.strip() for x in lines]

f = open("index.txt", "r")
i = int(f.read().strip())
f.close()

for follower in followers[i:]:
    if utils.WriteFollowerIDs(api, follower):
        print(i)

    i += 1

    f = open("index.txt", "w")
    f.write(str(i))
    f.close()
