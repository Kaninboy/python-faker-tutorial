import pandas as pd
from faker import Faker

# display the first 5 rows of the csv file
def read_csv(file_path):
    df = pd.read_csv(file_path)
    print(df.head())

# write a csv file with fake data using Faker
def write_mock_csv(file_path, num_rows):
    fake = Faker()
    data = []
    for _ in range(num_rows):
        data.append([fake.uuid4(), fake.name(), fake.address().replace('\n',' '), fake.phone_number()])
    try:
        df_existing = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        df_existing = pd.DataFrame(columns=['id','name', 'address', 'phone_number'])
    df = pd.DataFrame(data, columns=['id','name', 'address', 'phone_number'])
    df_combined = pd.concat([df_existing, df], ignore_index=True)
    df_combined.to_csv(file_path, index=False)


if __name__ == '__main__':
    write_mock_csv('fake.csv', 20)
    read_csv('fake.csv')