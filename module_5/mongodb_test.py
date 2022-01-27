use('pytech')
db.students.insertOne({											
'student_id' : '246810',           								
'first_name' : 'Rebecca',								
'last_name' : 'Walters',											
'enrollments':    [
		    {
		'term' : 'fall 2020',
		'gpa' : '3.256',
		'start_date' : 'August 24, 2020',
		'end_date' : 'December 18, 2020',
		'courses' : 	[
				{
					'course_id' : 'BIO 100',
					'description' : 'Biology I',
					'instructor' : 'Savanna Parker',
					'grade' : 'A'
				},
				{
					'course_id' : 'ENG 243',
					'description' : 'British Literature I',
					'instructor' : 'Daniel Davenport',
					'grade' : 'A'
				}]

	},
	{
		'term' : 'spring 2021',
		'gpa' : '3.589',
		'start_date' : 'January 3, 2021',
		'end_date' : 'May 24, 2021',
		'courses' : 	[
				{
					'course_id' : 'BIO 101',
					'description' : 'Biology II',
					'instructor' : 'Savanna Parker',
					'grade' : 'A'
				},
				{
					'course_id' : 'ENG 244I',
					'description' : 'British Literature II',
					'instructor' : 'Heather Moore',
					'grade' : 'A'
				}]

	},
	{
		'term' : 'fall 2021',
		'gpa' : '3.499',
		'start_date' : 'August 8, 2021',
		'end_date' : 'December 14, 2021',
		'courses' : 	[
				{
					'course_id' : 'PYS 400',
					'description' : 'Introduction to Psychology',
					'instructor' : 'Evan Williams',
					'grade' : 'A'
				},
				{
					'course_id' : 'MTH 100',
					'description' : 'Calculus I',
					'instructor' : 'Jonathan Conley',
					'grade' : 'B'
				}]
	},
	{
		'term' : 'spring 2022',
		'gpa' : '3.545',
		'start_date' : 'January 7, 2022',
		'end_date' : 'May 22, 2022',
		'courses' : 	[
				{
					'course_id' : 'CHM 200',
					'description' : 'Chemistry I',
					'instructor' : 'George Bragg',
					'grade' : 'C'
				},
				{
					'course_id' : 'ART 100',
					'description' : 'Introduction to Art',
					'instructor' : 'Kristen Smith',
					'grade' : 'A'
				}]



	}]
}
										

)