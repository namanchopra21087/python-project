def count_length(lst):
    count = 0
    for i in lst:
        if len(i)>5:
            count=count+1
    return count

print("Number of users with length > 5 : {}".format(count_length(['test','testing','hgu','san','earth is round'])))