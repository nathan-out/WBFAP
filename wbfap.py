import sys, os, json

def print_banner():
    print(
        """
██╗    ██╗██████╗ ███████╗ █████╗ ██████╗ 
██║    ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗
██║ █╗ ██║██████╔╝█████╗  ███████║██████╔╝
██║███╗██║██╔══██╗██╔══╝  ██╔══██║██╔═══╝ 
╚███╔███╔╝██████╔╝██║     ██║  ██║██║     
 ╚══╝╚══╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝     

by nathan.out

        """
    )

def get_dirs_from_path(path):
    elements = os.listdir(path)
    return [element for element in elements if os.path.isdir(os.path.join(path, element))]

def get_files_from_path(path):
    elements = os.listdir(path)
    return [element for element in elements if not os.path.isdir(os.path.join(path, element))]

def parse_artifacts(abs_path, user, artifacts_location):
    if os.path.exists(abs_path+'Users\\'+user+'\\AppData\\Local\\Google\\Chrome\\'):
        print('Chrome found!')

        print('Parsing Chrome artifacts...')
        for k,v in artifacts_location.items():
            print(k,':')
            for artifact_location in v:
                artifact_path = abs_path+'Users\\'+artifact_location.replace('%USERPROFILE%', user).replace('<Profile>', 'Default')
                if os.path.exists(artifact_path):
                    print('\t\t', artifact_path)
                    if not os.path.isdir(artifact_path):
                        print('FILE!')
                        # CONTINUER ICI, SQLITE3 à parser -> création d'une interface web ???
                    else:
                        elements = get_elements_from_path(artifact_path, '')


"""
    Get all elements from a given path in a string list. 
    If element_type = 'both' the function will return both directories and files.
    If element_type = 'dir' or 'file' the function will only returns the given type.
    Default is 'both'.
"""
def get_elements_from_path(path, element_type = 'both'):
    elements = os.listdir(path)
    if element_type == 'both': return elements
    if element_type == 'dir': return get_dirs_from_path(path)
    if element_type == 'file': return get_files_from_path(path)

if __name__ == "__main__":
    print_banner()
    #abs_path = input("Please provide the C:\ ABSOLUTE PATH of the system you want investigate on: ")
    abs_path = "D:\Forensic\c119-Malicious-Offer\challenge"
    print(abs_path)

    if abs_path[-1] != '\\':
        abs_path += "\\"
    
    ### user to investigate on
    users = get_elements_from_path(abs_path+'Users\\', element_type = 'dir')
    print("USERS: \n")
    i = 0
    for user in users:
        print("\t- ["+str(i)+"] "+user)
        i += 1
    user_indice = int(input('Please select a user you want investigate on: '))
    user = users[user_indice]
    print('User', user, 'is selected.\n\n')

    ### browsing artifacts
    f = open('artifacts_location.json')
    artifacts_location = json.load(f)
    parse_artifacts(abs_path, user, artifacts_location)