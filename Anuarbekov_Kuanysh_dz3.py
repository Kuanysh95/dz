tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Александр', 'Максим', 'Николай']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def gen_of_people():
    i = 0
    j = 0
    while i != len(tutors):
        if i >= len(klasses):
            yield (tutors[i], None)
            i += 1
            j += 1
        else:
            yield (tutors[i], klasses[j])
            i += 1
            j += 1


for gen in gen_of_people():
    print(gen)