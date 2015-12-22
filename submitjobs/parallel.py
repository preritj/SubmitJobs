#!/usr/bin/env python
from subprocess import Popen, PIPE
import re

def det_Ncores():
	"""
	The function det_Ncores() first attempts to determine
	the number of processign units available for computation.
	If successful, it returns the number of processign units.
	If not successful, returns 1.
	"""
	Ncores=1
	try:
		p=Popen('nproc',stdout=PIPE)
	except OSError:
		print "Unable to determine number of cores"
	else:
		Ncores=int(p.communicate()[0])
	return Ncores


def check_job(job_name):
	"""
	The function check_job( <job_name> ) checks if 
	any job by the name <job_name> is currently running.
	If found, returns the number of jobs running with that name.
	If not found, returns 0.
	""" 
	p=Popen('ps',stdout=PIPE)
	count=0
	for line in p.stdout:
		exp=re.compile(job_name)
		if exp.search(line.split()[3]) is not None:
			count+=1
	return count
