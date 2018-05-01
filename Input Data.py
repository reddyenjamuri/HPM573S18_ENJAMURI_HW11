import numpy as np

POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 15     # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate
DELTA_T = 1/5      # years (length of time step, how frequently you look at the patient)


# Part 1: Non-stroke annual mortality rate
a = -np.log(1-(18*100 - 36.2)/100000)

# Part 2: Rate of stroke (annual)
stroke_rate = -np.log(1-15/1000)

# Part 3: Rate of transition from Well state to Stroke state (annual)
b = stroke_rate*0.9
#         Rate of transition from Well state to Stroke Death state (annual)
c = stroke_rate*0.1

# Part 4: Rate of recurrent stroke (annual)
recur_stroke_rate = -np.log(1-0.17)/5

# Part 5: Rate of transition from Post-stroke state to Stroke state (annual)
d = recur_stroke_rate*0.8
#         Rate of transition from Post-stroke state to Stroke Death state (annual)
e = recur_stroke_rate*0.2

# Part 6: Rate of transition from Stroke state to Post-stroke state (annual)
f = 1/(1/52)

# transition rate matrix
TRANS_MATRIX = [
    [None,  b,     0.0,    c,      a],     # Well
    [0.0,   None,  f,      0.0,    0.0],     # Stroke
    [0.0,   d,     None,   e,      a],     # Post-Stroke
    [0.0,   0.0,   0.0,    None,   0.0],   # Stroke Death
    [0.0,   0.0,   0.0,    0.0,    None],  # Death
    ]


# RR of treatment in reducing incidence of stroke and stroke death while in Post-Stroke state
STROKE_RR = 0.75
# RR of treatment in increasing mortality due to bleeding
BLEEDING_RR = 1.05

# transition rate matrix
TRANS_MATRIX_ANTICOAG = [
    [None,   b,            0.0,     c,       a],               # Well
    [0.0,    None,         f,       0.0,     a],               # Stroke
    [0.0,    d*STROKE_RR,  None,    e,       a*BLEEDING_RR],   # Post-Stroke
    [0.0,    0.0,          0.0,     None,    0.0],             # Stroke Death
    [0.0,    0.0,          0.0,     0.0,     None],            # Death
    ]

# annual cost of each health state
ANNUAL_STATE_COST = [
    0,        # Well
    5000.0,   # Stroke
    200.0,    # Post-Stroke
    0,        # Stroke Death
    0         # Death
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1,         # Well
    0.8865,    # Stroke
    0.9,       # Post-Stroke
    0,         # Stroke Death
    0          # Death
    ]

# annual drug costs
Anticoagulant_COST = 2000.0

# annual probability of background mortality (number per 100,000 PY)
ANNUAL_PROB_BACKGROUND_MORT = (18*100-36.2)/100000
