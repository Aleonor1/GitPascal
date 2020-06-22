from git import Repo,remote


PATH_OF_GIT_REPO = r'/Users/adriannyikita/Desktop/GitPascal/.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

print("manci sarmale")

import os
os.system("git add .")
os.system('git commit -m "text2"')
os.system("git push")