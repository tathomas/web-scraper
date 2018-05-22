from lxml import html
from lxml import etree
from io import StringIO, BytesIO
from bs4 import BeautifulSoup
import requests

#-------------------------------------------------------------------------------# Method Declarations
#-------------------------------------------------------------------------------

def getGames (text):
 #TODO: Use etree and parsedhtml from below to decipher the html string
 #      The goal is to return a list of Game objects. Create the game objects
 #      in a loop, setting the values with the stirngs extracted from the html

 # Decipher html string

 # Loop -> create Game objects. Store in list

 # Return game_list

 return 1

def main():

 # Change URL here. Some may not work and have some text about 'robots.txt',
 # you just can't use that website for now
 page = requests.get('http://www.vegasinsider.com/nfl/odds/offshore/')
 tree = html.fromstring(page.content)
 
 #------------------------------------------------------------------------------
 # Uses etree
 #------------------------------------------------------------------------------

 # To print entire URL html text
 mystr = etree.tostring(tree, pretty_print=True)

 # To print one line at a time
 i=1
 for line in mystr:
  print i , "  " , line
  i+=1

 #------------------------------------------------------------------------------
 # Uses parsed html
 #------------------------------------------------------------------------------

 parsedhtml = BeautifulSoup(page.content, 'html')

 # finds specific class name inside html str

 # html text
 print parsedhtml.body.find('td', attrs={'class':'viCellBg2'})

 # actual text
 print parsedhtml.body.find('td', attrs={'class':'viCellBg2'}).text

 myGames = getGames(mystr)

#-------------------------------------------------------------------------------# Game Class
#-------------------------------------------------------------------------------

class Game:
 def __init__(self, team_a, team_b, line, ou):  #...other game stats
                                                # (score after, our bets...)
  self.team_a = team_a
  self.team_b = team_b
  self.line = line
  self.ou = ou

  # add self.*** = *** below to add more parts
 
#-------------------------------------------------------------------------------
  
#Run main
main()








