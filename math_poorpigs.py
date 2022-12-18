class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        timeslot=(minutesToTest/minutesToDie)
        result=ceil(log(buckets,timeslot+1))
        return int(result)
        