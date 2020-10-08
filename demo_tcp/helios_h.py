from ctypes import *  # c_ubyte, BigEndianStructure

# define
HEADER_MSIZE = 8
PAYLOAD_MSIZE = 1024

# enum kDT
kDT_NULL  = 0x00
kDT_MMAP  = 0x01
kDT_MEM   = 0x02
kDT_TEXT  = 0x03
kDT_PARAM = 0x04
kDT_RFSP  = 0x05
kDT_LNCH  = 0x06
kDT_PAUSE = 0x07
kDT_PLAY  = 0x08
kDT_CONT  = 0x09
kDT_DESC  = 0x0A
# 0x0B-0x0F
kDT_FHDR  = 0x10
kDT_ADC   = 0x11
kDT_RANGE = 0x12
kDT_DPPLR = 0x13
kDT_FFT3D = 0x14
kDT_HIST  = 0x15
kDT_PEAK  = 0x16
kDT_MEAS  = 0x17
kDT_CAP   = 0x18

# enum kPDT
kPDT_BIN  = 0x00
kPDT_STR  = 0x01
kPDT_JSON = 0x02

# enum
kPad      = 0x00
kRead     = 0
kWrite    = 1
kOngo     = 0
kDone     = 1
kFalse    = 0
kTrue     = 1


class helios_hdr(BigEndianStructure):
  '''
  big-endian, 64-bit
  struct helios_hdr {
    uint8_t dt;       /* Data type           */
    uint8_t rw:   1;  /* Read/Write          */
    uint8_t rt:   1;  /* Real time           */
    uint8_t rsvd: 4;  /* Reserved            */
    uint8_t pdt:  2;  /* Primitive data type */
    uint8_t arg[6];   /* Helios arguments    */
  }
  '''
  _pack_ = 1
  _fields_ = [
    ('dt',   c_ubyte),
    ('rw',   c_ubyte, 1),
    ('rt',   c_ubyte, 1),
    ('rsvd', c_ubyte, 4),
    ('pdt',  c_ubyte, 2),
    ('arg',  c_ubyte * 6)
  ]