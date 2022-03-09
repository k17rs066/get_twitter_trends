
import tweepy
import pandas as pd
import pprint

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
api = tweepy.API(auth ,wait_on_rate_limit = True)


""" WOEID の設定（トレンドを取得したい地域の番号を取得）
Twitter側で決められた場所のトレンドを取得する際に必要なIDを設定
例.
Tokyo	1118370
Osaka	15015370
Japan	23424856 ...
"""

# 日本、大阪、東京
woeids = {
    'JAPAN' : 23424856,
    'OSAKA' : 15015370,
    'TOKYO' : 1118370
}

for key,woeid in woeids.items():
    # トレンド情報を取得
    trends = api.get_place_trends(woeid)
    pprint.pprint (trends)
    # pandas データフレームに変換
    df = pd.DataFrame(trends[0]["trends"])

    FILE_NAME = 'tw_trends_'+ key +'.csv'
    df.index = df.index + 1
    # csvファイルを出力
    df.to_csv(FILE_NAME,encoding = 'utf-8-sig',index = True)


