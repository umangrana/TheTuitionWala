from django.db import models


# Create your models here
class Users(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Mobile_No = models.BigIntegerField()
    password = models.CharField(max_length=50)



class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    education = models.CharField(max_length=50)
    stream = models.CharField(max_length=50)
    studentID = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)

   # def create_unique_id():
    #    return ''.join(random.choices(string.digits, k=8))


    #def setstudentID(self,studentID):
     #   studentID= create_unique_id()

    #def getstudentID(self):
       # print("studentID:",studentID)


    def getstudentdetails(self):
         firstname = Student.firstname
         lastname = Student.lastname
         age = Student.age
         gender = Student.gender
         studentID = Student.studentID

class Faculty(models.Model):
       firstname = models.CharField(max_length=50)
       lastname = models.CharField(max_length=50)
       age = models.IntegerField
       gender = models.CharField(max_length=10)
       coursesOffered = models.CharField(max_length=250)
       facultyID = models.IntegerField(unique=True)
       email = models.URLField(unique=True)
       courseID = models.ForeignKey

     #  def create_unique_id():
      #      return ''.join(random.choices(string.digits, k=8))

       #def setfacultyID(self,facultyID):
            #facultyID= create_unique_id()

       #def getfacultyID(self):
            #print("facultyID:",facultyID)


       def getfacultydetails(self):
             firstname = Faculty.firstname
             lastname = Faculty.lastname
             age = Faculty.age
             gender = Faculty.gender
             facultyID = Faculty.facultyID

class MyStudent(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    education = models.CharField(max_length=50)
    stream = models.CharField(max_length=50)
    studentID = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)

   # def create_unique_id():
    #    return ''.join(random.choices(string.digits, k=8))


    #def setstudentID(self,studentID):
     #   studentID= create_unique_id()

    #def getstudentID(self):
       # print("studentID:",studentID)


    def getstudentdetails(self):
         firstname = Student.firstname
         lastname = Student.lastname
         age = Student.age
         gender = Student.gender
         studentID = Student.studentID


class Enrollment(models.Model):
    INSTITUTE_NAMES= (
        ('Vivekananda foundation','Vivekananda foundation'),
        ('Ragatuition', 'Ragatuition'),
        ('BRILLIANT ACADEMY', 'BRILLIANT ACADEMY'),
        ('MelhorInstitute', 'MelhorInstitute'),
        ('Prasads-Educational-Institutions', 'Prasads-Educational-Institutions'),
        ('TeachingFish', 'TeachingFish'),
        ('Srinivasa Coaching Center', 'Srinivasa Coaching Center'),
        ('Home Tuitions', 'Home Tuitions'),
        ('Prism Coaching Center', 'Prism Coaching Center'),
        ('Hemtor Tuitions', 'Hemtor Tuitions'),
    )
    SUBJECTS=(
        ('ENGLISH', 'ENGLISH'),
        ('MATHEMATICS', 'MATHEMATICS'),
        ('SOCIAL', 'SOCIAL'),
        ('PHYSICS', 'PHYSICS'),
        ('BIOLOGY', 'BIOLOGY'),
        ('COMMERCE', 'COMMERCE'),
        ('ECONOMICS', 'ECONOMICS'),
        ('CIVICS', 'CIVICS'),
        ('COMPUTER SCIENCES', 'COMPUTER SCIENCES'),
    )
    FEES = (
        ('500-1000 Per Month', '500-1000 Per Month'),
        ('1000-1500 Per Month', '1000-1500 Per Month'),
        ('1500-2000 Per Month', '1500-2000 Per Month'),
        ('Above 2000 Per Month', 'Above 2000 Per Month'),
    )
    institute_names=models.CharField(max_length=200, null=True, choices=INSTITUTE_NAMES)
    subjects=models.CharField(max_length=200, null=True, choices=SUBJECTS)
    fees=models.CharField(max_length=200, null=True, choices=FEES)
    courseID=models.CharField(max_length=200, null=True)
    Location=models.CharField(max_length=200, null=True)

