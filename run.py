from enum import Enum
import tw_tests
import woi_tests


class Site(Enum):
    TW = tw_tests
    WOI = woi_tests


site = Site.TW


def get_input_site() -> Site:
    sites = [site for site in Site]

    print("\nAvailable sites:")

    for i in range(len(sites)):
        print(str(i)+") " + sites[i].name)

    selection = input("Choose a site for the test to run on [0]: ") or 0

    try:
        selection = int(selection)
    except ValueError:
        raise ValueError("Please enter an integer!")

    return sites[selection]


def get_input_test_name() -> site.value.TestName:
    test_names = [test_name for test_name in site.value.TestName]

    print("\nAvailable tests:")

    for i in range(len(test_names)):
        print(str(i) + ") " + test_names[i].name)

    selection = input("Choose a test to run [0]: ") or 0

    try:
        selection = int(selection)
    except ValueError:
        raise ValueError("Please enter an integer!")

    return test_names[selection]


def get_input_environment() -> site.value.Environment:
    environments = [environment for environment in site.value.Environment]

    print("\nAvailable environments:")

    for i in range(len(environments)):
        print(str(i) + ") " + environments[i].name)

    selection = input("Choose the environment [0]: ") or 0

    try:
        selection = int(selection)
    except ValueError:
        raise ValueError("Please enter an integer!")

    return environments[selection]


if __name__ == "__main__":
    site = get_input_site()
    test_name = get_input_test_name()
    environment = get_input_environment()

    print("\nloading", test_name, "on",  environment, "for", site, "...\n")
    site.value.run_test(test_name, environment)
