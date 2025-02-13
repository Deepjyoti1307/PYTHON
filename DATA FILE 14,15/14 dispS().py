#Write a function dispS() in Python to read from text file “Data.TXT” and display those lines which starts with “S”

def dispS():
    try:
        with open("Data.TXT", "r") as file:
            for line in file:
                if line.strip().startswith('S'):
                    print(line.strip())
    except FileNotFoundError:
        print("Error: Data.TXT file not found")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    dispS()