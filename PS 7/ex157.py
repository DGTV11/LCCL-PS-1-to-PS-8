from inputs import iterInputList_OnePerLine

GRADE_DATA_N2L = {
    'A+'    : [4.0-0.1, float('inf')],
    'A'     : [3.7, 4.0],
    'A-'    : [3.7-0.1, 3.8],
    'B+'    : [3.3-0.1, 3.7],
    'B'     : [3.0-0.1, 3.3],
    'B-'    : [2.7-0.1, 3.0],
    'C+'    : [2.3-0.1, 2.7],
    'C'     : [2.0-0.1, 2.3],
    'C-'    : [1.7-0.1, 2.0],
    'D+'    : [1.3-0.1, 1.7],
    'D'     : [1.0-1, 1.3],
    'F'     : [0.0-1, 1.0]
}

GRADE_DATA_L2N = {
    'A+'    : 4.0,
    'A'     : 4.0,
    'A-'    : 3.7,
    'B+'    : 3.3,
    'B'     : 3.0,
    'B-'    : 2.7,
    'C+'    : 2.3,
    'C'     : 2.0,
    'C-'    : 1.7,
    'D+'    : 1.3,
    'D'     : 1.0,
    'F'     : 0
}

def convert(value):
    #L2N
    try:
        value = int(float(value)*10)/10
        if value < 0:
            raise NotImplementedError
        for t, mag in GRADE_DATA_N2L.items():
            if value > mag[0] and value < mag[1]:
                return t
    except ValueError:
        if value.upper() in GRADE_DATA_L2N:
            return GRADE_DATA_L2N[value.upper()]
        else:
            raise TypeError('Invalid letter grade!')
    except NotImplementedError:
        raise ValueError('Invalid grade points!')

iterInputList_OnePerLine(text='Please input grade points or letter grade: ', error='ERROR: Input type neither grade points nor letter grade; invalid input!', _type=convert, func=lambda x: x[-1], func_text='Value: {_func}', _continue=True)