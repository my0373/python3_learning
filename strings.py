def main():
    """
    The main function
    :return:
    """
    name = "Dave Grave"
    age = 60
    weight = "12.5"

    print_name_simple(name)

    print_name_upper(name)

    print_name_capitalised(name)

    print_name_age_positional(age, name, weight)

    print_name_age_mixed_positional(age, name, weight)

    print_name_age_tabulated_before(age, name, weight)

    print_name_age_tabulated_after(age, name, weight)

    print_with_quotes(age, name, weight)

    print_with_zeros(age, name, weight)


def print_with_zeros(age, name, weight):
    ## zero pad the age. Note it is always 9 long and pads to that.
    print('Name:"{0}" Age:"{1:>09}" Weight:"{2}"'.format(name.capitalize(),
                                                         age,
                                                         weight))


def print_with_quotes(age, name, weight):
    ## Add some double quotes as we are in a single quoted string
    print('Name:"{0}" Age:"{1:>9}" Weight:"{2}"'.format(name.capitalize(),
                                                        age,
                                                        weight))


def print_name_age_tabulated_after(age, name, weight):
    ## Print the name age and weight adding space before.the age
    print('Name:{0} Age:{1:>9} Weight:{2}'.format(name.capitalize(),
                                                  age,
                                                  weight))


def print_name_age_tabulated_before(age, name, weight):
    ## Print the name age and weight adding space after.the age
    print('Name:{0} Age:{1:<9} Weight:{2}'.format(name.capitalize(),
                                                  age,
                                                  weight))


def print_name_age_mixed_positional(age, name, weight):
    ## Print the name age and weight messing around with the positional arguments.
    print('Name:{0} Age:{2} Weight:{1}'.format(name.capitalize(),
                                               age,
                                               weight))


def print_name_age_positional(age, name, weight):
    ## Print the name age and weight as positional arguments.
    print('Name:{} Age:{} Weight:{}'.format(name.capitalize(),
                                            age,
                                            weight))

def print_name_capitalised(name):
    ## Print the name capitalised.
    print('{}'.format(name.capitalize()))


def print_name_upper(name):
    ## Print the name in all uppercase
    print('{}'.format(name.upper()))


def print_name_simple(name):
    ## Print the name in all lowecase
    print('{}'.format(name.lower()))


if __name__ == '__main__':
    main()
