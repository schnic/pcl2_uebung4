from lxml import etree as ET
import glob


def getfreqwords(indir, outfile):
    tree_counter = 0
    hash_dict = {}
    for element in indir:
        tree = ET.parse(element)
        root = tree.getroot()
        tree_counter += 1

        for article in root:
            for divider in article:
                for sentence in divider:
                    sent_str = ''
                    word_counter = 0

                    for word in sentence:
                        sent_str += str(word.get('lemma'))
                        sent_str += ' '
                        word_counter += 1

                    if word_counter >= 6:
                        if sent_str in hash_dict:
                            hash_dict[sent_str] += 1
                        else:
                            hash_dict[sent_str] = 1

                    else:
                        pass
            divider.clear()
        article.clear()

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
    text_list = []
    for filename in glob.glob('Text+Berg_Release_152_v01/**/SAC-Jahrbuch_*_mul.xml', recursive=True):
        text_list.append(filename)

    my_outfile = open('20 most freq words of SAC.txt', 'w')

    getfreqwords(text_list, my_outfile)

    my_outfile.close()

if __name__ == '__main__':
    main()
