from github import Github

access_token = "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"

g = Github(access_token)

user = g.get_user()

print(user.login)
