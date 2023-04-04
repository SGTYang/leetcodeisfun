class Solution(object):
    def partitionString(self, s):
        start_id = end_id = partition_count = 0
        while end_id < len(s):
            if s[end_id] in s[start_id:end_id]:
                partition_count += 1
                start_id = end_id 
            end_id += 1
        if s[end_id-1] in s[start_id:end_id]:
            partition_count += 1
        return partition_count