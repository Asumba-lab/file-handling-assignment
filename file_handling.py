def read_and_write_file():
    input_file = input("Enter the name of the file to read from: ")

    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        # Modify the lines - let's add line numbers and uppercase
        modified_lines = [f"{idx + 1}: {line.strip().upper()}\n" for idx, line in enumerate(lines)]

        # Write to new file
        with open("output.txt", 'w') as file:
            file.writelines(modified_lines)

        print("File has been read, modified, and written to 'output.txt'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError:
        print("Error: Unable to read or write the file.")

if __name__ == "__main__":
    read_and_write_file()
