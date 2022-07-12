# Github_webhook

Install requirements

pip install -r requirements.txt

Run the flask application

python run.py

Install ngrok from the official website

Run ngrok

./ngrok http 5000

The end point would be someting like this

https://61b1-157-50-5-27.in.ngrok.io/webhook/receive

Open github repo to which you want to register the endpoint
Goto settings-> webhook-> add the endpoint in the urls block, select the action specifiers and register.

to check the webhooks triggered

enter the url 

http://127.0.0.1:5000/webhook/display
