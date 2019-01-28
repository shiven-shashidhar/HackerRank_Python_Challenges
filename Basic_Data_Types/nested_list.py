if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    #find the 2nd lowest score
    students.sort(key=lambda student: student[1])

    for i in range(1, len(students)):
        if students[i][1]!=students[0][1]:
            second_lowest_score = students[i][1]
            break;

    second_lowest_names = [i[0] for i in students if i[1]==second_lowest_score]

    for i in sorted(second_lowest_names):
        print(i)








