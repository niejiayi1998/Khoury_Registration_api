from rest_framework import serializers
from . import models


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Grade
        fields = ['id', 'title']


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Term
        fields = ['id', 'title']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'full_name', 'email', 'password', 'grade', 'GPA']
        depth = 1


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Advisor
        fields = ['id', 'full_name', 'email', 'password']


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
        fields = ['id', 'department', 'name', 'credit']
        depth = 1


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Section
        fields = ['id', 'course', 'name', 'instructor', 'classSize', 'term']
        depth = 1


class TicketStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TicketStatus
        fields = ['id', 'title']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = ['id', 'student', 'section', 'created_time', 'status']
        depth = 1


class HistoryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HistoryStatus
        fields = ['id', 'title']


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.History
        fields = ['id', 'student', 'section', 'status']
        depth = 1


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = ['id', 'student', 'advisor', 'send_time', 'content']
        depth = 1