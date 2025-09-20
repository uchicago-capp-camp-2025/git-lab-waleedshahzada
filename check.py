import sys
import subprocess
import pathlib

HIDDEN_FILE = ".part2-done"


def check_git_output(command, contains):
    output = subprocess.run(["git", command], capture_output=True).stdout.decode()
    if contains.lower() in output.lower():
        return True
    else:
        return False


def check_status_clean():
    if not check_git_output("status", "nothing to commit, working tree clean"):
        print(
            "Ensure that you have committed or  any changes before running, run `git status` to check."
        )
        return False
    return True


def check_part1():
    # ensure that the repo has a commit with 'part 1 done'
    check_status_clean()
    if not check_git_output("log", "part 1 done"):
        print(
            "Part 1: Ensure that you have made a commit with the message 'part 1 done', run `git log` to check."
        )
    else:
        print("Part 1: Complete!")


def check_part2():
    # once file exists, check that change was reverted
    if pathlib.Path(HIDDEN_FILE).exists():
        if check_status_clean():
            print("Part 2: Complete!")
    else:
        # file doesn't exist yet, ask for change
        part2_text = pathlib.Path("part2.txt").read_text()
        if ":)" not in part2_text:
            print(
                "Be sure to add the happy face in part2.txt before running this command."
            )
        else:
            print(
                "OK, I've observed your change. Go ahead and undo it now using `git restore`"
            )
            with open(HIDDEN_FILE, "w") as f:
                f.write(":)")


def check_part3():
    if check_status_clean():
        print("Part 3: Complete!")
    else:
        print("Make sure to commit the changes!");

def check_part4():
    if check_git_output("status", "Your branch is up to date with 'origin/main'"):
        print("Part 4: Complete!")
    else:
        print("Make sure to push your changes to GitHub!");
        

def check_part5():
    # Run the git log command
    output = subprocess.run(["git", "log"], capture_output=True).stdout.decode()

    # The relevant commit SHA is the last one before the "part 1 done" message
    # Find the "part 1 done" message
    part1_idx = output.lower().index("part 1 done")
    # Look backwards from there to find the commit
    start = output[:part1_idx].rindex("commit") + len("commit ") 
    # The SHA runs from start to the next new line
    end = output[start:].index("\n") 
    # Extract the SHA
    sha = output[start : start + end]                                                                                                                                         

    print("sha:", sha)

    part5_text = pathlib.Path("part5.txt").read_text()
    if sha not in part5_text:
        print('Be sure to add the hash for the commit with the message "part 1 done" to part5.txt.')
    else:
        print("Great job, nearly done!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Be sure to pass the part you are checking, e.g. `python3 check.py` 1 for part 1"
        )
        sys.exit(1)
    if sys.argv[1] == "1":
        check_part1()
    elif sys.argv[1] == "2":
        check_part2()
    elif sys.argv[1] == "3":
        check_part3()
    elif sys.argv[1] == "4":
        check_part4()
    elif sys.argv[1] == "5":
        check_part5()
