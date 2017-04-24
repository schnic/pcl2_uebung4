import bz2
import random
import lxml.etree as ET


def gettitles(infile, testfile, trainfile, k):
    """Getting k randomly selected titles of the german wikipedia articles """

    # iterparses the infile
    parser = ET.iterparse(infile, events=('end',), tag='{http://www.mediawiki.org/xml/export-0.10/}title')

    # counter = 0

    # reservoir for the selected titles
    reservoir = []
    for position, item in enumerate(parser):  # tuples
        # counter += 1
        # print(position, item)
        # if counter == 20000:
        #     break

        # the first k elements will be put into the reservoir
        if position < k:
            reservoir.append(item[1].text)

        # decides if title will get randomly selected
        else:
            m = random.randint(0, position)

            # overwritten randomly selected titles will be written into the trainfile
            # the newly selected go into the reservoir
            if m < k:
                trainfile.write(reservoir[m])
                trainfile.write('\n')
                reservoir[m] = item[1].text

            # not randomly selected titles will directly go into the trainfile
            else:
                trainfile.write(str(position))
                trainfile.write(item[1].text)
                trainfile.write('\n')

        # clears the item and the whole branch of it
        item[1].clear()
        for ancestor in item[1].xpath('ancestor-or-self::*'):
            while ancestor.getprevious() is not None:
                del ancestor.getparent()[0]

    # writes the randomly selected titles into the testfile
    for element in reservoir:
        testfile.write(element)
        testfile.write('\n')


def main():

    # opening the bz2 file
    big_ass_file = bz2.open('dewiki-latest-pages-articles.xml.bz2', mode='r',
                            compresslevel=9, encoding=None, errors=None, newline=None)

    #opening the two outfiles for writing
    test_file = open('testfile.txt', 'w')
    train_file = open('trainfile.txt', 'w')

    # function "aufruf"
    gettitles(big_ass_file, test_file, train_file, 20)

    train_file.close()
    test_file.close()


if __name__ == '__main__':
    main()
