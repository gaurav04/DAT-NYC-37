from TwitterAPI import TwitterAPI

access_token_key = "118197143-lxLFvzNTbq0YwygedKusXeWQwLCk4KaE8DL0mACl"
access_token_secret = "cnwvXILlGw0R6o31EKaoJ7s2gQRRJ0cVVh5SYn7dtN43o"

api_key = "n7dLWfUSdZeLiXjFf24d8djP7"
api_secret = "TIBmvnQdtwA1rQ5KXmmfXO4kAKapE6Na5UQR2msShTp90Bca4S"

_debug = 0


api = TwitterAPI(api_key, api_secret, access_token_key, access_token_secret)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''

def retrieve_tweets(topic,
                    url="https://stream.twitter.com/1/statuses/filter.json",
                    method="GET", ):
    """

    Params:
    topic - must be in this format "#topic" or '@handle"
    Returns
    """
    response = api.request('statuses/filter', {'track': topic})
    if response.status_code != 200:
        raise ValueError("Unable to retrieve tweets, please check your API credentials")
    for x in response:
        try:
            yield x
        except UnicodeError as unicode_error:
            continue
