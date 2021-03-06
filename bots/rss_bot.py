import feedparser, settings, time, logging
from datetime import datetime, timezone

def get_feed_items():
    logging.info('Fetching RSS feeds')
    rss_items = []
    feed_data = [feedparser.parse(url) for url in settings.RSS_LIST]

    for feed_provider in feed_data:
        rss_items.append({
                'feed_title': get_feed_title(feed_provider),
                'items': [{
                    'title': i['title'],
                    'url': i['link'],
                    # Following conversion magic provided bei SO: https://stackoverflow.com/a/1697907
                    'timestamp': datetime.fromtimestamp(time.mktime(i['published_parsed'])).replace(tzinfo=timezone.utc)
                } for i in feed_provider['entries']]
            })
    logging.info('RSS Bot reporting success!')
    return rss_items

def get_feed_title(feed_provider):
    try:
        return feed_provider['feed']['title']
    except KeyError as e:
        logging.error('Feed {url} has no title. Error: {err}.'.format(url=feed_provider['url'], err=e))
        return 'Untitled Feed'

