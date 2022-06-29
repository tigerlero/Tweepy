# Tweepy

Get reports on a network of Twitter users.

## Requirements

* Python 3+
* Tweepy
* NetworkX
* Matplotlib

## Usage

1) Run `initial_user.py`. Generates `save.txt`, a text file with follower ids.
2) Run `read.py`. Generates text files with follower ids in the `ids` folder (you need to have the folder created).
3) Run `get_names.py`. Generates `NAME,ID` pairs in `names.txt`.
4) Run `graph.py`. Generates the report and a graph image.
