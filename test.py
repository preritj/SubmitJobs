#!/usr/bin/env python
from submitjobs import Jobs

jobs=Jobs()
#Submit 20 jobs
for i in range(20):
	jobs.submit(['./TestScript/MyRun'])
#Run the jobs and wait till the jobs are finished
jobs.run()
