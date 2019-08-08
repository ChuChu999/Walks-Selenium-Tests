from woi_tests import Environment, run_test, TestName


def get_input_test_name() -> TestName:
    test_names = [test_name for test_name in TestName]

    print("\nAvailable tests:")

    for i in range(len(test_names)):
        print(str(i) + ") " + test_names[i].name)

    selection = input("Choose a test to run [0]: ") or 0

    try:
        selection = int(selection)
    except ValueError:
        raise ValueError("Please enter an integer!")

    return test_names[selection]


def get_input_environment() -> Environment:
    environments = [environment for environment in Environment]

    print("\nAvailable environments:")

    for i in range(len(environments)):
        print(str(i) + ") " + environments[i].name)

    selection = input("Choose the environment [0]: ") or 0

    try:
        selection = int(selection)
    except ValueError:
        print("Please enter an integer!")

    return environments[selection]


if __name__ == "__main__":
    input_test_name = get_input_test_name()
    input_environment = get_input_environment()

    print("\nloading", input_test_name, "on", input_environment, "...\n")
    run_test(input_test_name, input_environment)
