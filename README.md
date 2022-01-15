# Software-Engineering-CSU33012
This repository is for accessing the GitHub API and attempting to do a GitHub visualization using the data extracted from my GitHub account.

My initial approach was to write my code using html, css and javascript. I downloaded Node.js and npm and followed my server to local host:8081. 

I found this quit challenging and decided to start from square 1 and changed my language to python as you could implement all areas of code within the same file.

I created a GitHub-Authorization token which allowed me access to my GitHub repositories.

My code requests access to the authorization token of the acquired github account, and will visualise the data of repository name, date created, last pushed commit, repo size and number of commits to that repository.

I have also left in my graph visualistion code as my graphs did not generate accurately, I will leave them to see the anticipated idea.

To run my code, must have python downloaded, my code uses python3.
(You can check by using python --version in the cmdprmpt).

In the terminal, navigate to the file with the code inside and type: 'python3 style.py'

You will be prompted for an access_token, here you enter the personalised access token of the github you would like to explore.


<img width="443" alt="Python Visualisation " src="https://user-images.githubusercontent.com/72949599/149622432-4ff770cd-1e9f-449a-afff-59ccdeb08cfa.png">

The above image shows the visualisation of the produced output from the Github API.





Reference material: https://www.youtube.com/watch?v=5QlE6o-iYcE
https://www.freecodecamp.org/news/learn-to-create-a-line-chart-using-d3-js-4f43f1ee716b/
https://github.com/PyGithub/PyGithub
