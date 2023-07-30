import subprocess
import os
import asyncio
import time #debug for time

agent = ''

async def downloader(browser, agent, output):
    with open('Queue.txt' , 'r+') as file:
        while True:
        
            link = file.readline() #using file method
            if link == '':
                file.truncate(0)
                file.close()
                subprocess.run("color 2", shell = True, capture_output = False)
                return "EOF. Download list complete"
                
        
            #standard stuff
            #cmd = "yt --embed-sub -f b --cookies-from-browser " + browser  + " --merge-output-format mkv "
            cmd = "yt --embed-sub --user-agent \"" + agent + "\" --extractor-args crunchyrollbeta:ua_workaround --cookies-from-browser " + browser  + " --merge-output-format mkv "
        
            #desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')    #For desktop Storing

            os.chdir(output)
            subprocess.run(cmd + link, shell=True, capture_output=False)

async def main():
    browser = input("Enter Default Browser: ")
    
    with open('uagent.txt', 'r') as text:
        agent = text.readline()
        text.close()


    output = input("Enter path to save files: ")
    input("Crunchyroll is using 30 min cookie rule, please go to crunchyroll and run 1 vid to refresh the cookie. Once you done this you may proceed to download")
    result = await downloader(browser, agent, output)
    print(result) 




if __name__ == "__main__":
    asyncio.run(main())


    

