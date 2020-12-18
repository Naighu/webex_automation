import argparse
import time
import re
import textwrap
from _thread import start_new_thread

from client import Client


def animation(text):
    animation = "|/-\\"
    idx = 0
    while True:
        print(text,
              animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.1)
        if not client.loading:
            break


parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="Webex Automation",
    description="This script will automate your webex meeting")

parser.add_argument('-name', help='Your Name to display in webex')
parser.add_argument('-email', help='Your email to display in webex')
parser.add_argument('-url', help='webex meeting url')

args = parser.parse_args()
client = Client()


def automate(option):
    start_new_thread(client.join, (args.url, args.name, args.email))
    animation("Connecting to webex")

    while option != 2 and client.error == None:
        print("\n")
        print(textwrap.dedent(
            '''\
        ******* Welcome to Webex Automation *********
        You are now Connected to the cisco webex .
        Avialable Options : \n
        1.Message in chat .
        2. Exit from meeting

        '''))
        option = int(input("Enter your option"))
        if option == 1:
            if(str(client.token) != ""):
                message = str(input("\nEnter the message to send"))
                start_new_thread(client.message, (message,))
                time.sleep(1)
                animation("Sending message")
            else:
                print("Join a meeting to enter send a text message")

        elif option == 2:
            print("******* Aborting the connection *********")
            if(str(client.token) != ""):
                print("Disconnecting ...")
                client.exit()
                print("You are now DisConnected from cisco webex")
            else:
                print("You didn't join a meeting")
        else:
            print("Invalid option")
    if client.error != None:
        print("Error occures \n")
        print(client.error)


def main():

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex, args.email)):
        automate(0)
    else:
        print("Please enter a valid email id ")


main()
