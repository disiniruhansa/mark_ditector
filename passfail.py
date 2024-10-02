# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20222171
# Date: 14.12.2023

#Importing graphics to draw the graph
from graphics import GraphWin, Rectangle, Point, Text, Line

#Checking whether the user is a staff or a student
while True:
    try:
        category = int(input("\nAre you a staff or a student? (staff = 1, student = 2):"))

        if (category != 1 and category != 2):
            print("Enter 1 or 2")
            continue
        else:
            break
    except ValueError:
            print("Integer required. Enter 1 or 2")


#Function to get the input
def asking_inputs():
    while True:
        try:
            #Getting the inputs
            PASS = int(input("\nPlease enter your credits at pass: "))
            if PASS not in range(0,121,20):
                print("Out of range")
                continue
                
            DEFER = int(input("Please enter your credits at defer: "))
            if DEFER not in range(0,121,20):
                print("Out of range")
                continue
                
            FAIL = int(input("Please enter your credits at fail: "))
            if FAIL not in range(0,121,20):
                print("Out of range")
                continue
            
            #Error messages for the inputs
            if PASS + DEFER + FAIL != 120:
                print("Total incorrect. Please enter again.")
                continue
                
            return PASS, DEFER, FAIL

        except ValueError:
            print("Integer required. Please enter again.")


#Function to checking the category of the entered inputs          
def progression_outcome(credit_volume):
    #Definning all the data using list
    progress = [(120, 0, 0)]
    
    module_trailer = [(100, 20, 0), (100, 0, 20)]

    module_retriever = [(80,40,0),(80,20,20),(80,0,40),(60,60,0),(60,40,20),
                    (60,20,40),(60,0,60),(40,80,0),(40,60,20),(40,40,40),
                    (40,20,60),(20,100,0),(20,80,20),(20,60,40),(20,40,60),
                    (0,120,0),(0,100,20),(0,80,40),(0,60,60)]

    exclude = [(40,0,80),(20,20,80),(20,0,100),(0,40,80),(0,20,100),(0,0,120)]
    
    #Recognizing the right progression outcome for inputs
    if credit_volume[0] == progress[0]:
        return "Progress"
    
    for item in module_trailer:
        if item == credit_volume[0]:
            return "Progress (Module trailer)"

    for item in module_retriever:
        if item == credit_volume[0]:
            return "Module retriever"

    for item in exclude:
        if item == credit_volume[0]:
            return "Excluded"
        
    return "Unknown outcome" 


#Function for creating the histrogram
def create_histogram(progress_count, trailer_count, retriever_count, excluded_count):
    win = GraphWin("Progression Histogram", 700, 500)

    downLine = Line(Point(10,300),Point(495,300))
    downLine.setArrow("both")
    downLine.setWidth (4)
    downLine.draw(win)

    # Function to create a bar in the histogram
    def create_bar(category, count, x, color):
        height = count * 30
        bar = Rectangle(Point(x, 300), Point(x + 50, 300 - height))
        bar.setFill(color)
        bar.draw(win)

        #Writing the count on top of each bar
        count_text = Text(Point(x + 25, 300 - height - 10), str(count))
        count_text.setSize(11)
        count_text.draw(win)

        #Writing the name of each bar
        category_text = Text(Point(x + 25, 315), category)
        category_text.setSize(12)
        category_text.setStyle("bold")
        category_text.draw(win)

    #Designing each bar and it's colour
    create_bar("Progress", progress_count, 50, "green")
    create_bar("Trailer", trailer_count, 150, "red")
    create_bar("Retriever", retriever_count, 250, "yellow")
    create_bar("Excluded", excluded_count, 350, "blue") 

    #writing the Heading
    my_heading = Text(Point(200, 40), 'Histogram results')
    my_heading.setSize(22)
    my_heading.setStyle("bold")
    my_heading.setFace("helvetica") 
    my_heading.draw(win)
        
    #Display total number of students
    total_students = progress_count + trailer_count + retriever_count + excluded_count
    total_text = Text(Point(120, 350), f"{total_students} outcomes in total.")
    total_text.setSize(14)
    total_text.setTextColor("grey")
    total_text.setStyle("bold")
    total_text.draw(win)

    win.getMouse()
    win.close()


#Opens the file in write mode 
def save_to_file(progression_data, filename='progression_data.txt'):
    with open(filename, 'w') as file:
        file.write("\nAll entered inputs and their progression outcomes:\n")
        for item in progression_data:
            file.write(f"\n{item[1]} - {item[0]}")
            

#Opens the file in reading mode
def load_from_file(filename='progression_data.txt'):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")
        


#THis is the main function to run this whole code        
def main():
    #Initializing the variables
    progress_count = 0
    trailer_count = 0
    retriever_count = 0
    excluded_count = 0
    progression_data = []

    while True:
        #Adding the inputs to a list
        PASS, DEFER, FAIL = asking_inputs()
        credit_volume = [(PASS, DEFER, FAIL)]

        outcome = progression_outcome(credit_volume)
        print("\nProgression outcome :",outcome)

        progression_data.append((credit_volume, outcome))

        #Counting the each counts
        if outcome == "Progress":
            progress_count += 1
        elif outcome == "Progress (Module trailer)":
            trailer_count += 1
        elif outcome == "Module retriever":
            retriever_count += 1
        elif outcome == "Excluded":
            excluded_count += 1

        #Askinh whether they want to continue or not
        option = input("\nWould you like to enter another set of data?\n"
                       "Enter 'y' for yes or 'q' to quit and view results: ")

        if option.lower() == 'y':
            continue
        elif option.lower() == 'q':
            break
        else:
            option = input("Enter 'y' or 'q':")
            continue

    #Printing all the enterted inputs in idle 
    print("\nAll entered inputs and their progression outcomes:")
    for item in progression_data:
        print(f"{item[1]} - {item[0]}")
        
    if (category == 1):
        
        #Calling function to create histrogram
        create_histogram(progress_count, trailer_count, retriever_count, excluded_count)

        #Calling function to save the text file
        save_to_file(progression_data)

        print("\nSaved progression data from the file:")
        load_from_file()


#Calling the main function
main()
