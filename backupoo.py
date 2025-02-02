#!/usr/bin/python3
''' Execute backup job.

Usage: python backup.py <job_name>

This script allows the user to execute a backup job to backup a single file or a directory.

The job to be executed is specified by name as the single ommand line argument passed to the script.ArithmeticError

The job details are defined in a job object that is included as a member of a list in the configuration file.
'''

# import modules

import sys
from emailconfig import EmailConfig
from job import Job
from backup import Backup, BackupFile, BackupDirectory
from backupcfg import job_msg, usage_msg, logfile, email_config, jobs, emailurl

def main():
    '''
    Execute backup job from job list with a name matching the first command line argument.
    '''

    # check for correct number of command line arguments
    if len(sys.argv) != 2:

        print(usage_msg)

    else:

        # if job number from command line in jobs list then perform backup job
        job_name = sys.argv[1]

        if job_name not in jobs:

            print(job_msg)

        else:

            # Get current job object
            job = jobs[jobs.index(job_name)]
            
            # Set job attributes

            # determine the type of backup to perform based upon job type
            backup = BackupFile() if job.is_file_job else BackupDirectory() 
            job.set_backup(backup)
           
            job.set_logfile(logfile)
            #job.set_email_config(email_config)
            job.set_emailurl(emailurl)
            
            # perform backup
            if not job.errors:
                job.do_backup()

            # send errors as email
            if job.errors:
                pass # job.do_email()

            # record result in logfile
            job.do_logfile()
            
    sys.exit(0)

if __name__ == '__main__':
    main()

