from django.shortcuts import render
import tweepy
# Create your views here.

def extractTweet(request):
    
    name = request.GET.get('name')
    tweet_count = request.GET.get('tweet_count')

    auth = tweepy.OAuth1UserHandler(
    "pEoRlOW5Gy8vHVKtef4QSqw4v", "uLKAFCvoifze0xAs3XmO3dxYyU8ImNQ30hjL0IKlgfaJZGWPYu",
    "2930663149-A15pkVJRmBy6x7eZid3AdMr6mA7iG3OorW4to1j", "0l0BkcPAkjgJhom8JUPNJvXGFVepbe8SNjSwXF9GvwRk5"
    )
    api = tweepy.API(auth)
    username = name #'MrBeast'  # Replace with the desired username
    tweet_count = tweet_count #5  # Number of tweets to extract

    tweets = api.user_timeline(screen_name=username, count=tweet_count)
    context = {
        'name':name,
        'tweet_count':tweet_count,
        'tweets': tweets
    }
    for tweet in tweets:
        print('Username: ', tweet.user.name,)
        print('Text: ',  tweet.text )
        print('Date: ', tweet.created_at)

    return render(request,'userform.html',context)
