import addressbook as ab
from functools import wraps


def parse_input(command_line: str) -> tuple[str, list]:
    for command in COMMANDS:
        if command_line.lower().startswith(command):
            args = command_line.lstrip(command).strip().split(" ", 1)
            args = (s.strip() for s in args)
            return command, args
    return command_line.lower(), ()


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "Sorry, there are not enough parameters or their value may be incorrect. "\
                   "Please use the help for more information."
        except Exception as e:
            return "**** Exception other" + e
    return wrapper


@input_error
def handler_add(*args) -> str:
    user = args[0]
    phone = args[1]
    if user in user_data:
        user_data.get_record(user).add_phone(ab.Phone(phone))
    else:
        rec = ab.Record(ab.Name(user), ab.Phone(phone))
        user_data.add_record(rec)
    return "Done"


@input_error
def handler_change(*args) -> str:
    user = args[0]
    phone = args[1]
    user_data[user].change_phone(ab.Phone(phone))
    return "Done"


@input_error
def handler_phone(*args) -> str:
    user = args[0]
    return user_data[user].get_phones()


def handler_show_all(*args) -> str:
    if len(user_data.keys()):
        result = []
        for user, record in user_data.items():
            result.append(f"{user}, {record.get_phones()}")
        return "\n".join(result)
    else:
        return "No users found, maybe you want to add them first?"


def handler_hello(*args) -> str:
    return "How can I help you?"


def handler_help(*args) -> str:
    command = " ".join(args)
    if not command:
        commands = list(COMMANDS.keys())
        commands.extend(COMMAND_EXIT)
        return "List of commands: " + ", ".join(commands)
    else:
        return COMMANDS_HELP.get(command,  f"Help for this command '{command}' is not yet available")


COMMAND_EXIT = ("good bye", "close", "exit")

COMMANDS = {
    "hello": handler_hello,
    "add": handler_add,
    "change": handler_change,
    "phone": handler_phone,
    "show all": handler_show_all,
    "help": handler_help
}

COMMANDS_HELP = {
    "hello": "Just hello",
    "add": "Add user and phone. Required username and phone.",
    "change": "Change user's phone. Required username and phone.",
    "phone": "Show user's phone. Required username.",
    "show all": "Show all user phone numbers.",
    "help": "List of commands  and their description.",
    "exit": "Exit of bot.",
    "close": "Exit of bot.",
    "good bye": "Exit of bot."
}

user_data = ab.AddressBook()


def main():
    print("Bot init")
    while True:
        try:
            user_input = input("Enter your command:")
        except KeyboardInterrupt:
            print("\r")
            break
        if user_input.lower() in COMMAND_EXIT:
            break
        else:
            command, args = parse_input(user_input)
            try:
                result = COMMANDS[command](*args)
            except KeyError:
                print("Your command is not recognized, try to enter other command. "
                      "To get a list of all commands, you can use the 'help' command")
            else:
                if result:
                    print(result)
    print("Good bye")


if __name__ == "__main__":
    main()






# if __name__ == "__main__":
#     ab = AddressBook()
#     rec = Record(Name("Jon1"),[Phone("000-0001"),Phone("000-0002")],email=Email("bademail"))
#     rec.add_phone(Phone("000-0003"))
#     #rec.remove_phone("00-0001")
#     #print(rec)

#     ab.add_record(rec)
#     rec = Record("Jon2", ["200-0001", "200-0002"])
#     ab.add_record(rec)
#     rec = Record("Jon3", "300-0001", "Jon3@email.com")
#     ab.add_record(rec)

#     ab['Jon1'].remove_phone("000-0001")
#     ab['Jon1'].address.value="Jon1 Home Street"
#     ab['Jon2'].email.value = "Jon2@email.com"

#     for v in ab.values():
#         print( v)
