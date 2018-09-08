
# OS
import os, re, requests, json

# Webapp
from flask import Blueprint, request, jsonify, Response

TOKEN = os.environ.get("GIT_TOKEN")

webBP = Blueprint("webBP", __name__, template_folder="webfiles")

@webBP.route("/addIssue", methods=["POST"])
def addIssue():
	json = request.get_json(force=True)
	
	try:
		web = json["git"]
		issue = json["issue"]
	except KeyError:
		return jsonify({}), 400
		
	m = re.search("github.com/(.+?)/(.+?)(/|$)", web)
	try:
		user = m.group(1)
		repo = m.group(2)
	except AttributeError:
		return jsonify({}), 400

	headers = {
	    "Content-Type":"application/json",
	    "Authorization": "token %s" % TOKEN,
	}

	web = "https://api.github.com/repos/" + user + "/" + repo + "/issues"
	r = requests.post(web, json=issue, headers=headers)
	
	resp = Response(response = r.text,
	                status = r.status_code,
	                mimetype = "application/json")
	
	return resp

@webBP.route("/acceptInvitations", methods=["GET"])
def acceptInvitations():
	
	headers = {
	    "Content-Type":"application/json",
	    "Authorization": "token %s" % TOKEN,
	}	
	
	web = "https://api.github.com/user/repository_invitations"
	
	r = requests.get(web, headers=headers)
	
	resp = Response(response = r.text,
	                status = r.status_code,
	                mimetype = "application/json")	
	
	
	for invitation in r.json():
		newWeb = web + "/" + str(invitation["id"])
		r = requests.patch(newWeb, headers=headers)	
	
	return resp
