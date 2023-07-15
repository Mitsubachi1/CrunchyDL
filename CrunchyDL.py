import subprocess
import os
import threading
import time

def main():
    browser = input("Enter Default Browser: ")
    agent = input("Enter User Agent of browser: ")
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
                exit()
        
            #standard stuff
            #cmd = "yt --embed-sub -f b --cookies-from-browser " + browser  + " --merge-output-format mkv "
            cmd = "yt --embed-sub --user-agent " + agent + " --extractor-args crunchyrollbeta:multitrack_adaptive_hls_v2 --cookies-from-browser " + browser  + " --merge-output-format mkv "
        
            #desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')    #For desktop Storing

            os.chdir(output)
            subprocess.run(cmd + link, shell=True, capture_output=False)


if __name__ == "__main__":
    main()


    

