from github import Github
import requests
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


token = input("access_token")
url = "https://api.github.com/user/repos"

g = Github(token)

headers = {
    "Authorization":"token {}".format(token)
}
data = {
    "visibility" : "all",
    "type" : "all",
    "sort" : "full_name",
    "direction" : "asc"
}

#Attempt to create a graph nbased off info in each repository
def GraphCreation(repo):
    output = requests.get(url,data=json.dumps(data),headers=headers)
    output
    data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
    data = pd.DataFrame(data, columns=[repo.name,repo.created_at,repo.pushed_at,repo.language,repo.size])


#user = g.get_user()
#repoData = repoToData(user)

#ata = pd.DataFrame.from_dict(repoData, orient = 'index', columns = ["Repo Name", 
#"Date created", "Date Last Pushed",, "Language" "Repo Size"])
#plt.show()


#Idea of code below referenced from https://github.com/PyGithub/PyGithub
def commitsToRepo(repo):
    try:
        if repo.get_commits() is not None:
            totalCommits = repo.get_commits().totalCount
            print("Number of commits:")
            print(totalCommits)
    except:
        print("No commits made to this repository")

#def commits_of_repo_github(repo, owner, api):          code reference from https://towardsdatascience.com/introduction-to-git-data-extraction-and-analysis-in-python-e7e2bf9b4606
#    commits = []
#    next = True
#    i = 1
#    while next == True:
#        url = api + '/repos/{}/{}/commits?page={}&per_page=100'.format(owner, repo, i)
#        commit_pg = gh_session.get(url = url)
#        commit_pg_list = [dict(item, **{'repo_name':'{}'.format(repo)}) for item in commit_pg.json()]    
#        commit_pg_list = [dict(item, **{'owner':'{}'.format(owner)}) for item in commit_pg_list]
#        commits = commits + commit_pg_list
#        if 'Link' in commit_pg.headers:
#            if 'rel="next"' not in commit_pg.headers['Link']:
#                next = False
#        i = i + 1
#    return commits
print("****************************************************************************")
for repo in g.get_user().get_repos():
    print("Repository name:",repo.name)
    print("Date created", repo.created_at, "    Last pushed commit",repo.pushed_at)
    print("Language:",repo.language,       "    Size:",repo.size)
    commitsToRepo(repo)
    #print(graphCreation(repo))
    print("***********************************************************************")
