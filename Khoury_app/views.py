from django.shortcuts import render
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from . import serializers
from . import models

# Create your views here.
from .serializers import SectionSerializer


class TermList(generics.ListCreateAPIView):
    queryset = models.Term.objects.all()
    serializer_class = serializers.TermSerializer


class StudentList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


@csrf_exempt
def student_login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        studentData = models.Student.objects.get(email=email,
                                                 password=password)
    except models.Student.DoesNotExist:
        studentData = None

    if studentData:
        return JsonResponse({'bool': True, 'student_id': studentData.id})
    else:
        return JsonResponse({'bool': False})


class AdvisorList(generics.ListCreateAPIView):
    queryset = models.Advisor.objects.all()
    serializer_class = serializers.AdvisorSerializer


class AdvisorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Advisor.objects.all()
    serializer_class = serializers.AdvisorSerializer


@csrf_exempt
def advisor_login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        advisorData = models.Advisor.objects.get(email=email,
                                                 password=password)
    except models.Advisor.DoesNotExist:
        advisorData = None

    if advisorData:
        return JsonResponse({'bool': True, 'advisor_id': advisorData.id})
    else:
        return JsonResponse({'bool': False})


class AdminList(generics.ListCreateAPIView):
    queryset = models.Admin.objects.all()
    serializer_class = serializers.AdminSerializer


class AdminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Admin.objects.all()
    serializer_class = serializers.AdminSerializer


@csrf_exempt
def admin_login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        adminData = models.Admin.objects.get(email=email, password=password)
    except models.Admin.DoesNotExist:
        adminData = None

    if adminData:
        return JsonResponse({'bool': True, 'admin_id': adminData.id})
    else:
        return JsonResponse({'bool': False})


class DepartmentList(generics.ListCreateAPIView):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseDetailSerializer


class SectionList(generics.ListCreateAPIView):
    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer


class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionDetailSerializer


class TicketStatusList(generics.ListCreateAPIView):
    queryset = models.TicketStatus.objects.all()
    serializer_class = serializers.TicketStatusSerializer


class TicketList(generics.ListCreateAPIView):
    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketSerializer


class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketDetailSerializer


class PendingTicketList(generics.ListAPIView):
    serializer_class = serializers.TicketSerializer

    def get_queryset(self):
        return models.Ticket.objects.filter(status=2)


class HistoryStatusList(generics.ListCreateAPIView):
    queryset = models.HistoryStatus.objects.all()
    serializer_class = serializers.HistoryStatusSerializer


class HistoryList(generics.ListCreateAPIView):
    queryset = models.History.objects.all()
    serializer_class = serializers.HistorySerializer


class HistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.History.objects.all()
    serializer_class = serializers.HistoryDetailSerializer


class MessageList(generics.ListCreateAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageDetailSerializer


class MessageToStudent(generics.ListAPIView):
    serializer_class = serializers.MessageSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        student = models.Student.objects.get(pk=student_id)
        return models.Message.objects.filter(student=student).order_by(
            '-send_time')


# Specific Course Chapter List
class CourseSectionList(generics.ListCreateAPIView):
    serializer_class = serializers.SectionSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        course = models.Course.objects.get(pk=course_id)
        return models.Section.objects.filter(course=course)


# fetch student section enroll status
# @csrf_exempt
# def fetch_enroll_status(request, student_id, course_id):
#     student = models.Student.objects.filter(id=student_id).first()
#     course = models.Course.objects.filter(id=course_id).first()
#     enrollStatus = models.History.objects.filter(course=course,
#                                                  student=student)
#
#     if enrollStatus:
#         return JsonResponse({'bool': True})
#     else:
#         return JsonResponse({'bool': False})


@csrf_exempt
def find_historyId(request, student_id, section_id):
    student = models.Student.objects.filter(id=student_id).first()
    section = models.Section.objects.filter(id=section_id).first()
    status = models.HistoryStatus.objects.filter(id=2).first()
    historyId = models.History.objects.filter(student=student,
                                              section=section,
                                              status=status).first().id
    return JsonResponse({'historyId': historyId})


# find student dashboard myCourse (current registered course)
class MyCourseList(generics.ListAPIView):
    serializer_class = serializers.HistorySerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        student = models.Student.objects.get(pk=student_id)
        status = models.HistoryStatus.objects.get(pk=2)
        return models.History.objects.filter(student=student, status=status)
