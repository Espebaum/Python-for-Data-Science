import unittest
from ft_filter import ft_filter

def is_42Seoul(info):
    return info['School'] == '42Seoul'


def is_42Paris(info):
    return info['School'] == '42Paris'


def is_from_Tokyo(info):
    return 'Tokyo' in info['School']


def has_long_name(info):
    return len(info['Name']) >= 8

class TestFtFilter(unittest.TestCase):
    def test_is_42Seoul(self):
        self.assertTrue(is_42Seoul({'Name': 'gyopark', 'School': '42Seoul'}))
        self.assertFalse(is_42Seoul({'Name': 'James', 'School': '42Paris'}))

    def test_ft_filter(self):
        users = [
            {'Name': 'James', 'School': '42Paris'},
            {'Name': 'gyopark', 'School': '42Seoul'},
            {'Name': 'Satoru', 'School': '42Tokyo'},
            {'Name':'I have long name', 'School': '테스트할때스쿨지워보세요키에러남'}
        ]
        expected_result_42Seoul = [{'Name': 'gyopark', 'School': '42Seoul'}]
        expected_result_42Paris = [{'Name': 'James', 'School': '42Paris'}]
        expected_result_42Tokyo = [{'Name': 'Satoru', 'School': '42Tokyo'}]
        expected_result_long_name = [{'Name':'I have long name', 'School': '테스트할때스쿨지워보세요키에러남'}]
        
        # ft_filter와 비교
        self.assertEqual(ft_filter(is_42Seoul, users), expected_result_42Seoul)
        self.assertEqual(ft_filter(is_42Paris, users), expected_result_42Paris)
        self.assertEqual(ft_filter(is_from_Tokyo, users), expected_result_42Tokyo)
        self.assertEqual(ft_filter(has_long_name, users), expected_result_long_name)
        
        # filter와 비교 (리스트로 변환)
        self.assertEqual(list(filter(is_42Seoul, users)), expected_result_42Seoul)
        self.assertEqual(list(filter(is_42Paris, users)), expected_result_42Paris)
        self.assertEqual(list(filter(is_from_Tokyo, users)), expected_result_42Tokyo)
        self.assertEqual(list(filter(has_long_name, users)), expected_result_long_name)


    def test_ft_filter_empty(self):
        users = []
        expected_result = []
        self.assertEqual(ft_filter(is_42Seoul, users), expected_result)
        self.assertEqual(ft_filter(is_42Seoul, users), expected_result)
        self.assertEqual(ft_filter(is_42Seoul, users), expected_result)
        self.assertEqual(ft_filter(is_42Seoul, users), expected_result)

        # filter와 비교 (리스트로 변환)
        self.assertEqual(list(filter(is_42Seoul, users)), expected_result)
        self.assertEqual(list(filter(is_42Paris, users)), expected_result)
        self.assertEqual(list(filter(is_from_Tokyo, users)), expected_result)
        self.assertEqual(list(filter(has_long_name, users)), expected_result)


    def test_ft_filter_no_match(self):
        users = [
            {'Name': 'James', 'School': '42Paris'},
            {'Name': 'Satoru', 'School': '42Tokyo'}
        ]
        expected_result = []
        self.assertEqual(ft_filter(is_42Seoul, users), expected_result)
        self.assertEqual(list(filter(is_42Seoul, users)), expected_result)


if __name__ == '__main__':
    unittest.main()