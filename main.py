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

class Student:
    def __init__(self, full_name, note1, note2, note3):
        self.full_name = full_name
        self.notes = [note1, note2, note3]



class App:

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
    def get_mention(number):
        if medium < 10:
            return 'Insuffisant'
        elif medium >= 10 and note < 12:
            return 'Passable'
        elif medium >= 12 and note < 16:
            return 'Bien'
        elif medium >= 16 and note <= 20:
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
    def dec_sort(resultats_dict):
        