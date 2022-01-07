# Functions with Outputs
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_f_lastname = l_name.title()
    #print(f"{formated_f_name} {formated_f_lastname}")
    return f"{formated_f_name} {formated_f_lastname}"

formated_string = format_name(f_name="DArwIn", l_name="vElasco")
print(formated_string)