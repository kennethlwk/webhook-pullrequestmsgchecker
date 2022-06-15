#!/usr/bin/python3
#
# ============================================================================================================================
# File name   : pullrequest_webhook.py
# Created By  : Kenneth Wei-Kiat Lam
# Created Date: 6/14/2022
# ============================================================================================================================
# Description:
#   - This webhook will check the title and body description of the pull request
#   - The requester need to specify “please”, “appreciate”, “would be great” phrases in the title and the body of the message
#   - Impolite pull request will be rejected
#   - Requester would need to delete the branch, and recreate the branch with the polite phrases in the  description
# ============================================================================================================================
# Setup requirement :
#   - User need to download and install ngrok
#       *  https://ngrok.com/download
#   - User need to create a github webhook and include the forwarding URL from ngrok to github webhook
#       *  https://github.com/<OWNER>/<REPO>>/settings/hooks
#   - User need to install flask
#       *   pip install Flask
#   - User need to set the protected branch and checked the "Require status checks to pass before merging"
#       * https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule
# ============================================================================================================================

import requests
import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def api_root():
    return "Welcome to pull request description checker!!"


@app.route('/github', methods=['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        webhook_payload_string = json.dumps(request.json)
        webhook_payload = json.loads(webhook_payload_string)

        pr_title = webhook_payload["pull_request"]["title"]
        pr_body = webhook_payload["pull_request"]["body"]
        pr_status_url = webhook_payload["pull_request"]["statuses_url"]

        headers = {'Content-Type': 'application/json'}

        mandatory_word = ("please", "appreciate", "would be great")
        pr_commit_states = ("failure", "pending", "success")

        if "pull_request" in webhook_payload:
            status = True
            for word in mandatory_word:
                if word in pr_title and word in pr_body:
                    print("You are polite!!!")
                    payload = {"state": pr_commit_states[2],
                               "description": "PR accepted! Thanks for written 'please', 'appreciate', or 'would be great' in your description ",
                               "context": "SUCCESS"}
                    response = requests.post(pr_status_url, headers=headers, json=payload, verify=False)
                    return response.json()
                elif status:
                    status = False
                    print("You are impolite!!")
                    payload = {"state": pr_commit_states[0],
                               "description": "PR rejected! You must write 'please', 'appreciate', or 'would be great' in your description",
                               "context": "FAILURE"}
                    response = requests.post(pr_status_url, headers=headers, json=payload, verify=False)
                    return response.json()
        else:
            print(
                "Please Delete your pull request branch, and create a new commit with better pull request description "
                "in title and body!")
            payload = {"state": pr_commit_states[1],
                       "description": "Please delete your branch! You must write 'please', 'appreciate', or 'would be great' in your description",
                       "context": "PENDING"}
            response = requests.post(pr_status_url, headers=headers, json=payload, verify=False)
            return response.json()


if __name__ == '__main__':
    app.run(debug=True)
