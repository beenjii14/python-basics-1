DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():
    # List conversion
    all_python_developers = [developer['name'] for developer in DATA if developer['language'] == 'python']
    for developer in all_python_developers:
        print(developer)

    all_plazi_devs = [developer for developer in DATA if developer['organization'] == 'Platzi']
    for developer in all_plazi_devs:
        print(developer)

    # Filter
    all_python_developers = list(filter(lambda developer: developer['language'] == 'python', DATA))
    print(all_python_developers)
    # of legal age with filter
    legal_age = list(filter(lambda developer: developer['age'] >= 18, DATA))
    adults = list(map(lambda developer: developer['name'], legal_age))
    old_people = list(map(lambda developer: developer | { 'old': developer['age'] >= 18}, DATA))
    print('old people: ', old_people)
    for developer in adults:
        print(f'of legal age: ', developer)

if __name__ == '__main__':
    main()
