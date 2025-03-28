class Solution:
    def activitySelection(self, start, finish):
        n=len(start)
        activities=sorted(zip(start,finish), key=lambda x:x[1])
        activity_count=1
        last_finish_time=activities[0][1]
        for i in range(1,n):
            if activities[i][0]>last_finish_time:
                activity_count+=1
                last_finish_time=activities[i][1]
        return activity_count
