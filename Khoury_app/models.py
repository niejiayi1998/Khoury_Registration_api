from django.db import models


# Term Model
class Term(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'term'
        verbose_name_plural = "terms"

    def __str__(self):
        return self.title


# Department Model
class Department(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'department'
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name


# Student Model
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    GPA = models.FloatField(max_length=5, default=4.0)

    class Meta:
        db_table = 'student'
        verbose_name_plural = "Students"

    def __str__(self):
        return self.full_name


# Advisor Model
class Advisor(models.Model):
    full_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   null=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    @property
    def department_name(self):
        return self.department.name

    class Meta:
        db_table = 'advisor'
        verbose_name_plural = "Advisors"

    def __str__(self):
        return self.full_name


class Admin(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'admin'
        verbose_name_plural = "Admins"

    def __str__(self):
        return self.full_name


# Course Model
class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    credit = models.IntegerField()

    @property
    def department_name(self):
        return self.department.name

    class Meta:
        db_table = 'course'
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name


# Section Model
class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=1)
    instructor = models.CharField(max_length=150)
    classSize = models.IntegerField()
    location = models.CharField(max_length=50, null=True)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)

    class Meta:
        db_table = 'section'
        verbose_name_plural = "Sections"

    @property
    def course_name(self):
        return self.course.name

    @property
    def term_name(self):
        return self.term.title

    def total_enrolled_students(self):
        total_enrolled_students = History.objects.filter(
            section=self).count()
        return total_enrolled_students

    def __str__(self):
        return f"{self.course}-{self.name}-{self.term}"


# Ticket Status
class TicketStatus(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        db_table = 'ticket_status'
        verbose_name_plural = "Ticket Status"

    def __str__(self):
        return self.title


# Ticket Model
class Ticket(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    request = models.CharField(max_length=20, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(TicketStatus, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ticket'
        verbose_name_plural = "Tickets"

    # @property
    # def student_id(self):
    #     return self.student.id

    @property
    def student_name(self):
        return self.student.full_name

    @property
    def section_name(self):
        return self.section.name

    @property
    def course_name(self):
        return self.section.course.name

    def __str__(self):
        return f"{self.student}-{self.request}-{self.section}-{self.status}"


# Status
class HistoryStatus(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        db_table = 'history_status'
        verbose_name_plural = "History Status"

    def __str__(self):
        return self.title


# History Model
class History(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    status = models.ForeignKey(HistoryStatus, on_delete=models.CASCADE)

    class Meta:
        db_table = 'history'
        verbose_name_plural = "Histories"

    @property
    def course(self):
        return self.section.course.name

    @property
    def instructor(self):
        return self.section.instructor

    @property
    def section_name(self):
        return self.section.name

    def __str__(self):
        return f"{self.student}-{self.section}-{self.status}"


# Message Model
class Message(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    send_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        db_table = 'message'
        verbose_name_plural = "Messages"

    @property
    def advisor_name(self):
        return self.advisor.full_name

    def __str__(self):
        return f"{self.student}-{self.advisor}-{self.send_time}"
