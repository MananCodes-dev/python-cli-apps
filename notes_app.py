def add_note():
    note_content = input("Enter the note content")
    with open("notes.txt", "a") as file:
        file.write(note_content + "\n")
    print(f"Note added: {note_content}")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        if notes:
            print("\nYour Notes:")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note.strip()}")
        else:
            print("No notes available.")
    except FileNotFoundError:
        print("No Notes file found. Please add a note first.")

def delete_note():
    with open("notes.txt", "r") as file:
        pass
    print("All notes deleted.")

while True:
    print("\n--- Notes Application Menu ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete All Notes")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        add_note()
    elif choice == '2':
        view_notes()
    elif choice == '3':
        delete_note()
    elif choice == '4':
        print("Exiting the Notes application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")