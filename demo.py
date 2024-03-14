output_file = open("demo.py", "w")
with open("oop.py", "r") as scan:
    output_file.write(scan.read())
    output_file.close()
