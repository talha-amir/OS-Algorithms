from tabulate import tabulate

def completion_time(n,a_time,b_time):
    data = list(zip(list(range(n)), a_time, b_time))
    data.sort(key=lambda x:(x[1],x[2]))
    c_t = [0]*n
    clock = 0
    for process in data:
        clock += process[2]
        c_t[process[0]] = clock
    return c_t

def turn_around_time(c_time,a_time):
    return [(c-a) for c,a in zip(c_time,a_time)]

def waiting_time(t_time,b_time):
    return [(t-b) for t,b in zip(t_time,b_time)]

def print_all(p_list,a_list,b_list,c_list,t_list,w_list):
    m = [p_list,a_list,b_list,c_list,t_list,w_list]
    m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    print('\n'*2)
    print(tabulate(m ,headers= ['Process List','Arrival Time',' Burst Time', 'Completion Time', 'Turn Over Time'  ,'Waiting Time'],tablefmt="github"),end='\n\n')
    print(
        f"Average Waiting Time = {str(sum(w_list)/len(w_list))}",
        f"Average Turn Around Time = {str(sum(t_list)/len(t_list))}",
        sep='\n',
    )


def SJF():
    n = int(input("Number of Processes"))
    arrival_time = [ int(input(f"Arrival Time for P{i+1}")) for i in range(n)]    
    burst_time = [ int(input(f"Burst Time for P{i+1}")) for i in range(n)]
    c_t = completion_time(n,arrival_time,burst_time)
    ta_t = turn_around_time(c_t,arrival_time)
    w_t = waiting_time(ta_t,burst_time)
    print_all([(i+1) for i in range(n)],arrival_time,burst_time,c_t,ta_t,w_t)


if __name__ == "__main__":
    SJF()