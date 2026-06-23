from django.urls import path
from .views import CourseListView, CourseDetailView
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet,
    StudentViewSet,
    EnrollmentViewSet
)

urlpatterns = [
    path(
        'courses/',
        CourseListView.as_view(),
        name='course-list'
    ),
    path(
        'courses/<int:pk>/',
        CourseDetailView.as_view(),
        name='course-detail'
    ),
]

router = DefaultRouter()

router.register(
    'courses',
    CourseViewSet
)

router.register(
    'students',
    StudentViewSet
)

router.register(
    'enrollments',
    EnrollmentViewSet
)

urlpatterns = router.urls