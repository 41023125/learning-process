import discord
# import time
# import random
# import os
import asyncio
from discord.ext import commands
import re
import requests
from  RDscore import RDscore
from size import get_image_size

# client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)
# 調用event函式庫


@client.event
# 當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game('玩三小')
    # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.idle, activity=game)


@client.event
# 當有訊息時
async def on_message(message):
    if message.content.startswith('媽死了') or message.content.startswith('習近平') or message.content.startswith('操你媽'):
        await message.channel.send('禁止說髒話')
        user = message.author
        await user.send('警告一次！')
        target_user_id = 765595942166069248  # 將此處替換成您的特定人的使用者ID
        target_user = await client.fetch_user(target_user_id)
        await target_user.send(f'{user.name} 罵了一次髒話！')
        target_user_id = 851815166350065664
        target_user = await client.fetch_user(target_user_id)
        # 送出私訊給特定人
        await target_user.send(f'{user.name} 罵了一次髒話！')
        # 刪除觸發訊息
        await message.delete()
    # 隨便監聽
    if message.channel.id != 1083412185553838130 and message.author != client.user:
        # 取得特定頻道物件
        channel = client.get_channel(1083412185553838130)

        # 傳送訊息到特定頻道
        await channel.send(f"{message.author.name}: {message.content}")
    # 回報機制
    if message.content == '!回報':
        # 傳送私訊給使用者
        channel = client.get_channel(1083687436472832080)
        dm_channel = await message.author.create_dm()
        await message.delete()
        await dm_channel.send("\n!回報過程將被全程監控!\n請輸入要回報下列哪個問題:\n  `!檢舉`\n  `!建議`\n  `!其他`\n  `!結束`\n回報程序將在5分鐘後自動結束\n")
        ex = True

        def check(m):
            return m.channel == dm_channel and m.author == message.author
        while True:

            try:
                reply = await client.wait_for('message', check=check, timeout=300.0)
            except asyncio.TimeoutError:
                await dm_channel.send("回應逾時，請再試一次")
                break
            else:
                if reply.content in ['!檢舉', '!建議', '!其他']:
                    ex = False
                    reply.content = re.sub("!", "", reply.content)
                    await channel.send(f"{message.author.name}發出了" + reply.content)
                    await dm_channel.send("請說明要"+reply.content+"什麼事情\n並在最後單獨輸入`!結束`\n結束本次回報")
                    continue
                elif reply.content in ['!結束']:
                    await dm_channel.send("已結束本次回報")
                    ex = True
                    await channel.send(f"{message.author.name}結束回報\n--------------------------------------------------------------------")
                    break
                else:
                    if ex != True:
                        await channel.send(reply.content)
                        continue
                    else:
                        await dm_channel.send("無效輸入,請重新輸入")
    if message.content.startswith('!clearc回報'):
        # 指定要刪除訊息的頻道
        channel = client.get_channel(1083687436472832080)
        # 刪除指定頻道中的所有訊息
        await channel.purge()


@client.event
async def on_message(message):
    # 如果消息发送者是机器人，则不响应
    if message.author.bot:
        return

    # 如果消息是 @bot 回复，则获取被回复的消息内容
    if message.content.startswith('@bot'):
        # 获取被回复的消息对象
        replied_message = message.reference.resolved
        # 如果被回复的消息是文本消息，则打印文本内容
        if replied_message.content:
            print(f"Replied message: {replied_message.content}")
            await message.channel.send("Hi")
        # 如果被回复的消息包含图片，则打印图片的 URL
        if replied_message.attachments:
            for attachment in replied_message.attachments:
                if attachment.content_type.startswith('image/'):
                    print(f"Received image: {attachment.url}")# 回复一条消息
                    response = requests.get(attachment.url)
                    with open(f"1234.jpg", "wb") as f:
                        f.write(response.content)
                        # print(f"Saved image: {attachment.filename}")
                        sp = RDscore("1234.jpg",get_image_size("1234.jpg"))
                        # print(get_image_size("1234.jpg"))
                        if sp == -1:
                            await message.channel.send("sorry"+str(get_image_size("1234.jpg"))+"尚未增加")
                        else :
                            await message.channel.send("當前SP值:\n"+str(sp[0])+"\n召骰所需SP值:\n"+str(sp[1])+"\n總共有:\n"+str(sp[2]))

# TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面
client.run(
    'MTA4MjI1NTYzNjA3MjUwMTI4OQ.G5-8gW.6rfAE87_NTFsR_T-SxQy4Bo_7m3DUlio2tq4Ds')
