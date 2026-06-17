from flask import Flask, render_template, jsonify

app = Flask(__name__)

# API Data
college_data = {
    "name": "ABC College of Engineering",
    "tagline": "Excellence in Engineering Education",
    "about": {
        "title": "About Our College",
        "description": "ABC College of Engineering is a premier institution dedicated to providing world-class engineering education. Established in 1995, we have been nurturing innovative minds and producing industry-ready engineers who contribute significantly to technological advancement.",
        "stats": [
            {"number": "28+", "label": "Years of Excellence"},
            {"number": "5000+", "label": "Alumni"},
            {"number": "50+", "label": "Expert Faculty"},
            {"number": "95%", "label": "Placement Rate"}
        ]
    },
    "courses": [
        {
            "name": "Computer Science Engineering",
            "duration": "4 Years",
            "description": "Learn cutting-edge technologies including AI, ML, and Cloud Computing"
        },
        {
            "name": "Electronics & Communication",
            "duration": "4 Years",
            "description": "Master the fundamentals of electronics and communication systems"
        },
        {
            "name": "Mechanical Engineering",
            "duration": "4 Years",
            "description": "Design and innovate with advanced mechanical systems"
        },
        {
            "name": "Civil Engineering",
            "duration": "4 Years",
            "description": "Build the infrastructure of tomorrow with sustainable practices"
        },
        {
            "name": "Electrical Engineering",
            "duration": "4 Years",
            "description": "Power the world with innovative electrical solutions"
        },
        {
            "name": "Information Technology",
            "duration": "4 Years",
            "description": "Specialize in software development and IT infrastructure"
        }
    ],
    "achievements": [
        {
            "title": "NAAC A+ Accreditation",
            "year": "2023",
            "description": "Recognized for excellence in education and infrastructure"
        },
        {
            "title": "Best Engineering College Award",
            "year": "2022",
            "description": "Awarded by National Education Council"
        },
        {
            "title": "100+ Research Publications",
            "year": "2023",
            "description": "Faculty and students published in international journals"
        },
        {
            "title": "Industry Partnership Awards",
            "year": "2021-2023",
            "description": "Collaborations with 50+ leading tech companies"
        }
    ],
    "contact": {
        "address": "123 Engineering Road, Tech City, State - 123456",
        "phone": "+91 98765 43210",
        "email": "admissions@abccollege.edu",
        "hours": "Mon - Sat: 9:00 AM - 5:00 PM"
    },
    "why_choose_us": {
        "title": "Why Choose Us?",
        "subtitle": "Experience the ABC College Advantage",
        "features": [
            {
                "icon": "fa-award",
                "title": "Industry-Ready Curriculum",
                "description": "Our curriculum is designed in collaboration with industry experts to ensure you're job-ready from day one."
            },
            {
                "icon": "fa-users",
                "title": "Expert Faculty",
                "description": "Learn from PhD holders and industry veterans with decades of combined experience."
            },
            {
                "icon": "fa-flask",
                "title": "State-of-the-Art Labs",
                "description": "Access cutting-edge laboratories and equipment for hands-on learning experience."
            },
            {
                "icon": "fa-globe",
                "title": "Global Exposure",
                "description": "International collaborations, exchange programs, and global internship opportunities."
            },
            {
                "icon": "fa-briefcase",
                "title": "100% Placement Assistance",
                "description": "Dedicated placement cell with tie-ups with 200+ top companies."
            },
            {
                "icon": "fa-lightbulb",
                "title": "Innovation Hub",
                "description": "Incubation center and startup support for aspiring entrepreneurs."
            }
        ]
    },
    "departments": [
        {
            "name": "Computer Science & Engineering (CSE)",
            "head": "Dr. Rajesh Kumar",
            "image": "fa-laptop-code",
            "color": "from-blue-500 to-cyan-500",
            "description": "Focus on AI, Machine Learning, Data Science, Software Engineering, and Cloud Computing with industry partnerships"
        },
        {
            "name": "Electronics & Communication (ECE)",
            "head": "Dr. Priya Sharma",
            "image": "fa-microchip",
            "color": "from-purple-500 to-pink-500",
            "description": "Specialization in VLSI Design, Embedded Systems, IoT, and Communication Technologies with modern labs"
        },
        {
            "name": "Electrical & Electronics (EEE)",
            "head": "Dr. Vikram Singh",
            "image": "fa-bolt",
            "color": "from-yellow-500 to-orange-500",
            "description": "Specialization in Power Systems, Renewable Energy, Smart Grid, and Electrical Machines with practical training"
        },
        {
            "name": "Mechanical Engineering",
            "head": "Dr. Amit Patel",
            "image": "fa-cogs",
            "color": "from-orange-500 to-red-500",
            "description": "Expertise in Robotics, CAD/CAM, Automotive Engineering, and Manufacturing with advanced workshop"
        },
        {
            "name": "Civil Engineering",
            "head": "Dr. Sunita Verma",
            "image": "fa-building",
            "color": "from-green-500 to-teal-500",
            "description": "Focus on Structural Engineering, Construction Management, Smart Cities, and Sustainable Infrastructure"
        }
    ],
    "campus_facilities": [
        {
            "name": "Digital Library",
            "icon": "fa-book-reader",
            "description": "24/7 access to 50,000+ digital resources and research papers"
        },
        {
            "name": "Sports Complex",
            "icon": "fa-futbol",
            "description": "Olympic-size swimming pool, gym, cricket ground, and indoor sports arena"
        },
        {
            "name": "Smart Classrooms",
            "icon": "fa-chalkboard-teacher",
            "description": "AI-enabled classrooms with interactive displays and VR support"
        },
        {
            "name": "Research Centers",
            "icon": "fa-microscope",
            "description": "Dedicated research labs for each department with advanced equipment"
        },
        {
            "name": "Hostel Facilities",
            "icon": "fa-bed",
            "description": "AC and non-AC hostels with Wi-Fi, mess, and recreational areas"
        },
        {
            "name": "Cafeteria",
            "icon": "fa-utensils",
            "description": "Multi-cuisine food court serving hygienic and nutritious meals"
        },
        {
            "name": "Medical Center",
            "icon": "fa-heartbeat",
            "description": "On-campus healthcare with 24/7 emergency services"
        },
        {
            "name": "Transportation",
            "icon": "fa-bus",
            "description": "Fleet of buses covering all major routes in the city"
        }
    ],
    "placement_highlights": {
        "title": "Placement Highlights",
        "subtitle": "Our Students Are Sought After by Top Companies",
        "stats": [
            {"number": "95%", "label": "Placement Rate", "color": "text-blue-600"},
            {"number": "₹24 LPA", "label": "Highest Package", "color": "text-green-600"},
            {"number": "₹8.5 LPA", "label": "Average Package", "color": "text-purple-600"},
            {"number": "200+", "label": "Recruiters", "color": "text-orange-600"}
        ],
        "top_companies": [
            "Google", "Microsoft", "Amazon", "Apple", "Meta", "Tesla",
            "Adobe", "Cisco", "IBM", "Oracle", "SAP", "Intel"
        ]
    },
    "testimonials": [
        {
            "name": "Rahul Sharma",
            "role": "Software Engineer at Google",
            "year": "Batch 2023",
            "image": "fa-user-graduate",
            "quote": "ABC College provided me with the perfect blend of theoretical knowledge and practical skills. The faculty support and placement guidance were exceptional. I landed my dream job at Google!",
            "rating": 5
        },
        {
            "name": "Priya Patel",
            "role": "Data Scientist at Microsoft",
            "year": "Batch 2022",
            "image": "fa-user-graduate",
            "quote": "The research opportunities and industry projects at ABC College gave me a competitive edge. The mentorship I received was invaluable in shaping my career.",
            "rating": 5
        },
        {
            "name": "Amit Kumar",
            "role": "Product Manager at Amazon",
            "year": "Batch 2023",
            "image": "fa-user-graduate",
            "quote": "The holistic development approach at ABC College, combining technical skills with soft skills training, prepared me for leadership roles in the corporate world.",
            "rating": 5
        }
    ],
    "announcements": [
        {
            "title": "Admissions Open 2026-27",
            "date": "April 1, 2026",
            "type": "Admission",
            "description": "Applications are now open for B.Tech and M.Tech programs for the academic year 2026-27. NAAC A+ Accredited Institution with 95% placement record. Apply before May 31st.",
            "link": "/admissions"
        },
        {
            "title": "End Semester Examination Timetable Released",
            "date": "March 25, 2026",
            "type": "Academic",
            "description": "Final examination schedule for all semesters has been released. Check your student portal for detailed timetable and exam centers.",
            "link": "#"
        },
        {
            "title": "National Level Hackathon 2026",
            "date": "April 15-17, 2026",
            "type": "Event",
            "description": "Register for our annual 24-hour hackathon with prizes worth ₹5 Lakhs. Open to all engineering students across India.",
            "link": "#"
        },
        {
            "title": "International Symposium on AI & ML",
            "date": "May 5-7, 2026",
            "type": "Event",
            "description": "Join researchers and industry experts for our international symposium on Artificial Intelligence and Machine Learning innovations.",
            "link": "#"
        },
        {
            "title": "Placement Drive 2026 - 50+ Companies",
            "date": "March 20, 2026",
            "type": "Placement",
            "description": "Campus recruitment drive begins with 50+ top companies including Google, Microsoft, Amazon, and more. 95% placement record maintained.",
            "link": "#"
        },
        {
            "title": "Graduation Day 2026",
            "date": "June 20, 2026",
            "type": "Event",
            "description": "Annual convocation ceremony for Batch 2026. Chief Guest: Dr. K. Radhakrishnan, Former ISRO Chairman.",
            "link": "#"
        }
    ]
}

@app.route('/')
def home():
    return render_template('home.html', data=college_data, page='home')

@app.route('/about')
def about():
    return render_template('about.html', data=college_data, page='about')

@app.route('/academics')
def academics():
    return render_template('academics.html', data=college_data, page='academics')

@app.route('/admissions')
def admissions():
    return render_template('admissions.html', data=college_data, page='admissions')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html', data=college_data, page='achievements')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', data=college_data, page='gallery')

@app.route('/student-updates')
def student_updates():
    return render_template('student-updates.html', data=college_data, page='student-updates')

@app.route('/contact')
def contact():
    return render_template('contact.html', data=college_data, page='contact')

@app.route('/api/college')
def api_college():
    return jsonify(college_data)

@app.route('/api/courses')
def api_courses():
    return jsonify(college_data['courses'])

@app.route('/api/achievements')
def api_achievements():
    return jsonify(college_data['achievements'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
