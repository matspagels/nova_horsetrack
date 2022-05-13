#import of packages
import numpy as np 
import matplotlib.pyplot as plt
import requests
import time
import pandas as pd
import os
from csv import writer
from csv import DictWriter

users = pd.read_csv("users.csv")

class User:
    def __init__(self, username, password, balance):
        
        self.username = username
        self.password = password
        self.balance = balance

        df = pd.read_csv("users.csv", sep=";")        
        self.user_id = len(df.index) + 1
        
        new_user_df = pd.DataFrame()

        new = new_user_df.append({
                'id': self.user_id,
                'username': self.username,
                'password': self.password,
                'balance': int(self.balance),
                'total money bet': 0,
                'nr_win': 0,
                'nr_loss': 0, 
                'nr_bets': 0, }, ignore_index=True)

        new.to_csv("users.csv", sep = ";", mode='a', index=False, header=False)

def appender(username, password, balance):
    
    df = pd.read_csv("users.csv", sep=";")

    new = {
                'id': len(df.index),
                'username': username,
                'password': password,
                'balance': int(balance),
                'total money bet': 0,
                'nr_win': 0,
                'nr_loss': 0, 
                'nr_bets': 0,
                'logged_in' : 0}

    append_series = pd.Series(new)

    new_df = df.append(append_series, ignore_index = True)

    new_df.to_csv("users.csv", sep = ";", mode='w', index=False, header=True)

def change_database(user_id, variable_to_change, new_value):

    df = pd.read_csv("users.csv", sep=";")
    column_number = df.columns.get_loc(variable_to_change)
    df.iat[user_id, column_number] = new_value
    df.to_csv("users.csv", sep = ";", mode='w', index=False, header=True)

def add_database(user_id, variable_to_change, new_value):

    df = pd.read_csv("users.csv", sep=";")
    column_number = df.columns.get_loc(variable_to_change)
    df.iat[user_id, column_number] += new_value
    df.to_csv("users.csv", sep = ";", mode='w', index=False, header=True)

def sub_database(user_id, variable_to_change, new_value):

    df = pd.read_csv("users.csv", sep=";")
    column_number = df.columns.get_loc(variable_to_change)
    df.iat[user_id, column_number] -= new_value
    df.to_csv("users.csv", sep = ";", mode='w', index=False, header=True)        

def create_user(username,password, balance):
    

    df = pd.read_csv("users.csv", sep=";")


    if username in list(df["username"]):
        
        print("There seems to someone with the same name as you. Please take another one.")
        
    else:
        new_user = User(username, password, balance) 
   
def login_user(username, password):
    
    df = pd.read_csv("users.csv", sep=";")
    if username in list(df["username"]):
        user_id = df.index[df['username']==username].tolist()[0] 
                                                    
        
        if password == df["password"][user_id]:
            
            print("This was the right password you are now logged in")
        
        else:
            
            print("Wrong password, sorry...")
    else:
        
        print("Username does not exist.")      







