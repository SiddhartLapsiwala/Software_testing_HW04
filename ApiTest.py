import unittest.mock
import mock
from API_Connect import retrive_commit
from API_Connect import retrive_list_of_repo


class ApiTest(unittest.TestCase):
    def _mock_response(
            self,
            status=200,
            content="CONTENT",
            json_data=None,
            raise_for_status=None):
        """
        since we typically test a bunch of different
        requests calls for a service, we are going to do
        a lot of mock responses, so its usually a good idea
        to have a helper function that builds these things

        """
        mock_resp = mock.Mock()
        # mock raise_for_status call w/optional error
        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        # set status code and content
        mock_resp.status_code = status
        mock_resp.content = content
        # add json data if provided
        if json_data:
            mock_resp.json = mock.Mock(
                return_value=json_data
            )
        return mock_resp

    @mock.patch('requests.get')
    def test_valid_repo(self,mock_get):
        """ test for valid repo """
        json_response = [{
          'name': 'Software_Testing_567',
        },{
          'name': 'Stevens---810',
        }, {
          'name': 'Software_Testing_Assign2',
        }, {
          'name': 'Software_testing_HW04',
        }, {
          'name': 'SSW-555-GEDCOM-Project',
        }]
        mock_resp = self._mock_response(json_data=json_response)
        mock_get.return_value = mock_resp
        result = retrive_list_of_repo("SiddhartLapsiwala")
        self.assertEqual(len(result), 5)

    @mock.patch('requests.get')
    def test_valid_commit(self, mock_get):
        """ test for valid commit of repo """
        json_response = [{
            'sha': '0e2da5e190f0ec5eb8a86227894215e11b30eb65',
        }, {
          'sha': '0e2da5e190f0ec5eb8a86227894215e11b30eb65',
        }, {
          'sha': '0e2da5e190f0ec5eb8a86227894215e11b30eb65',
        }]

        mock_resp = self._mock_response(json_data=json_response)
        mock_get.return_value = mock_resp
        result = retrive_commit("SiddhartLapsiwala", "Stevens---810")
        self.assertEqual(result["Stevens---810"], 3)

    @mock.patch('requests.get')
    def test_invalid_repo_name(self, mock_get):
        """ test for invalid repo name"""
        mock_resp = self._mock_response(status=404)
        mock_get.return_value = mock_resp
        with self.assertRaises(ValueError) as context:
            retrive_list_of_repo("Siddhartlapsifdgdfgd")

        self.assertTrue('Please check repository name!!' in str(context.exception))


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
