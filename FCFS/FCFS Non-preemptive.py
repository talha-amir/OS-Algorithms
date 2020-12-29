from tabulate import tabulate

def completion_time(n,a_time,b_time):
    c_time = [0]*n
    a_time = a_time[::]
    cpu_clock = 0
    t_p = 0 
    c_p = a_time.index(min(a_time))
    while t_p < n:
        if cpu_clock >= a_time[c_p]: 
            cpu_clock += b_time[c_p]
            c_time[c_p] = cpu_clock
            a_time[c_p] = float('inf')
            c_p = a_time.index(min(a_time))
            t_p += 1
        else:
            while cpu_clock < a_time[c_p]:
                cpu_clock +=1
    
    return c_time

def turn_around_time(c_time,a_time):
    return [(c-a) for c,a in zip(c_time,a_time)]

def waiting_time(t_time,b_time):
    return [(t-b) for t,b in zip(t_time,b_time)]

def print_all(p_list,a_list,b_list,c_list,t_list,w_list):
    m = [p_list,a_list,b_list,c_list,t_list,w_list]
    m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    print('\n'*2)
    print(tabulate(m ,headers= ['Process List','Arrival Time',' Burst Time', 'Completion Time', 'Turn Over Time'  ,'Waiting Time'],tablefmt="github"),end='\n\n')
    print("Average Waiting Time = "+ str(sum(w_list)/len(w_list)),"Average Turn Around Time = "+ str(sum(t_list)/len(t_list)),sep='\n')

def FCFS():
    n = int(input("Number of Processes"))
    arrival_time = [ int(input(f"Arrival Time for P{i+1}")) for i in range(n)]    
    burst_time = [ int(input(f"Burst Time for P{i+1}")) for i in range(n)]
    c_t = completion_time(n,arrival_time,burst_time)
    ta_t = turn_around_time(c_t,arrival_time)
    w_t = waiting_time(ta_t,burst_time)
    print_all([(i+1) for i in range(n)],arrival_time,burst_time,c_t,ta_t,w_t)

if __name__ == "__main__":
    FCFS()