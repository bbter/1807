# class ChinaGetter:
#     """A simple localizer a la gettext"""
#
#     def __init__(self):
#         self.trans = dict(dog=u"小狗", cat=u"小猫")
#
#     def get(self, msgid):
#         """We'll punt if we don't have a translation"""
#         try:
#             return self.trans[msgid]
#         except KeyError:
#             return str(msgid)
#
#
# class EnglishGetter:
#     """Simply echoes the msg ids"""
#
#     def get(self, msgid):
#         return str(msgid)
#
#
# def get_localizer(language="English"):
#     """The factory method"""
#     languages = dict(English=EnglishGetter, China=ChinaGetter)
#     return languages[language]()
#
#
# # Create our localizers
# e, g = get_localizer("English"), get_localizer("China")
# # Localize some text
# for msgid in "dog parrot cat bear".split():
#     print(e.get(msgid), g.get(msgid))








# print(sum(range(1,101)))



import time,random
import queue,threading
q = queue.Queue()
def Producer(name):
  count = 0
  while count <20:
    time.sleep(random.randrange(3))
    q.put(count)
    print('Producer %s has produced %s baozi..' %(name, count))
    count +=1

def Consumer(name):
  count = 0
  while count <20:
    time.sleep(random.randrange(4))
    if not q.empty():
        data = q.get()
        print(data)
        print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' %(name, data))
    else:
        print("-----no baozi anymore----")
    count +=1
p1 = threading.Thread(target=Producer, args=('A',))
c1 = threading.Thread(target=Consumer, args=('B',))
p1.start()
c1.start()













