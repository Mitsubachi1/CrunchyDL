import subprocess, os
import asyncio #learning how to use this module (ﾉ´･ω･)ﾉ ﾐ ┸━┸
import json #new import in dev

agent = ''

async def downloader(browser, agent, output, queue):
    os.chdir(output)
    for link in queue:
        cmd = "yt --embed-sub --user-agent \"" + agent + "\" --extractor-args crunchyrollbeta:hardsub=en-US,None --cookies-from-browser " + browser  + " --merge-output-format mkv "
        task = await asyncio.create_subprocess_shell(cmd + link, shell=True)
        await task.communicate()
#   workaround
        #crunchyrollbeta:ua_workaround
async def queue(browser, agent, output):
    with open('Queue.txt' , 'r+') as file:
        queue, second_queue = [], []
        link = file.readline()
        
        while link != '':
            queue.append(link)
            link = file.readline()
        file.close()

#? Split the list down to half, if uneven still down the half and second list will be longer by 1
        splitIndex = len(queue) // 2
        second_queue = queue[splitIndex:]
        queue = queue[:splitIndex]
        task = [downloader(browser, agent, output, queue), downloader(browser, agent, output, second_queue)]
        await asyncio.gather(*task)
        print(queue)
        print(second_queue)
              

async def main():
    #check for existance of json file, makes one if unavailable
    if(os.path.isfile('config.json')):
        with open('config.json', 'r') as text:
            configType =  text.read()
            text.close()
        info = json.loads(configType)
        browser = info["browser"]
        agent = info["agent"]
        output = info["save_output"]
        print(info) #!DEBUG
        print (agent)

    else:
        #Setup basic args for util
        print("No JSON File Found. Will create one with following info for faster experience.")
        browser = input("Enter Default Browser: ")
        agent = input("Enter your useragent for provided browser")
        output = input("Enter path to save files: ")
        data = {
            "browser" : browser,
            "agent" : agent,
            "save_output" : output
        }
        with open('config.json' , 'w+') as config:
            config.write(json.dumps(data, indent= 5))
            config.close()


    #Advise User
    input("Crunchyroll is using 30 min cookie rule, please go to crunchyroll and run 1 vid to refresh the cookie. Once you done this you may proceed to download")

    await queue(browser, agent, output)
     


if __name__ == "__main__":
    asyncio.run(main())


    

