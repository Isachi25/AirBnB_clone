import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def tearDown(self):
        storage.reset()  # Reset storage to ensure a clean slate for each test

    def test_quit(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.hbnb_command.onecmd("quit"))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_EOF(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.hbnb_command.onecmd("EOF"))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_emptyline(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("\n")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_count(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("create BaseModel")
            self.hbnb_command.onecmd("count BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "1")

    def test_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Assuming the generated ID has a length of 36 characters

    def test_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("show BaseModel 1")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("destroy BaseModel 1")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("all BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "[]")

    def test_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("update BaseModel 1 name 'New Name'")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_with_dict(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("create BaseModel")
            self.hbnb_command.onecmd("update BaseModel 1 {'name': 'Updated Name', 'value': 42}")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_help_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("help show")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Prints the string representation", output)

if __name__ == '__main__':
    unittest.main()
