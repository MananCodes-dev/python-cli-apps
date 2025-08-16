import re 

#Tokenzer (lexer)
def tokenize(expression):
    tokens = re.findall(r'\d+|[+\-*/()]', expression)
    return tokens

#Parser and Evaluator
def evaluate(tokens):
    expression = "".join(tokens)
    try:
        return eval(expression) # Python does the heavy lifting here
    except Exception as e:
        return f"Error: {e}"
    
# REPL (Read-Eval-Print Loop)
print("Welcome to MiniCalc! Type 'exit' to quit.")
while True:
    expr = input("Enter an expression: ")
    if expr.lower() == 'exit':
        print("Exiting MiniCalc. Goodbye!")
        break
    tokens  = tokenize(expr)
    result = evaluate(tokens)
    print(f"Result: {result}")
print("Thanks for using MiniCalc!")