class EnrollmentForm_Table(models.Model):
    Username=models.CharField(max_length=200)
    Student_Name=models.CharField(max_length=200)
    Email=models.EmailField()
    COURSEID=(
        ('CVE1','CVE1'),
        ('CVM2','CVM2'),
        ('CVS3','CVS3'),
        ('CVP4','CVP4'),
        ('CVB5','CVB5'),
        ('CVC6','CVC6'),
        ('CVCS7','CVCS7'),
        ('CRE1','CRE1'),
        ('CRM2','CRM2'),
        ('CRS3','CRS3'),
        ('CRP4','CRP4'),
        ('CRB5','CRB5'),
        ('CRSC6','CRSC6'),
        ('CBC1','CBC1'),
        ('CBE2','CBE2'),
        ('CBC3','CBC3'),
        ('CBM4','CBM4'),
        ('CBSC5','CBSC5'),
        ('CME1','CME1'),
        ('CMM2','CMM2'),
        ('CMS3','CMS3'),
        ('CMB4','CMB4'),
        ('CMC5','CMC5'),
        ('CME6','CME6'),
        ('CMCS7','CMCS7'),
        ('CPE1','CPE1'),
        ('CPC2','CPC2'),
        ('CPE3','CPE3'),
        ('CPCS4','CPCS4'),
        ('CPM5','CPM5'),
        ('CTE1','CTE'),
        ('CTM2','CTM2'),
        ('CTS3','CTS3'),
        ('CTP4','CTP4'),
        ('CTB5','CTB5'),
        ('CSE1','CSE1'),
        ('CSM2','CSM2'),
        ('CSS3','CSS3'),
        ('CSP4','CSP4'),
        ('CSB5','CSB5'),
        ('CSC6','CSC6'),
        ('CSE7','CSE7'),
        ('CSC8','CSC8'),
        ('CHE1','CHE1'),
        ('CHM2','CHM2'),
        ('CHS3','CHS3'),
        ('CHP4','CHP4'),
        ('CHB5','CHB5'),
        ('CHCS6','CHCS6'),
        ('CPRE1','CPRE1'),
        ('CPRM2','CPRM2'),
        ('CPRP3','CPRP3'),
        ('CPRB4','CPRB4'),
        ('CPRCS5','CPRCS5'),
        ('CHME1','CHME1'),
        ('CHMM2','CHMM2'),
        ('CHMP3','CHMP3'),
        ('CHMB4','CHMB4'),
        ('CHME5','CHME5'),
        ('CRE1','CRE1'),
    )
    STATUS=(
        ('Approved','Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )
    INSTITUTE_NAMES= (
        ('Vivekananda foundation','Vivekananda foundation'),
        ('Ragatuition', 'Ragatuition'),
        ('BRILLIANT ACADEMY', 'BRILLIANT ACADEMY'),
        ('MelhorInstitute', 'MelhorInstitute'),
        ('Prasads-Educational-Institutions', 'Prasads-Educational-Institutions'),
        ('TeachingFish', 'TeachingFish'),
        ('Srinivasa Coaching Center', 'Srinivasa Coaching Center'),
        ('Home Tuitions', 'Home Tuitions'),
        ('Prism Coaching Center', 'Prism Coaching Center'),
        ('Hemtor Tuitions', 'Hemtor Tuitions'),
    )
    CourseID=models.CharField(max_length=200, null=True, choices=COURSEID)
    Mobile_No=models.BigIntegerField()
    status=models.CharField(max_length=200, null=True, choices=STATUS, default='Pending')
    Institute_Name = models.CharField(max_length=200, null=True, choices=INSTITUTE_NAMES)

class Teaching_Form(models.Model):
    Entity_Name = models.CharField(max_length=200)
    ENTITIES = (
        ('FACULTY/TUTOR', 'FACULTY/TUTOR'),
        ('INSTITUTION', 'INSTITUTION')
    )
    SUBJECTS = (('ENGLISH', 'ENGLISH'),
        ('MATHEMATICS', 'MATHEMATICS'),
        ('SOCIAL', 'SOCIAL'),
        ('PHYSICS', 'PHYSICS'),
        ('BIOLOGY', 'BIOLOGY'),
        ('COMMERCE', 'COMMERCE'),
        ('ECONOMICS', 'ECONOMICS'),
        ('CIVICS', 'CIVICS'),
        ('COMPUTER SCIENCES', 'COMPUTER SCIENCES'),
    )
    FEES = (('500-1000 Per Month', '500-1000 Per Month'),
        ('1000-1500 Per Month', '1000-1500 Per Month'),
        ('1500-2000 Per Month', '1500-2000 Per Month'),
        ('Above 2000 Per Month', 'Above 2000 Per Month'),
    )
    Entity_Type = models.CharField(max_length=200, choices=ENTITIES)
    Academic_Qualification_IF_Tutor = models.CharField(max_length=300, blank=True)
    Years_Of_Establishment_IF_Institution = models.CharField(max_length=300, blank=True)
    Address=models.CharField(max_length=500)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Subject_1 = models.CharField(max_length=200, choices=SUBJECTS, null=True)
    Subject_2 = models.CharField(max_length=200, choices=SUBJECTS, null=True)
    Subject_3 = models.CharField(max_length=200, choices=SUBJECTS, null=True)
    Subject_4 = models.CharField(max_length=200, choices=SUBJECTS, null=True)
    Subject_5 = models.CharField(max_length=200, choices=SUBJECTS, null=True)
    Subject_6 = models.CharField(max_length=200, choices=SUBJECTS, null=True)
    Average_Fee_Per_Subject = models.CharField(max_length=200, choices=FEES, null=True)
