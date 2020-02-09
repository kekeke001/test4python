import extract_employee
import extract_health_report


if __name__ == '__main__':
    # 读取员工数据
    _emp = extract_employee.get_employee_data()
    # 读取打卡数据
    _health_report = extract_health_report.get_health_report_data()