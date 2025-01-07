def get_input(prompt, upper=False):
    return input(prompt).strip() if not upper else input(prompt).strip().upper()
        
def get_valid_input(prompt, validantions, upper_choice=False):
    while True:
        value = validate_input(
            get_input(prompt, upper=upper_choice),
            validantions
        )
        if value != None:
            return value

def validate_input(value, validations):
    errors = False
    for validation, error_message in validations:
        if not validation(value):
            print(error_message)
            errors = True
    return value if not errors else None
