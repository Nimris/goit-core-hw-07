from main2 import AddressBook, Record
from main3 import get_upcoming_birthdays
from time import strftime

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone/birthday in correct formats."
        except IndexError:
            return "Enter the arguments for the command."
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return str(e)
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lower().strip()
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book):
    name, new_number = args
    book[name] = new_number
    return "Contact updated"

@input_error
def show_phone(args, book):
    name = args[0]
    return book[name]
   
@input_error 
def show_all(args, book):
    if book:
        return "\n".join(f"{phone}" for name, phone in book.items())
    return "No contacts are available."

@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.add_birthday(birthday)
    return "Birthday added."
     
@input_error
def show_birthday(args, book):
    name = args[0]
    return book.birthday
    record = book.find(name)
    if record and record.birthday:
        return record.birthday.strftime('%d.%m.%Y')
    return "Birthday not found."
    
@input_error
def birthdays(args, book):
    return get_upcoming_birthdays(book)

    
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)
        
        match command:
            case 'exit' | 'close':
                print('Good bye!')
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, book))
            case "change": 
                print(change_contact(args, book))
            case "phone": 
                print(show_phone(args, book))
            case "all":
                print(show_all(args, book))
            case "add-birthday":
                print(add_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "birthdays":
                print(birthdays(args, book))
            case _:
                print("Invalid command")
    
if __name__ == "__main__":
    main()