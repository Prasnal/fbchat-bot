# Facebook bot

Facebook chat bot uses python fbchat library. This bot has a few main functionalities. You can use them by sending message:

* ``` !cat ``` - bot send you picture of random cat
* ``` !stat ``` - bot tell you how many messages is at the conversation
* ``` !quote ``` - bot send you random quotation

You can ask a question to Bot by putting his name in the conversation i.e John, would you like to talk with me? <br />
Every day at 8a.m and 10p.m the Bot sends message automatically to all groups where he is added.

Bot also can sends pictures of mentioned people. To use this function you should add your friends name and surname in the list in the config file and create directory named as their name and surname (i.e John Doe will have directory named John Doe) and put friend's pictures in that directory. During conversation just mention your friend to send his random photo (``` @John Doe ```).
