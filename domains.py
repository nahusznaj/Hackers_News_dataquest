import read

df = read.load_data()
common_domains = df['url'].value_counts()
print(common_domains[0:100])

