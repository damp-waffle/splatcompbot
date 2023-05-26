import asyncio
import pause
import tweet

async def work():
    while True:
        pause.hours(1)
        try:
            tweet.makeTweet()
        except:
            pass

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(work())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()