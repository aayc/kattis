import argparse
import os
import subprocess

def test_solution(solution):
    """Test solution file using input.txt output.txt

    Arguments:

    solution : solution base file name

    TODO allow multiple input files
    """
    for subdir, _, files in os.walk("."):
        for fname in files:
            if fname == solution:
                with open(subdir + "/input.txt", "r") as f:
                    testcases = f.read()

                with open(subdir + "/output.txt", "r") as f:
                    expected = f.read()

                process = subprocess.Popen(["python3", subdir + "/" + fname], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                output = process.communicate(input=str.encode(testcases))[0].decode('ASCII')

                print("expected:\n" + expected)
                print("output:\n" + output)
                print("TEST RESULT: ", "PASS" if expected == output else "FAIL")

                return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tester for Kattis solutions")
    parser.add_argument("solution", type=str, help="Python solution file")

    args = parser.parse_args()
    test_solution(args.solution)
