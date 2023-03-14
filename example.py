import pulp

from my_scip_api import SCIP as MySCIP


scip_path = "scip"


P = pulp.LpProblem(sense=pulp.LpMaximize)

x = pulp.LpVariable(name="x", lowBound=0)
y = pulp.LpVariable(name="y", lowBound=0)

P += x + 2 * y <= 1
P += 3 * x + y <= 1

P += x + y

status = P.solve(solver=MySCIP(path=scip_path, timeLimit=10))

print(status, pulp.value(x), pulp.value(y))
