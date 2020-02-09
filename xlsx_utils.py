import xlrd


def read(file_path, sheet_name):
    print(f'Try to read sheet {sheet_name} from xlsx-file {file_path}')
    # get workbook
    _workbook = xlrd.open_workbook(file_path)
    # get sheet_by_name
    _sheet = _workbook.sheet_by_name(sheet_name)
    # get rows count
    _rows_count = _sheet.nrows
    # read row by index
    _result = []
    for _row_idx in range(_rows_count):
        _row_data = _sheet.row_values(_row_idx)
        _result.append(_row_data)
    return _result


def write(file_path, sheet_name, data):
    print(f'Try to write sheet: {sheet_name} to xlsx-file:{file_path}')


def extract_columns(file_path, sheet_name, column_name_str, extract_to):
    _data = read(file_path=file_path, sheet_name=sheet_name)
    _column_names = column_name_str.split(',')
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
    print(_result)
    return _result


