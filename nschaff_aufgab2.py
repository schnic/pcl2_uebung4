import bz2
import random
import lxml.etree as ET


def gettitles(infile, testfile, trainfile, k):

    parser = ET.iterparse(infile, events=('end',), tag='{http://www.mediawiki.org/xml/export-0.10/}title')
    
    # counter = 0
    reservoir = []
    for position, item in enumerate(parser):
        # counter += 1
        # print(position, item)

        # if counter == 20000:
        #    break
        if position < k:
            reservoir.append(item[1].text)
        else:
            m = random.randint(0,position)
            if m < k:
                    trainfile.write(reservoir[m])
                    trainfile.write('\n')
                    reservoir[m] = item[1].text
            else:
                trainfile.write(str(position))
                trainfile.write(item[1].text)
                trainfile.write('\n')


        


    for element in reservoir:
        testfile.write(element)
        testfile.write('\n')

    train_file.close()
    test_file.close()


def main():
    
    big_ass_file = bz2.open('dewiki-latest-pages-articles.xml.bz2', mode='r', \
        compresslevel=9, encoding=None, errors=None, newline=None)
    
    test_file = open('testfile.txt', 'w')
    train_file = open('trainfile.txt', 'w')

    gettitles(big_ass_file, test_file, train_file, 20)




if __name__ == '__main__':
    main()