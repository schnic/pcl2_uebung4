from lxml import etree as ET
import glob


def getfreqwords(indir, outfile):
    """getting the most frequent lemmatised sentences of SAC-files"""

    # dictionary for the lemmatised sentences
    hash_dict = {}

    # goes through all the files, every file is parsed.
    for element in indir:
        tree = ET.parse(element)
        root = tree.getroot()

        # goes through every 'tag' here just refered by the deepness into the xml file
        for article in root:
            for divider in article:

                # empty string and counter for tokens
                for sentence in divider:
                    sent_str = ''
                    word_counter = 0

                    # fills up the empty string with the lemmas of every word line of a s tag
                    for word in sentence:
                        sent_str += str(word.get('lemma'))
                        sent_str += ' '
                        word_counter += 1

                    # if there were 6 or more lemmas it gets into the dictionary
                    if word_counter >= 6:
                        if sent_str in hash_dict:
                            hash_dict[sent_str] += 1
                        else:
                            hash_dict[sent_str] = 1
                    else:
                        pass

            # clears the branches of the tree
                divider.clear()
            article.clear()

    # writes the most frequent words in the outfile
    entry_count = 0
    for entry in (sorted(hash_dict, key=hash_dict.get, reverse=True)):
        outfile.write(str(hash_dict[entry]))
        outfile.write('\t')
        outfile.write(entry)
        outfile.write('\n')
        entry_count += 1
        if entry_count == 20:
            break


def main():

    # gets a list with all the files we want to go through
    text_list = []
    for filename in glob.glob('Text+Berg_Release_152_v01/**/SAC-Jahrbuch_*_mul.xml', recursive=True):
        text_list.append(filename)

    # opening the outfile
    my_outfile = open('20_most_freq_lemma_sentences_of_SAC.txt', 'w')

    # function
    getfreqwords(text_list, my_outfile)

    my_outfile.close()

if __name__ == '__main__':
    main()
