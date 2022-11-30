from django.db import models


# Grade Model
class Grade(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'grade'
        verbose_name_plural = "Grades"

    def __str__(self):
        return self.title


# Student Model
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    GPA = models.FloatField(max_length=5)

    class Meta:
        db_table = 'student'
        verbose_name_plural = "Students"

    def __str__(self):
        return self.full_name


# Advisor Model
class Advisor(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

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


# Department Model
class Department(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'department'
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name


# Course Model
class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    credit = models.IntegerField()

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
    term = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        db_table = 'section'
        verbose_name_plural = "Sections"

    def __str__(self):
        return f"{self.course}-{self.name}-{self.year}-{self.term}"


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
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(TicketStatus, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ticket'
        verbose_name_plural = "Tickets"

    def __str__(self):
        return f"{self.student}-{self.section}-{self.status}"


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

    def __str__(self):
        return f"{self.student}-{self.section}-{self.status}"


# Message Model
class Message(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    send_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=500)

    class Meta:
        db_table = 'message'
        verbose_name_plural = "Messages"

    def __str__(self):
        return f"{self.student}-{self.advisor}-{self.send_time}"
