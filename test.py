#!/usr/bin/env python
from submitjobs import Jobs

jobs=Jobs()
for i in range(20):
	jobs.submit(['./TestScript/MyRun'])
jobs.run()
