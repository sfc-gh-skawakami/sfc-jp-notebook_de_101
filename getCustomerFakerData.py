from snowflake.snowpark.types import IntegerType, StringType, DateType, StructType, StructField
import faker
import pandas as pd
from datetime import datetime

def gen_fake_customers(row_nums: int) -> pd.DataFrame:
    faker_row_output = []

    for i in range(row_nums):
        fake = faker.Faker('nl_NL')
        fake_customer = {}
        fake_customer['id'] = fake.unique.random_int()
        fake_customer['first_name'] = fake.first_name()
        fake_customer['last_name'] = fake.last_name()
        fake_customer['email'] = fake.email()
        fake_customer['phone_number'] = fake.phone_number()
        fake_customer['bsn_number'] = fake.ssn()
        fake_customer['address'] = fake.address()                                  
        fake_customer['city'] = fake.city()
        fake_customer['province'] = fake.province()
        fake_customer['birthdate'] = fake.date_between_dates(date_start=datetime(1965,1,1), date_end=datetime(2003,12,31))  
        faker_row_output.append(fake_customer)

    pd_df_fake_custmers = pd.DataFrame.from_dict(faker_row_output)

    return pd_df_fake_custmers
