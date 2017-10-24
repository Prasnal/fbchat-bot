import fbchat
import cat
from fbchat.models import *
import random


class EchoBot(fbchat.Client):

    def __init__(self,email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def send_cat(self,thread_id,thread_type):
        img=cat.getCat(directory=None,filename='cat',format='jpg')
        #self.sendLocalImage(img,'cat',thread_id,thread_type)
        self.sendLocalImage(img, message = None,thread_id=thread_id,thread_type=thread_type)


    def check_msg(self,msg,thread_id,thread_type):
        print(msg)
        if (msg=='!kot'):
            self.send_cat(thread_id,thread_type)


    def onMessage(self, mid, author_id, message, message_object, thread_id, thread_type, ts, metadata,msg):
        print(author_id)
        print(thread_id)
        print(thread_type)
        print(message)
        self.friendConnect(author_id)
        self.check_msg(message,thread_id,thread_type)
        print(self.fetchThreadList())


    def onInbox(self, unseen, unread, recent_unread, msg):
        print("test")

bot = EchoBot("<email>", "<password>",None,3)
bot.listen()
