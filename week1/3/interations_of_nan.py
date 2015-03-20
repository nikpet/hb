def iterations_of_nan_expand(expanded):
    if "" == expanded:
        return 0
    if "NaN" not in expanded:
        return False
    return expanded.count("Not a ")


if __name__ == '__main__':
    print(iterations_of_nan_expand(""))
    print(iterations_of_nan_expand("Not a NaN"))
    print(iterations_of_nan_expand("""Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN"""))
    print(iterations_of_nan_expand("Show these people!"))
