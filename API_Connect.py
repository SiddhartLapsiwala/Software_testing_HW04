import unittest
import requests


def retrive_repo_details(repo_name):
    result = dict()
    list_of_repo = list()
    url = "https://api.github.com/users/" + repo_name + "/repos"
    resp = requests.get(url)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ValueError("Please check repository name!!")
    else:
        data = resp.json()
        for i in range(0, len(data)):
            temp = data[i]
            list_of_repo.append(temp["name"])

    # Get Number of Commits to each repo
    for j in range(0, len(list_of_repo)):
        url_commit = "https://api.github.com/repos/" + repo_name + "/"+list_of_repo[j]+"/commits"
        resp_commit = requests.get(url_commit)
        if resp.status_code != 200:
            # This means something went wrong.
            raise ValueError("Please check repository name!!")
        else:
            data_commit = resp_commit.json()
            result[list_of_repo[j]] = len(data_commit)

    return result


def main():

    repo_name = input("Enter GitHub Repository Name: ")
    try:
        result = retrive_repo_details(repo_name)
        print("Result :: \n")
        if len(result) == 0:
            print("No Repository Found.")
        for key, value in result.items():
            print("Repo Name: " + key + " || " + "No. of Commits: " + str(value))
    except ValueError as e:
        print(str(e))
    except Exception:
        print("Unable to connect to server..")


if __name__ == '__main__':
    main()
    unittest.main(exit=False, verbosity=2)