from behave import given, then
from more_itertools import first
from schema import Schema


@given("we have numbers")
def step_impl(context):
    schema = Schema(
        {'name': str, 'value': str}
    )

    assert schema.is_valid(first(
        context.table).as_dict()), f"Expect a table of {schema.schema}, got {first(context.table).as_dict().keys()}"

    numbers = {}
    for row in context.table:
        row = schema.validate(row.as_dict())
        name = row['name'].strip()
        value = int(row['value'])

        numbers[name] = value

    context.numbers = numbers


@then("we expect addition results")
def step_impl(context):
    schema = Schema(
        {'name_1': str, 'name_2': str, 'equals': str}
    )

    assert schema.is_valid(first(
        context.table).as_dict()), f"Expect a table of {schema.schema}, got {first(context.table).as_dict().keys()}"

    numbers = context.numbers
    assert numbers, "We expect numbers to be defined before this task"

    for row in context.table:
        row = schema.validate(row.as_dict())
        name_1 = row['name_1'].strip()
        name_2 = row['name_2'].strip()

        equals = int(row['equals'])

        val_1 = numbers[name_1]
        val_2 = numbers[name_2]

        assert val_1 + val_2 == equals, f"{val_1} + {val_2} != {equals}"

