report_file = open("um-server-01.txt")##


def sales_reports(report_file): ##the definition of the function is the file

    for line in report_file: ##for the line in the text file
        line = line.rstrip()## line is line strip is removing space in right
        day = line[0:3]## day is the line from first to third char
        if day == "Mon":## if the day is mon. monday
            print(line)## print the line


sales_reports(report_file)## run the sales report of monday
