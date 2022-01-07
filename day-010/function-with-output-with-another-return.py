# Functions with Outputs
def format_name(f_name, l_name):
    """Take a first and last name and format it to
    return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_f_lastname = l_name.title()
    #print(f"{formated_f_name} {formated_f_lastname}")
    return f"{formated_f_name} {formated_f_lastname}"

formated_string = format_name(f_name=input("What is your first name? "),
l_name=input("What is your last name? "))
print(formated_string)

