"""Wizards."""


class MismatchError(Exception):
    """
    Class MismatchError inherits its properties from Exception class.

    Should have user-defined message.
    """

    def __init__(self, message):
        """
        Class constructor.

        :param message: user message
        """
        self.message = message


class Wand:
    """Class for Wand object."""

    def __init__(self, wood_type, core):
        """Define wand attributes."""
        self.wood_type = wood_type
        self.core = core

    def set_wood_type(self, wood_type):
        """Give wand a new wood type."""
        self.wood_type = wood_type

    def set_core(self, core):
        """Give wand a new core."""
        self.core = core

    @staticmethod
    def check_wand(wand):
        """Make sure object is Wand class and has both required arguments."""
        if type(wand) != Wand:
            raise MismatchError("The wand like that does not exist!")
        elif wand.wood_type is None:
            raise MismatchError("The wand like that does not exist!")
        elif wand.core is None:
            raise MismatchError("The wand like that does not exist!")

    def __str__(self):
        """Object returns in a string format."""
        return self.wood_type + ", " + self.core


class Wizard:
    """Class for Wizard object."""

    def __init__(self, name, wand=None):
        """Define wizaed's name and wand if it's formatted correctly"""
        self.name = name
        if wand is None:
            self.wand = None
        else:
            wand.check_wand(wand)
            self.wand = wand

    def set_wand(self, wand):
        """Give wizard a new wand if wand is correctly formatted."""

        wand.check_wand(wand)
        self.wand = wand

    def get_wand(self):
        """Return wand."""

        return self.wand

    def __str__(self):
        """Return wizard's name if object is called."""

        return self.name


class School:
    """Class for school object."""

    schools = [
        "Hogwarts School of Witchcraft and Wizardry", "Durmstrang Institute",
        "Ilvermorny School of Witchcraft and Wizardry", "Castelobruxo",
        "Beauxbatons Academy of Magic"
    ]

    students = []

    def __init__(self, name: str):
        """Define school name and make sure it exists in the schools list."""

        if name not in School.schools:
            raise MismatchError("There is no such school!")
        else:
            self.name = name

    def add_wizard(self, wizard):
        """Add a new wizard to the school.

        wizard must have a name and a correct wand.
        wizard must be of Wizard class
        """

        if type(wizard) != Wizard:  # Isn't Wizard class instance
            raise MismatchError("It's a filthy muggle!")
        elif wizard.get_wand() is None:  # No wand defined
            raise MismatchError("It's a filthy muggle!")
        elif len(str(wizard)) < 1:  # No name defined
            raise MismatchError("It's a filthy muggle!")
        elif wizard in School.students:
            return str(wizard) + " is already studying in this school!"
        else:
            School.students.append(wizard)
            return str(wizard) + " started studying in " + self.name + "."

    def remove_wizard(self, wizard):
        """Remove a wizard from the school"""

        if wizard in School.students:
            School.students.remove(wizard)

    def get_wizards(self):
        """Return a list of students in school."""
        students_str = []   # since students in list are objects, they must be converted to string, i think hehe
        for student_object in School.students:
            students_str.append(str(student_object))
        return students_str

    def get_wizard_by_wand(self, wand):
        """Search for a wizard, based on wand."""
        wand.check_wand(wand)
        for student in School.students:
            if student.get_wand() == wand:
                return student
        return None

    def __str__(self):
        """When object is called, return it's name"""
        return self.name

if __name__ == '__main__':

    wand1 = Wand("Holly", "Phoenix feather")
    wand2 = Wand("Vine", "Dragon heartstring")
    bad_wand = Wand(None, "empty")
    assert str(wand1) == 'Holly, Phoenix feather'
    assert str(wand2) == 'Vine, Dragon heartstring'

    wizard1 = Wizard("Harry Potter")
    wizard2 = Wizard("Hermione Granger")
    assert str(wizard1) == 'Harry Potter'
    assert str(wizard2) == 'Hermione Granger'

    bad_wizard = Wizard(None, None)
    school = School("Hogwarts School of Witchcraft and Wizardry")
    assert str(school) == 'Hogwarts School of Witchcraft and Wizardry'

    assert wizard1.get_wand() is None
    wizard1.set_wand(wand1)
    assert str(wizard1.get_wand()) == 'Holly, Phoenix feather'
    # wizard1.set_wand(bad_wand)  # --> MismatchError: The wand like that does not exist!

    assert school.add_wizard(wizard1) == 'Harry Potter started studying in Hogwarts School of Witchcraft and Wizardry.'
    assert school.get_wizards().__len__() == 1

    # school.add_wizard(wizard2)  # --> MismatchError: It's a filthy muggle!
    # school.add(bad_wizard)  # --> MismatchError: It's a filthy muggle!
    wizard2.set_wand(wand2)
    assert school.add_wizard(wizard2) == 'Hermione Granger started studying in Hogwarts School of Witchcraft and Wizardry.'

    assert school.get_wizards().__len__() == 2
    assert school.add_wizard(wizard1) == 'Harry Potter is already studying in this school!'

    assert str(school.get_wizard_by_wand(wand1)) == 'Harry Potter'
    assert str(school.get_wizard_by_wand(wand2)) == 'Hermione Granger'

    school.remove_wizard(wizard1)