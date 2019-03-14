""" Parse and aggregate the selfcheck Daily XML file and output csv """

import csv
import untangle


# Identify fields for CSV output
#csv_header = ['Date', 'CheckoutSuccess', 'CheckoutFail', 'CheckinSuccess', 'CheckinFail', 'ReturnSuccess', 'ReturnFail', 'ReturnSessionStartCount','ItemSortedCount', 'ItemRejectedCount', 'RenewedSuccess','RenewedFail', 'UserLoginSuccess','UserLoginFail', 'LmsOfflineCount', 'PaymentSuccess', 'PaymentFailed', 'CoinboxEmptyCount', 'SuccessfulTransactions', 'FailedTransactions', 'CheckOutBookCount', 'TotalTransactions']
csv_header = ['Date', 'CheckoutSuccess', 'CheckoutFail', 'CheckinSuccess', 'CheckinFail', 'ReturnSessionStartCount', 'ReturnSuccess', 'ReturnFail', 'RenewedSuccess','RenewedFail', 'UserLoginSuccess','UserLoginFail', 'LmsOfflineCount', 'PaymentSuccess', 'PaymentFailed', 'CoinboxEmptyCount', 'SuccessfulTransactions', 'FailedTransactions', 'CheckOutBookCount', 'TotalTransactions']

output_fields = ['tbDateToggle', 'CheckoutOKCount', 'CheckoutFailedCount1', 'CheckinOKCount', 'CheckinFailedCount', 'ReturnSessionStartCount', 'ItemSortedCount2', 'ItemRejectedCount2', 'RenewedOKCount','RenewedFailedCount', 'UserLoginCount','UserLoginFailedCount', 'LmsOfflineCount', 'PaymentCount', 'PaymentFailedCount', 'CoinboxEmptyCount', 'SuccessfulTransactions', 'FailedTransactions', 'CheckOutBookCount', 'TotalTransactions']
output_filename = 'selfcheck.csv'
# Open and Parse the xml file

try:
    obj = untangle.parse('data/201902_Daily_AllDeviceStatistics.xml')
except  Exception:
    raise("Unable to parse input file")

# create output file & write header row
with open(output_filename, 'w') as output_file:
    csvwriter = csv.writer(output_file, dialect='excel')
    csvwriter.writerow(csv_header)

    # process each row and write to CSV

    for row in range(0, len(obj.Report.Tablix1.EventDateTimePaging_Collection.EventDateTimePaging.EventDateTime_Collection.EventDateTime)):
        # clear the list
        csv_output=['null']*len(output_fields)
        # extract each element and place in csv output row
        for element in range(0, len(output_fields)):
             field = output_fields[element]
             csv_output[element] = obj.Report.Tablix1.EventDateTimePaging_Collection.EventDateTimePaging.EventDateTime_Collection.EventDateTime[row][field]
             print(str(element) + ": " + output_fields[element] + ": " + csv_output[element])
        csvwriter.writerow(csv_output)

output_file.close()



