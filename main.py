from functions import random_quote
import fbchat
import cat
from fbchat.models import *
import random
import config


class EchoBot(fbchat.Client):

    def __init__(self,email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def send_quote(self,thread_id,thread_type):
        quote=random_quote()
        self.sendMessage(quote, thread_id=thread_id, thread_type=thread_type)

    def send_cat(self,thread_id,thread_type):
        img=cat.getCat(directory=None,filename='cat',format='jpg')
        self.sendLocalImage(img, message = None,thread_id=thread_id,thread_type=thread_type)


    def check_msg(self,msg,thread_id,thread_type):
        print(msg)
        if (msg=='!cat'):
            self.send_cat(thread_id,thread_type)
        elif (msg=='!quote'):
            self.send_quote(thread_id,thread_type)


    def onMessage(self, mid, author_id, message, message_object, thread_id, thread_type, ts, metadata,msg):
        #print(author_id)
        #print(thread_id)
        #print(thread_type)
        #print(message)
        self.friendConnect(author_id)
        self.check_msg(message,thread_id,thread_type)
        #print(self.fetchThreadList())



bot = EchoBot(config.username, config.password,None,3)
bot.listen()
