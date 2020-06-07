# Webex-Webhooks
Code to create a chatbot with the help of webhook and Webex Teams API.

##Overview

Webex-Webhook guides you to create an interactive bot yourself, with the help of current webex API and webhook api provided by Cisco.

There are a few steps that we need to follow before we can use the code. It will be easy once we get through the first part that is binding everything together which is quite confusing but once you understand it, you can easily do it.

1. Login to (https://developer.webex.com/) and create a bot.[We will be mentioning this bot to get message and push messages to the chat]
  --There will be "Bot's Access Token", Copy that and keep it safe.

2. Next thing to do is, Go to this link: (https://developer.webex.com/docs/api/v1/webhooks/create-a-webhook) and copy your Bearer token from the right side window, again keep this safe in your notes.

3. Create your own group on webex teams. You can do it via GUI only. [This is the group in which we will be testing our bot, so add your bot and yourself in that group.]

3. Open Postman application and Send a *GET* request to (https://api.ciscospark.com/v1/rooms) with below parameters:
  --In the below tab, Go to the Authorization tab and select type "Bearer Token" and paste your bearer token there.
  --Now, go to headers tab and add "Content-type : " as "application/json".
  Press send. 
  You will see a list of messages from your own webex teams: Example:
  `
  "items": [
        {
            "id": "Y2lzY29zcGFyazovOWFlM2YtZmU3ZC0zYTNkLTlhZDMtZGQ3Misodsmdsmd",
            "title": "ABCD",
            "type": "direct",
            "isLocked": false,
            "lastActivity": "2020-06-07T12:15:36.340Z",
            "creatorId": "Y2lzY29zcGFyazovL3VzL1BFT5NGIzLTRiODsffdfxvcxYtOTEwNy0yOWY4NjY2NzNkNjM",
            "created": "2020-06-07T12:14:04.540Z",
            "ownerId": "Y2lzY29zcGFyazovL3VzL09VpBVElPTi8xZWI2NWZkZi05NjQzdsadsLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY"
        }
   `     
  --From the list of json chats data that you currently see, select your group name that you have created. you can see the name of your     group in the title. Copy the id value "Y2lzY29zcGFyazovOWFlM2YtZmU3ZC0zYTNkLTlhZDMtZGQ3Misodsmdsmd" and keep it in your notes.  

4. Now, again in the Postman application, Select "POST" and in url bar paste this : (https://api.ciscospark.com/v1/webhooks) 
  --In the below tab, Go to the Authorization tab and select type "Bearer Token" and paste your bearer token there.
  --Now, go to headers tab and add "Content-type : " as "application/json".
  --go to body tab and your body format must look like this:
  
    ```
    {
      "resource" : "messages",
      "event" : "created",
      "filter" : "roomId=Y2lzY29zcGFyazovOWFlM2YtZmU3ZC0zYTNkLTlhZDMtZGQ3Misodsmdsmd",
      "targetUrl" : "http://81d082ef807c.ngrok.io",
      "name" : "check"
  }
  ```
  
  --No need to change resource,event. but in *filter* put your group is that you have taken above as "roomId=yourgroupid". 
  
  --For *targetUrl*, you can give your own external server on which you have a listener or you can just create one using tunneling  application like ngrok. You can download ngrok and just run it, you do not need to do anything else, just open cmd and go to the directory using cd where it is installed as *ngrok.exe*, type in cmd: *ngrok http 8080*, now the port must be same as your internal server 127.0.0.1:8080, for ngrok to tunnel the traffic for you.
  
  --For "name": put it as your webex group name that you have created.
  
  Click Send and your webhook is registered now. you will be presented with below like data:
  
  ```
  {
    "id": "Y2lzY29zcGFyazovL3VzkwnlkwqnrlkwqnrlqnrL1dFQkhPT0svODRkNjYtMzUzZDZiZTk0YWQ1",
    "name": "check",
    "targetUrl": "http://81d082ef807c.ngrok.io",
    "resource": "messages",
    "event": "created",
    "filter": "roomId=Y2lzY29zcGFyazovL3VzL1JbrkjqwbkrjqwbrkjwrtZDcwYWFkOWJlMDg2wwr",
    "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FObkeqbrkjqZkZi05NjQzLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY",
    "createdBy": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82MDVbrkjewrkjLTQ0NDUtOTBkYy1jM2VmZTBkZTAxMjg",
    "appId": "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL0NmMzkyNWejrewjrh2Y0MmFiNzcwZmZhZjFhNTIyMjcxZDI5OTQ4NDhjNjk2YWMwYTEwN2Q2YTg5MjI3",
    "ownedBy": "creator",
    "status": "active",
    "created": "2020-06-07T15:21:01.666Z"
}
```

**Your group is registered now.
Time to add bot in this.

--the requets will be exactly same like above. but all you need to change is:

```
{
      "resource" : "messages",
      "event" : "created",
      "filter" : "roomId=Y2lzY29zcGFyazovOWFlM2YtZmU3ZC0zYTNkLTlhZDMtZGQ3Misodsmdsmd&mentionedPeople=me",
      "targetUrl" : "http://81d082ef807c.ngrok.io",
      "name" : "check"
  }
  ```
  
  **if you see closely above request, I have just added made a small change in *filter*, everything is intact, the roomId is same as well, only add *&mentionedPeople=me* at the end of the roomId and click send.
  
5. We are good to go now. Make sure while running the python script, the port number must match and also ngrok must be running, because our webhook is binded to our ngrok address only. Make changes to the script, like change *bot_token*, add your own bot token that you kept in step 1.
 
  
