# Campus Progress Tracker

A Java Spring Boot web application for tracking academic progress in educational institutions with role-based dashboards for School Admin, Faculty, Students, and Parents.

## Features

### Role-Based Login System
- **School/Admin**: Overall school-wide analytics and monitoring
- **Faculty**: Daily syllabus logging, student feedback tracking, parent remarks
- **Student**: Confidence feedback submission, progress tracking, revision requests
- **Parent**: Child's progress monitoring, faculty remarks, revision suggestions

### Dashboards
#### School Dashboard
- Overall syllabus completion percentage
- Student confidence distribution (High/Medium/Low)
- Subjects needing attention alerts
- Recent syllabus updates
- Interactive charts using Chart.js

#### Faculty Dashboard
- Add daily syllabus logs with completion percentage
- View student confidence feedback
- Identify weak topics
- Add remarks for parents
- Track personal teaching progress

#### Student Dashboard
- Submit confidence feedback for topics
- Request revision for difficult topics
- View personal confidence history
- Track syllabus progress by subject
- Visual progress indicators

#### Parent Dashboard
- Search and view child's progress
- Subject-wise confidence levels
- Syllabus completion status
- Faculty remarks
- Weak subjects identification
- Revision suggestions

## Technology Stack

- **Backend**: Spring Boot 3.2.0, Java 17
- **Database**: H2 (in-memory)
- **Security**: Spring Security with BCrypt password encoding
- **Frontend**: Thymeleaf templates, HTML5, CSS3
- **Charts**: Chart.js for data visualization
- **Build Tool**: Maven

## Project Structure

```
campus-progress-tracker/
├── src/
│   ├── main/
│   │   ├── java/com/campus/tracker/
│   │   │   ├── CampusProgressTrackerApplication.java
│   │   │   ├── config/
│   │   │   │   ├── SecurityConfig.java
│   │   │   │   └── DataInitializer.java
│   │   │   ├── controller/
│   │   │   │   ├── MainController.java
│   │   │   │   ├── SchoolController.java
│   │   │   │   ├── FacultyController.java
│   │   │   │   ├── StudentController.java
│   │   │   │   └── ParentController.java
│   │   │   ├── entity/
│   │   │   │   ├── User.java
│   │   │   │   ├── Role.java
│   │   │   │   ├── SyllabusLog.java
│   │   │   │   ├── StudentConfidence.java
│   │   │   │   ├── ConfidenceLevel.java
│   │   │   │   └── ParentRemark.java
│   │   │   ├── repository/
│   │   │   │   ├── UserRepository.java
│   │   │   │   ├── SyllabusLogRepository.java
│   │   │   │   ├── StudentConfidenceRepository.java
│   │   │   │   └── ParentRemarkRepository.java
│   │   │   └── service/
│   │   │       ├── UserService.java
│   │   │       ├── SyllabusLogService.java
│   │   │       ├── StudentConfidenceService.java
│   │   │       ├── ParentRemarkService.java
│   │   │       └── CustomUserDetailsService.java
│   │   └── resources/
│   │       ├── application.properties
│   │       ├── templates/
│   │       │   ├── login.html
│   │       │   ├── school/dashboard.html
│   │       │   ├── faculty/dashboard.html
│   │       │   ├── student/dashboard.html
│   │       │   └── parent/dashboard.html
│   │       └── static/
│   │           └── css/
│   │               └── style.css
├── pom.xml
└── README.md
```

## Prerequisites

- Java 17 or higher
- Maven 3.6 or higher
- Modern web browser

## Installation & Setup

### 1. Install Maven (if not already installed)

**Windows:**
```bash
# Download Maven from https://maven.apache.org/download.cgi
# Extract to a directory (e.g., C:\Program Files\Apache\maven)
# Add to PATH: System Environment Variables
# MAVEN_HOME = C:\Program Files\Apache\maven
# PATH = %MAVEN_HOME%\bin
```

**Verify installation:**
```bash
mvn --version
```

### 2. Build the Project

```bash
cd campus-progress-tracker
mvn clean package
```

### 3. Run the Application

```bash
mvn spring-boot:run
```

Or run the JAR file directly:
```bash
java -jar target/campus-progress-tracker-1.0.0.jar
```

### 4. Access the Application

Open your browser and navigate to:
```
http://localhost:8080
```

## Demo Credentials

The application comes with pre-loaded demo users:

| Role | Username | Password |
|------|----------|----------|
| School Admin | admin | admin123 |
| Faculty | faculty1 | faculty123 |
| Student | student1 | student123 |
| Parent | parent1 | parent123 |

## Database

The application uses H2 in-memory database. You can access the H2 console at:
```
http://localhost:8080/h2-console
```

**Connection Details:**
- JDBC URL: `jdbc:h2:mem:campusdb`
- Username: `sa`
- Password: (leave empty)

## Sample Data

On first startup, the application automatically creates:
- 6 demo users (1 admin, 2 faculty, 2 students, 1 parent)
- 4 sample syllabus logs
- 4 sample student confidence records
- 2 sample parent remarks

## Usage

### School Admin
1. Login with admin credentials
2. View overall school statistics
3. Monitor confidence distribution
4. Identify subjects needing attention
5. Review recent syllabus updates

### Faculty
1. Login with faculty credentials
2. Add daily syllabus logs
3. Track completion percentages
4. View student confidence feedback
5. Add remarks for parents

### Student
1. Login with student credentials
2. Submit confidence feedback for topics
3. Request revision if needed
4. View personal progress history
5. Track syllabus completion

### Parent
1. Login with parent credentials
2. Search for child by name
3. View subject-wise confidence
4. Check syllabus completion
5. Read faculty remarks
6. Review revision suggestions

## API Endpoints

### Authentication
- `GET /login` - Login page
- `POST /login` - Authenticate user
- `GET /logout` - Logout user

### Dashboards
- `GET /school/dashboard` - School admin dashboard
- `GET /faculty/dashboard` - Faculty dashboard
- `GET /student/dashboard` - Student dashboard
- `GET /parent/dashboard` - Parent dashboard

### Faculty Operations
- `POST /faculty/add-log` - Add syllabus log
- `POST /faculty/add-remark` - Add parent remark

### Student Operations
- `POST /student/add-feedback` - Submit confidence feedback

## Customization

### Change Port
Edit `src/main/resources/application.properties`:
```properties
server.port=8081
```

### Change Database
For production, replace H2 with MySQL/PostgreSQL:
```properties
spring.datasource.url=jdbc:mysql://localhost:3306/campusdb
spring.datasource.username=root
spring.datasource.password=yourpassword
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
```

Add MySQL dependency to `pom.xml`:
```xml
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <scope>runtime</scope>
</dependency>
```

## Security

- Passwords are encrypted using BCrypt
- Role-based access control implemented
- CSRF protection enabled
- Session management handled by Spring Security

## Development

### Add New Users
Modify `DataInitializer.java` to add more demo users.

### Add New Fields
Update entity classes and corresponding repositories, services, and controllers.

### Customize UI
Edit HTML templates in `src/main/resources/templates/` and CSS in `src/main/resources/static/css/`.

## Troubleshooting

### Port Already in Use
Change the port in `application.properties` or stop the process using port 8080.

### Maven Not Found
Ensure Maven is installed and added to system PATH.

### Database Connection Issues
Check H2 console is accessible at `/h2-console` with correct credentials.

## License

This project is created for educational purposes.

## Support

For issues or questions, please refer to the Spring Boot documentation:
https://spring.io/projects/spring-boot
