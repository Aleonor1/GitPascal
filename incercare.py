from git import Repo,remote


PATH_OF_GIT_REPO = r'/Users/adriannyikita/Desktop/GitPascal/.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()

git_push()

print("manci sarmale")