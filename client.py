
import requests


class Client:
    def __init__(self):
        self.end_point = "/join"
        self.url = "http://127.0.0.1:5003"
        # a token will be generated in server side and by using this token other automations are controlled (like sending messages and exit from the meeting)
        self.token = None
        self.headers = {"authentication": "jhf85yb#fl43d"}
        self.loading = True
        self.error = None

    def join(self,webexUrl, name, email):
        self.end_point = "/join"
        body = {"name": name, "email": email,"url":webexUrl}
        try:
            response = requests.post(
                self.url + self.end_point,
                headers=self.headers,
                json=body)
            json_object = response.json()
            if(json_object["success"]):
                self.token = json_object["id"]
            else:
                self.error = json_object["error"]
            self.loading = False
            return json_object
        except requests.exceptions.ConnectionError as e:
            print("connection error")
            print("Server is not started .Start the server and run again")
            self.loading = False
            self.error = str(e)
        except Exception as e:
            self.loading = False
            self.error = str(e)
            print(str(e))

    def message(self, message):
        self.loading = True
        self.end_point = "/message"
        body = {"id": self.token, "chat_message": message}
        try:
            response = requests.post(
                self.url + self.end_point,
                headers=self.headers,
                json=body)
            json_object = response.json()

            self.loading = False
            if(not json_object["success"]):
                self.error = "Error occures try again"
        except requests.exceptions.ConnectionError as e:
            print("connection error")
            print("Server is not started .Start the server and run again")
            self.loading = False
            self.error = str(e)
        except Exception as e:
            self.loading = False
            self.error = str(e)
            print(str(e))

    def exit(self):
        self.loading = True
        self.end_point = "/exit"
        body = {"id": self.token}
        try:
            response = requests.post(
                self.url + self.end_point,
                headers=self.headers,
                json=body)
            json_object = response.json()

            self.loading = False
            if(not json_object["success"]):
                self.error = "Error occures try again"
        except requests.exceptions.ConnectionError as e:
            print("connection error")
            print("Server is not started .Start the server and run again")
            self.loading = False
            self.error = str(e)
        except Exception as e:
            self.loading = False
            self.error = str(e)
            print(str(e))
