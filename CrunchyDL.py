import subprocess
import os
import threading #implement later
import time #debug for time

from selenium import webdriver

agent = ''
def main():
    browser = input("Enter Default Browser: ")
    
    with open('uagent.txt', 'r') as text:
        agent = text.readline()
        text.close()


    output = input("Enter path to save files: ")
    input("Crunchyroll is using 30 min cookie rule, please go to crunchyroll and run 1 vid to refresh the cookie. Once you done this you may proceed to download")
    downloader(browser, agent, output) 





 

def downloader(browser, agent, output):
    with open(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','Queue.txt') , 'r+') as file:
        while True:
        
            link = file.readline() #using file method
            if link == '':
                file.truncate(0)
                file.close()
                subprocess.run("color 2", shell = True, capture_output = False)
                print("EOF. Download list complete")
                exit(0)
                
        
            #standard stuff
            #cmd = "yt --embed-sub -f b --cookies-from-browser " + browser  + " --merge-output-format mkv "
            cmd = "yt --embed-sub --user-agent \"" + agent + "\" --extractor-args crunchyrollbeta:ua_workaround --cookies-from-browser " + browser  + " --merge-output-format mkv "
        
            #desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')    #For desktop Storing

            os.chdir(output)
            subprocess.run(cmd + link, shell=True, capture_output=False)




















if __name__ == "__main__":
    main()


    

