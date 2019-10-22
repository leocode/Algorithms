import unittest
from ..components.alone_at_party import AloneAtParty


class AloneAtPartyTest(unittest.TestCase):
    def test_canary(self):
        self.assertEqual(True, True)

    def test_no_guest(self):
        # given
        guest_pairing = AloneAtParty([])

        # when
        guest_arrived = guest_pairing.guest_arrived()

        # then
        self.assertEqual(False, guest_arrived)

    def test_one_guest(self):
        # given
        guest_pairing = AloneAtParty([21])

        # when
        only_one_guest = guest_pairing.more_than_one_guest()

        # then
        self.assertEqual(False, only_one_guest)

    def test_one_alone_guests(self):
        # given
        guest_pairing = AloneAtParty([25, 19, 21, 25, 21])

        # when
        age_guest_without_pair = guest_pairing.lonely_guest()

        # then
        self.assertEqual(True, age_guest_without_pair)

    def test_no_alone_guests(self):
        # given
        guest_pairing = AloneAtParty([25, 19, 21, 25, 21, 19])

        # when
        age_guest_without_pair = guest_pairing.lonely_guest()

        # then
        self.assertEqual(False, age_guest_without_pair)


if __name__ == '__main__':
    unittest.main()
