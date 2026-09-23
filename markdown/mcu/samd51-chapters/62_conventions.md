# 60. Conventions

*Source: `Atmel-SAMD51.pdf`, pages 2112-2114 — SAMD51 family datasheet*

                                              SAM D5x/E5x Family Data Sheet
                                                                                          Conventions


60.    Conventions


60.1   Numerical Notation
       Table 60-1. Numerical Notation

        Symbol                                  Description
        165                                     Decimal number
        0b0101                                  Binary number (example 0b0101 = 5 decimal)
        '0101'                                  Binary numbers are given without prefix if
                                                unambiguous
        0x3B24                                  Hexadecimal number
        X                                       Represents an unknown or do not care value
        Z                                       Represents a high-impedance (floating) state for
                                                either a signal or a bus



60.2   Memory Size and Type
       Table 60-2. Memory Size and Bit Rate

        Symbol                                  Description
        KB (kbyte)                              kilobyte (210 = 1024)
        MB (Mbyte)                              megabyte (220 = 1024*1024)
        GB (Gbyte)                              gigabyte (230 = 1024*1024*1024)
        b                                       bit (binary '0' or '1')
        B                                       byte (8 bits)
        1kbit/s                                 1,000 bit/s rate (not 1,024 bit/s)
        1Mbit/s                                 1,000,000 bit/s rate
        1Gbit/s                                 1,000,000,000 bit/s rate
        word                                    32 bit
        half-word                               16 bit



60.3   Frequency and Time
       Table 60-3. Frequency and Time

        Symbol                                  Description
        kHz                                     1 kHz = 103 Hz = 1,000 Hz




       © 2019 Microchip Technology Inc.       Datasheet                              DS60001507E-page 2112
                                                             SAM D5x/E5x Family Data Sheet
                                                                                                         Conventions

       ...........continued
        Symbol                                                    Description
        KHz                                                       1 KHz = 1,024 Hz, 32 KHz = 32,768 Hz
        MHz                                                       1 MHz = 106 Hz = 1,000,000 Hz
        GHz                                                       1 GHz = 109 Hz = 1,000,000,000 Hz
        s                                                         second
        ms                                                        millisecond
        µs                                                        microsecond
        ns                                                        nanosecond



60.4   Registers and Bits
       Table 60-4. Register and Bit Mnemonics

        Symbol              Description
        R/W                 Read/Write accessible register bit. The user can read from and write to this bit.
        R                   Read-only accessible register bit. The user can only read this bit. Writes will be
                            ignored.
        W                   Write-only accessible register bit. The user can only write this bit. Reading this bit will
                            return an undefined value.
        BIT                 Bit names are shown in uppercase. (Example ENABLE)
        FIELD[n:m]          A set of bits from bit n down to m. (Example: PINA[3:0] = {PINA3, PINA2, PINA1,
                            PINA0}
        Reserved            Reserved bits are unused and reserved for future use. For compatibility with future
                            devices, always write reserved bits to zero when the register is written. Reserved bits
                            will always return zero when read.
                            Reserved bit field values must not be written to a bit field. A reserved value will not be
                            read from a read-only bit field.
                            Do not write any value to reserved bits of a fuse.

        PERIPHERALi If several instances of a peripheral exist, the peripheral name is followed by a number
                    to indicate the number of the instance in the range 0-n. PERIPHERAL0 denotes one
                    specific instance.
        Reset               Value of a register after a Power-on Reset. This is also the value of registers in a
                            peripheral after performing a software Reset of the peripheral, except for the Debug
                            Control registers.




       © 2019 Microchip Technology Inc.                        Datasheet                            DS60001507E-page 2113
                                                      SAM D5x/E5x Family Data Sheet
                                                                                                 Conventions

...........continued
 Symbol              Description
 SET/CLR             Registers with SET/CLR suffix allows the user to clear and set bits in a register without
                     doing a read-modify-write operation. These registers always come in pairs. Writing a ‘1’
                     to a bit in the CLR register will clear the corresponding bit in both registers, while
                     writing a ‘1’ to a bit in the SET register will set the corresponding bit in both registers.
                     Both registers will return the same value when read. If both registers are written
                     simultaneously, the write to the CLR register will take precedence.




© 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 2114
