
import os
import json
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.models import MessageEvent
from linebot.models import TextMessage
from linebot.models import ImageMessage
from linebot.models import TextSendMessage
from linebot.models import ImageSendMessage
from linebot.models import VideoSendMessage
from linebot.exceptions import InvalidSignatureError

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

def lambda_handler(event, context):
    @handler.add(MessageEvent, message=TextMessage)
    def handle_text_message(event):

        event_text = event.message.text

        if event_text == "Hello":
            reply_messages = [
                TextSendMessage(
                    text=f'World'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "吃什麼":
            reply_messages = [
                TextSendMessage(
                    text=f'火鍋'
                ),
                TextSendMessage(
                    text=f'拉麵'
                ),
                TextSendMessage(
                    text=f'壽司'
                ),
                TextSendMessage(
                    text=f'咖哩飯'
                ),
                TextSendMessage(
                    text=f'Pizza'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "人物介紹":
            reply_messages = [
                TextSendMessage(
                    text=f'我叫做羅。'
                ),
                TextSendMessage(
                    text=f'我叫做沈'
                ),
                TextSendMessage(
                    text=f'我叫做Neil。'
                ),
                TextSendMessage(
                    text=f'我叫做FKT。'
                ),
                TextSendMessage(
                    text=f'我叫柏均'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "配對地點":
            reply_messages = [
                TextSendMessage(
                    text=f'信義商圈。'
                ),
                TextSendMessage(
                    text=f'中山商圈'
                ),
                TextSendMessage(
                    text=f'板橋耶誕城。'
                ),
                TextSendMessage(
                    text=f'南紡購物中心'
                ),
                TextSendMessage(
                    text=f'華泰名品城'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "任務挑戰":
            reply_messages = [
                TextSendMessage(
                    text=f'雙人吃pocky。'
                ),
                TextSendMessage(
                    text=f'頭套絲襪'
                ),
                TextSendMessage(
                    text=f'對視十秒。'
                ),
                TextSendMessage(
                    text=f'十連拍標'
                ),
               TextSendMessage(
                    text=f'交互蹲跳20下'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "App介紹":
            reply_messages = [
                TextSendMessage(
                    text=f'當冬季的寒風吹拂，凜冬將至，萬物似乎都沉浸在一片靜謐之中。但在這寒冷的季節裡，有一個溫暖的節日正悄悄接近——一年一度的聖誕夜。'
                ),
                TextSendMessage(
                    text=f'街道上開始裝飾著五彩繽紛的燈飾和聖誕樹，每個角落都洋溢著節日的歡樂和期待。這是一個充滿奇蹟和歡笑的時刻，也是一個關於愛與被愛的夢想。'
                ),
                TextSendMessage(
                    text=f'然而，在這充滿歡樂的季節裡，也許你還是一個人。孤單地走在燈火闌珊的街頭，看著身邊的情侶手牽手，心中不免泛起一絲寂寞。但別擔心，聖誕節不僅僅是一個家庭團聚的時刻，也是一個尋找愛情的好機會。在這個節日裡，許多人都渴望找到屬於自己的另一半，去分享這份節日的喜悅。'
                ),
                TextSendMessage(
                    text=f'因此，我們特別為你準備了一個特別的機會——一次認識優質男士的機會。這些男士不僅有著良好的品德和積極的生活態度，還擁有各自獨特的魅力和才華。他們都在尋找一位能夠共度美好時光的伴侶。'
                ),
                TextSendMessage(
                    text=f'此刻，為自己勇敢一次，給自己一個重獲新生的機會。不要讓這個聖誕夜成為另一個孤單的夜晚。來加入我們，認識這些優質男士，也許你會在這個聖誕節找到那個特別的他，與他一起度過一個難忘的節日時光。讓愛在這個寒冷的冬季綻放，帶給你溫暖和幸福。'
                ),
               
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "使用者體驗":
            reply_messages = [
                TextSendMessage(
                    text=f'今天配對到的人還滿意嗎？ '
                ),
                TextSendMessage(
                    text=f'一到五顆星你願意給他幾顆呢？'
                ),
                TextSendMessage(
                    text=f'有留下後續聯絡方式了嗎？'
                ),
                TextSendMessage(
                    text=f'有後續約出來嗎'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/become_ambassader.jpg",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/become_ambassader.jpg",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        else:
            reply_messages = [
                TextSendMessage(
                    text=f'不好意思！我們現在還不認識這句話，或許可以試試點擊選單內容！'
                ),
            ]
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )


    try:
        # get X-Line-Signature header value
        signature = event['headers']['x-line-signature']

        # get request body as text
        body = event['body']
        handler.handle(body, signature)
    except InvalidSignatureError:
        return {
            'statusCode': 502,
            'body': json.dumps("Invalid signature. Please check your channel access token/channel secret.")
        }
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!")
    }
