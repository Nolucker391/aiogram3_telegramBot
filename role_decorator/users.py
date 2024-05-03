import enum


class User(enum.Enum):
    student = "student"
    admin = 'admin'
    teacher = 'teacher'
    all = None

