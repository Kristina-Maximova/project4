import pytest


@pytest.fixture
def card_number_1() -> str:
    return "7000657954654659"


@pytest.fixture
def card_mask_1() -> str:
    return "7000 65** **** 4659"


@pytest.fixture
def account_number_1() -> str:
    return "76846547230523498765"


@pytest.fixture
def account_mask_1() -> str:
    return "**8765"
