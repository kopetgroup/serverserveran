#!/usr/bin/env python

import sys, time, os.path, fnmatch, multiprocessing, re, random, os, subprocess, threading, json
from os.path import basename
from pprint import pprint

FNULL = open(os.devnull, 'w')
# Pattern of files to be searched.
fileNamePatternRegex = '^.+\.([a-z0-9A-Z])*$'

# Search directory where the file exists
searchDir = './bots'
#os.path.dirname(os.path.realpath(__file__))

global curlProcess


"""
Watch the directory of searchDir for files or directories with the
name matched the fileNamePattern.
"""
def run():
    listedBots = [] # List of files that exist last time
    activeWorkers = {} # The worker that working now
    while True:
        currentBots = []
        # Finding the files
        for file in os.listdir(searchDir):
            #if (re.match(fileNamePatternRegex, file)):
                # Put it in a list of current fileNamePattern files
                currentBots.append(basename(file))
        # Get the new files according to the last files list (listedBots)
        newBots = [x for x in currentBots if x not in set(listedBots)]
        # Get the diappeared files according to the last files list (listedBots)
        removedBots = [x for x in listedBots if x not in set(currentBots)]
        # Set the last files list to the current file list
        listedBots = currentBots
        # Create new worker for new fileNamePattern files
        for newBot in newBots:

            activeWorkers[newBot] = {}
            activeWorkers[newBot]['instance'] = multiprocessing.Process(name=newBot, target=worker)
            activeWorkers[newBot]['instance'].daemon = True
            activeWorkers[newBot]['instance'].start()

        # Stop disappeared worker for new fileNamePattern files
        for removedBot in removedBots:
            activeWorkers[removedBot]['instance'].terminate()
        # Check the file list every second
        time.sleep(4)


def worker():
    workerName = multiprocessing.current_process().name
    while True:
        bot = threading.Thread(name=workerName, target=doCurlBot)
        bot.start()
        bot.join()

def doCurlBot():
    domain = threading.currentThread().getName()

    print(domain)

    #os.system('python /var/www/html/pitone/bots/'+domain)

    json_data=open('./bots/'+domain)
    data = json.load(json_data)
    json_data.close()

    print "namabot : ", data['name']
    os.system(data['app']+' '+data['path']+' '+data['name'])

    time.sleep(5)
if __name__ == "__main__":
    run()
