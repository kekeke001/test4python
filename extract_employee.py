import xlsx_utils

#
def get_employee_data():
    return xlsx_utils.extract_columns(file_path=r'C:\Users\h\PycharmProjects\xiajie\test\resources\employee.xlsx',
                    sheet_name='Sheet1',
                    column_name_str='Name,HW_PM',
                    extract_to='')