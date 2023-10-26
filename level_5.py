# Short Hand If-else
a = 10
print("Zero") if a == 0 else print("Not Zero") if a == 5 else print("Not 5")

# Enumerate
# It gives the index and value both 

a = [34,67,23,87,12,98,38,45,76]

# start navigating from index 0
for index, elements in enumerate(a):
    print(index, end=" , ")
    print(elements)
print("-----------------------------------------")
# start navigating from index 5
for index, elements in enumerate(a, start=5):
    print(index, end=" , ")
    print(elements)
    
# Some Important Commands

# Create a virtual environment
# python -m venv myEnv

# Activate the virtual environment (Windows)
# activate myEnv

# Deactivate the virtual environment
# deactivate

# Output the list of installed packages and their versions to a file
# pip freeze > requirements.txt

# Install the packages listed in the requirements.txt file
# pip install -r requirements.txt

# These commands are very useful when working on a project with a team