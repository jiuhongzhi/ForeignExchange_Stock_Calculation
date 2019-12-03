# support_and_resistance_shaluosi.py
# ------FxPro----8.26------------
OPEN = 1.10783
HIGH = 1.11525
LOW = 1.10509
CLOSE = 1.11438
PP = (HIGH + CLOSE + LOW) / 3
R1 = 2 * PP - LOW
S1 = 2 * PP - HIGH
R2 = PP + (R1 - S1)
S2 = PP - (R1 - S1)
R3 = HIGH + 2 * (PP - LOW)
S3 = LOW - 2 * (HIGH - PP)
print('R3 = ' + str(R3))
print('R2 = ' + str(R2))
print('R1 = ' + str(R1))
print('PP = ' + str(PP))
print('S1 = ' + str(S1))
print('S2 = ' + str(S2))
print('S3 = ' + str(S3))








