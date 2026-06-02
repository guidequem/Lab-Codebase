import requests
import json
import time
import hashlib
import hmac
import base64
import pyautogui as pg

def sendMessage(msg):
    webhook = 'https://hooks.slack.com/services/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'
    payload = {"text":msg}
    try:
        r = requests.post(webhook,json = payload)
        return True
    except:
        time.sleep(60)
        r = requests.post(webhook,json = payload)
        return True

print("Scan running. Do not touch computer.")
time.sleep(30)

while True:
    a = pg.locateOnScreen('scan.png')

    if str(a) == 'None':
        time.sleep(20)
        pg.press('enter')
        time.sleep(20)
        pg.write('Markertlab2022')
        time.sleep(20)
        pg.press('enter')
        time.sleep(20)
    else:
        print("Scan still running.")
    a = pg.locateOnScreen('Arrow.png')

    if str(a) == 'None':
        sendMessage('Scan complete.')
        while True:
            a = pg.locateOnScreen('Arrow.png')
            if not str(a) == 'None':
                print('Found. Resuming.')
                break
            time.sleep(10)
            
    time.sleep(30)
print('Finished.')
