import dataset_drive

def test_1():
    dataset = dataset_drive.load()
    print(dataset.head())
