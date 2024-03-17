import requests


def send_discord_notification(message):
    webhook_url = "https://discord.com/api/webhooks/1218227266539225168/i_aDfq8NSxVXydSdHmRVqtbf-AxkR4yV1ZEvN03rm3Ury4LmAQuFUKIkO9qDycTqfAOj"
    data = {"content": message}
    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print("Notification sent to Discord!")
    else:
        print("Failed to send notification!")
