from unittest import TestLoader, TestSuite, TextTestRunner


from tests.test_minimizer import TestMinimizer
from tests.test_automata_convertor import TestAutomataConvertor
from tests.test_automata_generator import TestAutomataGenerator
from tests.test_sequence_generator import TestSequenceGenerator
from tests.test_automata_comparison import TestAutomataComparison
from tests.test_sequence import TestSequence

def run():
    test_classes_to_run = [TestMinimizer]
    loader = TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    meta_suite = TestSuite(suites_list)
    TextTestRunner().run(meta_suite)


if __name__ == '__main__':
    run()
