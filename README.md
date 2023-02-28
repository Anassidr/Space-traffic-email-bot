# Space news!
## Exploiting a public API with Python to receive emails about Space traffic

Given that I like space-related things, I wrote a script to receive an email everytime an astronaut leaves or goes into space (to the International Space Station for e.g) 

In order to do this:

1. I wrote a .py script where there is : 
    - A function that can send an email using the library smtplib (uses gmail's server smtp)
    - A function that retrieves the list of astronauts from the API, converts it into a Pandas DataFrame, and compares it to the last df we had stored. 
    - If this function detects that there was a change in the list, an email is sent using the first function. 

2. I created a cronjob that executes the script. This allows me to automatically run the script daily locally on my computer. 
