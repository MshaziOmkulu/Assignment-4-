def modify_content(content):
    # Example modification: make all text uppercase
    return content.upper()

def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            modified = modify_content(content)

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as file:
            file.write(modified)

        print(f"Modified content written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Cannot read the file.")

if __name__ == "__main__":
    main()
