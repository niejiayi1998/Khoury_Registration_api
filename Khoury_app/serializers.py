from rest_framework import serializers
from . import models


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Term
        fields = ['id', 'title']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'full_name', 'email', 'password', 'GPA']


class AdvisorSerializer(serializers.ModelSerializer):
    department_name = serializers.ReadOnlyField()

    class Meta:
        model = models.Advisor
        fields = ['id', 'department', 'full_name', 'email', 'password', 'department_name']


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Admin
        fields = ['id', 'full_name', 'email', 'password']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ['id', 'name']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'department', 'title', 'name', 'description', 'credit']


class CourseDetailSerializer(serializers.ModelSerializer):
    department_name = serializers.ReadOnlyField()

    class Meta:
        model = models.Course
        fields = ['id', 'department', 'title', 'name', 'description',
                  'credit', 'department_name']


class SectionSerializer(serializers.ModelSerializer):
    total_enrolled_students = serializers.ReadOnlyField()

    class Meta:
        model = models.Section
        fields = ['id', 'course', 'name', 'instructor', 'classSize',
                  'location', 'term', 'total_enrolled_students']


class SectionDetailSerializer(serializers.ModelSerializer):
    course_name = serializers.ReadOnlyField()
    term_name = serializers.ReadOnlyField()
    class Meta:
        model = models.Section
        fields = ['id', 'course', 'name', 'instructor', 'classSize', 'location',
                  'term', 'course_name', 'term_name']


class TicketStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TicketStatus
        fields = ['id', 'title']


class TicketSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField()
    section_name = serializers.ReadOnlyField()
    course_name = serializers.ReadOnlyField()

    class Meta:
        model = models.Ticket
        fields = ['id', 'student', 'section', 'request', 'created_time',
                  'status', 'student_name', 'section_name',
                  'course_name']


class TicketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = ['id', 'student', 'section', 'request', 'created_time',
                  'status']


class HistoryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HistoryStatus
        fields = ['id', 'title']


class HistorySerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField()
    instructor = serializers.ReadOnlyField()
    section_name = serializers.ReadOnlyField()

    class Meta:
        model = models.History
        fields = ['id', 'student', 'section', 'status', 'course', 'instructor'
                  , 'section_name']



class HistoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.History
        fields = ['id', 'student', 'section', 'status']
        depth = 1


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = ['id', 'student', 'advisor', 'send_time', 'content', 'advisor_name']


class MessageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = ['id', 'student', 'advisor', 'send_time', 'content']
        depth = 1
