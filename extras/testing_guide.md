---
geometry: margin=1in
---

# Stick Board

## Continuity test

Check continuity between points connected in the two images:

### 3.3V net

![](3.3v.png)

### GND net

![](gnd.png)

## Smoke test

Supply 3.3V power to the V+ pin and the GND pin at the highlighted test points. 
Verify all boards behave "normally": no magic smoke, draws nonzero current, does not draw more than 1A.
Components may be warm but should not be hot to touch after running for any amount of time.

![](testpoints.png)