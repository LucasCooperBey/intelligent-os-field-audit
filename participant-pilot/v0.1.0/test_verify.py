"""source: distinguish invalid evidence, wrong claims and checker success without admission decisions."""
import copy
import json
import unittest
from pathlib import Path
from verify import check

class ClaimChecks(unittest.TestCase):
    def setUp(self):
        self.example = json.loads(Path(__file__).with_name('example-result.json').read_text())
    def test_reference_example_only_validates_claim_shape(self):
        result = check(self.example)
        self.assertTrue(result['valid_record'])
        self.assertFalse(result['auto_invite'])
        self.assertIn('Claim checker only', result['limit'])
    def test_missing_task_is_unknown_not_a_pass(self):
        del self.example['boundary']
        self.assertEqual(check(self.example)['tasks']['boundary'], 'could_not_evaluate')
    def test_missing_queue_cannot_be_called_empty(self):
        self.example['missing_input']['queue_a'] = 'no_work'
        self.assertEqual(check(self.example)['tasks']['missing_input'], 'claims_do_not_match')
    def test_unfinished_output_cannot_be_accepted(self):
        self.example['result_check']['accepted'] = True
        self.assertEqual(check(self.example)['tasks']['result_check'], 'claims_do_not_match')
    def test_numeric_zero_is_not_boolean_false(self):
        self.example['boundary']['external_send'] = 0
        self.assertEqual(check(self.example)['tasks']['boundary'], 'claims_do_not_match')
    def test_wrong_method_version_is_invalid(self):
        self.example['pilot_version'] = 'v1'
        self.assertFalse(check(self.example)['valid_record'])
    def test_missing_provenance_is_invalid(self):
        del self.example['provenance']['model']
        self.assertFalse(check(self.example)['valid_record'])

if __name__ == '__main__':
    unittest.main()
