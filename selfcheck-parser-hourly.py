""" Parse and aggregate the selfcheck Hourly XML file and output csv """

import csv
import untangle


# Identify fields for CSV output
#csv_header = ['Date', 'CheckoutSuccess', 'CheckoutFail', 'CheckinSuccess', 'CheckinFail', 'ReturnSuccess', 'ReturnFail', 'ReturnSessionStartCount','ItemSortedCount', 'ItemRejectedCount', 'RenewedSuccess','RenewedFail', 'UserLoginSuccess','UserLoginFail', 'LmsOfflineCount', 'PaymentSuccess', 'PaymentFailed', 'CoinboxEmptyCount', 'SuccessfulTransactions', 'FailedTransactions', 'CheckOutBookCount', 'TotalTransactions']
csv_header = ['Date', 'Time', 'Device Name', 'CheckoutSuccess', 'CheckoutFail', 'CheckinSuccess', 'CheckinFail', 'ReturnSessionStartCount', 'ReturnSuccess', 'ReturnFail', 'RenewedSuccess','RenewedFail', 'UserLoginSuccess','UserLoginFail', 'LmsOfflineCount', 'PaymentSuccess', 'PaymentFailed', 'CoinboxEmptyCount', 'SuccessfulTransactions', 'FailedTransactions', 'CheckOutBookCount', 'TotalTransactions']
output_fields = ['DeviceName', 'txtCheckoutOkCountRow1', 'txtCheckoutFailedCountRow1', 'txtCheckinOkCountRow1', 'txtCheckinFailedCountRow1', 'txtReturnSessionStartCountRow1', 'ItemSortedCount', 'ItemRejectedCount', 'txtRenewedOkCountRow1', 'txtRenewedFailedCountRow1', 'txtUserLoginCountRow1', 'txtUserLoginFailedCountRow1', 'txtLmsOfflineCountRow1', 'txtCashPaymentCountRow1', 'txtCashPaymentFailedCountRow1', 'txtCoinboxEmptyCountRow1', 'txtSuccessfulTransactionsCountRow1', 'txtFailedTransactionsCountRow1', 'MediaTypeTotal1', 'txtTotalRow1']
output_filename = 'selfcheck_hourly.csv'
# Open and Parse the xml file

try:
    obj = untangle.parse('data/201902_Hourly_AllDeviceStatistics.xml')
except  Exception:
    raise("Unable to parse input file")

# create output file & write header row
with open(output_filename, 'w') as output_file:
    csvwriter = csv.writer(output_file, dialect='excel')
    csvwriter.writerow(csv_header)

    # process each row and write to CSV

    # iterate on date
    for date_row in range(0, len(obj.Report.Tablix1.EventDateTimePaging_Collection.EventDateTimePaging)):
        # clear the list
        csv_output = ['null']*len(csv_header)
        csv_output[0] = obj.Report.Tablix1.EventDateTimePaging_Collection.EventDateTimePaging[date_row]['txtDateHeader']
        print("date: "+csv_output[0])
        # iterate on hour
        for  hour_row in range(0, len(obj.Report.Tablix1.EventDateTimePaging_Collection.EventDateTimePaging[date_row].EventDateTime_Collection.EventDateTime)):
            csv_output[1] = obj.Report.Tablix1.EventDateTimePaging_Collection.EventDateTimePaging[date_row].EventDateTime_Collection.EventDateTime[hour_row]['tbDateToggle']
            print("hour: "+csv_output[1])
            #iterate on station
            for station_row in range(2, len(obj.Report.Tablix1.EventDateTimePaging_Collection.EventDateTimePaging[date_row].EventDateTime_Collection.EventDateTime[hour_row].LocationFullName_Collection.LocationFullName.Details_Collection.Details)):
                # extract each element and place in csv output row
                for element in range(0, len(output_fields)):
                     field = output_fields[element]
                     csv_output[element+2] = obj.Report.Tablix1.EventDateTimePaging_Collection.EventDateTimePaging[date_row].EventDateTime_Collection.EventDateTime[hour_row].LocationFullName_Collection.LocationFullName.Details_Collection.Details[station_row][field]
                     print(str(element) + ": " + output_fields[element] + ": " + csv_output[element+2])
                csvwriter.writerow(csv_output)

output_file.close()



