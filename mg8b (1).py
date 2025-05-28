#destiney cardenas
#1/27/25
#magic 8 ball

import random
import time
magic8List = ["OF course!","Yes...","Outcome looks good","Definitely","100percent good chance","Maybe","Ask again later","I'm not sure","Perhaps","Chances are 50/50","NO","Absolutely not","Nuh uh","Probably not","0 Chances"]

def ball():
    print("Welcome to magic 8 Ball!\nAsk me a question and I'll tell your your outcome.")
    while True:
        quest = input("Ask me a yes or no question... ")
        if quest.endswith("?"):
            print("Shake...")
            time.sleep(1)
            print("Shake...")
            time.sleep(1)
            print("Shake...")
            time.sleep(1)
            print(random.choice(magic8List))
            ask = input("do you want to ask another question? ")
            if ask == "no":
                break
        else:
            print("ERROR: Please make sure the question ends with a question mark.")
            return ball()

ball()
