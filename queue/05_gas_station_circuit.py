def canCompleteCircuit(gas, cost):
    total_gas=0
    curr_gas=0
    start=0
    for i in range(len(gas)):
        diff=gas[i]-cost[i]
        total_gas+=diff
        curr_gas+=diff
        if curr_gas<0:
            start=i+1
            curr_gas=0
    return start if total_gas>=0 else -1

gas = list(map(int, input("Enter gas array: ").split()))
cost = list(map(int, input("Enter cost array: ").split()))

result = canCompleteCircuit(gas, cost)

if result == -1:
    print("It is NOT possible to complete the circuit.")
else:
    print(f"Start at gas station index {result} to complete the circuit.")
