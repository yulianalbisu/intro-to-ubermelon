log_file = open("um-server-01.txt")


def sales_reports(log_file): ##function to put the name of the file

    for line in log_file: ##in each line
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


sales_reports(log_file)
