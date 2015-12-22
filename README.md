# SubmitJobs
## Simple python script for submitting jobs in parallel
### tested on linux/MacOS

Example on how to run scripts in parallel can be found in test.py located in the main directory 

* Jobs class takes two *optional* arguments on initialization :  
j = Jobs( Script_name , Ncores )    
Script_name is the name of the script you want to run  
Ncores is the number of processing units to be used for computation   

If the arguments are not specified, these parameters are **automatically** determined. 
(To go in to some detail, Ncores is determined using 'nproc' command while Script_name using 'ps' command)

* To submit jobs, do :   
  j.submit(p)  
  where p is the script to be run. For example,   
    to run 'ls -a'          ,     p=['ls','-al']  
    to run './MyScript'     ,     p=['./MyScript']  

* Finally, to run the jobs, do :
  j.run() 

After you run test.py, output looks something like this :  
Using 2 cores for computation  
  10 jobs submitted  
  2 jobs running,   8 jobs in line  
  2 jobs running,   6 jobs in line  
  2 jobs running,   4 jobs in line  
  2 jobs running,   2 jobs in line  
  2 jobs running,   0 jobs in line  
  Runs finished  
