from internetspeedtwitterbot import InterSpeedTwitterBot

CONTRACT_DOWN_SPEED = 300
CONTRACT_UP_SPEED = 300
GRACE_GAP = 50

twitter_bot = InterSpeedTwitterBot()
twitter_bot.get_internet_speed()
if twitter_bot.down < CONTRACT_DOWN_SPEED - GRACE_GAP or twitter_bot.up < CONTRACT_UP_SPEED - GRACE_GAP:
    twitter_bot.tweet_at_provider()
    twitter_bot.quit_browser()

# TODO: ✅ update speedtest driver to get results URL
