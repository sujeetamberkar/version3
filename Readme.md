# Dashboard Django Project

## Introduction
This project, named "Dashboard", is a Django-based web application designed to facilitate student and teacher interactions. It features a main project named "dashboard" with two subordinate applications:

- `student`: Handles functionalities such as student logins, notices, course materials, and marks viewing.
- `teacher`: Manages teacher logins, notice postings, course material uploads, and marks entries.

## Test Users
### Superuser
A superuser account is available for administrative access:
- Username: `sujeet`
- Password: `admin`

### Groups and Test Users
The application has two main groups, each with test users:

#### Teachers
- Username: `test_teacher`
- Password: `teacher@1234`

#### Students
1. Raj
   - Username: `raj`
   - Password: `raj@1234`

2. Abhi
   - Username: `abhi`
   - Password: `abhi@1234`

### Prerequisites

- Git
- Python 3.6 or higher
- pip (Python package installer)


## Setup Instructions

1. Clone the repository:

```
git clone https://github.com/sujeetamberkar/version3.git

```
2. Navigate to the project directory:

```
    cd version3
```
3. Activate the virtual environment:
- a) On macOS and Linux:
```
source my_env/bin/activate
```
- b) On Windows:
```
my_env\Scripts\activate
```
4. Install the required packages:
```
pip install -r requirements.txt
```


5. Navigate to the Django project directory:
```
cd dashboard
```


6. Run database migrations:
```
python manage.py migrate
```


7. Run the development server:
```
python manage.py runserver
```


8. Open a web browser and enter the following URL to access the application:
```
http://127.0.0.1:8000/
```

## Authors

- **Sujeet Amberkar** - *Initial work* - [Sujeet Amberkar](https://github.com/sujeetamberkar)
