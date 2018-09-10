import sys
import os

def remove_watermark(keyword, source, destination=None):
    f_name = source.split(".")[0]
    t1 = f_name + '_t1.pdf'
    t2 = f_name + '_t2.pdf'
    if not destination:
        destination = f_name + "_clean.pdf"
    os.system('qpdf --stream-data=uncompress ' + source + ' ' + t1)
    book = open(t1, "rb")
    book_clean = open(t2, "wb")
    stream, inside_stream, keep = '', False, True
    for line in book:
        if line == 'stream\n':
            inside_stream = True
        if inside_stream: stream += line
        else: book_clean.write(line)
        if keyword in line: keep = False
        if 'endstream' in line:
            if keep:
                book_clean.write(stream)
            else:
                cnt = len(stream) - len('stream\n\nendstream\n')
                book_clean.write('stream\n' + ' ' * cnt + '\nendstream\n')
            stream, inside_stream, keep = '', False, True

    book_clean.close()
    os.system('qpdf --stream-data=compress ' + t2 + ' ' + destination)
    os.system('rm ' + t1)
    os.system('rm ' + t2)
    print 'Success! Wrote to ' + destination

if __name__ == '__main__':
    """
    Usage ./figaro.py keyword source.pdf [destination.pdf]
    """
    remove_watermark(*sys.argv[1:])
