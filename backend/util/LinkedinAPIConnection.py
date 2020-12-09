import requests
import os


def getLinkedinToken(clientID, clientSecret):
    url = "https://www.linkedin.com/oauth/v2/accessToken"

    payload = f"grant_type=client_credentials&client_id={clientID}&client_secret={clientSecret}"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text


if __name__ == '__main__':

    print(getLinkedinToken(os.getenv("LINKEDIN_CLIENT_ID"), os.getenv("LINKEDIN_CLIENT_SECRET")))
