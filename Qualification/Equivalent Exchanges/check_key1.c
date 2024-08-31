
bool check1(ulong param_1)

{
  ulong local_20;
  int local_c;
  
  local_c = 0;
  for (local_20 = param_1; local_20 != 0; local_20 = local_20 / 10) {
    local_c = local_c + 1;
  }
  return 0xf < local_c;
}

