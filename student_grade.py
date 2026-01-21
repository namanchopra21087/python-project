if __name__ == '__main__':
    stud_grade={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stud_grade[name]=score

    stud_score=sorted(set(stud_grade.values()),reverse=True)
    second_lowest_score=stud_score[len(stud_score)-2]

    name=[]
    for n in stud_grade.keys():
        if stud_grade[n]==second_lowest_score:
            name.append(n)
    for name in sorted(name):
        print(name)
