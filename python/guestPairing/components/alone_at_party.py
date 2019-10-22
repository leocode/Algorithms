import sys


class AloneAtParty:
    def __init__(self, guest_list):
        self.guest_list = guest_list
        self.lonely_guest_age = None

        if not self.guest_arrived():
            print("Your guests have not arrived yet")
            return

        if not self.more_than_one_guest():
            print("Only one guest arrived so far")
            return

        if self.lonely_guest():
            print("The person alone is " + str(self.lonely_guest_age) + " years old.")
            return

        print("Everybody's got a pair.")
        pass

    def guest_arrived(self):
        if self.guest_list:
            return True

        return False

    def more_than_one_guest(self):
        if len(self.guest_list) > 1:
            return True

        return False

    def lonely_guest(self):
        lonely_guest = [age for age in self.guest_list if self.guest_list.count(age) < 2]
        if lonely_guest:
            self.lonely_guest_age = lonely_guest[0]
            return True

        return False


if __name__ == "__main__":
    args = []
    for arg in sys.argv:
        args.append(arg.replace(',', ''))

    AloneAtParty(args[1:])
