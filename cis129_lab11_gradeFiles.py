# CIS 129
# Ian Lochridge
# 5/2/25
# This program allows user to write and read grades from a txt and csv file

import csv  #import CSV Files

def writeGradeTxt():  #write the grades to txt file

    with open('grades.txt', mode='w') as grades:  #open new file 
        print()
        grade = int(input('Enter grade, -1 to end: '))  #take user inp
        grades.write(f'{grade}\n')  #write grade to txt file

        while grade != -1:  #sentinel controlled while loop
            grade = int(input('Enter grade, -1 to end: '))  #take user inp
            if grade != -1:  #block -1 from being written
                grades.write(f'{grade}\n')  #write grade to txt file


def readGradeTxt():  #read the grades from txt file

    total = 0  #total of grades
    count = 1  #num of grades

    with open('grades.txt', mode='r') as grades:  #open file 
        print()
        for record in grades:  #iterate through records
            print(f'Grade ({count}): {record}')  #print record
            total += int(record)  #sum record
            count += 1  #update count
        
        print(f'Total: {total}')  #print total
        print(f'Count: {count-1}')  #print count
        print(f'Average: {round((total/(count-1)), 2)}')  #print avg rounded to 2 pts


def writeGradeCsv():  #write grades & student info to csv

    with open('grades.csv', mode='w', newline='') as grades:  #open new csv
        print()
        writer = csv.writer(grades)  #establish writer as csv.writer
        exitValue = "y"  #establish sentinel

        fName = input('Enter student\'s first name: ')  #take user input
        lName = input('Enter student\'s last name: ')  #take user input
        examGrade1 = int(input('Enter exam 1: '))  #take user input
        examGrade2 = int(input('Enter exam 2: '))  #take user input
        examGrade3 = int(input('Enter exam 3: '))  #take user input
        writer.writerow([fName, lName, examGrade1, examGrade2, examGrade3])  #write csv file

        exitValue = input('Enter another student (y/n): ')  #prompt sentinel

        while exitValue != 'n':  #sentinel controlled while loop
            print()
            fName = input('Enter student\'s first name: ')  #take user input
            lName = input('Enter student\'s last name: ')  #take user input
            examGrade1 = int(input('Enter exam 1: '))  #take user input
            examGrade2 = int(input('Enter exam 2: '))  #take user input
            examGrade3 = int(input('Enter exam 3: '))  #take user input
            writer.writerow([fName, lName, examGrade1, examGrade2, examGrade3])  #write csv file
            exitValue = input('Enter another student (y/n): ')  #prompt sentinel

    with open('grades.csv', 'r', newline='') as grades:  #open csv file to read
        print()
        reader = csv.reader(grades)  #establish reader as csv.reader
        for record in reader:  #iterate through records
            print(f'{record}')  #print record
            print()

def main():
    writeGradeTxt()
    readGradeTxt()
    writeGradeCsv()

main()
