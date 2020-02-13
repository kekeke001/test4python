import extract_employee
import extract_health_report
import xlsx_utils

if __name__ == '__main__':
    # 读取员工数据
    # _emp = extract_employee.get_employee_data()
    # print(_emp)
    # 读取打卡数据
    # _health_report = extract_health_report.get_health_report_data()
    # print(_health_report)
    # _data = xlsx_utils.merge(source_path=[r'.\test\resources\employee.xlsx ', r'.\test\resources\health_report.xlsx'], sheet_name='Sheet1')
    # xlsx_utils.write(file_path=r'.\test\results\merge.xlsx', sheet_name='Sheet1', data=_data)
    #
    _files = []
    _files.append({"path": r".\test\resources\employee.xlsx", "sheet": "Sheet1", "key_column": "WorkSN"})
    _files.append({"path": r".\test\resources\health_report.xlsx", "sheet": "Sheet1", "key_column": "工号"})
    _data = xlsx_utils.merge_files(_files)
    xlsx_utils.write(file_path=r'.\test\results\merge_files.xls', sheet_name='Sheet1', data=_data)
