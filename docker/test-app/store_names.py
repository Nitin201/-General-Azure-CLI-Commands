def load_names():
    try:
        with open("names.txt", "r") as file:
            names = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        names = []
    return names

def store_names():
    names = load_names()

    print("Enter names (type 'done' to finish):")
    while True:
        name = input("Enter a name: ")
        if name.lower() == "done":
            break
        names.append(name)

    # Save the names to the file
    with open("names.txt", "w") as file:
        for name in names:
            file.write(name + "\n")

    print("\nYou have entered the following names:")
    for idx, n in enumerate(names, start=1):
        print(f"{idx}. {n}")

if __name__ == "__main__":
    store_names()
