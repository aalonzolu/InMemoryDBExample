from src.constants import InvalidInput, InvalidCommand, NoTransaction
from src.inmdb import InMDB


def parse_input(text) -> (str, str, int):
    pieces = text.split()
    try:
        pieces[0] = pieces[0].upper()
    except KeyError:
        pass
    if len(pieces) == 3:
        return pieces
    elif len(pieces) == 2:
        return pieces[0], pieces[1], None
    elif len(pieces) == 1:
        return pieces[0], None, None
    else:
        raise InvalidInput


def execute_command(db, fn, arg1, arg2):
    if fn == "SET":
        db.set(arg1, arg2)
    elif fn == "GET":
        print(db.get(arg1))
    elif fn == "UNSET":
        db.unset(arg1)
    elif fn == "NUMEQUALTO":
        print(db.numequalto(arg1))
    elif fn == "BEGIN":
        db.begin()
    elif fn == "ROLLBACK":
        db.rollback()
    elif fn == "COMMIT":
        db.commit()
    else:
        raise InvalidCommand



if __name__ == '__main__':
    print('In Memory DB CLI')
    db = InMDB()
    input_command = ""
    while True:
        try:
            input_command = input("\n>> ")
            fn, name, value = parse_input(input_command)
            if fn == "END":
                print("Exiting")
                break
            else:
                execute_command(db, fn, name, value)
        except NoTransaction:
            print("NO OPEN TRANSACTION")
            pass
        except KeyboardInterrupt:
            print("EXITING")
            break
        except InvalidInput:
            print("INVALID INPUT")
            pass
        except InvalidCommand:
            print("INVALID COMMAND")
