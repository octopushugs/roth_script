# Script to calculate approximate allowable Roth IRA contributions
from constants import *
from math import *

supplied_agi = int(
  input('Enter your estimated Adjusted Gross Income: ').replace(',', '')
)
response_string_list = []

# Handle responses for single filing outside the provided range
if supplied_agi < SINGLE_PHASE_OUT_RANGE_START():
  response_string_list.append(
    (f"If you're filing as Single you may contribute the maximum: ${MAX_CONTRIBUTION()}")
  )

elif supplied_agi > SINGLE_PHASE_OUT_RANGE_END():
  response_string_list.append(
    "If you're filing as Single you can make no contributions this year"
  )

# Handle responses for married jointlg filing outside the provided range
if supplied_agi < MJ_PHASE_OUT_RANGE_START():
  response_string_list.append(
    (f"If you're filing as Married Jointly you may contribute the maximum: ${MAX_CONTRIBUTION()}")
  )
elif supplied_agi > MJ_PHASE_OUT_RANGE_END():
  response_string_list.append(
    "If you're filing as Married Jointly you may make no contributions this year"
  )

# Handle when agi is in the goldilocks zone
if SINGLE_PHASE_OUT_RANGE_START() <= supplied_agi <= SINGLE_PHASE_OUT_RANGE_END():
  single_limit = run_calculation(supplied_agi, 'single')
  response_string_list.append(
    (f"If you're filing as Single you may contribute a reduced amount: ${single_limit}")
  )

if MJ_PHASE_OUT_RANGE_START() <= supplied_agi <= MJ_PHASE_OUT_RANGE_END():
  mj_limit = run_calculation(supplied_agi, 'married_jointly')
  response_string_list.append(
    (f"If you're filing as Married Jointly you may contribute a reduced amount: ${mj_limit}")
  )

for string in response_string_list:
  print(string)

quit()

