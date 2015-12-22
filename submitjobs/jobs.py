#!/usr/bin/env python
from subprocess import Popen,PIPE
from  parallel import det_Ncores, check_job
from time import sleep
import re

#class for parallel job submissions
class Jobs :
	Ncores=0 			#Number of processing units to use
	Nsub=0			 	#Number of jobs submitted
	Nrem=0 				#Number of jobs remaining
	Nrun=0 				#Number of jobs still running
	JobName=None 		#name of the job script
	JobList=[] 			#List of jobs

	def __init__(self, name=None, n=det_Ncores()):
		self.Ncores=n
		self.JobName=name
		print "Using", n, "cores for computation"

	def submit(self, p):
		self.Nsub+=1
		if self.JobName == None :
			self.JobName=re.sub(r'(.*)/', r'', p[0])
		self.JobList.append(p)

	def run(self) :
		print "%s jobs submitted" % self.Nsub
		self.Nrem=self.Nsub
		for p in self.JobList:
			while(self.Nrun>=self.Ncores): 
				sleep(1)
				self.run_fin()
			Popen(p)
			self.Nrem-=1
			self.Nrun+=1
		while(self.Nrun>0):
			sleep(1)
			self.run_fin()
		print "Runs finished"	
		return 0	
			
	def run_fin(self):
		if check_job(self.JobName)!=self.Nrun:
			print "%s jobs running,   %s jobs in line" %(self.Nrun, self.Nrem)
			self.Nrun=check_job(self.JobName)
			
