import pyautogui as pg
import time
import requests

def sendMessage(msg):
    webhook = '' #webhook goes here
    payload = {"text":msg}
    try:
        r = requests.post(webhook,json = payload)
        return True
    except:
        time.sleep(60)
        r = requests.post(webhook,json = payload)
        return True

print('60 seconds before starting.')
time.sleep(60)
pg.moveTo(300,300)

X,Y = pg.position()

n = 301
send = False
while True:
    a = pg.locateOnScreen('scan.png')
    if not str(a) == 'None':
        sendMessage("Scan started.")
        pg.moveTo(300,300)
        time.sleep(2)
    while Y == 300:
        if n > 500:
            n = 300
        else:
            n+=5
        pg.moveTo(n,300)
        time.sleep(1)
        print(str(X) + ' , ' + str(Y))
        try:
            a = pg.locateOnScreen('scan.png')

            if str(a) == 'None':
                pg.moveTo(n,500)
                send = True
        except:
            time.sleep(10)
        X,Y = pg.position()

        if Y < 305 and Y > 295:
            Y = 300
    if send:
        print('Mouse moved.')
        sendMessage('Scan complete.')

    while not Y == 300:
        send = False
        X,Y = pg.position()
        try:
            a = pg.locateOnScreen('scan.png')

            if not str(a) == 'None':
                pg.moveTo(n,300)
                print("re-engaged")
                time.sleep(60)
                pg.moveTo(n,300)
                X,Y = pg.position()
        except:
            time.sleep(10)


