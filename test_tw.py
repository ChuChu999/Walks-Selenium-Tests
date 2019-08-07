from tw_actions import Environment
from tw_tests import run_test, TestName

if __name__ == "__main__":
    run_test(TestName.LOAD_ALL_TOURS, Environment.STAGING)
