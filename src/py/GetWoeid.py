
import tweepy
import pandas as pd

# Twitter APIのKey/Token
API_KEY = "Bofvgz5vtXr6CcO3CHfenuqEK"
API_KEY_SECRET = "ihibdcpxqy03vlRm7opPG3uAHl9NcZf5tC3dTVKAagG4fbSgmN"
TOKEN = "950320951954059265-57KXiXHds4UfrgLrEVrKLsZubNaM3VV"
TOKEN_SECRET = "jbZ02YIDxdpuP63wu1H6wiAtrWTFGwX5LUsibljdQmt4V"

"""
Tweepy 設定
"""
# Twitter APIのアクセス認証
auth = tweepy.OAuthHandler(API_KEY,API_KEY_SECRET) 
# アクセストークン設定
auth.set_access_token(TOKEN, TOKEN_SECRET)
# api にアクセス
api = tweepy.API(auth)

# 世界中のwoeid を取得
for woeid in api.available_trends():
    print(woeid)