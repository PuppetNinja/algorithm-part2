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
            job_list.append(Job(job_details[0], job_details[1]))

class Job:

    def __init__(self, weight, length):
        self.weight = int(weight)
        self.length = int(length)
        self.ratio = self.weight / self.length
    def __repr__(self):
        return "job detail: weight is: %s, length is: %s, amount of (weight - length): %s, ratio of weight/length: %s" %
            (self.weight, self.length, self.weight - self.length, self.ratio)
    def __str__(self):
        return "%s %s %s" % (self.weight, self.length, self.ratio)

if __name__ == '__main__':
    # the job list
    job_list = []
    # create job list from the raw data
    print("Start reading the raw data......")
    read_jobs('jobs.txt', job_list)

    print("Finish reading the raw data......")
    print("Sort the jobs with decreasing order of (weight - length)")
     
    print("*******************************************")
    print(" Greedy Scheduling using (weight - length) ")
    print("*******************************************")
