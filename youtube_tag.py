import pandas as pd
import urllib as ub
import os #join paths/folders to store csv.

#----------------------
#load from url
url='' #download root

def load_youtube_csv_url(url):
    ub.request.retrieve(url)
    #use os.path.join to store the csv file to folder.

#load from directory
def load_youtube_csv(): #load csv we downloaded.
    csv_path=("youtube.csv")
    return pd.read_csv(csv_path)

youtube=load_youtube_csv()    

#-------------------
#function to save the tag to a file.
def get_tag(text_file):
    read=(youtube["Keyword"])
    file_open=open(text_file, 'w')
    n= 10
    while n>=0:
        n=n-1
        tag=str(read[n]+',')
        file_open.write(tag)
        if n==0:
            break

#write the tags to a file.
get_tag("vantage_tags.txt")    

#--------------------
import pyperclip as pc #copy to clipboard.

file_open=open('vantage_tags.txt', 'r') #open the file you previously written the tags.

copy_tags = file_open.read()

pc.copy(copy_tags)