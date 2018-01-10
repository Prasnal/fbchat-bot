# -*- coding: UTF-8 -*-
from functions import random_quote
from functions import return_id
from multiprocessing import Process
import fbchat
import cat
from fbchat.models import *
import random
import config
from unidecode import unidecode
import schedule
import time
import os




class ReactionBot(fbchat.Client):

    def __init__(self,email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def send_quote(self,thread_id,thread_type):
        quote=random_quote()
        self.sendMessage(quote, thread_id=thread_id, thread_type=thread_type)

    def send_friend_photo(self,photo_list,thread_id,thread_type):
        for person in photo_list:
            photo=random.choice(os.listdir(unidecode(person+'/')))
            path=person+'/'+photo
            path=unidecode(path)
        self.sendLocalImage(path, message=None, thread_id=thread_id, thread_type=thread_type)

    def send_cat(self,thread_id,thread_type):
        img=cat.getCat(directory=None,filename='cat',format='jpg')
        self.sendLocalImage(img, message = None,thread_id=thread_id,thread_type=thread_type)


    def check_msg(self,msg,thread_id,thread_type):
        print(msg)
        val=False
        if ('Czy ' in msg) or ('czy ' in msg) or ('?' in msg):
            val=True

        friend_list=config.friend_list
        photo_list=[i for i in friend_list if '@'+str(i) in msg]

        if (msg=='!cat'):
            self.send_cat(thread_id,thread_type)
        elif (msg=='!quote'):
            self.send_quote(thread_id,thread_type)
        elif (photo_list):
            self.send_friend_photo(photo_list,thread_id,thread_type)
        elif(msg=='!stat'):
            self.show_statistics(thread_id,thread_type)
        elif(val):
            self.talk(thread_id,thread_type,msg)
        elif(('john' in msg) or ('John' in msg)):
            self.sendMessage('🙋', thread_id=thread_id, thread_type=thread_type)

    def show_statistics(self,thread_id,thread_type):
        #msgs=self.fetchThreadMessages(thread_id)
        msgs = self.fetchThreadMessages(thread_id, limit=10000000000000)
        msgs.reverse()
        count=str(len(msgs))
        msg="Since I was added to conversation, we've written "+ count +" messages"
        self.sendMessage(msg, thread_id=thread_id, thread_type=thread_type)

    def talk(self,thread_id,thread_type,msg):
        if (('john' in msg) or ('John' in msg) or (not random.randrange(5))):
            choises = ('yes', 'no', 'I don\'t know', 'don\'t ask me about this','xD')
            my_choise = random.choice(choises)
            self.sendMessage(my_choise, thread_id=thread_id, thread_type=thread_type)


    def onMessage(self, mid, author_id, message, message_object, thread_id, thread_type, ts, metadata,msg):
        self.friendConnect(author_id)
        self.check_msg(message,thread_id,thread_type)


class EverydayMessageBot(Process, fbchat.Client):
    def __init__(self, email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self, email, password, debug, user_agent)
        self.my_schedule()

    def my_schedule(self):
        schedule.every().day.at("8:00").do(self.good_morning)
        schedule.every().day.at("22:00").do(self.good_night)

        while 1:
            schedule.run_pending()
            time.sleep(1)
            self.good_morning()

    def find_groups_ID(self):
        all_messages = self.find_all_messages()
        all_groups = [return_id(str(i)) for i in all_messages if str(i)[1] == 'G']
        return all_groups

    def find_all_messages(self):
        new_threads = self.fetchThreadList(offset=0, limit=1, thread_location=ThreadLocation.INBOX)
        threads = self.fetchThreadList(offset=1, limit=20, thread_location=ThreadLocation.INBOX)
        i = 20
        while new_threads:
            new_threads = self.fetchThreadList(offset=i, limit=20, thread_location=ThreadLocation.INBOX)
            threads += new_threads
            i += 20
        return threads

    def good_morning(self):
        morning_msg = 'Good morning everyone! Have a nice day with cats. Quotation for today: \n \n' + random_quote()
        groups = self.find_groups_ID()

        for i in groups:
            self.sendMessage(morning_msg, thread_id=i, thread_type=ThreadType.GROUP)

    def good_night(self):
        afternoon_msg='Good night!'
        for i in groups:
            self.sendMessage(afternoon_msg, thread_id=i, thread_type=ThreadType.GROUP)


bot = ReactionBot(config.username, config.password,None,3)
p=Process(target=bot.listen)
p.start()

bot2 = EverydayMessageBot(config.username, config.password,None,3)
bot2.start()
p.join()
bot2.join()
