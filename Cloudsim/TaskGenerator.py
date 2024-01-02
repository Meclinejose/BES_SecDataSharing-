from SimPy.Simulation import *
from Cloudsim.Task import *
from Cloudsim.Job import *
import numpy

class TaskGenerator(Process):

    def __init__(self, scenario, input_parameters):

        Process.__init__(self)
        self.scenario = scenario

        # Following are input parameters to the task generator.
        # Stores a list of input parameter tuples
        self.task_parameters = list(map(lambda x:tuple([0.0]) + tuple(list (map(lambda y:int(y), [1.0]))), input_parameters))
        # XXX: Keep seeds modifiable later on!
        #self.cpuRandomObject = random.Random (1)
        #self.memRandomObject = random.Random (2)
        
        # This list of tasks is submitted to the scheduler
        self.tasklist = []

    def numJobs(self):

        return self.task_parameters[0][1]

    def generate_tasks (self):

        for each in self.task_parameters:

            mode=each,
            startingTaskId=each,
            numJobs=each,
            rateOfJobGeneration=each,
            startingJobId=each,
            lowInstrBound=each,
            highInstrBound=each,
            lowMemBound=each,
            highMemBound = each

            if (mode == 'W'):
                # Note that job-task correspondence is one-to-one
                webTaskBucket = []

                for taskId in xrange (startingTaskId, startingTaskId + numJobs):
                    name = "Job%s-%s" % (0, taskId)
                    reqInstr = int (random.uniform (lowInstrBound, highInstrBound))
                    reqMem = int (random.uniform (lowMemBound, highMemBound))
                    # JobId = 0, TaskId = taskId
                    jobInTask = Job (name, reqInstr, reqMem, taskId, numJobs, 0)
                    task = Task ("Task" + str(taskId), taskId, [jobInTask])
                    webTaskBucket.append(task)
                
                self.tasklist.append (webTaskBucket)

            elif (mode == 'S'):
                # Create a set of jobs for the task
                joblist = []

                for jobId in xrange (startingJobId, startingJobId + numJobs):
                    name = "Job%s-%s" % (jobId, startingTaskId)
                    reqInstr = int (random.uniform (lowInstrBound, highInstrBound))
                    reqMem = int (random.uniform (lowMemBound, highMemBound))
                    joblist.append (Job (name, reqInstr, reqMem, startingTaskId, numJobs, jobId))
             
                task = Task ("Task" + str(startingTaskId), startingTaskId, joblist)
                self.tasklist.append ([task])

    def getNJobsFromBucket (self, i, rateOfJobGeneration, N, jobsToBeAdded):
        '''
        Gets N jobs from the current Task Bucket.
        1) If there are at least rateOfJobGeneration number of jobs within the current
           task, then return a list of that many jobs.
        2) Else, extract as many jobs as possible from the current task, and extract the
           remainder number of jobs from the next task (recursion used).
        '''
        if N == 0:
            return []
        try:
                ''''#for k in range (rateOfJobGeneration):
                #jobsToBeAdded.append (self.tasklist[i][0].joblist.pop(0))'''
        except IndexError: # Not enough jobs in the current task
            try:
                self.tasklist[i].pop(0) # Move to next task
                jobsToBeAdded + self.getNJobsFromBucket(i, rateOfJobGeneration, rateOfJobGeneration - len(jobsToBeAdded), jobsToBeAdded)
            except IndexError: # Exhausted all tasks in the bucket. Move on.
                return jobsToBeAdded

        return jobsToBeAdded

    def run(self, finish):

        # Populate the task list
        self.generate_tasks()
         
        #activate (self.scenario.scheduler, self.scenario.scheduler.run())
        self.tasklist=[3,4,5,6]

        times = len (self.tasklist)

        # For each task bucket
        for i in range(len(self.task_parameters)):

            mode=self.task_parameters[i],
            startingTaskId=self.task_parameters[i],
            numJobs=self.task_parameters[i],
            rateOfJobGeneration=self.task_parameters[i],
            startingJobId=self.task_parameters[i],
            lowInstrBound=self.task_parameters[i],
            highInstrBound=self.task_parameters[i],
            lowMemBound=self.task_parameters[i],
            highMemBound = self.task_parameters[i]

            times = len(self.tasklist)
            # For each task in a task bucket
            for x in range(times):

                while (numJobs):

                    jobsToBeAdded = self.getNJobsFromBucket (i, rateOfJobGeneration, rateOfJobGeneration, [])

                    for each in jobsToBeAdded:
                        self.scenario.scheduler.addJob(each)
                        numJobs -= 1

                    yield hold, self, 1
                    #print "Current time: " + str(now())

            self.scenario.remainingTasks -= 1
