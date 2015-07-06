#
#   Scrapes Video Links from user Playlist
#   and Tests Youtube functionality on Google Chrome
#   Also Downloads audio using youtube-dl
#
#
import os,sys,time,unittest,bs4
import urllib.request,urllib.response, urllib.error
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
#
# Classes 
#
#
# Selenium for Browser Automation
class SelTest(unittest.TestCase):

	def setUp(self):
			self.driver=webdriver.Firefox()

	def test_stats(self):
            # Open Browser and grab Stats
        	driver = self.driver
        	driver.get(thread2_arg)
        	
	def tearDown(self):
       	 	self.driver.close()

# Beautiful Soup for Scrpaing Web Data 
class SoupScrape:

   #  
    def GetStats(self,code):
        #
        video_url = 'http://www.youtube.com/watch?v=' + code
        startpage = urllib.request.urlopen(video_url)
        soup = BeautifulSoup(startpage.read())
        #
        # Get Number of Views
        rawview_data = soup.find('div', {'class': 'watch-view-count'})
        view_number = rawview_data.contents[0]
        #
        # Get Number of Likes and Dislikes
        raw_like = soup.find('button',{'class':'like-button-renderer-like-button'})
        raw_dislike=soup.find('button',{'class':'like-button-renderer-dislike-button'})
        # Likes
        likes = raw_like.contents[0]
        for data in likes:
            num_of_likes = data

        # Dislikes
        dislikes = raw_dislike.contents[0]
        for data in dislikes:
            num_of_dislikes = data

        print(view_number,num_of_likes, num_of_dislikes)
  
#       
# Main Program
if __name__ == "__main__":
    #
    #
    stat_fetch = SoupScrape()
    songcode_list = []
    artist_file = open('baycolablist.txt','r')
    artist_list = artist_file.readlines()
    artist_file.close()
    for artist in artist_list:
        input_artist = 'yTsearch.py --q ' + "'" + artist + "'" 
        os.system('python3 ' + input_artist)
        video_file = open('temp.txt','r')
        video_list = video_file.readlines()
        x = 0
        for line in video_list:
            song = line
            begin = (len(song)-2)-11
            end = begin + 11 
            song_code = song[begin:end]
            songcode_list.append(song_code)

        for code in songcode_list:
            stat_fetch.GetStats(code)
            
    artist_file.close()



