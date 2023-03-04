# Space news bot! 
## Exploiting a public API with Python to receive emails about Space traffic

Given that I like space-related things, I wrote a script to receive an email everytime an astronaut leaves or goes into space (to the International Space Station for example) 

In order to do this:

1. Write a .py script where there is : 
    - A function that can send an email using the library smtplib (uses gmail's server smtp)
    - A function that retrieves the list of astronauts from the API, converts it into a Pandas DataFrame, and compares it to the last df we had stored. 
    - If this function detects that there was a change in the list, a message is formatted then an email is sent using the first function. 

2. Create a cronjob that executes the script. This allows you to automatically run the script with the frequency you want (I run it daily). 
