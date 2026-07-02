import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { CourseCard } from '../course-card/course-card';
import { CourseService } from '../course';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [CommonModule, FormsModule, CourseCard],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css'
})
export class CourseList implements OnInit {

  private courseService = inject(CourseService);

  courses: any[] = [];
  loading = false;
  searchTerm = '';

  ngOnInit(): void {

  this.loading = true;

  this.courses = [
    { name: 'Angular', code: 'CS101', credits: 4, grade: 'A' },
    { name: 'Java', code: 'CS102', credits: 3, grade: 'A+' },
    { name: 'Python', code: 'CS103', credits: 3, grade: 'A' },
    { name: 'React', code: 'CS104', credits: 4, grade: 'B+' },
    { name: 'Database Systems', code: 'CS105', credits: 3, grade: 'A' }
  ];

  this.loading = false;

}

  get filteredCourses() {

    return this.courses.filter(course =>
      course.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );

  }

  trackByIndex(index: number) {
    return index;
  }

}