import unittest.mock
import requests


def retrive_list_of_repo(user_name):
    list_of_repo = list()
    url = "https://api.github.com/users/" + user_name + "/repos"
    resp = requests.get(url)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ValueError("Please check repository name!!")
    else:
        data = resp.json()
        for i in range(0, len(data)):
            temp = data[i]
            list_of_repo.append(temp["name"])

    return list_of_repo


def retrive_commit(user_name, repo_name):
    """Get Number of Commits for repo_name"""
    result = dict()
    url_commit = "https://api.github.com/repos/" + user_name + "/"+repo_name+"/commits"
    resp_commit = requests.get(url_commit)
    if resp_commit.status_code != 200:
        # This means something went wrong.
        raise ValueError("Please check repository name!!")
    else:
        data_commit = resp_commit.json()
        result[repo_name] = len(data_commit)

    return result


def main():

    user_name = input("Enter GitHub Repository Name: ")
    try:
        result = retrive_list_of_repo(user_name)
        print("Result :: \n")
        if len(result) == 0:
            print("No Repository Found.")
        for i in range(0, len(result)):
            commits = retrive_commit(user_name, result[i])
            print("Repo Name: " + result[i] + " || " + "No. of Commits: " + commits)
    except ValueError as e:
        print(str(e))
    except Exception:
        print("Unable to connect to server..")


if __name__ == '__main__':
    main()
    unittest.main(exit=False, verbosity=2)

