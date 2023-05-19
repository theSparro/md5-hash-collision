import hashlib
import pprint

# Initialize hash table
hashtable = {}

# Function to add key and value to the hash table
def add(key, value):
    # Check if the key is already present
    if key in hashtable:
        print("Key already present")
    else:
        # Add the key and value to the hash table
        hashtable[key] = value
        print("Added successfully")


# Function to check for collision of hash values
def checkCollision(input, hash):
    # Check if the value is already present in hashtable
    collision = False
    key_collisions = []
    for key, value in hashtable.items():
        if value == hash and key != input:
            collision = True
            key_collisions.append(key)
    if collision == False:
        print("No collision detected\n")
    else:
        print("Collision detected with: ", key_collisions)
        print("both files have the same hash value: ", hash, '\n')


# Function to compute the MD5 hash for a string
def computeHash(input_data, object_type):
    # Create a MD5 hash object
    md5 = hashlib.md5()
    if object_type == "file":
        # Open the file for reading in binary mode
        with open(input_data, 'rb') as file:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: file.read(4096),b""):
                md5.update(byte_block)
            return md5.hexdigest()
    elif object_type == "string":
        # Update the hash string
        md5.update(input_data.encode('utf-8'))
        # Return the hexadecimal representation of hash
        return md5.hexdigest()


# Function to determineinput type (file/string)
def checkInput(input_data):
    # Try to open as a file
    try:
        with open(input_data, 'rb') as file:
            return "file"
    except IOError:
        return "string"


while True:
    # Ask the user for input
    print("Enter the file name or string to compute the hash value: ")
    input_data = input()
    # Check the input type
    input_type = checkInput(input_data)
    # Compute the hash
    hash = computeHash(input_data, input_type)
    print("The hash value is: ", hash)
    # Add the key and value to the hash table
    add(input_data, hash)
    # Check for collision
    checkCollision(input_data, hash)
    # Print the hash table
    print("Hash Table: ")
    pprint.pprint(hashtable)
    print('\n')
