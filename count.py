import read

df = read.load_data()

# Before moving on I run some checks that are commented now:
#print(df.head(3))
#print(df['headline'].iloc[6])
#print(df['headline'].dtype)

#In order to count which words appear most often in the headlines I will combine all the values of the column headline into one string; then I will split the string into a list of words, and then I will count how many times each word appears in the list.

#print(len(df['headline']))


onelongstring = ""

for i in df['headline']:
    i = str(i)
    onelongstring += " " + i.lower() #previously I had the problem that strings were being joined without a space. So I added a space " " string to fix this.
    # I also converted all strings in lowercase so that I count smartly


    #What I want now is to find the 100 most common words in the headlines.

    #These are two ways that I explored. The most hands-on is by coding it from scratch. Alternatively, use the Counter class.

    #First the pedestrian way:

list_of_headlines = onelongstring.split(' ')

dict_count = {}

for item in list_of_headlines:
    if item not in dict_count:
        dict_count[item] = 1
    else:
        dict_count[item] += 1

sortes = sorted(dict_count.values(), reverse=True)
sortes = sortes[0:100]


#I took this function from https://thispointer.com/python-how-to-find-keys-by-value-in-dictionary/

def getKeysByValues(dictOfElements, listOfValues):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] in listOfValues:
            listOfKeys.append(item[0])
    return  listOfKeys



most_common = getKeysByValues(dict_count, sortes)
#print(len(most_common))
print(most_common[0:3])

#There are some issues with this method: I get 101 most common words and I don't know how to reduce it to 100; every time I run the code it gives the list of most common words in different order; it includes the space as a word ' '

# Now let's try using the Counter class.
# Find docs in https://docs.python.org/3/library/collections.html#collections.Counter

import collections

the_most_common = collections.Counter(onelongstring).most_common(100)
#print(the_most_common[0:3])

#Evidently, this method is more powerful since it took me one line of code to produce the 100 most common words in the long string of headlines. I didn't need to split the long string into words!
#It's also ordered!
#It includes too the space as an element... I don't know how to fix this.
