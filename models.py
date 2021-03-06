from datetime import datetime
from pony.orm import *

db = Database()

class Entry(db.Entity):
    title = Required(str)
    url = Required(str)
    timestamp = Optional(datetime, 0)
    published = Required(bool)
    publish_time = Optional(datetime, 0)

class RedditEntry(Entry):
    reddit_id = Required(str)   # use this to check for dupes
    score = Required(int)
    subreddit = Required(str)
    author = Required(str)

class NewsriverEntry(Entry):
    source = Optional(str)

class RSSEntry(Entry):
    feed_title = Required(str)

class TwitterEntry(Entry):
    twitter_id = Required(int, size=64)
    retweet_count = Optional(int)
    favorite_count = Optional(int)
    twitter_user = Required(str)
    twitter_weight = Optional(int)

class Proverb(db.Entity):
    # man oh man, this is so stupid
    text = Required(str)

