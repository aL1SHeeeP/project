import sqlite3

def data_grades():
    # создаем подключение
    con = sqlite3.connect("mydb.db")
    # получаем курсор
    cursor = con.cursor()
    grades = [str(num)+letter for num in range(5,12) for letter in 'АБВГ']
    grades = [(i, x) for i, x in enumerate(grades)]

    cursor.executemany('''
                        INSERT INTO grades
                        (grade_id, 
                        grade_name)
                        VALUES (?, ?)''', grades)

    query = con.execute("SELECT * FROM grades")
    print(query.fetchall())
    con.commit()
    con.close()


def data_1():
    # создаем подключение
    con = sqlite3.connect("mydb.db")
    # получаем курсор
    cursor = con.cursor()
    subjects = [
        (1, 'Русский язык', 'russian', 1, 2, 1, True),
        (2, 'Математика', 'math', 3, 5, 5, True),
        (3, 'Английский язык', 'english', 6, 6, 6, True),
        (4, 'Второй иностранный', 'second_language', 1, 2, 1, False),
        (5, 'Информатика', 'IT', 2, 4, 4, False),
        (6, 'Физика', 'physics', 2, 5, 5, False),
        (7, 'Биология', 'biology', 2, 5, 5, False),
        (8, 'Химия', 'chemistry', 2, 4, 4, False),
        (9, 'Литература', 'literature', 3, 3, 3, True)
    ]
    cursor.executemany('''
                        INSERT INTO subjects
                        (subject_id, 
                        subject_name, 
                        subject_name_eng, 
                        subj_min,
                        subj_max,
                        subj_value,
                        subj_general)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''', subjects)
    con.commit()
    con.close()


def langteachers():
    con = sqlite3.connect("mydb.db")
    # получаем курсор
    cursor = con.cursor()
    english_teachers = [(i, x) for i, x in enumerate([
        'Митрошина Ирина Владимировна',
        'Земскова Алина Антоновна',
        'Короёва Мария  Леонидовна',
        'Прилепский Павел Александрович',
        'Маслий Евгений Игоревич',
        'Подшиловаа Ольга Николаевна',
        'Голомысова Элла Владиславовна',
        'Савенко Мария Сергеевна',
        'Кузнецов Дмитрий Валерьевич',
        'Строилова Виктория Сергеевна'
    ])]
    cursor.executemany('''INSERT INTO english_teachers
                                (teacher_id, 
                                teacher_name)
                                VALUES (?, ?)''', english_teachers)
    con.commit()

    second_teachers = [(i, x) for i, x in enumerate([
        'Денькова Анастасия Игоревна',
        'Де Ла Крус Титуана Андрес',
        'Лысюк Василина Андреевна',
        'Козьмина Олеся Александровна',
        'Данилова Мария Александровна',
        'Крюкова Валерия Сергеевна',
        'Кузнецов Дмитрий Валерьевич',
        'Строилова Виктория Сергеевна'
    ])]
    cursor.executemany('''INSERT INTO second_lang_teachers
                            (teacher_id, 
                            teacher_name)
                            VALUES (?, ?)''', second_teachers)
    con.commit()
    con.close()


if __name__ == '__main__':
    #data_1()
    data_grades()
    pass