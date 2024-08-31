
bool check3(ulong param_1)

{
  byte bVar1;
  uint uVar2;
  bool bVar3;
  ulong local_40;
  ulong local_28;
  ulong local_20;
  
  if ((long)param_1 < 0) {
    local_28 = 0;
    local_40 = param_1;
    while (local_40 != 0) {
      uVar2 = (uint)local_40;
      local_40 = local_40 >> 1;
      bVar1 = 0;
      for (local_20 = local_28; local_20 != 0; local_20 = local_20 >> 1) {
        bVar1 = bVar1 + 1;
      }
      local_28 = local_28 | (long)(int)(uVar2 & 1) << (bVar1 & 0x3f);
    }
    bVar3 = param_1 == local_28;
  }
  else {
    bVar3 = false;
  }
  return bVar3;
}

