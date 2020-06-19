from constants import *

# Runs the actual calculation here according to the IRS rules, found here:
# https://www.irs.gov/retirement-plans/amount-of-roth-ira-contributions-that-you-can-make-for-2019
# Accepts an AGI as an int or double and a string filing type to determine
# which constants to use
def run_calculation(agi, filing_type):
  if filing_type == 'single' :
    phase_out_start = SINGLE_PHASE_OUT_RANGE_START()
    phase_out_end = SINGLE_PHASE_OUT_RANGE_END()
  else:
    phase_out_start = MJ_PHASE_OUT_RANGE_START()
    phase_out_end = MJ_PHASE_OUT_RANGE_END()

  # Magic math for the calculation:
  # 1. Start with your modified AGI (MAGI).
  # 2. Subtract phase out range start from MAGI
  # 3. Divide by 15000
  # 4. Multiply by the max contribution limit
  # 5. Subtract from the max contribution
  step_2_val = agi - phase_out_start
  step_3_val = step_2_val / 15000
  step_4_val = step_3_val * MAX_CONTRIBUTION()

  return round((MAX_CONTRIBUTION() - step_4_val), 3)
