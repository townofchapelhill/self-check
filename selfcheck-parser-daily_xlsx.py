""" Parse and aggregate the selfcheck Daily excel file and output csv """

from openpyxl import load_workbook
import re
import csv

# import access keys and locations
# import secrets
# import filename_secrets


# Identify fields for CSV output
csv_header = ['Date', 'CheckoutSuccess', 'CheckoutFail', 'CheckinSuccess', 'CheckinFail', 'ReturnSessionStartCount', 'ReturnSuccess', 'ReturnFail', 'RenewedSuccess','RenewedFail', 'UserLoginSuccess','UserLoginFail', 'LmsOfflineCount', 'PaymentSuccess', 'PaymentFailed', 'CoinboxEmptyCount', 'SuccessfulTransactions', 'FailedTransactions', 'TotalTransactions']

output_fields = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19]
output_filename = 'data/selfcheck-Daily-2019-05-05.csv'

# Open the workbook and set up access to the worksheet
try:
    self_check_input_daily = os.getenv("SelfCheck_input_filename")
    print("Input Filename: " + self_check_input_daily)
    self_check_output_daily = os.getenv("SelfCheck_output_filename")
    print("Output Filename: " + self_check_output_daily)

    workbook  = load_workbook(filename = self_check_input_daily, read_only=True)
    worksheet = workbook.active
    worksheet_list = list(worksheet.values)
except  Exception:
    raise("Unable to parse input file")

# create output file & write header row
with open(self_check_output_daily, 'w') as output_file:
    csvwriter = csv.writer(output_file, dialect='excel')
    csvwriter.writerow(csv_header)


    # Select each row aggregate with a date (dd month yyyy) in the first field (daily total)
    for row in range(0, len(worksheet_list)):
        # clear the list
        csv_output=['null']*len(output_fields)
        # process each row and write to CSV
        if worksheet_list[row][0] == "Total":
            # Final line of spreadsheet
            break
        match = re.match('^\d+\s\w+\s+\d{4}', worksheet_list[row][0])
        if match:
            for element in range(0, len(output_fields)):
                csv_output[element] = worksheet_list[row][output_fields[element]]
            csvwriter.writerow(csv_output)

    # close and terminate
    output_file.close()
