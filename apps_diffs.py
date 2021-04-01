import csv

original_files="/Users/muhammadaqib/Desktop/original_files.csv"
worked_files="/Users/muhammadaqib/Desktop/worked_files.csv"

def main():

    original_files_list=[]
    worked_files_list=[]

    with open(original_files, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            original_files_list.append(row[0])
        
        print("original files length: ", len(original_files_list))

    with open(worked_files, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            worked_files_list.append(row[0].lower())

        print("worked files length", len(worked_files_list))
        print("worked files unique length", len(set(worked_files_list)))


    undone_files=[]

    for original_file in original_files_list:
        if original_file.lower() not in worked_files_list:
            undone_files.append(original_file)

    print(undone_files)

    for element in worked_files_list:
        if worked_files_list.count(element) > 1:
            print(element)


if __name__ == "__main__":
    main()