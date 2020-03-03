import sys
from notebook import Notebook, Note


class Menu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.definitions,
            "6": self.quit
        }
        self.definition_choices = {
            "1": self.explain_object,
            "2": self.explain_attributes,
            "3": self.explain_methords,
            "4": self.explain_self,
            "5": self.explain_init,
            "6": self.explain_str,
            "7": self.quit
        }

    def display_menu(self):
        print(""" Notebook Menu 
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Get to know the main definitions 
        6. Quit
        """)

    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
            for note in notes:
                print("{0}: {1}\n{2}".format(
                    note.id, note.tags, note.memo))

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")

        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        id = input("Enter a note id: ")

        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

    def display_definiotion_menu(self):
        print(
            """
            1. об’єкт,
            2. атрибути класу,
            3. методи класу,
            4. self,
            5. метод __init__,
            6. метод __str__,
            7. quit
            """
        )

    def definitions(self):
        definitions = "об’єкт, атрибути класу, методи класу, self, метод __init__, метод __str__"
        definitions = definitions.split(",")
        print(definitions)
        while True:
            self.display_definiotion_menu()
            n_definition = input("Enter a number of definition to know: ")
            action = self.definition_choices.get(n_definition)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(n_definition))

    def explain_object(self):
        print()
        print("Об'єкт – модель, яка може щось зробити й існують речі,"
              " які можуть бути зроблені для неї та з нею.")

        object_example = tuple()
        object_example = object_example + tuple('7')
        object_example = object_example + tuple('9')
        object_example.count('7')
        print(object_example)
        print('x = ', object_example[0])
        print('x = ', object_example.__getitem__(0))  # special method
        print('x = ', tuple.__getitem__(object_example, 0))
        print(dir(object_example))
        print(
            "Створили об’єкт певного типу \n"
            "Додали до об’єкту дані\n"
            "Виконали дії над об’єктами за допомогою оператора і методів"
        )

    def explain_attributes(self):
        print()
        print(
            """
            Термін для ідентифікації видів об'єктів – клас. Клас описує об'єкт. Клас це креслення
             за яким буде цей об'єкт виготовлено.
              Наприклад, в аудиторії два вікна але кожне з них має
               спільні для класу вікон ознаки (атрибути) і відповідні поведінки. 
            """
        )
        print("Атрибути класу Note:")
        print("memo, tags, creation_date, id")

    def explain_methords(self):
        print()
        print(" У визначенні класу, як правило, задані змінні екземпляра(поля, атрибути),\n"
              " також відомі як члени даних, що містить об'єкт, а також МЕТОДИ,\n"
              " також відомі як функції-члени, що об'єкт може виконувати. ")
        print("Методи і атрибути класу Menu:")
        print(dir(self))

    def explain_self(self):
        print()
        print(
            """
            
        Let's say you have a class ClassA which contains a method methodA defined as:
  
        
        def methodA(self, arg1, arg2):
            # do something
     
        
        and ObjectA is an instance of this class.      
        Now when ObjectA.methodA(arg1, arg2) is called, python internally converts it for you as:
        
        ClassA.methodA(ObjectA, arg1, arg2)
        
        The self variable refers to the object itself.
            """
        )
        type_s = type(self)
        print("Is self an {}?".format(type(self)))
        print(isinstance(self, type_s))

    def explain_init(self):
        print()
        print(
            """Ініціалізує створений раніше екземпляр класу.
            object.__init__(self[, args])-> None
            
            self - Посилання на екземпляр.

            args - Позиційні і / або аргументи, які відіграють роль в процесі ініціалізації
            екземпляра.Це аргументи, які були передані в вираженні конструювання примірника.
            """)

    def explain_str(self):
        print("""
        Дозволяє визначити результат функції str () при передачі в неї примірника даного класу.
    object .__ str __ (self) -> str
    
    self - Посилання на екземпляр.""")


if __name__ == "__main__":
    Menu().run()