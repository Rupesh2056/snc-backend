from django.core.management.base import BaseCommand

from course.models import Course, Enrollment
from meta.models import MetaData
from user.models import Instructor, Student
import random
from django.contrib.auth import get_user_model

User = get_user_model()


def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='admin'
        )
        print("superuser created with username: admin and password: admin")

def create_metadatas():
    meta_datas = {
        "shift" : ["Morning","Day","Evening","Night"],
        "gender" : ["Male","Female","Other"],
        "credit" : ["25hr","45 hr","90hr"],
        "mode" : ["online","Offline","Hybrid"],
        }

    for key,values in meta_datas.items():
        for value in values:
            MetaData.objects.get_or_create(key=key,value=value)
     

def create_course():
    credit_metas = list(MetaData.objects.filter(key="credit"))
    for i in range(10):
        course_title = f"Course {i}"
        course_code = f"C-{i}"
        obj,created = Course.objects.get_or_create(title=course_title,code=course_code)
        obj.meta_data.add(random.choice(credit_metas))


def create_students_instructors():
    shift_metas = list(MetaData.objects.filter(key="shift"))
    gender_metas = list(MetaData.objects.filter(key="gender"))

    for i in range(10):
            full_name = f"Student {i}"
            email = f"Student{i}@student.com"
            instructor_full_name = f"Instructor {i}"
            instructor_email = f"instructor{i}@instructor.com"

            student,student_created = Student.objects.get_or_create(full_name=full_name,email=email)
            instructor,instructor_created = Instructor.objects.get_or_create(full_name=instructor_full_name,email=instructor_email)

            student.meta_data.set([random.choice(shift_metas),random.choice(gender_metas)])
            instructor.meta_data.set([random.choice(shift_metas),random.choice(gender_metas)])




def create_enrollments():
    enrollment_metas = list(MetaData.objects.filter(key="mode"))
    for i in range(10):
        student_id = random.choice(range(1,11))
        course_id = random.choice(range(1,11))
        enrollment,created = Enrollment.objects.get_or_create(student_id=student_id,course_id=course_id)

        enrollment.meta_data.add(random.choice(enrollment_metas))

class Command(BaseCommand):
    """
    Assigns UserPoint with its respectiver customer.
    python manage.py assign_customer
    """
    help = "Assigns UserPoint with its respectiver customer."

    

    def handle(self, **options):
        create_superuser()
        create_metadatas()
        create_course()
        create_students_instructors()
        create_enrollments()

        print("All datas created.")
        
        

            

        
