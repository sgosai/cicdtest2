def test_passing():
    """This test will pass because the assertions are true."""
    assert 1 + 1 == 2
    assert "hello".upper() == "HELLO"

def test_failing():
    """This test will fail intentionally."""
    assert 1 + 1 == 2

# import pytest
# from multiply import multiply_logic
# # from CommonServerPython import CommandResults

# @pytest.mark.parametrize(
#     "args, expected_value", 
#     [
#         ({'num1': '5', 'num2': '3'}, 15),
#         ({'num1': '10', 'num2': '2'}, 10),
#         ({'num1': '-2', 'num2': '4'}, -80)
#     ]
# )
# def test_multiply_logic(args, expected_value):
#     """
#     Given: Arguments provided to the XSOAR command.
#     When: Running the multiply_logic function.
#     Then: Ensure the correct integer multiplication is returned in the CommandResults.
#     """
#     # Run the function
#     result = multiply_logic(args)
    
#     # Assert the outputs match expected behavior
#     # assert result.outputs['Value'] == expected_value
#     # assert f'The result is {expected_value}' in result.readable_output
#     # assert result == expected_value
#     assert 3 == 4
#     # assert f'The result is {expected_value}' in result.readable_output