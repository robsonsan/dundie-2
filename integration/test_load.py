import pytest
from subprocess import check_output


@pytest.mark.integration
def test_load():
    """Test command load"""
    a = check_output(
        ["dundie", "load", "tests/assets/people.csv"]
    )
    print(a)
    out = check_output(
        ["dundie", "load", "tests/assets/people.csv"]
    ).decode('UTF-8').split('\n')
    if out[-1] == '':
        assert len(out[:-1]) == 2
    else:
        assert len(out) == 2
