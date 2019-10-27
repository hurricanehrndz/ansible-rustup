import os
import pytest


@pytest.fixture
def scenario():
    implementation = "rustup_{}".format(
      os.environ['MOLECULE_SCENARIO']
    )
    return pytest.importorskip(implementation)
