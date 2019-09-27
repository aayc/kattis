import sys
import argparse
import os
import subprocess

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tester for Kattis solutions")
    parser.add_argument("solution", type=str, help="Python solution file")

    args = parser.parse_args()

    for subdir, dirs, files in os.walk("."):
        for fname in files:
            if fname == args.solution:
                print("FOUND SOLUTION FILE.  Beginning test...")
                with open(subdir + "/input.txt", "r") as f:
                    testcases = f.read()

                with open(subdir + "/output.txt", "r") as f:
                    expected = f.read()

                process = subprocess.Popen(["python3", subdir + "/" + fname], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                output = process.communicate(input=str.encode(testcases))[0].decode('ASCII')

                print("expected:|" + expected + "|")
                print("output:|" + output + "|")
                print("TEST RESULT: ", "PASS" if expected == output else "FAIL")
