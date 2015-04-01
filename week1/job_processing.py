# Coursera Algorithm Part II
# The script for Q1 and Q2 of week 1 PA
# Author: Chao Zhang

from __future__ import division

def read_jobs(raw_data, job_list):
    with open('%s' % raw_data, 'r') as data_content:
        # skip the first line
        data_content.readline()
        # read the raw data and 
        for job_data in data_content.readlines():
            job_details = job_data.rsplit(" ")
            job_list.append(job(job_details[0], job_details[1]))

class Job:

    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
        self.ratio = weight / length

if __name__ == '__main__':
    # the job list
    job_list = []
    # create job list from the raw data
    read_jobs('jobs.txt', job_list)
