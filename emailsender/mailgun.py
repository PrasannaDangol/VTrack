import requests
import config


def send_simple_message():
    return requests.post(
        config.domain,
        auth=("api", config.api),
        data={"from": "Prasanna Dangol <prasanna.dangol17509@gmail.com>",
              "to": "Freyja Norse <witchfreyja17509@gmail.com>",
              "subject": "Vehicle Found",
              "text": "Congratulations Freyja Norse, Your vehicle has been found"})


# You can see a record of this email in your logs: https://app.mailgun.com/app/logs.

# You can send up to 300 emails/day from this sandbox server.
# Next, you should add your own domain so you can send 10000 emails/month for free.

send_simple_message()
