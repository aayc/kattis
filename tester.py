import argparse
import os
import subprocess

def test_solution(solution):
    """Test solution file using input.txt output.txt

    Arguments:

    solution : solution base file name

    """
    for subdir, _, files in os.walk("."):
        for fname in files:
            if fname == solution:
                passes = 0
                n_tests = 0
                i = 1

                while os.path.exists(f"{subdir}/input{i}.txt"):
                    with open(f"{subdir}/input{i}.txt", "r") as f:
                        testcases = f.read()

                    with open(f"{subdir}/output{i}.txt", "r") as f:
                        expected = f.read()

                    process = subprocess.Popen(["python3", subdir + "/" + fname], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                    output = process.communicate(input=str.encode(testcases))[0].decode('ASCII')
                    success = expected == output

                    print("expected:\n" + expected)
                    print("output:\n" + output)
                    print("TEST RESULT: ", "PASS" if success else "FAIL")

                    passes += 1 if success else 0
                    n_tests += 1
                    i += 1

                print(f"TEST RESULTS: {passes}/{n_tests}")
                return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tester for Kattis solutions")
    parser.add_argument("solution", type=str, help="Python solution file")

    args = parser.parse_args()
    test_solution(args.solution)
