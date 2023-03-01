
import os 
import requests as re
 
import smtplib, ssl

def kindbot_emails(receiver_email, message):

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "kindpythonbot@gmail.com"
    password = os.environ.get("kindpythonbot_password") 
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 
    return 

#-----------------------------------------------------------------------------------------

import pandas as pd

def compare_traffic():
    data = re.get("http://api.open-notify.org/astros.json").json()
    astronauts = []
    for astronaut in data['people']:
        astronauts.append([astronaut['name'],astronaut['craft']])
    header = ["astronaut", "craft"]
    df = pd.DataFrame(astronauts, columns=header)

    #Compare dataframe we just built to the dataframe we had stored on the computer from the last API call 
    path = "/home/thinkpadder/Documents/DE/kindpythonbot_astronauts/astronauts_list.csv"
    old_df = pd.read_csv(path)
    message = ""

    if not df.equals(old_df):
        
        arrivals = df[df.isin(old_df)['astronaut']==False]
        departures = old_df[old_df.isin(df)['astronaut']==False]

        for i in range(len(departures)): 
            message += f"{departures.iloc[i][0]} has left space ({departures.iloc[i][1]}) \n"
            
        for i in range(len(arrivals)): 
            message += f"{arrivals.iloc[i][0]} has entered space ({arrivals.iloc[i][1]}) \n"

        message += f"There are currently {data['number']} astronauts in Space :) \n"

        message += f"Have a nice day"

        # df.to_csv(path, index=False) #overwrite old df with new df 

        #send email in case there is change in df 
        receiver_emails = ["anasskamal.id@gmail.com"]
        message = 'Subject: {}\n\n{}'.format("Space news!", message)

        for email in receiver_emails:
            kindbot_emails(email, message)


    return

#-----------------------------------------------------------------------------------------

compare_traffic()


