import re

def convert_to_latex(expression):
    # Replace common functions and operators with their LaTeX equivalents
    replacements = {
        #'exp': r'e^{',
        'cos': r'\cos',
        'sin': r'\sin',
        'tan': r'\tan',
        'cot': r'\cot',
        '*': r'\cdot ',
        '^': r'^',
        '(': r'(',
        ')': r')',
        'y\'': r"y'",
        'y\'\'': r"y''"
    }
    
    # Handle the exponentiation fix for the exp function
    #def fix_exp(match):
    #    return r'e^{' + match.group(1) + r'}'

    # Use regex to find exp(x) and replace it with e^{x}
    #expression = re.sub(r'exp\(([^)]+)\)', fix_exp, expression)

    # Perform replacements
    for old, new in replacements.items():
        expression = expression.replace(old, new)
    
    return expression

def convert_to_latex2(expression):
    # Replace common functions and operators with their LaTeX equivalents
    replacements = {
        r'\bexp\((.*?)\)': r'e^{\1}',  # Match exp(x) and replace with e^{x}
        r'\bcos\((.*?)\)': r'\\cos{\left(\1\right)}',
        r'\bsin\((.*?)\)': r'\\sin{\left(\1\right)}',
        r'\btan\((.*?)\)': r'\\tan{\left(\1\right)}',
        r'\bcot\((.*?)\)': r'\\cot{\left(\1\right)}',
        r'\*': r' \cdot ',
        r'\^': r'^{',
        r'\(': r'\\left(',
        r'\)': r'\\right)',
        r"y\'\'": r"y''",
        r"y\'": r"y'"
    }

    # Perform replacements using regex for more complex patterns
    for pattern, replacement in replacements.items():
        expression = re.sub(pattern, replacement, expression)

    return expression


def convert_to_latex3(expression):
    # Replace common functions and operators with their LaTeX equivalents
    replacements = {
        r'\bexp\(([^)]+)\)': r'e^{\1}',   # Match exp(x) and replace with e^{x}
        r'\bcos\(([^)]+)\)': r'\\cos{\left(\1\right)}',
        r'\bsin\(([^)]+)\)': r'\\sin{\left(\1\right)}',
        r'\btan\(([^)]+)\)': r'\\tan{\left(\1\right)}',
        r'\bcot\(([^)]+)\)': r'\\cot{\left(\1\right)}',
        r'\bsec\(([^)]+)\)': r'\\sec{\left(\1\right)}',
        r'\bcsc\(([^)]+)\)': r'\\csc{\left(\1\right)}',
        r'\*\*': r'^',                   # Replace ** with ^
        r'\*': r' \\cdot ',              # Replace * with \cdot
        r'\(': r'\\left(',               # Replace ( with \left(
        r'\)': r'\\right)',              # Replace ) with \right)
        r"y\'\'": r"y''",                # Replace y'' with y''
        r"y\'": r"y'",                   # Replace y' with y'
        r'(\d+)\^(\d+)': r'\1^{\2}',     # Replace 2^3 with 2^{3}
        r'(\d+)\s+(\d+)': r'\1 \cdot \2' # Replace space between numbers with \cdot
    }

    # Perform replacements using regex for more complex patterns
    for pattern, replacement in replacements.items():
        expression = re.sub(pattern, replacement, expression)

    return expression