
undefined8 main(void)

{
  char cVar1;
  undefined8 uVar2;
  long in_FS_OFFSET;
  undefined8 local_80;
  undefined8 local_78;
  undefined8 local_70;
  undefined8 local_68;
  FILE *local_60;
  char local_58 [72];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  setbuf(stdin,(char *)0x0);
  setbuf(stdout,(char *)0x0);
  setbuf(stderr,(char *)0x0);
  puts("Psssst, I heard you\'re looking for a flag. I can trade a flag for 4 keys, whaddaya say?");
  printf("Key 1: ");
  local_80 = 0;
  __isoc99_scanf(&DAT_00102068,&local_80);
  printf("Key 2: ");
  local_78 = 0;
  __isoc99_scanf(&DAT_00102068,&local_78);
  printf("Key 3: ");
  local_70 = 0;
  __isoc99_scanf(&DAT_00102068,&local_70);
  printf("Key 4: ");
  local_68 = 0;
  __isoc99_scanf(&DAT_00102068,&local_68);
  cVar1 = check1(local_80);
  if (cVar1 != '\0') {
    cVar1 = check2(local_80,local_78);
    if (cVar1 != '\0') {
      cVar1 = check3(local_70);
      if (cVar1 != '\0') {
        cVar1 = check4(local_70,local_68);
        if (cVar1 != '\0') {
          local_60 = fopen("flag.txt","r");
          fgets(local_58,0x40,local_60);
          printf("Thanks for the keys! Here\'s your flag as promised: %s\n",local_58);
          uVar2 = 0;
          goto LAB_0010168d;
        }
      }
    }
  }
  puts("Those aren\'t valid keys! >:(");
  uVar2 = 1;
LAB_0010168d:
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar2;
}

