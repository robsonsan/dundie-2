from dundie.utils.log import get_logger

log = get_logger()


def load(filepath):
    """Loads data from filepath to the database.
    >>> len(load('assets/people.csv'))
    2
    """
    try:
        with open(filepath) as file_:
            lines =  [line.strip() for line in file_.readlines()]
            for line in lines:
                print(line)
            return lines
    except FileNotFoundError as e:
        print(f'File not found {e}')
