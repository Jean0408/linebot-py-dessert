#!/usr/bin/env python
# coding: utf-8

# In[7]:


from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os


# In[2]:


app=Flask(__name__)


# In[3]:


channel_secret='5b0e8c50c53a76748bf55e555ba1c0af'
channel_assess_token='kElBlWI92yZb0ASbU4ZL0LTXcQN5BsZVfytnUnNv3nC7wAp/DEzZL5ILDprBB7Ia5aqjWSPjkjCCTQctVfBLTY9K59jjdeawxglSf5YL0Ojjm7Jd+4bSVnskOsDRkCSGmhkqlT2f6sNqOB8xvn1WTQdB04t89/1O/w1cDnyilFU='

line_bot_api=LineBotApi(channel_assess_token)
handler=WebhookHandler(channel_secret)


# In[4]:


@app.route("/callback", methods=['POST'])
def callback():
    singnature=request.headers['X-Line-Signature']
    body=request.get_data(as_text=Ture)
    
    try:
        handler.handle(body, signature)
    except Exception as e:
        print(e)
        abort(400)
        
    return 'OK'


# In[5]:


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message=event.message.text
    reply_message="輸入："+ user_message
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_message))


# In[ ]:


if __name__=="__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


# In[3]:





# In[ ]:





# In[1]:


# d={'巴斯克燒乳酪蛋糕': '奶油乳酪 225g' '糖 30g'}


# In[3]:


# print(d['巴斯克燒乳酪蛋糕'])


# In[ ]:




