import streamlit as st
from PIL import Image
import pandas as pd
from helpers import *
from streamlit_option_menu import option_menu
import time
import requests
import matplotlib
import random
import pandas as pd
import numpy as np

welcome = st.container()
tutorial = st.container()
horsetrack = st.container()
leaderboard = st.container()
footer_picture = st.container()


#sidebar menu with option menu add-on

with st.sidebar:
    selected = option_menu("Navigation", ["Welcome", "Tutorial", "Racetrack", "Leaderboard"], 
        icons=['house', 'info-circle', 'strava', 'graph-up'], menu_icon="list", default_index=1)
    
    #userbase read process // login status confirmation

df = pd.read_csv("users.csv", sep=";")

if 1 in list(df["logged_in"]):
    logged_in = True
    logged_in_user = df.index[df["logged_in"]==1].tolist()[0]

if 1 not in list(df["logged_in"]):
    logged_in = False
    logged_in_user = -1

#welcome page


if selected == "Welcome":

    with welcome: 
        
        image = Image.open('logo.png')
        st.image(image)  
                                                     #main_page 
        st.title("Welcome to Nova´s Horsebetting Track!")
        st.subheader("Glad to have you here!")
        st.write("After opening your personal betting account, you will be able to bet on our wide array of race horses and jockeys - ready?")
        st.text("")
        st.write("Every new customer starts of with 1000 credits on the house. You can use the sidebar to navigate. If you haven´t done any betting so far, feel free to check our our 'Tutorial' after signing up!")
        st.text("")
        
    #login page start
    
        st.subheader("Login or Create a User")  
    
        if logged_in == False: 
            st.write("Please login in with your username and password. If you have no account please create a new user")
            col1, col2 = st.columns(2)
            username = col1.text_input("Username")
            password = col2.text_input("Password")
                
            if col1.button("Login"):
    
                    if logged_in == True:
    
                        st.write("You are already logged in. To switch users please log out before!")
    
                    if logged_in == False:
                    
                        #create dataframe
    
                        df = pd.read_csv("users.csv", sep=";")
    
                        #check if user is in database
    
                        if username in list(df["username"]):
    
                            user_id = df.index[df['username']==username].tolist()[0] #assign index
    
                            if password == df["password"][user_id]: #compare the password the user has typed in whith the password in the data base
                                
                                logged_in = True
    
                                logged_in_user = user_id
    
                                name = df["username"][logged_in_user]
    
                                st.write(f"Welcome. You are logged in as user {name}") 
    
                                change_database(logged_in_user, "logged_in", 1)
    
                                page = "Betting"
    
                            else:
                                st.write("Wrong Password. Please try again!")    
    
                        else:
    
                            st.write("Username does not exist. Try again or create new user!")
    
    
                #new user
    
            st.header("")
            st.header("")
    
            st.header("Create a new User")
            col3, col4 = st.columns(2)
    
            username_new = col3.text_input("Select Username")
                
            password_new = col4.text_input("Select Password")
    
            st.header("")
    
            if st.button("Create User"):
                    
                    df = pd.read_csv("users.csv", sep=";")
    
                    if username_new in list(df["username"]):
                        
                        st.write("This username is already taken. Please try again with another one.")
    
                    else:
                        
                        appender(username_new, password_new, 1000)
    
                        st.write(f"A new user {username_new} has been created successfully!")
    
        if logged_in == True:
    
            df = pd.read_csv("users.csv", sep=";")
    
            log_name = df["username"][logged_in_user]
    
            st.write(f"You are currently logged in as user {log_name}")
    
            if st.button("Logout"):
    
                if logged_in == False:
    
                    st.write ("You are already logged out!")
                
                if logged_in == True:
    
                    logged_in = False
    
                    change_database(logged_in_user, "logged_in", 0)
    
                    logged_in_user = -1
    
                    st.write("You were logged out successfully!")
                    
    image = Image.open('footer.png')
    st.image(image)        
                
                    
        
elif selected == "Tutorial":
    
    with tutorial:
        col1, col2, col3 =st.columns(3)
        col1.header("How To Play")
        st.write("")
        st.write("To bet and earn credits while doing this is what you have to do...")
        st.write("")
        col1, col2, col3 = st.columns(3)
        col1.subheader("Step 1:")
        col1.text("Decide On Your Champion")
        col1.write("")
        image = Image.open('pick.png')
        col1.write("")
        col1.image(image, width=200)  
        col2.subheader("Step 2:")
        col2.text("Pick Your Amount To Bet")
        col2.write("")
        image = Image.open('bet.png')
        col2.write("")
        col2.image(image, width=200)  
        col3.subheader("Step 3:")
        col3.text("Confirm Bet & Start")
        col3.write("")
        image = Image.open('go.png')
        col3.write("")
        col3.image(image, width=200)  
                         
        
elif selected == "Racetrack":
    
    with horsetrack:
        
        col1, col2, col3 = st.columns(3)
        
        image = Image.open('racetrack_links.png')
        col1.image(image)
        col2.header("")
        col2.header("")
        col2.header("The Racetrack")
        image = Image.open('racetrack_rechts.png')
        col3.image(image)
        
        df = pd.read_csv("users.csv", sep=";")

        if logged_in == True:

            name = df["username"][logged_in_user]
            current_balance = df["balance"][logged_in_user]

            if current_balance > 0:
                
                st.write("Your are here as:")
                st.text(name)
                st.write("Your credit score is:")
                st.write(int(current_balance))
                image = Image.open('line.png')
                st.image(image)
            
            st.subheader("These are the contesting horses:")
            
            col1, col2, col3, col4, col5, col6 = st.columns(6)
            
            image = Image.open("info_horses.png")
            col1.image(image)
            col1.header("")
            col2.header("")
            col2.write("Champion 1")
            col3.header("")
            col3.write("Champion 2") 
            col4.header("")
            col4.write("Champion 3")
            col5.header("")
            col5.write("Champion 4")
            col6.header("")
            col6.write("Champion 5")
            
            st.subheader("Pick your Champion!")
            
            horse_selection = st.radio("Choice", ('Champion 1', 'Champion 2', 'Champion 3', 'Champion 4', 'Champion 5'))

            st.write(f'You selected {horse_selection}')
            
            st.subheader(f"How much credits do you want to bet on {horse_selection}?")
            
            bet_size = st.slider('Slide the button to how much you want to risk!')
            st.write(f'You are betting {bet_size} on {horse_selection}')
            
            st.subheader("Are you ready to start?")
            ready = st.checkbox('I´m ready')

            if ready:
                st.write('Great - Good Luck!')
                
                st.subheader("Press Go")
                
                if st.button('Go', help("The suspension is high")):
                    
                    st.write("The race has started!")
                    st.write('The horses are running. Most races take about 100 seconds!')
                    st.text("For you, we sped it up..")
                        
                    race_bar = st.progress(0)

                    for percent_complete in range(100):
                                time.sleep(0.1)
                                race_bar.progress(percent_complete + 1)
                    for percent_complete in range(100):
                                  time.sleep(0.1)
                                  race_bar.progress(percent_complete + progress1)  
                                  
                    time = 0
                    progress1 = 0
                    progress2 = 0
                    progress3 = 0
                    progress4 = 0
                    progress5 = 0
                    pro = True

                    while pro == True:
                        
                            steps = random.randint(1, 3)
                            
                            progress1 += steps
                            
                            
                            if progress1 >= 100:
                                pro = False
                        
                            steps = random.randint(1, 3)
                            
                            progress2 += steps
                           
                            
                            if progress2 >= 100:
                                pro = False
                            
                        
                            steps = random.randint(1, 3)
                           
                            progress3 = progress3 + steps
                           
                            
                            if progress3 >= 100:
                                pro = False
                                
                        
                            steps = random.randint(1, 3)
                            
                            progress4 = progress4 + steps
                            
                            
                            if progress4 >= 100:
                                pro = False
                                
                        
                            steps = random.randint(1, 3)
                            
                            progress5 = progress5 + steps
                            
                            
                            if progress5 >= 100:
                                pro = False
                                
                    
                                

                    winners = pd.DataFrame({'Start to Finish (in s)' : [int(progress1), int(progress2), int(progress3), int(progress4), int(progress5)]},
                                           index=['Champion 1', 'Champion 2','Champion 3','Champion 4','Champion 5'])
                    

                    winners = winners.sort_values(by='Start to Finish (in s)', ascending=True)

                    st.subheader("The Winner is...")

                    st.subheader(winners[0:1].index[0])
                    
                    st.header("")
                
                    st.write(winners)
                    
                    

                    if logged_in == True:
                               
                               horse = horse_selection
                               bet = bet_size
                
                               df = pd.read_csv("users.csv", sep=";")
                               starting_balance = df["balance"][logged_in_user]
                
                               if starting_balance - bet_size >= 0:
                
                                   add_database(logged_in_user, "total bet amount", bet)
                
                                   add_database(logged_in_user, "nr_bets", 1)
                
                                   sub_database(logged_in_user, "balance", bet)
                
                                   #define if win or loose
                        
                                   win = True
                                   
                                   if str(horse_selection) == str(winners[0:1].index[0]):                                       
                                           win = True
                                           
                                   else:                                          
                                           win = False                                           
                                   
                                   if win == True:
                                       
                                       st.write("Congrats! You bet on the right horse")
                                       st.write(f"You won: {bet_size*3}")
                                       add_database(logged_in_user, "balance", bet_size*3)
                                       add_database(logged_in_user, "nr_win", 1)
                
                                   if win == False:
                                       
                                       st.write("Not this time.. Try again!")
                                       add_database(logged_in_user, "nr_loss", 1)
                
                                   df = pd.read_csv("users.csv", sep=";")
                
                                   user_balance = df["balance"][logged_in_user]
                                   
                                   st.write(f"You lost your bet of: {bet_size}")
                
                                   st.write(f"Your new credits: {int(user_balance)}!")
                
                               else:
                
                                   col7.write("I guess you need a bit more credits for that!")
                
                
                if logged_in == False:
                
                               col7.write("Tell the chashier you´re here first and check in, Sir..") 
    
                if current_balance == 0:
    
                    st.header(f"Sorry {name}!")
                    st.write(f"You don´t have any credits left, better luck next time!")
    
            if logged_in == False:
                
                st.write("")
                col1, col2, col3 = st.columns(3)
                col2.write("You have to Check-In first!")
    
                
elif selected == "Leaderboard":
        
        with leaderboard:
            st.header("See how you hold up in comparison to your fellow betters!")
            st.subheader("Hope to see you up there.. ""(not in the loss section)")
    
        df = pd.read_csv("users.csv", sep=";") 
    
        criteria = {"Total Wins" : "nr_win", "Total Losses" : "nr_loss", "Balance" : "balance", "Number of Total Races Betted on" : "nr_bets"}
    
        lables = st.selectbox("What Do You Want To Compare?", ["Total Wins", "Total Losses", "Balance", "Number of Total Races Betted on"])
        
        col1, col2, col3 = st.columns(3)
        
        st.write(df.sort_values(by=[criteria[lables]], ascending = False).head(10)[["username", criteria[lables]]])
