#
#   Scrapes Video Links from user Playlist
#   and Tests Youtube functionality on Google Chrome
#   Also Downloads audio using youtube-dl
#
# Modules
import os,sys
import urllib.request,urllib.response, urllib.error
#
# Youtube API Modules
#
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
# More API Material
# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyCBLlHNB1UEeV3o6hDJKIohNszWEku-le4"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
#
#   Youtube Search Functions 
#
def youtube_search(search_string, max_results=25):

    input = search_string.q
    print(input)
    outfile = open('temp.txt','w')

    # outfile = open(input,'w')
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
                # Call the search.list method to retrieve results matching the specified
                # query term.
    search_response = youtube.search().list(q=search_string.q, part="id,snippet", maxResults=max_results).execute()
    videos = []
                # Add each result to the appropriate list, and then display the lists of
                # matching videos
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],search_result["id"]["videoId"]))

    
    for x in range(0,len(videos)):
        outfile.write(videos[x]+'\n')
    
    outfile.close()


def search(artist):

    argparser.add_argument("--q", help="Search term", default=artist)
    argparser.add_argument("--max-results", help="Max results", default=5)
    args = argparser.parse_args()
    youtube_search(args)
    



# Main Program

if __name__ == "__main__":
    #
    # Youtube Search
    #
    artist = sys.argv[1]
    search(artist)


   