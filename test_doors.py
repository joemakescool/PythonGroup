
from Doors_Opening import get_doors_open
from urllib.request import urlopen


def get_url(url):
    """
    takes a url page log and makes a it list
    :param url: a url of a page log
    :return: a list of the page log
    """
    print("Getting url file :)", url)
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            story_words.append(line_words)
    return story_words


url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv"
sort_me = get_url(url)

my_input_list = []

input_to_func = ""
for item in sort_me:
    new_string = ""
    print(item)
    for thing in item:
        new_string = new_string + thing
    #makes the input string
    y = new_string[3::]
    y = y.replace(",", "")
    #set up the input
    LD = y[0]
    RD = y[1]
    CL = y[2]
    ML = y[3]
    LI = y[4]
    LO = y[5]
    RI = y[6]
    RO = y[7]
    GS = y[8]
    #calls outside function
    get_doors_open(LD, RD, CL, ML, LI, LO, RI, RO, GS)
