import string
import random
import time
import crayons
from discord_webhook import *

print("{}".format(crayons.green('ANTARES NITRO GENERATOR UNCHECKED by TheQuesing')))

webhookurl = 'https://discord.com/api/webhooks/996649892850172016/1pT_vTukpYrhWGB6LAZ09LGB2CjL1u4pRN1COV-Q-Ji8C3bhy9rybHAI8FpkxOWivUfh' 

amount = 10000000000000000000000000000000000000000000000000000000000000000000000000000000

def send():
    webhook = DiscordWebhook(url=webhookurl, content="https://discord.gift/" + code) 
    response = webhook.execute()

for x in range(1, int(amount) + 1):
    code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    send() 
    print("{}".format(crayons.magenta('\n> Código: ' + code + '\n- Código Numero: %d' % (x))))
    time.sleep(0.5)
    print("{}".format(crayons.green('- Código Enviado!!')))
    time.sleep(1.65)