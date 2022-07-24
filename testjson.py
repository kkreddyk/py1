import json
import numpy as np
val='{"k":"v","a":"b"}'
print(json.loads(val)["k"])

print(json.dumps(43))

a=np.array([1,2])
print(a)