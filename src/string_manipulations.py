


if __name__ == "__main__" : 
    print(f"Hello world. Lets check out some string manipulation capabilities of Python 3.")

    # https://www.kaggle.com/code/colinmorris/strings-and-dictionaries/tutorial
    single_quote_string = 'Pluto is a planet'
    double_quote_string = "Pluto is a planet"
    another_string = 'My dog is named "Pluto"'
    
    # broken_string_due_to_wrong_use_of_quotes = 'Pluto's a planet!'
    this_is_ok = 'Pluto\'s a planet!'
    # SyntaxError: unterminated string literal

    print(single_quote_string == double_quote_string)
    print( single_quote_string == another_string)

    newline_helloworld = "hello\nworld"
    triplequoted_hello = """hello
world"""
    print(newline_helloworld)
    print( newline_helloworld == triplequoted_hello)

    # You could change the way print behaves. Wow
    print("hello", end='')
    print("pluto")

    # Strings are like lists (read arrays). 
    # And lists allow indexing 
    # As well as a slicing. You could have a slice of the list.
    name = "I have a long name"
    print (name)
    print (name[0])
    print ( name[1:5])
    print ( name[-3:])
    print ( len(name))

    # Some special string functions
    crazy = "CrAzY"
    print(f"Crazy string { crazy}")
    print(f"Upper case { crazy.upper()}")
    print(f"Lower case { crazy.lower()}")
    find = "z"
    print(f"Index of {find} is { crazy.index(find)}")
    