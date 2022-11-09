# fork_gitlab_repo

### Description
This tool can be used to fork repositories in Gitlab using the Gitlab API. 

To use, you will need to know:
1. The repository you would like to fork
2. What you would like to name the fork
3. The namespace you would like to fork to
4. The urls to the projects you want to use in the script

### To use:

Clone the repo, then `cd` into the repo, and set up a virtual environment with the Pipfile provided:
```
cd fork_gitlab_repo
pipenv install
pipenv shell
```

Note: This assumes you have pipenv installed on your machine already. See official pipenv documention for [installing pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv)

You will need to set the `url` values in the fork_gitlab_repo function to the urls of the projects you would like to use as fork templates. The ones provided are not actual repos, just examples. :)

Generate a Gitlab [API personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html).

You can use the `--token`, `--repo`, `--name`, and `--namespace` options or set them using the environment variables FORK_TOKEN, FORK_REPO, FORK_NAME, FORK_NAMESPACE to bypass the prompts:

```
./fork_gitlab_repo.py --token "yourtokenhere" --repo "template" --name "template fork --namespace "lmshipp" 
```
or

```
export FORK_TOKEN="yourtokenhere"
export FORK_REPO="template"
export FORK_NAME="template fork"
export FORK_NAMESPACE="lmshipp"
./fork_gitlab_repo.py
```

If these options are not provided, you will be prompted for the name of the repo to fork, and the name of the new repo to create, and the namespace you would like to fork to.

If you are unsure what to do, the options available can be accessed using the `--help` option:

```
./fork_gitlab_repo.py  --help
```

