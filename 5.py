class job:
    def __init__(self,id,deadline,profit):
        self.id=id
        self.deadline=deadline
        self.profit=profit


def job_scheduling(Jobs):
    Jobs.sort(key=lambda x:x.profit,reverse=True)

    max_deadline=max(job.deadline for job in Jobs)

    slots=[-1]*max_deadline
    max_profit=0

    for job in Jobs:
        for i in range (job.deadline-1,-1,-1):
            if(slots[i]==-1):
                slots[i]=job.id
                max_profit=job.profit+max_profit
                break


    print("Jobs order:",slots)
    print("Max profit is:",max_profit)
Jobs=[
    job("J1",4,90),
    job("J2",3,180),
    job("J3",3,100),
    job("J4",2,50)    ]

job_scheduling(Jobs)
