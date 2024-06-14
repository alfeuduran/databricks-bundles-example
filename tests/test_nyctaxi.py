# Databricks notebook source
from runtime.nutterfixture import NutterFixture, tag


class MyTableTest(NutterFixture):
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        self.actual_row_count = 0

    def run_test_row_count_in_table(self):
        # This is the 'run' part where you perform your operations
        # Query the Spark table and get the row count
        self.actual_row_count = spark.table("samples.nyctaxi.trips").count()

    def assertion_test_row_count_in_table(self):
        # This is the 'assertion' part where you check the conditions
        assert (
            self.actual_row_count == 21932
        ), f"Expected 97 rows, found {self.actual_row_count}"


# Create an instance of your test class
test = MyTableTest()

# Execute the tests
result = test.execute_tests()

# Print the test results
print(result.to_string())

result.exit(dbutils)

# is_job = dbutils.notebook.entry_point.getDbutils().notebook().getContext().currentRunId().isDefined()
# if is_job:
#   result.exit(dbutils)
