from flask import Blueprint, request, render_template
from app.extensions import data

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')


@webhook.route('/receiver', methods=["POST"])
def receiver():
    # check the type of data returned from the webhook
    if request.headers['Content-Type'] == 'application/json':
        res = request.json
        if res.get('head_commit') is not None:
            # for push request
            action = "push"
            author = res['head_commit']['author']['name']
            to_branch = res['ref']
            timestamp = res['head_commit']['timestamp']
            # insert into mongodb cluster
            data.insert_one({"action": action, "author": author, "to_branch": to_branch, "timestamp": timestamp})
        elif res.get('action') is not None:
            if res.get('action') == 'opened':
                # for pull request
                action = "pull"
                author = res['pull_request']['base']['user']['login']
                from_branch = res['pull_request']['head']['ref']
                to_branch = res['pull_request']['base']['ref']
                timestamp = res['pull_request']['created_at']
                # insert into mongodb cluster
                data.insert_one({"action": action, "author": author, "from_branch": from_branch, "to_branch": to_branch,
                                 "timestamp": timestamp})
            else:
                # for merge action
                action = "merge"
                author = res['pull_request']['base']['user']['login']
                from_branch = res['pull_request']['head']['ref']
                to_branch = res['pull_request']['base']['ref']
                timestamp = res['pull_request']['created_at']
                # insert into mongodb cluster
                data.insert_one({"action": action, "author": author, "from_branch": from_branch, "to_branch": to_branch,
                                 "timestamp": timestamp})
        return {}, 200


@webhook.route('/display', methods=['GET'])
def display():
    # fetch the latest record in the mongodb storage
    res = data.find().sort('_id', -1).limit(1)
    # return the html webpage and pass the fetched record to it
    return render_template("index.html", res=res[0])

