from getgauge.python import step,continue_on_failure,Messages,Table


@continue_on_failure
@step("Should Continue <table>")
def should_continue(table):
    for num in table:
        failassert(num)
        Messages.write_message(f"continuing inside the step{num}")

@step("Should break")
def should_break():
    assert False, "breaks"

@step("Make sure it continues")
def make_sure_it_continues():
    Messages.write_message("continuing...")


def failassert(num):
    assert False, f"assert1 for index {num}"
    assert False, f"assert2 for index {num}"



