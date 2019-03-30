<p align="center">
  <img src="https://imgur.com/g2KAZGh.png">
</p>

# AutoGitReporter
A restAPI for automated issues creating in GitHub.

## How it works?
The GitHub user [@AutoGitReporter](https://github.com/AutoGitReporter) responds to this API accepting invites to collab in the differents repos, and, at the same time creating issues when something goes wrong in an app when you want.

## How to use?
You must do a POST to https://autogitreporter.herokuapp.com/addIssue with a json body like this

```json
{
  "git":"https://www.github.com/userExample/repoExample",
  "issue":{
    "title":"",
    "body":"",
    "assignees": [
      "octocat"
    ],
    "milestone": 1,
    "labels": [
      "bug"
    ]
  }
}  
```
- This will create an issue in repoExample of userExample.
- The "issue" compontent of the json is descripted here by [GitHub API](https://developer.github.com/v3/issues/#parameters-2)
- The return of the post is the same that is descripted in the GitHub web linked above.
- Milestone, Labels and Assignee is only accepted if the bot [@AutoGitReporter](https://github.com/AutoGitReporter) has push access.
- You can give push permissions to [@AutoGitReporter](https://github.com/AutoGitReporter). It will accept it in 24hs.

## Template/Module for use
The template or module to use will contains the next functions:

- [ ] Logging all the activity that the dev wants to be in the issue.
- [ ] Getting specs of the computer where is running.
- [ ] Java/JavaScript/PHP/.NET/Python versions.
