import json

FILENAME = "notes.json"

def load_notes():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_notes(notes):
    with open(FILENAME, "w") as file:
        json.dump(notes, file, indent=2)

def add_note():
    notes = load_notes()
    text = input("Enter your note: ")
    notes.append({"text": text})
    save_notes(notes)
    print("Note saved!")

def view_notes():
    notes = load_notes()
    if not notes:
        print("No notes yet.")
        return

    print("Your Notes:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note['text']}")

def main():
    while True:
        print("\n--- Notes App (JSON) ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main()