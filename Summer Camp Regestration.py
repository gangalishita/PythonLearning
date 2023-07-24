class Students(object):
    # Defining each variable and initiating the class
    def __init__(self, name, grade, version, python_exp, command_exp, vector_overlay, system):
        self.name = name
        self.grade = grade
        self.version = version
        self.python_exp = python_exp
        self.command_exp = command_exp
        self.vector_overlay = vector_overlay
        self.system = system

    def self_introduction(self):
        # Creating an introduction using student data
        intro = "Hi, my name is %s and I'm in %s grade. I use %s version of python on a %s system." % (self.name, self.grade, self.version, self.system)
        # Checking for proficiency in Python and command line experience
        if self.python_exp <= 3:
            if self.command_exp <= 3:
                intro += "I am not that proficient in Python or in command line experience."
            elif 4 >= self.command_exp <= 7:
                intro += "I am not that proficient in Python and am somewhat proficient in command line experience."
            else:
                intro += "I am not that proficient in Python and am very proficient in command line experience."
        elif 4 >= self.python_exp >= 7:
            if self.command_exp <= 3:
                intro += "I am somewhat proficient in Python but inexperienced in command line experience."
            elif 4 >= self.command_exp <= 7:
                intro += "I am somewhat proficient in Python and in command line experience."
            else:
                intro += "I am somewhat proficient in Python and am very proficient in command line experience."
        elif 8 >= self.python_exp:
            if self.command_exp <= 3:
                intro += "I am very proficient proficient in Python but inexperienced in command line experience."
            elif 4 >= self.command_exp <= 7:
                intro += "I am very proficient proficient in Python and somewhat proficient in command line experience."
            else:
                intro += "I am very proficient proficient in Python and in command line experience."

        # Checking if they have previously created a vector overlay
        if self.vector_overlay is True:
            intro += "I have also created a vector overlay before."
        else:
            intro += "I also haven't created a vector overlay before."

        return intro


# List of students and their info
students = [
    Students("Alex", 12, 3.1, 6, 1, False, "Mac"),
    Students("Max", 10, 1.3, 4, 3, True, "Chrome"),
    Students("Leyla", 11, 4.2, 3, 3, False, "Windows"),
    Students("Eve", 10, 2.2, 9, 8, True, "Mac"),
    Students("Sam", 9, 1.1, 9, 2, True, "Windows"),
    Students("Madison", 11, 2.0, 8, 10, False, "Linus"),

]


# Printing an intro for each student and saving it to "registration.txt"
with open("registration.txt", "w") as my_file:
    for student in students:
        introduction = student.self_introduction()
        print(introduction)
        print()
        my_file.write((str(introduction) + '\n'))
