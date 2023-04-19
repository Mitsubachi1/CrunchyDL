import subprocess
import os
import time


browser = input("Enter Default Browser: ")
with open(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','Queue.txt') , 'r') as file: # open file at user desktop
    
    while True:
        # Ask for input(Derpecated)
        #link = input("Enter CrunchyRoll Link: ") #Deprecated when using file method
        
        link = file.readline() #using file method
        if link == '':
            file.close()
            print("EOF. Download list complete")
            exit()
        
        #standard stuff
        cmd = "yt --embed-sub -f b --cookies-from-browser " + browser  + " --merge-output-format mkv "
        #crunchyroll stuff (gotta figure out multitrack args)
        #cmd = "yt --extractor-args funimation:multitrack_adaptive_hls_v2 --embed-sub -f b --cookies-from-browser " + browser  + " --merge-output-format mkv "


        # Change directory to desktop
        # Run the ytdl in the command prompt
        
        #desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')    #For desktop Storing
        destination = "File location here"     #Store on HDD

        os.chdir(destination)
        subprocess.run(cmd + link, shell=True, capture_output=False)

        #remove line after run
        
        #gotta implement it later
        




