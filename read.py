# The dataset does not name the columns, so I add them by hand "submission_time", "upvotes", "url", "headline"

def load_data():
    import pandas as pd
    data = pd.read_csv('hn_stories.csv', names = ["submission_time", "upvotes", "url", "headline"])
    return data

if __name__ == "__main__":
   # This will call load_data if you run the script from the command line.
   load_data()
