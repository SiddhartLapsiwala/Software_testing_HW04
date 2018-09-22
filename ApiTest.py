import unittest
from API_Connect import retrive_repo_details

class ApiTest(unittest.TestCase):
    def test_valid_repo(self):
        """ test for valid repo """
        result = retrive_repo_details("SiddhartLapsiwala")
        self.assertEqual(len(result), 5)

    def test_valid_commit(self):
        """ test for valid commit of repo """
        result = retrive_repo_details("SiddhartLapsiwala")
        self.assertEqual(result.get("Software_Testing_Assign2"), 10)

    def test_invalid_repo_name(self):
        """ test for invalid repo name"""
        with self.assertRaises(ValueError) as context:
            retrive_repo_details("Siddhartlapsifdgdfgd")

        self.assertTrue('Please check repository name!!' in str(context.exception))


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()