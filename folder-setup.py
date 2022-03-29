import os

# Creates 3D Graphics directory structure in current directory:
# ---
# Scene Name
#   | Renders
#   | Exports
#   | Scene Files

# Currently only tested with Windows errors

try:
    ## User Input
    while True:
        proj_name = input("Enter Project Name: ")
        if not proj_name.isalnum:
            print('\nEnter alphanumeric characters only\n')
            continue
        break

    ## Folder Creation
    try:
        os.makedirs(proj_name)
    except FileExistsError:
        print('\nThe folder "%s" already exists\n' % proj_name)
        exit()
    except FileNotFoundError or NotADirectoryError:
        print('\nERROR:\nname "%s" is invalid\n' % proj_name)
        exit()

    os.chdir(proj_name)
    os.makedirs('Renders')
    os.makedirs('Exports')
    os.makedirs('Scene Files')
    print("Done!")
except KeyboardInterrupt:
    print('\nExiting...\n')