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

def display_title(text):
    l = len(text)
    upper_line, mid_line, lower_line = '\n+', '|  ', '+'
    for i in range(l+4):
        upper_line += '-'
        lower_line += '-'
    mid_line += text+'  |'
    upper_line += '+'
    lower_line += '+'
    print(upper_line, mid_line, lower_line, sep='\n')

def parse_artifacts(abs_path, user, artifacts_location):
    if os.path.exists(abs_path+'Users\\'+user+'\\AppData\\Local\\Google\\Chrome\\'):
        print('Chrome found!')

        print('\nPARSING CHROME ARTIFACTS...\n')
        for k,v in artifacts_location.items():
            display_title(k)
            for artifact_location in v:
                artifact_path = abs_path+'Users\\'+artifact_location.replace('%USERPROFILE%', user).replace('<Profile>', 'Default')
                if os.path.exists(artifact_path):
                    print('\t', artifact_path)
                    if not os.path.isdir(artifact_path):
                        parse_database(artifact_path, user, k)
                    else:
                        elements = get_elements_from_path(artifact_path, '')

"""
    Parse database provided. Export it into a csv file.
    user parameter and artifact_name are only for export naming.
"""
def parse_database(db_path, user, artifact_name):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # listing all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # default sqlite tables, useless for us
    useless_tables = ['sqlite_master', 'sqlite_sequence']

    # Affichage de la liste des tables
    for table in tables:
        if table[0] not in useless_tables:
            # here table to export
            datas = cursor.execute('SELECT * FROM '+table[0]+';').fetchall()
            # create outputs dir
            import os
            export_folder = 'EXPORT_'+user
            if not os.path.exists(os.path.join(export_folder, artifact_name)): os.makedirs(os.path.join(export_folder, artifact_name))
            filename = os.path.join(os.path.join(export_folder, artifact_name), user+'_'+artifact_name+'_'+table[0]+'.csv')
            
            # avoid empty files
            if datas != []:
                with open(filename, 'w', encoding='utf-8') as out:
                    # write columns name
                    col = [desc[0] for desc in cursor.description]
                    header = ''
                    for i in range(len(col)):
                        if i==len(col)-1: header+=col[i]+'\n'
                        else: header+=col[i]+','
                    out.write(header)

                    # write datas
                    for line in datas:
                        formated_line = ','.join(map(str, line))
                        out.write(f'{formated_line}\n')
    conn.close()

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
    print('codé en dur A ENLEVER ENSUITE', abs_path)

    if abs_path[-1] != '\\':
        abs_path += "\\"
    
    ### user to investigate on
    users = get_elements_from_path(abs_path+'Users\\', element_type = 'dir')
    display_title('USER FOUND')
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
    display_title('Parsing completed!')