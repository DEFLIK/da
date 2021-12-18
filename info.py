import pandas as pd


def get_top(data, size, sort_column, search_colum, value):
    filtered = data[data[search_colum].apply(lambda x: is_connected(x, value))]
    lowercased = filtered[sort_column].apply(lambda x: x.lower())
    sorted = lowercased.value_counts()
    return sorted.head(size)


def is_connected(job: str, qual: str):
    job_words = job.replace('-', ' ').lower().split()
    qual_words = qual.replace('-', ' ').lower().split()

    return not set(job_words).isdisjoint(qual_words)


data = pd.read_csv("works.csv").dropna()
non_specialized = list(filter(lambda x: not is_connected(x[0], x[1]), zip(data["jobTitle"], data["qualification"])))

print(f"На {len(data)} людей, не по должности работают {len(non_specialized)}")
print(
    "Топ образование среди тех, кто работает менеджером \n",
    get_top(data, 5, "qualification", "jobTitle", "менеджер"))
print(
    "Топ работ, среди тех, кто по образованию инженер \n",
      get_top(data, 5, "jobTitle", "qualification", "инженер"))
