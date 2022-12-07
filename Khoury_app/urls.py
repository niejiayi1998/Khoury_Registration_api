from django.urls import path
from . import views

urlpatterns = [
    path('term/', views.TermList.as_view()),

    # user url
    path('admin/', views.AdminList.as_view()),
    path('admin/<int:pk>/', views.AdminDetail.as_view()),
    path('admin-login', views.admin_login),

    path('advisor/', views.AdvisorList.as_view()),
    path('advisor/<int:pk>/', views.AdvisorDetail.as_view()),
    path('advisor-login', views.advisor_login),

    path('student/', views.StudentList.as_view()),
    path('student/<int:pk>/', views.StudentDetail.as_view()),
    path('student-login', views.student_login),

    # course-section url
    path('department/', views.DepartmentList.as_view()),
    path('department/<int:pk>/', views.DepartmentDetail.as_view()),
    path('course/', views.CourseList.as_view()),
    path('course/<int:pk>/', views.CourseDetail.as_view()),
    path('section/', views.SectionList.as_view()),
    path('section/<int:pk>/', views.SectionDetail.as_view()),
    # Specific Course Chapters
    path("course-sections/<int:course_id>/<int:term_id>",
         views.CourseSectionList.as_view()),
    path('my-course/<int:student_id>/', views.MyCourseList.as_view()),
    path('fetch-enroll-status/<int:student_id>/<int:course_id>',
         views.fetch_enroll_status),

    # ticket url
    path('ticket-status/', views.TicketStatusList.as_view()),
    path('ticket/', views.TicketList.as_view()),
    path('ticket/<int:pk>/', views.TicketDetail.as_view()),
    path('ticket/pending/', views.PendingTicketList.as_view()),
    path('drop-ticket/<int:student_id>/<int:section_id>',
         views.find_drop_ticket),
    path('enroll-ticket/<int:student_id>/<int:course_id>',
         views.find_enroll_ticket),

    # history url
    path('history-status/', views.HistoryStatusList.as_view()),
    path('history/', views.HistoryList.as_view()),
    path('history/<int:pk>/', views.HistoryDetail.as_view()),
    path('find-historyId/<int:student_id>/<int:section_id>',
         views.find_historyId),

    # message url
    path('message/', views.MessageList.as_view()),
    path('message/<int:pk>/', views.MessageDetail.as_view()),
    path('message-to-student/<int:student_id>',
         views.MessageToStudent.as_view()),
]
