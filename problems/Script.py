TEMPLATE_FILE = "template.md"
QUESTION_FILE = "question.txt"

# Read template string
template_string = open(TEMPLATE_FILE).read()

# Read question number and names
lines = open(QUESTION_FILE).readlines()

counter = 0
file_name = ""


for line in lines:
    line = line.replace("\n", "")
    if counter % 2 == 0:
        file_name = line
        file_name += ". "
    else:
        file_name += line
        text = open(file_name+".md", 'w')
        text.write("# ")
        text.write(file_name)
        text.write("\n")
        text.write(template_string)
        text.close()
    counter += 1
