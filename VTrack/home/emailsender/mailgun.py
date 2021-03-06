import requests
from .config import *


def send_vehicle_found_message():
    resp = requests.post(
        domain,
        auth=("api", api),
        data={"from": "Prasanna Dangol <prasanna.dangol17509@gmail.com>",
              "to": "Freyja Norse <witchfreyja17509@gmail.com>",
              "subject": "Vehicle Found",
              "text": "Congratulations Freyja Norse, Your vehicle has been found"})
    if resp.status_code == 200:
        print("Success")
    else:
        print("Failure")
    return resp

def missing_report_message(message):
    resp = requests.post(
        domain,
        auth=("api", api),
        data={"from": "Prasanna Dangol <prasanna.dangol17509@gmail.com>",
              "to": "Freyja Norse <witchfreyja17509@gmail.com>",
              "subject": "Vehicle Found",
              "text": message})
    if resp.status_code == 200:
        print("Success")
    else:
        print("Failure")
    return resp



# You can see a record of this email in your logs: https://app.mailgun.com/app/logs.

# You can send up to 300 emails/day from this sandbox server.
# Next, you should add your own domain so you can send 10000 emails/month for free.


