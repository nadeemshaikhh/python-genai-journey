def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved!")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if not notes:
                print("No notes yet.")
            else:
                print("Your Notes:")
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note.strip()}")
    except FileNotFoundError:
        print("No notes file found. Add a note first.")

def main():
    while True:
        print("\n--- Notes App ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
