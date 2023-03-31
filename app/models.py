from app import db


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, unique=True)
    email = db.Column(db.String(20), index=True, unique=True)
    passwd = db.Column(db.String(20))

    def __repr__(self):
        return f'Пользователь {self.name}'


class Subjects(db.Model):
    subject_id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(30), index=True, unique=True)
    subject_name_eng = db.Column(db.String(30), index=True, unique=True)
    subj_min = db.Column(db.Integer)
    subj_max = db.Column(db.Integer)
    subj_value = db.Column(db.Integer)
    subj_general = db.Column(db.Boolean, default=True) # по умолчанию обязательный
    subj_10 = db.Column(db.Boolean, default=True)#по умолчанию для 10 класса

    def __repr__(self):
        return f'Предмет {self.subject_name}'


class Grades(db.Model):
    grade_id = db.Column(db.Integer, primary_key=True)
    grade_name = db.Column(db.String(3), index=True, unique=True)

    def __repr__(self):
        return f'Класс {self.subject_name}'


class Curriculum(db.Model):
    lesson_id = db.Column(db.Integer, primary_key=True)
    les_subject = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'))
    les_grade = db.Column(db.Integer, db.ForeignKey('grades.grade_id'))
    les_number = db.Column(db.Integer)
    les_day = db.Column(db.Integer)

    def __repr__(self):
        return f'Урок {self.subject_name}'

class EnglishTeachers(db.Model):
    teacher_id = db.Column(db.Integer, primary_key=True)
    teacher_name = db.Column(db.String(30), index=True, unique=True)

    def __repr__(self):
        return f'{self.teacher_name}'


class SecondLangTeachers(db.Model):
    teacher_id = db.Column(db.Integer, primary_key=True)
    teacher_name = db.Column(db.String(30), index=True, unique=True)

    def __repr__(self):
        return f'{self.teacher_name}'


class EnglishGroups(db.Model):
    group_id = db.Column(db.Integer, primary_key=True)
    group_grade = db.Column(db.Integer, db.ForeignKey('grades.grade_id'))
    group_teacher = db.Column(db.Integer, db.ForeignKey('english_teachers.teacher_id'))
    group_name = db.Column(db.String(10), index=True)
    group_level = db.Column(db.String(3), index=True)

    def __repr__(self):
        return f'Группа {self.group_name}'


class SecondLangGroups(db.Model):
    group_id = db.Column(db.Integer, primary_key=True)
    group_lang = db.Column(db.Integer)  # 0 - фр, 1- исп 2-нем 3-кит
    group_grade = db.Column(db.Integer, db.ForeignKey('grades.grade_id'))
    group_teacher = db.Column(db.Integer, db.ForeignKey('second_lang_teachers.teacher_id'))
    group_name = db.Column(db.String(10), index=True)
    group_level = db.Column(db.String(3), index=True)

    def __repr__(self):
        return f'Группа {self.group_name}'

class Pupils(db.Model):
    pupil_id = db.Column(db.Integer, primary_key=True)
    pupil_name = db.Column(db.String(30), index=True, unique=True)
    grade = db.Column(db.Integer, db.ForeignKey('grades.grade_id'))
    eng_group = db.Column(db.Integer, db.ForeignKey('english_groups.group_id'))
    second_group = db.Column(db.Integer, db.ForeignKey('second_lang_groups.group_id'))

    def __repr__(self):
        return f'{self.pupil_name}'