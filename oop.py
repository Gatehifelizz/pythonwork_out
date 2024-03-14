def main():
    print("Hello")
    print("welcome Gatehi")


if __name__ == "__main__":
    main()

# import filecmp

# f1 = "./oop1.py"
# f2 = "./oop.py"

# shallow comparison
# result = filecmp.cmp(f1, f2)
# print(result)
# deep comparison
# result = filecmp.cmp(f1, f2, shallow=False)
# print(result)


# reading files
f1 = open("oop.py", "r")
f2 = open("oop1.py", "r")

f1_data = f1.readlines()
f2_data = f2.readlines()
i = 0
for line1 in f1_data:
    i += 1
    for line2 in f2_data:
        # matching line1 from both files
        if line1 == line2:
            print("line", i, ":Identical")
        else:
            print("line", i, ":")
            # else print that line from both files
            print("\tfile1 1:", line1, end='')
            print("\tfile1 2:", line2, end='')
        break
        f1.close()
        f2.close()
