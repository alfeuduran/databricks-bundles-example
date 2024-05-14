import pytest
from bundlesDevOpsDemo.main import get_taxis, get_spark

@pytest.fixture
def setup_taxis():
    spark_session = get_spark()
    taxis = get_taxis(spark_session)
    return taxis

def test_taxi_count(setup_taxis):
    # setup_taxis is the taxis DataFrame returned by the fixture
    assert setup_taxis.count() > 5