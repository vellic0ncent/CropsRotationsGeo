def rotation_length(row):
    length = row.drop_duplicates().shape[0]
    return length


def rotation_count(row):
    count = row.value_counts().min()
    return count


def add_rotation_info(data):
    data['RotationLength'] = data.apply(rotation_length, axis=1)
    data['RotationCount'] = data.apply(rotation_count, axis=1)