
bool check2(ulong param_1,ulong param_2)

{
  bool bVar1;
  ulong local_28;
  ulong local_20;
  int local_18;
  int local_14;
  ulong local_10;
  
  if (param_2 == 0) {
    bVar1 = false;
  }
  else {
    local_18 = 0;
    for (local_10 = param_2; local_10 != 0; local_10 = local_10 >> 2) {
      local_18 = local_18 + ((uint)local_10 & 1);
    }
    if (local_18 < 7) {
      bVar1 = false;
    }
    else {
      local_14 = 0;
      for (local_20 = param_1; local_28 = param_2, local_20 != 0; local_20 = local_20 / 10) {
        local_14 = local_14 +
                   (int)local_20 + ((int)(local_20 / 10 << 2) + (int)(local_20 / 10)) * -2;
      }
      for (; local_28 != 0; local_28 = local_28 / 10) {
        local_14 = local_14 -
                   ((int)local_28 + ((int)(local_28 / 10 << 2) + (int)(local_28 / 10)) * -2);
      }
      bVar1 = local_14 == 0x69;
    }
  }
  return bVar1;
}

