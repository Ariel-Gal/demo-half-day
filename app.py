import ast

def process_data(user_input):
    ast.literal_eval(user_input)
    return True
