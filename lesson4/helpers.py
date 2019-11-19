# ============================================================================ #
# A set a functions to help us inspect a function's inputs
# ============================================================================ #
def print_banner(n):
    print("*" * n)

# ---------------------------------------------------------------------------- #
def print_arg(name, value, end="\n"):
    print(name, "=", value, end=end)

# ---------------------------------------------------------------------------- #
def show_input(func_name, arg_names, arg_values):
    
    # a string contains the list of arg names seperated by ", "
    arg_string = ", ".join(arg_names)
    
    # our function "signiture" as a string
    func_sig = func_name + "(" + arg_string + ")"
    
    # print the functionc call signature, e.g. arg_name(input1, input2...)
    print(func_sig + ":", end=" ")
    
    # print the names and values of each input (except the last one), followed
    # by a ", "
    for k in range(len(arg_names)-1):
        print_arg(arg_names[k], arg_values[k], end=", ")


    # print the last arg (with a trailing newline)
    print_arg(arg_names[-1], arg_values[-1])
    

    # construct a filled function signiture, where the variable names are
    # replaced by their actual values
    filled_sig = func_sig
    for k in range(len(arg_names)):
        filled_sig = filled_sig.replace(arg_names[k], str(arg_values[k]))
        
    
    return filled_sig
    
# ---------------------------------------------------------------------------- #
def show_func(func, arg_names, arg_values):
    
    # print our banner
    print_banner(5)
    
    sig = show_input(func.__name__, arg_names, arg_values)
    
    # do the calculation
    result = func(*arg_values)
    
    # display the result
    print(sig, "=", result)
    
    # show the ending banner
    print_banner(5)
    
    # return the result
    return result
    
# ---------------------------------------------------------------------------- #