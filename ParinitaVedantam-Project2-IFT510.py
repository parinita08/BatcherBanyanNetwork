#Batcher Banyan Network - Project 2
#Parinita Vedantam - IFT510
import random

def BatcherSorter(randoms):
    BatcherSort = {
        0: "A1",
        1: "A2",
        2: "A3",
        3: "A4",
        4: "A5",
        5: "A6",
        6: "A7",
        7: "A8",
        8: "A1",
        9: "A2",
        10: "A3",
        11: "A4",
        12: "A5",
        13: "A6",
        14: "A7",
        15: "A8"
        }
    print(randoms)
    randoms.sort()
    print(f"Array after sort:{randoms}")
    return BatcherSort

def path(input, destination):
    path1 = {
        "A1": ["B1", "B5"],
        "A2": ["B2", "B6"],
        "A3": ["B3", "B7"],
        "A4": ["B4", "B8"],
        "A5": ["B1", "B5"],
        "A6": ["B2", "B6"],
        "A7": ["B3", "B7"],
        "A8": ["B4", "B8"],
    }
    path2 = {
        "B1": ["C1", "C3"],
        "B2": ["C2", "C4"],
        "B3": ["C1", "C3"],
        "B4": ["C2", "C4"],
        "B5": ["C5", "C7"],
        "B6": ["C6", "C8"],
        "B7": ["C5", "C7"],
        "B8": ["C6", "C8"],
    }
    path3 = {
        "C1": ["D1", "D2"],
        "C2": ["D1", "D2"],
        "C3": ["D3", "D4"],
        "C4": ["D3", "D4"],
        "C5": ["D5", "D6"],
        "C6": ["D5", "D6"],
        "C7": ["D7", "D8"],
        "C8": ["D7", "D8"],
    }
    outputPath = {
        "D1": ["Output 0", "Output 1"],
        "D2": ["Output 2", "Output 3"],
        "D3": ["Output 4", "Output 5"],
        "D4": ["Output 6", "Output 7"],
        "D5": ["Output 8", "Output 9"],
        "D6": ["Output 10", "Output 11"],
        "D7": ["Output 12", "Output 13"],
        "D8": ["Output 14", "Output 15"]

    }

    userOutput = input
    BanyanNetwork = [path1 , path2, path3, outputPath]

    for i, paths in enumerate(destination):
        print(destination, " ", userOutput, " ---> ", end="")
        userOutput = BanyanNetwork[i][userOutput][int(paths)]

    print(f" {userOutput}")


def main():
    userInput = int(input(" Number of Inputs: "))
    randoms = random.sample(range(0,15), userInput)
    packets = BatcherSorter(randoms)

    for i in range(userInput):
        destination = "{0:04b}".format(randoms[i])
        path(packets[randoms[i]], destination)

if __name__ == "__main__":
    main()   