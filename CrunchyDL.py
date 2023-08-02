import subprocess, os
import asyncio #learning how to use this module (ﾉ´･ω･)ﾉ ﾐ ┸━┸
import json #new import in dev

agent = ''

async def downloader(browser, agent, output, queue):
    os.chdir(output)
    for link in queue:
        cmd = "yt --embed-sub --user-agent \"" + agent + "\" --extractor-args crunchyrollbeta:ua_workaround --cookies-from-browser " + browser  + " --merge-output-format mkv "
        task = await asyncio.create_subprocess_shell(cmd + link, shell=True)
        await task.communicate()

async def queue(browser, agent, output):
    with open('Queue.txt' , 'r+') as file:
        queue, second_queue = [], []
        link = file.readline()
        
        while link != '':
            queue.append(link)
            link = file.readline()
        file.close()

        if (len(queue) % 2) == 0: #split list in half, proceed to download
            splitIndex = len(queue) // 2
            second_queue = queue[splitIndex:]
            queue = queue[:splitIndex]
            task = [downloader(browser, agent, output, queue), downloader(browser, agent, output, second_queue)]
            await asyncio.gather(*task)
        print(queue)
        print(second_queue)

        

        
                

async def main():
    #Setup basic args for util
    browser = input("Enter Default Browser: ")
    with open('uagent.txt', 'r') as text:
        agent = text.readline()
        text.close()
    output = input("Enter path to save files: ")
    #Advise User
    input("Crunchyroll is using 30 min cookie rule, please go to crunchyroll and run 1 vid to refresh the cookie. Once you done this you may proceed to download")

    await queue(browser, agent, output)
     


if __name__ == "__main__":
    asyncio.run(main())


    

