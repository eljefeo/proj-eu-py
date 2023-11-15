# This is a sample Python script.

from time import perf_counter

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def run(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name:*^20}')  # Press Ctrl+F8 to toggle the breakpoint.

    start = perf_counter()
    problem1()
    end = perf_counter()

    print("Elapsed time:", end-start)

def problem1():
    print('here from problem')
    total = 0;
    for i in range(3,1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i;

        #System.out.println("Sum of all multiples of 3 or 5 less than 1000 : " + total);
    print('result: ', total)
    return total;

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
