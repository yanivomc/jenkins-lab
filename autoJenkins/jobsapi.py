from autojenkins import Jenkins
import time
# configure jenkins URL
j = Jenkins('http://jenkins:8080', auth=('admin', 'admin'))

job = 'FirstPythonJob_unittest'
# Trigger manual build and get results
#run job
j.build(job)

#get last result info
jobstatus = j.last_result(job)['result']
x = str(jobstatus)

# Check Job status and do something when completed / failed etc.. 
while x == "None":
    print ("Job ", job , "is still building")
    time.sleep(5)
    x = j.last_result(job)['result']
    x = str(x)
    if x != "None":
        print ("Job Status is:" , x)
    else:
        pass
