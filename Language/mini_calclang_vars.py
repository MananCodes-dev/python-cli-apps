import re

print("🧮 MiniCalcLang v0.2 — variables enabled. Type 'exit' to quit.")

# Symbol table (environment)
ENV = {}

IDENT = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')

def eval_expr(expr: str):
    """
    Safely evaluate arithmetic with variables defined in ENV.
    Allowed: + - * / ( ) numbers and identifiers that exist in ENV.
    """
    # Find all tokens that look like identifiers; ensure they exist in ENV
    for name in set(IDENT.findall(expr)):
        # skip if it's a Python keyword we don't use, but here we only allow identifiers
        if name not in ENV:
            # If someone types just 'let' or similar by mistake, treat as undefined
            raise NameError(f"Undefined variable '{name}'")

    # Evaluate with no builtins; only ENV variables are available as names
    return eval(expr, {"__builtins__": None}, ENV)

def handle_line(line: str):
    line = line.strip()
    if not line:
        return

    # Match: let x = expr   OR   x = expr
    m = re.match(r'^(?:let\s+)?([A-Za-z_]\w*)\s*=\s*(.+)$', line)
    if m:
        name, expr = m.group(1), m.group(2)
        try:
            value = eval_expr(expr)
            ENV[name] = value
            print(f"{name} = {value}")
        except Exception as e:
            print("Error:", e)
        return

    # Otherwise treat it as an expression to evaluate
    try:
        value = eval_expr(line)
        print("=>", value)
    except Exception as e:
        print("Error:", e)

def repl():
    while True:
        try:
            line = input(">> ")
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break
        if line.lower().strip() == "exit":
            break
        handle_line(line)

if __name__ == "__main__":
    repl()
