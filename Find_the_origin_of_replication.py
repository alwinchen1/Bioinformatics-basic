"""
Problem: Find the origin of replication (30%)
Description:
    Write a function that can identify the origin of replication from a circular DNA.
    Return the first origin’s starting and ending (excluding) index (start from 0).
    If not found, return (-1, -1).

Input:
    dna: string, circular DNA in linear form (e.g. “ATCCGGATATACGTAG”)
        Public: 160 < len(dna) < 1,000
        Private: 16,000 < len(dna) < 100,000
    ori: string, the origin of replication (e.g. “TATA”)
        3 < len(ori) < 10

Output:
    Tuple: (start index, end index) (e.g. (7, 11))
"""


def find_ori(dna, ori): 
    """
    Identify start and end index of the origin of replication
    in the given circular DNA.
    """    
    circular_dna = [x for x in dna]
    start, end = -1, -1
    
    # convert dna into circular dna
    for i in range(len(ori) - 1):
        circular_dna.append(dna[i])

    for i in range(len(circular_dna) - len(ori) + 1):
        fragment = circular_dna[i:i + len(ori)]
        fragment = ''.join(fragment)
        if fragment == ori:
            start, end = i % len(dna),((i+len(ori)) % len(dna))
            break
    
    T = (start, end)
    return (T)



if __name__ == "__main__":
    import sys

    input_path, output_path = sys.argv[1], sys.argv[2]

    with open(input_path, "r") as f, open(output_path, "w") as o:
        for i, line in enumerate(f):
            inputs, ans = line.split("\t")
            dna, ori = inputs.split(",")
            start, end = ans.split(",")

            your_start, your_end = find_ori(dna, ori)
            your_ans = "{},{}".format(your_start, your_end)
            # Uncomment the following line if you want to check your answers.
            # assert (your_ans + "\n") == ans, "Wrong answer at input#{}".format(i+1)
            o.write(your_ans + "\n")
