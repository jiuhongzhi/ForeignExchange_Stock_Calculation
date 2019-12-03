# support_and_resistance_baidu.py

# ------HY---8.23-------------
OPEN = 1.10882
HIGH = 1.11124
LOW = 1.10627
CLOSE = 1.10807
# ------FxPro----8.23------------
OPEN = 1.10832
HIGH = 1.11124
LOW = 1.10628
CLOSE = 1.10783
# ------ICMarkets----8.23------------
OPEN = 1.10843
HIGH = 1.11134
LOW = 1.10637
CLOSE = 1.10793
# ------FxPro----8.26------------
OPEN = 1.10783
HIGH = 1.11525
LOW = 1.10509
CLOSE = 1.11438
PP = (HIGH + LOW + CLOSE) / 3
R1 = 2 * PP - LOW
R2 = PP + HIGH - LOW
R3 = 2 * PP + HIGH - 2 * LOW
S1 = 2 * PP - HIGH
S2 = PP + LOW - HIGH
S3 = 2 * PP + LOW - 2 * HIGH
print('R3 = ', R3)
print('R2 = ', R2)
print('R1 = ', R1)
print('PP = ', PP)
print('S1 = ', S1)
print('S2 = ', S2)
print('S3 = ', S3)








