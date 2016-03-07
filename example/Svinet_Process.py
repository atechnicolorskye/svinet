'''
Process protein networks for Svinet
Essentially the same as CESNA_Process, but displays number of nodes
'''


def Proc_Svinet(Net):
    with open(Net, 'r') as I_Net:
        Input_Net = I_Net.readlines()

    node_counter = 1

    Nodes = {}

    Output = set()

    for line in Input_Net[1:]:
        line_s = line.split('\t')
        if line_s[0] not in Nodes:
            Nodes[line_s[0]] = node_counter
            node_counter += 1
        if line_s[1] not in Nodes:
            Nodes[line_s[1]] = node_counter
            node_counter += 1
        # print str(Nodes[line_s[0]]) + '\t' + str(Nodes[line_s[1]]) + '\n'
        Output.update([str(Nodes[line_s[0]]) + '\t' + str(Nodes[line_s[1]]) + '\n'])
        # print Output

    # Enable repetitions
    # with open('pp_networks_rep.txt', 'w') as O:
    #     for line in Input_Net[1:]:
    #         line_s = line.split('\t')
    #         if line_s[0] not in Nodes:
    #             Nodes[line_s[0]] = node_counter
    #             node_counter += 1
    #         if line_s[1] not in Nodes:
    #             Nodes[line_s[1]] = node_counter
    #             node_counter += 1
    #         O.write(str(Nodes[line_s[0]]) + '\t' + str(Nodes[line_s[1]]) + '\n')

    # Need to know number of nodes for Svinet, checked 5197 for pp network and 1494 for 1912.edges
    print node_counter - 1

    Output = sorted(Output)

    with open('pp_networks_num.txt', 'w') as O:
        for edge in Output:
            O.write(edge)


if __name__ == '__main__':
    Proc_Svinet('network.txt')
