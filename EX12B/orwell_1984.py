"""Orwell 1984."""


class Citizen:
    """Class which represents a single citizen."""

    def __init__(self, name, party, status="citizen"):
        """
        Class constructor.

        :param name: name of the citizen
        :param party: party which he belongs to
        :param status: status
        """
        self.name = name
        if isinstance(party, Party):
            party = party
        else:
            party = None
        if status == "prole":
            self.party = None
            self.status = status
        elif status == "nonperson":
            self.name = None
            self.party = None
            self.status = status
        elif status == "under surveillance":
            self.party = party
            self.status = status
            if self.party is not None:
                self.party.add_party_member(self)
        else:
            self.status = "citizen"
            self.party = party
            if self.party is not None:
                self.party.add_party_member(self)

    def set_party(self, party):
        """
        Set citizen's party. The method does not return anything.

        :param party: new party (Inner or Outer, both are Party class instances)
        """
        if isinstance(party, Party) is True or party is None:
            if self.party is not None and self in self.party.get_party_members():
                self.party.remove_party_member(self)
            if party is not None:
                party.add_party_member(self)
            if party is None and self.party is not None:
                self.party.remove_party_member(self)
                self.party = None
            else:
                self.party = party

    def get_party(self):
        """
        Get the citizen's party.

        :return: party object
        """
        return self.party

    def set_status(self, status):
        """
        Set citizen's status. The method does not return anything.

        :param status: new status
        """
        valid_statuses = ["citizen", "under surveillance"]
        if status == "nonperson" and self.party is not None:
            self.status = "nonperson"
            self.party.vaporize(self)
        elif status == "prole":
            self.party = None
            self.status = "prole"
        elif status in valid_statuses:
            self.status = status

    def get_status(self):
        """
        Get the citizen's status.

        :return: status
        """
        return self.status

    def set_name(self, name):
        """
        Set the citizen's name. The method does not return anything.

        :param name: new name
        """
        self.name = name

    def get_name(self):
        """
        Get the citizen's name.

        :return: name
        """
        return self.name

    def __str__(self):
        """
        Compute string representation of this object.

        :return: f"BIG BROTHER IS WATCHING YOU, {self.name}"
        """
        return f"BIG BROTHER IS WATCHING YOU, {self.name}"


class Party:
    """Party class."""

    def __init__(self):
        """Class constructor."""
        self.members = []
        pass

    def get_party_members(self):
        """
        Get the list of party members.

        :return: list
        """
        return self.members

    def add_party_member(self, citizen):
        """
        Add the citizen to the party members' list.

        Citizen must be instance of Citizen class, must have name, must not already be a member and must not have a
        'nonperson' status.
        Does not return anything.
        :param citizen Citizen class instance
        """
        if isinstance(citizen, Citizen) is True:
            if citizen.name is not None:
                if citizen.get_status() != "nonperson":
                    if citizen not in self.get_party_members():
                        self.members.append(citizen)
                        citizen.party = self

    def remove_party_member(self, citizen):
        """Remove the citizen from the party members' list."""
        if citizen in self.members:
            self.members.remove(citizen)

    def vaporize(self, citizen):
        """
        Remove the citizen from the party members, set his name and party to None and status to nonperson.

                    The method does not return anything.
        :param citizen: Citizen class instance

        """
        if citizen in self.members:
            citizen.set_party(None)
            citizen.status = "nonperson"
            citizen.name = None

    def get_privileges(self):
        """
        Get privileges granted by party.

        :return: None
        """
        return None

    @staticmethod
    def get_slogan():
        r"""
        Get the party slogan.

        :return: "WAR IS PEACE\nFREEDOM IS SLAVERY\nIGNORANCE IS STRENGTH"
        """
        return "WAR IS PEACE\nFREEDOM IS SLAVERY\nIGNORANCE IS STRENGTH"


class InnerParty(Party):
    """Inner party class, which extends the Party class."""

    def get_privileges(self):
        """
        Get privileges granted by party (Override).

        :return: "Everything"
        """
        return "Everything"

    def __str__(self):
        """
        Compute string representation of this object.

        :return: "Inner party"
        """
        return "Inner party"


class OuterParty(Party):
    """Outer party class, which extends the Party class."""

    def __str__(self):
        """
        Compute string representation of this object.

        :return: "Outer party"
        """
        return "Outer party"


class BigBrother:
    """Big brother class."""

    def __init__(self, inner_party, outer_party):
        """
        Class constructor.

        :param inner_party: inner party object
        :param outer_party: outer party object
        """
        self.inner_members = inner_party.get_party_members()
        self.outer_members = outer_party.get_party_members()
        self.vaporised_count = 0

    def get_all_citizens(self):
        """
        Get all citizens who are members in the parties.

        :return: list
        """
        return self.inner_members + self.outer_members

    def massive_vaporize(self, status):
        """
        Vaporize people with a given status.

        :param status: string
        :return: number of vaporized people per session
        """
        current_session = 0
        all_citizens = self.get_all_citizens()[:]  # copy of the list
        for citizen in all_citizens:
            if citizen.get_status() == status:
                citizen.get_party().remove_party_member(citizen)
                citizen.get_party().vaporize(citizen)
                self.vaporised_count += 1
                current_session += 1
        return current_session

    def get_number_of_vaporized(self):
        """
        Get number of vaporized people of all time.

        :return: integer
        """
        return self.vaporised_count
