import helpers as h
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python3 "/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/ex182.py" <input file> <redaction key file> <output file>')
        quit()
    infn = h.purify_fn(sys.argv[1])
    rkfn = h.purify_fn(sys.argv[2]) #redaction key
    ofn = h.purify_fn(sys.argv[3])

    with open(infn, 'r') as inf, open(rkfn, 'r') as rkf, open(ofn, 'w') as outf:
        loaded_file = inf.read()

        new_file = h.batch_replace(loaded_file, {txt:'*'*len(txt) for txt in h.read_opened_file_lines(rkf)})
        outf.write(new_file)