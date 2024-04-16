subject_to_teachers = {}
with open('nameToSubject.txt', 'r') as file:
    for line in file:
        teacher, subjects = line.strip().split(':')
        teacher = teacher.replace(' ', '')
        subjects = subjects.replace(' ', '')
        for subject in subjects.split(','):
            if subject not in subject_to_teachers:
                subject_to_teachers[subject] = [teacher]
            else:
                subject_to_teachers[subject].append(teacher)
with open('subjectToName.txt', 'w') as file:
    for subject, teachers in subject_to_teachers.items():
        if subject.strip() == '': continue
        print(f"{subject.strip()}: {', '.join(teachers)}")
        file.write(f"{subject.strip()}: {', '.join(teachers)}\n")