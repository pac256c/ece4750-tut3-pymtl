#=========================================================================
# RegIncr
#=========================================================================
# This is a simple model for a registered incrementer. An eight-bit value
# is read from the input port, registered, incremented by one, and
# finally written to the output port.

from pymtl import *

class RegIncr( Model ):

  # Constructor

  def __init__( s, nbits=8 ):

    # Port-based interface

    s.in_ = InPort  ( Bits(nbits) )
    s.out = OutPort ( Bits(nbits) )

    # Sequential logic

    s.reg_out = Wire( Bits(nbits) )

    @s.tick
    def block1():
      if s.reset:
        s.reg_out.next = 0
      else:
        s.reg_out.next = s.in_

    # Combinational logic 
    @s.combinational
    def block2():
      s.out.value = s.reg_out + 1

  def line_trace(s):
    return "in:{} ({}) out:{}".format(s.in_, s.reg_out, s.out)
