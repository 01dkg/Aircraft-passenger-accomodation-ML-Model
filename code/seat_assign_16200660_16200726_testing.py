import unittest
from seat_assign_16200660_16200726 import total_available_seats,empty_seat_row

class seatAssignTest(unittest.TestCase):

      def test_total_available_seats(self):
        seats_available= total_available_seats(empty_seat_row)
        self.assertEqual(seats_available,53)

      def test_total_available_seats2(self):
        seats_available = total_available_seats(empty_seat_row)
        self.assertEqual(seats_available, 10)
if __name__ == '__main__':
    unittest.main()