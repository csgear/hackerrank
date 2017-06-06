from collections import namedtuple

n, students = input(), namedtuple('Student', input())

avg = sum( [ float(student.MARKS) for student in students(input().split())
          for _ in range(n) ]) / n

print(avg)
