from getgauge.python import step,continue_on_failure,Messages,Table
from delayed_assert.delayed_assert import assert_expectations,expect


@continue_on_failure
@step("Should Continue <table>")
def should_continue(table):
    for num in table:
        failassert(num)
        Messages.write_message(f"continuing inside the step{num}")
    assert_expectations()

@step("Should break")
def should_break():
    assert False, "breaks"

@step("Make sure it continues")
def make_sure_it_continues():
    Messages.write_message("continuing...")


def failassert(num):
    expect(False, f"soft assert 1 for index {num}")
    expect(False, f"soft assert 2 for index {num}")



