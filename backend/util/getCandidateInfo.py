import LinkedinAPIConnection
import os
import requests
import re


def getCandidateInfo(LinkedInURL):
    """
    get candidates info from linked in
    :param LinkedInURL:
    :return: a diction
    """
    clientID = os.getenv("LINKEDIN_CLIENT_ID")
    clientSecret = os.getenv("LINKEDIN_CLIENT_SECRET")

    token = LinkedinAPIConnection.getLinkedinToken(clientID, clientSecret)

    if match := re.search(r"https://www.linkedin.com/in/(.*)/", LinkedInURL, re.IGNORECASE):
        profileID = match.group(1)
    elif match := re.search(r"www.linkedin.com/in/(.*)/", LinkedInURL, re.IGNORECASE):
        profileID = match.group(1)
    else:
        profileID = LinkedInURL

    url = f"https://api.linkedin.com/v2/people/(id:{profileID})?projection=(id,firstName,lastName)"
    print(url)

    payload = {}
    files = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload, files=files)

    return response.text


if __name__ == '__main__':
    print("testing with : https://www.linkedin.com/in/titouan-joseph-revol/")
    getCandidateInfo("https://www.linkedin.com/in/titouan-joseph-revol/")
    print("testing with : www.linkedin.com/in/titouan-joseph-revol/")
    getCandidateInfo("www.linkedin.com/in/titouan-joseph-revol/")
    print("testing with : titouan-joseph-revol")
    getCandidateInfo("titouan-joseph-revol")
