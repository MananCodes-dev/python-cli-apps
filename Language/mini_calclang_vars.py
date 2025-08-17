# MiniCalcLang V2 - Now with Variables!
# Day 20 Extension: Adding variable support to our mini language

import re

class MiniCalcLangV2:
    def __init__(self):
        self.variables = {}  # Store our variables
        self.history = []    # Store command history
    
    def tokenize(self, expression):
        """Break expression into tokens"""
        # Updated regex to handle variable names
        token_pattern = r'(\d+\.?\d*|[+\-*/()=]|[a-zA-Z_][a-zA-Z0-9_]*)'
        tokens = re.findall(token_pattern, expression)
        return [token.strip() for token in tokens if token.strip()]
    
    def is_variable(self, token):
        """Check if token is a valid variable name"""
        return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token) is not None
    
    def is_assignment(self, tokens):
        """Check if this is a variable assignment (contains =)"""
        return '=' in tokens
    
    def handle_assignment(self, tokens):
        """Handle variable assignment: x = 5"""
        try:
            eq_index = tokens.index('=')
            
            if eq_index == 0 or eq_index == len(tokens) - 1:
                raise ValueError("Invalid assignment syntax")
            
            # Get variable name (left side of =)
            var_name = tokens[eq_index - 1]
            if not self.is_variable(var_name):
                raise ValueError(f"Invalid variable name: {var_name}")
            
            # Get expression (right side of =)
            expr_tokens = tokens[eq_index + 1:]
            value = self.evaluate_expression(expr_tokens)
            
            # Store the variable
            self.variables[var_name] = value
            return f"{var_name} = {value}"
            
        except Exception as e:
            raise ValueError(f"Assignment error: {str(e)}")
    
    def substitute_variables(self, tokens):
        """Replace variable names with their values"""
        result = []
        for token in tokens:
            if self.is_variable(token):
                if token in self.variables:
                    result.append(str(self.variables[token]))
                else:
                    raise ValueError(f"Undefined variable: {token}")
            else:
                result.append(token)
        return result
    
    def evaluate_expression(self, tokens):
        """Evaluate mathematical expression"""
        # First substitute any variables
        tokens = self.substitute_variables(tokens)
        
        # Convert to string and evaluate
        expression = ' '.join(tokens)
        
        # Basic validation
        allowed_chars = set('0123456789+-*/(). ')
        if not all(c in allowed_chars for c in expression):
            raise ValueError("Invalid characters in expression")
        
        try:
            result = eval(expression)
            return round(result, 6) if isinstance(result, float) else result
        except Exception as e:
            raise ValueError(f"Math error: {str(e)}")
    
    def execute(self, command):
        """Execute a command in MiniCalcLang"""
        command = command.strip()
        
        # Add to history
        self.history.append(command)
        
        # Handle special commands
        if command.lower() == 'vars':
            return self.show_variables()
        elif command.lower() == 'clear':
            self.variables.clear()
            return "Variables cleared"
        elif command.lower() == 'history':
            return self.show_history()
        elif command.lower() in ['help', '?']:
            return self.show_help()
        
        # Parse the command
        tokens = self.tokenize(command)
        
        if not tokens:
            return "Empty command"
        
        try:
            # Check if it's an assignment
            if self.is_assignment(tokens):
                return self.handle_assignment(tokens)
            else:
                # It's an expression to evaluate
                result = self.evaluate_expression(tokens)
                return str(result)
                
        except Exception as e:
            return f"Error: {str(e)}"
    
    def show_variables(self):
        """Show all defined variables"""
        if not self.variables:
            return "No variables defined"
        
        result = "Variables:\n"
        for name, value in self.variables.items():
            result += f"  {name} = {value}\n"
        return result.strip()
    
    def show_history(self):
        """Show command history"""
        if not self.history:
            return "No history"
        
        result = "History:\n"
        for i, cmd in enumerate(self.history[-10:], 1):  # Show last 10
            result += f"  {i}. {cmd}\n"
        return result.strip()
    
    def show_help(self):
        """Show help information"""
        return """
MiniCalcLang V2 Commands:
  Basic math: 2 + 3, 10 * 5, (4 + 6) / 2
  Variables:  x = 5, y = x + 3, result = x * y
  Commands:   vars (show variables), clear (clear variables)
             history (show history), help (this help)
        """.strip()

def main():
    """Main REPL loop"""
    calc = MiniCalcLangV2()
    
    print("🔢 MiniCalcLang V2 - Now with Variables!")
    print("Type 'help' for commands, 'quit' to exit")
    print("-" * 40)
    
    while True:
        try:
            user_input = input(">>> ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye! 👋")
                break
            
            if user_input:
                result = calc.execute(user_input)
                print(result)
            
        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break
        except EOFError:
            print("\nGoodbye! 👋")
            break

def test_minicalclang():
    """Test the enhanced calculator"""
    calc = MiniCalcLangV2()
    
    test_commands = [
        "5 + 3",
        "x = 10",
        "y = 5",
        "x + y",
        "result = x * y",
        "result + 100",
        "vars",
        "z = x + y + result"
    ]
    
    print("🧪 Testing MiniCalcLang V2...")
    print("-" * 30)
    
    for cmd in test_commands:
        print(f">>> {cmd}")
        result = calc.execute(cmd)
        print(result)
        print()

if __name__ == "__main__":
    # Uncomment to run tests first
    # test_minicalclang()
    
    main()
