import datetime as dt
import uuid
import json


def save_file(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file)

def add_note():
    title = input("Введите заголовок заметки:  ")
    description = input("Введите описание заметки:  ")
    id = str(uuid.uuid4())
    datetime = dt.datetime.now().strftime("%d-%m-%Y в %H:%M:%S")

    note = {"id": id,
            "title": title,
            "description": description,
            "datetime": datetime,
            "edit": datetime
            }

    notes.append(note)
    save_file(notes)
    print(f"Заметка {note['id']} успешно добавлена ")

def load_notes():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def show_all_notes(notes):
    if len(notes) != 0:
        notes.sort(key = lambda x: x['datetime'])
        print("Список всех заметок")
        for note in notes:
            print("/-------------------------------------/")
            print(f"ID - {note['id']}")
            print(f"TITLE - {note['title']}")
            print(f"DESCRIPTION - {note['description']}")
            print(f"DATE AND TIME - {note['datetime']}")
            print(f"LAST EDIT - {note['edit']}")
            print("/-------------------------------------/")
    else:
        print("Пока список заметок пуст :(")

def edit_note():
    show_all_notes(notes)
    note_id = input("Введите ID заметки для редактирования: ")
    if len(notes) != 0:
        for note in notes:
            flag = True
            if note["id"] == note_id:
                new_title = input('Введите новый заголовок ')
                new_description = input('Введите новое описание ')
                datetime = dt.datetime.now().strftime("%Y-%m-%d в %H:%M:%S")
                note["title"] = new_title
                note["description"] = new_description
                note["edit"] = datetime
                save_file(notes)
                print("Заметка успешно отредактирована")
                flag = False
        if flag:
            print("Заметка с таким ID была не найдена :(")
    else:
        print("Заметок еще нет. Нечего искать")

def delete_note():
    if len(notes) != 0:
        show_all_notes(notes)
        delete_id = input("Введите ID заметки для удаления")
        flag = True
        for note in notes:
            if note['id'] == delete_id:
                notes.remove(note)
                print("Заметка успешно удалена")
                flag = False
                save_file(notes)
        if flag:
            print("Заметка с таким ID была не найдена :(")
    else:
        print("Заметок еще нет. Нечего искать")

def filter_notes_date():
    date = input("За какую дату вывести заметки? (format: дд-мм-гггг)")
    day = date.split("-")[0]
    mon = date.split("-")[1]
    ye = date.split("-")[-1]
    ye_now = int(dt.datetime.now().strftime("%Y-%m-%d").split("-")[0])
    if (31 >= int(day) >= 1) and (12 >= int(mon) >= 1) and (ye_now >= int(ye) >= 1):
        filt_notes = list(filter(lambda x: x['datetime'].split(" ")[0] == date, notes))
        if len(filt_notes) != 0:
            show_all_notes(filt_notes)
        else:
            print("Заметок с такой датой не найдено")
    else:
        print("Неверный формат даты")

def filter_notes_tag():
    if len(notes) != 0:
        tag = input("Введите ключевое слово, по которому будем искать. ")
        fil_notes = list(filter(lambda x : (tag in x['description']) or (tag in x['title']) , notes))
        if fil_notes:
            show_all_notes(fil_notes)
        else:
            print(f"По данному слову({tag}) ничего не найдено")

def delete_all_notes():
    for note in notes:
        notes.remove(note)
        save_file(notes)
    print("Заметки очищены")


notes = load_notes()


programm = True

while programm:
    print("Введите 1 чтобы Вывести список заметок")
    print("Введите 2 чтобы Добавить заметку")
    print("Введите 3 чтобы Редактировать заметку")
    print("Введите 4 чтобы Удалить заметку")
    print("Введите 5 чтобы Удалить все заметки")
    print("Введите 6 чтобы Выбрать заметки по дате")
    print("Введите 7 чтобы Выбрать заметки по тегу")
    print("Введите 0 чтобы Выйти")

    choice = input("Введите команду ")

    match choice:
        case '1':
            show_all_notes(notes)
        case '2':
            add_note()
        case '3':
            edit_note()
        case '4':
            delete_note()
        case '5':
            delete_all_notes()
        case '6':
            filter_notes_date()
        case '7':
            filter_notes_tag()
        case '0':
            print("Завершение работы ")
            programm = False
        case _:
            print("Не могу найти команду. Попробуйте еще.")