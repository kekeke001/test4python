import xlrd
import xlwt


# 读数据
def read(file_path, sheet_name):
    # print(f'Try to read sheet {sheet_name} from xlsx-file {file_path}')
    _workbook = xlrd.open_workbook(file_path)  # get workbook 获取工作簿
    _sheet = _workbook.sheet_by_name(sheet_name)  # get sheet_by_name 获取页签
    _rows_count = _sheet.nrows  # get rows count 统计行数
    _result = []
    for _row_idx in range(_rows_count):
        _row_data = _sheet.row_values(_row_idx)  # 获取行元素，将行以列表输出
        _result.append(_row_data)
    return _result


# 读多个excel表格数据，合并，去重
def merge(source_path, sheet_name):
    _data1 = []
    for _idx in source_path:
        _data1.append(read(_idx, sheet_name))

    # 合并
    _rec = []
    _data = []
    for x in range(len(_data1)):
        for y in range(len(_data1[x])):
            _rec.extend(_data1[y][x])
        _data.append(_rec)
        _rec = []

    # 去重
    _content = []
    for _idx in _data:
        _row_content = []
        for _idy in _idx:
            if _idy not in _row_content:
                _row_content.append(_idy)
        _content.append(_row_content)
    print(_content)
    return _content


# 读取多个excel表格输出
# 读取数据
def read1(source_path, sheet_name):
    _data = []
    for i in source_path:
        _workbook = xlrd.open_workbook(i)
        _sheet = _workbook.sheet_by_name(sheet_name)
        for rownum in range(_sheet.nrows):
            _data.append(_sheet.row_values(rownum))
    print(_data)


# 写xlsx文件

def write(file_path, sheet_name, data):
    print(f'Try to write sheet: {sheet_name} to xlsx-file:{file_path}')
    _workbook = xlwt.Workbook()  # 生成Workbook对象（xlwt.Workbook.Workbook类)
    _sheet = _workbook.add_sheet(sheet_name)  # 创建xlwt.Worksheet.Worksheet类的sheet对象
    # sheet1.write(, , 'ID')  # 在第 0 行第 0 列写入数据‘ID'
    for _row_idx in range(len(data)):
        _row = data[_row_idx]
        for _col_idx in range(len(_row)):
            _sheet.write(_row_idx, _col_idx, _row[_col_idx])
    print(dir(_sheet))
    _workbook.save(file_path)


# 提取列元素
def extract_columns(file_path, sheet_name, column_name_str=''):
    _data = read(file_path=file_path, sheet_name=sheet_name)
    # 如果待抽取列为空，默认返回所有列数据
    if column_name_str is None or column_name_str == '':
        return _data
    _column_names = column_name_str.split(',')  # [Name，HW_PM]
    # 获取对应列的索引
    _column_index = []
    _xlsx_head = _data[0]
    for _column_name in _column_names:
        _idx = _xlsx_head.index(_column_name)
        _column_index.append(_idx)
    print(f'column index list:{_column_index}')
    # 获取数据
    _result = []
    for _row in _data:
        _rec = []
        for _idx in _column_index:
            _rec.append(_row[_idx])
        _result.append(_rec)
    print(f'Extract{len(_result)} rows from xlsx data.')
    return _result


if __name__ == '__main__':
    # write(file_path=r'.\test\results\xx.xlsx', sheet_name='Sheet1', data=[['ID', 'Name'], ['1', 'KeKeKe']])
    # print(read(file_path=r'.\test\results\xx.xlsx', sheet_name='Sheet1'))
    _data = extract_columns(file_path=r'.\test\resources\employee.xlsx', sheet_name='Sheet1',
                            column_name_str='Name,HW_PM')
    # write(file_path=r'.\test\results\xx.xlsx', sheet_name='Sheet1', data=_data)
