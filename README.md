# alert_bot

**Configs:**
1. conf.json - main config. Structure is in an example file
2. regreq.json - List of registration requests. Format - json array (empty config - ``[]``)
3. regs.jsin - List of registred users. Format - json array (empty config - ``[]``)

**Example request:** 

``curl --request POST --header "Content-Type: application/json" --data '{"msg":"Hi! Here is some test msg","secret":"123456"}' <bot_host>/SendAlert ``
