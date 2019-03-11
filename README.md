# alert_bot

**Configs:**
1. conf.json - main config. Structure is in an example file
2. strings.json - list of strings for users messages
**Data**
1. regs.json - List of registred users. Format - json array (empty config - ``[]``)
2. subscriptions.json - list of active channels. Structure in example file

**Example request:** 

``curl --request POST --header "Content-Type: application/json" --data '{"msg":"Hi! Here is some test msg","secret":"123456"}' <bot_host>/SendAlert ``
