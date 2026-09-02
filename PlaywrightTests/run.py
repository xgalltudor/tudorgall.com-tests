import subprocess
import os


def run_tests():
    script_dir = os.path.dirname(__file__)
    test_suites_dir = os.path.join(script_dir, 'test_suites')
    subprocess.run(['pytest', '-vv', test_suites_dir])


if __name__ == '__main__':
    run_tests()
