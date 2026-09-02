class Student:
    def __init__(self, full_name, note1, note2, note3):
        self.full_name = full_name
        self.notes = [note1, note2, note3]

class App:
    def __init__(self):
        self.students = {}
        chose = 0
        while chose != 3:
            print('1. Ajouter etudiant')
            print('2. Afficher classement')
            print('3. Quitter')
            try:
                chose = int(input('\n\t[+] Enter Your Chose: '))
            except ValueError:
                print('[-] Please Enter A Number -_-')
            match chose:
                case 1:
                    student_name = str(input('[+] Enter Student Name: '))
                    student_notes = []
                    student_notes_sum = 0
                    while len(student_notes) < 3:
                        try:
                            data = float(input(f'[+] Enter {student_name} Note {len(student_notes) + 1}: '))
                            if data <= 20 and data >= 0:
                                student_notes.append(data)
                                student_notes_sum += data
                            else:
                                print('[-] Please Enter A Value Between 0 and 20')
                        except ValueError:
                            print('[-] Please Enter An Number Between 0 and 20')
                    medium = float(student_notes_sum / 3)
                    print(f'[+] The Medium Of {student_name} Is: {medium:.2f}')
                    mention = App.get_mention(medium)
                    self.students[student_name] = {
                        'moyenne': medium,
                        'notes': student_notes,
                        'mention': mention
                    }
                case 2:
                    App.dec_sort(list(self.students.items()))
        print('Au Revoir !')
                    

    @staticmethod
    def calculate_medium(notes):
        sum = 0
        for note in notes:
            sum += note
        return float(sum / 3)


    @staticmethod
    def appreciation(students):
        for student in students:
            medium = App.calculate_medium(student['notes'])
            print(f'[+] {student['nom']} {medium:.2f} {get_mention(medium)}')


    @staticmethod
    def get_mention(medium):
        if medium < 10:
            return 'Insuffisant'
        elif medium >= 10 and medium < 12:
            return 'Passable'
        elif medium >= 12 and medium < 16:
            return 'Bien'
        elif medium >= 16 and medium <= 20:
            return 'Tres bien'
        return ''

    @staticmethod
    def get_resultats_dict(students):
        output_dict = {}
        for student in students:
            medium = App.calculate_medium(student['notes'])
            output_dict[student['nom']] = {
                'moyenne': medium,
                'mention': App.get_mention(medium)
            }

    @staticmethod
    def dec_sort(students_tuples_list):
        for _ in students_tuples_list:
            for id in range(0, len(students_tuples_list) - 1):
                tmp = students_tuples_list[id]
                if students_tuples_list[id + 1][1]['moyenne'] > tmp[1]['moyenne']:
                    students_tuples_list[id] = students_tuples_list[id + 1]
                    students_tuples_list[id + 1] = tmp
        for id, student in enumerate(students_tuples_list):
            print(f'{id + 1}. {student[0]} - {student[1]['moyenne']:.2f}')

    
    @staticmethod
    def get_echec_students(resultats_dict):
        echec_students = []
        for student_name in resultats_dict:
            if resultats_dict[student_name]['moyenne'] < 10:
                echec_students.append((student_name, resultats_dict[student_name]['moyenne']))
        print(echec_students)

app = App()