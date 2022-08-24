from .utils import load_cli_args

def test_load_cli_args():
    io_args = ['app.py', '5,2,6,1,4,3', '12']
    num_list, expected_result = load_cli_args(io_args)
    assert num_list == [5,2,6,1,4,3]
    assert expected_result == 12
    assert type(expected_result) is int