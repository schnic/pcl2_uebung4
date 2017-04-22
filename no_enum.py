import bz2
import random
import lxml.etree as ET


def gettitles(infile, testfile, trainfile, k):

    parser = ET.iterparse(infile, events=('end',), tag='{http://www.mediawiki.org/xml/export-0.10/}title')
    
    counter = -1
    reservoir = []
    for (position, item) in parser:
        counter += 1
        position = str(counter)    # position == counter !!!
        # print(position, item)

        # if counter == 20000:
        #    break
        if counter < k:
            reservoir.append(item.text)
        else:
            m = random.randint(0,counter)
            if m < k:

                    trainfile.write(reservoir[m])
                    trainfile.write('\n')
                    reservoir[m] = item.text
            else:
                trainfile.write(str(position))
                trainfile.write('\t')
                trainfile.write(item.text)
                trainfile.write('\n')
        item.clear()


        


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