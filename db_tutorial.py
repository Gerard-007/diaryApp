from peewee import *


db = SqliteDatabase("students.db")

class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)
    
    class Meta:
        database = db

#user inputs stores as dictionary...
students = [
	{'username': 'Gerard',
	 'points': 2000},
	{'username': 'Blessing',
	 'points': 1200},
	{'username': 'StefNora',
	 'points': 3000},
	{'username': 'Luke',
	 'points': 2300}
]


def add_students():
    for student in students:
        try:
            Student.create(username = student['username'],
                points = student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()
        
def top_student():
    #Select all student record, order them by highest point, get only the 1st record
    student = Student.select().order_by(Student.points.desc()).get()
    return student.username
	

#This block runs the program logics
if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    
    print("The top student now is: {}".format(top_student()))