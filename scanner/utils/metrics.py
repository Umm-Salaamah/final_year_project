# metrics.py

def calculate_detection_accuracy(results):
    total_headers = len(results)
    correct_identifications = sum(1 for header in results.values() if header['status'] == 'Present')
    accuracy = (correct_identifications / total_headers) * 100
    return accuracy

def calculate_false_positive_rate(results):
    false_positives = sum(1 for header in results.values() if header['status'] == 'Missing')
    total_missing = len(results) - sum(1 for header in results.values() if header['status'] == 'Present')
    false_positive_rate = (false_positives / total_missing) * 100
    return false_positive_rate

def calculate_coverage(results, expected_headers):
    headers_checked = len(results)
    total_expected = len(expected_headers)
    coverage = (headers_checked / total_expected) * 100
    return coverage
