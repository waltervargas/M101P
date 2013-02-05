import pymongo
import sys
from collections import defaultdict

def main():
    connection = pymongo.Connection("mongodb://localhost", safe=True)

    db = connection.students
    grades = db.grades

    students = defaultdict(list)
   
    for grade in grades.find({'type':'homework'}).sort('score',-1).sort('student_id',1):
        students[grade["student_id"]].append(grade["score"])

    for key in students:
        score = students[key]
        score.sort()
        
        if len(score) > 1:

            for student in grades.find({'student_id':key,"type":"homework","score":score[0]}):
                print "Remove score ", score[0], " of id ", key 
                grades.remove(student)
        

if __name__ == "__main__":
    main()
