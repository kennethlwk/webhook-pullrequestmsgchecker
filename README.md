# webhook-pullrequestmsgcheck

## Description:
   - This webhook will check the title and body description of the pull request
   - The requester need to specify “please”, “appreciate”, “would be great” phrases in the title and the body of the message
   - Impolite pull request will be rejected
   - Requester would need to delete the branch, and recreate the branch with the polite phrases in the  description

## Setup requirement :
   - Python 3 need to be installed 
       *  https://www.python.org/downloads/
       *  Edit Path Environment Variable and add your Python310 folder  C:\Users\youeFolder\AppData\Local\Programs\Python\Python310
       *  Edit Path Environment Variable and add your Python310\Scripts   C:\Users\yourFolder\AppData\Local\Programs\Python\Python310\Scripts
   - User need to download and install ngrok
       *  https://ngrok.com/download
       *  Edit Path Environment Variable and add your ngrok folder C:\Users\yourFolder\AppData\Local\Programs\ngrok
       *  Open a terminal, and execute "ngrok http 5000" command to start ngrok server
   - User need to create a github webhook and include the forwarding URL from ngrok to github webhook
       *  https://github.com/OWNER/REPO/settings/hooks
       *  Paste the ngrok forwarding url into ngrok webhook
       *  Select the "Let me select individual events" and checked the "Pull requests" checkbox
       *  ![image](https://user-images.githubusercontent.com/22057288/173825603-ad3a46ed-aeb2-40f0-9b3a-f7a4d8a247fd.png)
   - User need to install flask in 
       *   pip install Flask
   - User need to set the protected branch and checked the "Require status checks to pass before merging"
       * https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule
![image](https://user-images.githubusercontent.com/22057288/173727304-51c845a4-9c26-47b5-92ed-de8880af4feb.png)

## Testing:
   - Observe the request and respond http messages in the executing terminal
   - "Recent Deliveries" section in the webhook which lists, at a glance whether a delivery was successful (green check) or failed (red x).
   - Create pull request with a separate github account to fork and clone the repo which has the webhook configured and protected branch setup, perform different "actions" on the  github request to observe different states on the github pull request interface
  
## Result:
  Tested on the branch with protective branch configured and webhook configured
  - The picture below, show a branch created with politeness word and another branch without politeness word 
  ![image](https://user-images.githubusercontent.com/22057288/173721663-9f624d11-e86e-43bd-a6e6-2d12922f731e.png)
  
  - The branch without the politeness word have check failed, and it is recommended to delete the branch and recreate it with a politeness word included in the description
  ![image](https://user-images.githubusercontent.com/22057288/173722287-dc08aede-bb52-4867-a10d-f71dc77d49cf.png)
  
  - The branch with the politeness word is green and verify success
  ![image](https://user-images.githubusercontent.com/22057288/173722883-1a0ddf12-86af-48f6-b306-1fba93d8ed6e.png)

  
