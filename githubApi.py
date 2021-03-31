import requests
import json


def inputInfo():
    val = input("Enter github account name: ")
    # checks if value input is empty
    if(val == ""):
        return -1
    res = requests.get("https://api.github.com/users/" + val + "/repos")

    # checks if account is real
    if(res.status_code == 200):
        return val
    else:
        return -1


def grabRepoList(acc):
    res = requests.get("https://api.github.com/users/" + acc + "/repos")
    data = res.json()
    repoList = []
    for d in data:
        repoList.append(d['name'])
    commitList = []
    for repo in repoList:
        commitRes = requests.get(
            "https://api.github.com/repos/" + acc + "/" + repo + "/commits")
        commitData = commitRes.json()
        commitList.append(len(commitData))

    # checks if we were able to pull from correct amount of repos to commit lists
    if(len(repoList) != len(commitList)):
        return -1

    dataList = []
    for i in range(len(repoList)):
        dataList.append(str(repoList[i]) + " has " +
                        str(commitList[i]) + "commits")
    return dataList


def main():
    accountName = inputInfo()
    print(grabRepoList(accountName))


if __name__ == "__main__":
    main()
