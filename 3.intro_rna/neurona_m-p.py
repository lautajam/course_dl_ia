QUESTIONS = [
    "It's the weekend? ",
    "I have homework to do? ",
    "Is the cinema closed? ",
    "Movies release today?? ",
]

CAN_GO = 1
CANT_GO = 0
VALUE_N = 0
VALUE_Y = 1
TRESHOLD = 2
INIT_LOOP = 0
MIN_XN_VALUE = 0
MAX_XN_VALUE = 2
FIRST_VALUE_XN = -1
CINEMA_IS_CLOSED = 1
CINEMA_CLOSED_INDEX = 2


def check_xn(xn, question_index):
    """This function checks if the value of `xn` is within the correct range [0, 1] and if it is an integer. 
    If the value is invalid, it requests a new input and recursively calls itself until the value is correct.

    Args:
        xn (any): The first question entry value (must be 0 or 1).
        question_index (int): The question index for the QUESTIONS list.

    Returns:
        int: The validated `xn` value, within the range [0, 1].
    """

    if type(xn) == int and xn in range(MIN_XN_VALUE, MAX_XN_VALUE):
        return xn

    try:
        xn = int(input(QUESTIONS[question_index]))
    except:
        print("Invalid input. Please enter 0 or 1.")
        xn = FIRST_VALUE_XN

    return check_xn(xn, question_index)


def get_params():
    """This function obtains the Z(x) parameters required to enter the neuron.

    Returns:
        list[int]: Set of parameters for the MP neuron, which range between [0, 1].
    """

    z = []

    print(f"(Values: {VALUE_N}=no, {VALUE_Y}=yes)")
    for index in range(INIT_LOOP, len(QUESTIONS)):
        xn = check_xn(FIRST_VALUE_XN, index)
        z.append(xn)
    return z


def neuron_mp(z):
    """Neuron that decides whether we can go to the cinema or not.

    Args:
        z (list[int]): List of neuron parameters, which range between [0, 1].

    Returns:
        int: Returns 0 if we cannot go to the cinema, and 1 if we can go to the cinema.
    """
    
    if z[CINEMA_CLOSED_INDEX] == CINEMA_IS_CLOSED:
        return CANT_GO
    else:
        return CAN_GO if sum(z) >= TRESHOLD else CANT_GO


def main():
    """Main function where the complete logic of the MP neuron program is implemented.
    """

    print("Question: Can I go to the cinema?")
    
    neurona_params = get_params()
    answer = neuron_mp(neurona_params)

    if answer:
        print("Answer: I can go to the cinema.")
    else:
        print("Answer: I can't go to the cinema.")


if __name__ == "__main__":
    main()
