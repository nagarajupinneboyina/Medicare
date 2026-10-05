"""Pure validation and cleaning functions for raw patient data.

YOUR JOB: complete every function marked TODO.
Each takes messy text in and returns a clean value out — or raises
InvalidRecordError explaining what is wrong.
(Module 4 functions + Module 9 exceptions, working together.)
"""


class InvalidRecordError(Exception):
    """Raised when a patient row cannot be repaired safely."""
    # Nothing to add — inheriting from Exception is enough (Module 9).


def clean_name(raw_name: str) -> str:
    """Return the name stripped of extra spaces, in Title Case.

    >>> clean_name("  priya sharma ")
    'Priya Sharma'

    Raise InvalidRecordError("name is missing") if the result is empty.
    """
    name = raw_name.strip().title()

    if not name:
        raise InvalidRecordError("name is missing")

    return name


def parse_age(raw_age: str) -> int:
    """Convert age text to int; must be between 1 and 120.

    Raise InvalidRecordError for non-numbers ("abc") and out-of-range ages.
    HINT: wrap int(...) in try/except ValueError.
    """
    try:
     age = int(raw_age.strip())
    except ValueError:
     raise InvalidRecordError(f"invalid age: {raw_age}")

    if age < 1 or age > 120:
     raise InvalidRecordError(f"age out of range: {age}")

    return age


def parse_fee(raw_fee: str) -> float:
    """Convert a fee like '1,250.50' to 1250.50 (float).

    Steps: remove commas, strip spaces, reject empty / non-numeric /
    negative values with InvalidRecordError.
    """
    cleaned = raw_fee.replace(",", "").strip()

    if not cleaned:
     raise InvalidRecordError("fee is missing")

    try:
     fee = float(cleaned)
    except ValueError:
     raise InvalidRecordError(f"invalid fee: {raw_fee}")

    if fee < 0:
     raise InvalidRecordError("fee cannot be negative")

    return fee


def clean_department(raw_dept: str, default: str = "General") -> str:
    """Return the department in Title Case, or the default when blank.

    WHY a default: reception sometimes leaves the field empty; the
    clinic's rule is to file such visits under General.
    """
    department = raw_dept.strip()

    return department.title() if department else default
