import unittest
import program

class ProgramTests(unittest.TestCase):

    def test_string_to_list(self):
        #Given
        test_var = "This is a string to split"
        expected = ["This", "is", "a", "string", "to", "split"]

        #When 
        result = program.string_to_list(test_var)

        #Then 
        self.assertEqual(result, expected, "test_string_to_list failed happy path")

    def test_string_to_list_lengh(self):
        #Given
        test_var = "This is a string to split"
        expected = 6

        #When 
        result = len(program.string_to_list(test_var))

        #Then 
        self.assertEqual(result, expected, "test_string_to_list failed happy path")

    def test_string_to_list_delimiter(self):
        #Given
        test_var = "This|is|a|string|to|split"
        expected = ["This", "is", "a", "string", "to", "split"]
 
        #When 
        result = program.string_to_list(test_var, "|")

        #Then 
        self.assertEqual(result, expected, "test_string_to_list failed happy path")
    def test_string_to_list_delimiter_lengh(self):
        #Given
        test_var = "This|is|a|string|to|split"
        expected = 6

        #When 
        result = len(program.string_to_list(test_var, "|"))

        #Then 
        self.assertEqual(result, expected, "test_string_to_list failed happy path")

    def test_string_to_list_delimiter_lengh_fail(self):
        #Given
        test_var = "This||is|a|string|to|split"
        expected = 6

        #When 
        result = len(program.string_to_list(test_var, "|"))

        #Then 
        self.assertEqual(result, expected, "test_string_to_list failed happy path")

if __name__ == "__main__":
        unittest.main()