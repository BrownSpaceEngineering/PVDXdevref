# 42. AES – Advanced Encryption Standard

*Source: `Atmel-SAMD51.pdf`, pages 1412-1442 — SAMD51 family datasheet*

                                                          SAM D5x/E5x Family Data Sheet
                                                                  AES – Advanced Encryption Standard


42.    AES – Advanced Encryption Standard

42.1   Overview
       The Advanced Encryption Standard peripheral (AES) provides a means for symmetric-key encryption of
       128-bit blocks, in compliance to NIST specifications.
       A symmetric-key algorithm requires the same key for both encryption and decryption.
       Different key sizes are supported. The key size determines the number of repetitions of transformation
       rounds that convert the input (called the "plaintext") into the final output ("ciphertext"). The number of
       rounds of repetition is as follows:
         • 10 rounds of repetition for 128-bit keys
         • 12 rounds of repetition for 192-bit keys
         • 14 rounds of repetition for 256-bit keys



42.2   Features
         •   Compliant with FIPS Publication 197, Advanced Encryption Standard (AES)
         •   128/192/256 bit cryptographic key supported
         •   Encryption time of 57/67/77 cycles with 128-bit/192-bit/256-bit cryptographic key
         •   Five confidentiality modes of operation as recommended in NIST Special Publication 800-38A
         •   Electronic Code Book (ECB)
         •   Cipher Block Chaining (CBC)
         •   Cipher Feedback (CFB)
         •   Output Feedback (OFB)
         •   Counter (CTR)
         •   Supports Counter with CBC-MAC (CCM/CCM*) mode for authenticated encryption
         •   8, 16, 32, 64, 128-bit data sizes possible in CFB mode
         •   Optional (parameter) Galois Counter mode (GCM) encryption and authentication




       © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 1412
                                                                 SAM D5x/E5x Family Data Sheet
                                                                            AES – Advanced Encryption Standard


42.3   Block Diagram
       Figure 42-1. AES Block Diagram




                                                PLAINTEXT                                            CIPHERTEXT



                                              ADD ROUND KEY                                        ADD ROUND KEY




                                                SUBBYTES                                           INV SHIFT ROWS
                           ENCRYPTION ROUND




                                                                                DECRYPTION ROUND
                                               SHIFT ROWS                                           INV SUBBYTES

                                                              Nr-1 rounds                                                     Nr-1 rounds


                                               MIX COLUMNS                                         ADD ROUND KEY




          ENCRYPTION                          ADD ROUND KEY       DECRYPTION                       INV MIX COLUMNS




                                                SUBBYTES                                           INV SHIFT ROWS
                           FINAL ROUND




                                                                                FINAL ROUND




                                               SHIFT ROWS                                           INV SUBBYTES




                                              ADD ROUND KEY                                        ADD ROUND KEY




                                               CIPHERTEXT                                            PLAINTEXT




       © 2019 Microchip Technology Inc.                            Datasheet                                         DS60001507E-page 1413
                                                            SAM D5x/E5x Family Data Sheet
                                                                    AES – Advanced Encryption Standard


42.4     Signal Description
         Not applicable.



42.5     Product Dependencies
         In order to use this AES module, other parts of the system must be configured correctly, as described
         below.

42.5.1   I/O Lines
         Not applicable.

42.5.2   Power Management
         The AES will continue to operate in Standby sleep mode, if it's source clock is running.
         The AES interrupts can be used to wake up the device from Standby sleep mode. Refer to the Power
         Manager chapter for details on the different sleep modes.
         AES is clocked only on the following conditions:
           • When the DMA is enabled.
           • Whenever there is an APB access for any read and write operation to the AES registers. (Not in
             Standby sleep mode.)
           • When the AES is enabled & encryption/decryption is ongoing.

42.5.3   Clocks
         The AES bus clock (CLK_AES_APB) can be enabled and disabled in the Main Clock module, and the
         default state of CLK_AES_APB can be found in Peripheral Clock Masking. The module is fully clocked by
         CLK_AES_APB.
         Related Links
         15.6.2.6 Peripheral Clock Masking

42.5.4   DMA
         The AES has two DMA request lines; one for input data, and one for output data. They are both
         connected to the DMA Controller (DMAC). These DMA request triggers will be acknowledged by the
         DMAC ACK signals. Using the AES DMA requests requires the DMA Controller to be configured first.
         Refer to the device DMA documentation.

42.5.5   Interrupts
         The interrupt request line is connected to the interrupt controller. Using the AES interrupt requires the
         interrupt controller to be configured first. Refer to the Processor and Architecture chapter for details.
         All the AES interrupts are synchronous wake-up sources. See Sleep Mode Controller for details.
         Related Links
         18.6.3.3 Sleep Mode Controller

42.5.6   Events
         Not applicable.




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1414
                                                            SAM D5x/E5x Family Data Sheet
                                                                    AES – Advanced Encryption Standard

42.5.7   Debug Operation
         When the CPU is halted in debug mode, the AES module continues normal operation. If the AES module
         is configured in a way that requires it to be periodically serviced by the CPU through interrupts or similar,
         improper operation or data loss may result during debugging. The AES module can be forced to halt
         operation during debugging.

42.5.8   Register Access Protection
         All registers with write-access are optionally write-protected by the peripheral access controller (PAC),
         except the
         following register:
           • Interrupt Flag Register (INTFLAG)
         Write-protection is denoted by the Write-Protected property in the register description.
         Write-protection does not apply to accesses through an external debugger. Refer to PAC - Peripheral
         Access Controller chapter for details.
         Related Links
         27. PAC - Peripheral Access Controller

42.5.9   Analog Connections
         Not applicable.



42.6     Functional Description

42.6.1   Principle of Operation
         The following is a high level description of the algorithm. These are the steps:
           • KeyExpansion: Round keys are derived from the cipher key using Rijndael's key schedule.
           • InitialRound:
               – AddRoundKey: Each byte of the state is combined with the round key using bitwise XOR.
           • Rounds:
               – SubBytes: A non-linear substitution step where each byte is replaced with another according to a
                   lookup table.
               – ShiftRows: A transposition step where each row of the state is shifted cyclically a certain number
                   of steps.
               – MixColumns: A mixing operation which operates on the columns of the state, combining the four
                   bytes in each column.
               – AddRoundKey
           • Final Round (no MixColumns):
               – SubBytes
               – ShiftRows
               – AddRoundKey
         The relationship between the module's clock frequency and throughput (in bytes per second) is given by:
         Clock Frequency = (Throughput/2) x (Nr+1) for 2 byte parallel processing
         Clock Frequency = (Throughput/4) x (Nr+1) for 4 byte parallel processing




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1415
                                                              SAM D5x/E5x Family Data Sheet
                                                                      AES – Advanced Encryption Standard

          where Nr is the number of rounds, depending on the key length.

42.6.2    Basic Operation

42.6.2.1 Initialization
          The following register is enable-protected:
           • Control A (CTRLA)
          Enable-protection is denoted by the Enable-Protected property in the register description.
42.6.2.2 Enabling, Disabling, and Resetting
          The AES module is enabled by writing a one to the Enable bit in the Control A register (CTRLA.ENABLE).
          The module is disabled by writing a zero to CTRLA.ENABLE. The module is reset by writing a one to the
          Software Reset bit in the Control A register (CTRLA.SWRST).
42.6.2.3 Basic Programming
          The CIPHER bit in the Control A Register (CTRLA.CIPHER) allows selection between the encryption and
          the decryption processes. The AES is capable of using cryptographic keys of 128/192/256 bits to encrypt
          and decrypt data in blocks of 128 bits. The Key Size (128/192/256) can be programmed in the KEYSIZE
          field in the Control A Register (CTRLA.KEYSIZE). This 128-bit/192-bit/256-bit key is defined in the Key
          Word Registers (KEYWORD). By setting the XORKEY bit of CTRLA register, keyword can be updated
          with the resulting XOR value of user keyword and previous keyword content.
          The input data for processing is written to a data buffer consisting of four 32-bit registers through the Data
          register address. The data buffer register (note that input and output data shares the same data buffer
          register) that is written to when the next write is performed is indicated by the Data Pointer in the Data
          Buffer Pointer (DATABUFPTR) register. This field is incremented by one or wrapped by hardware when a
          write to the DATA register address is performed. This field can also be programmed, allowing the user
          direct control over which input buffer register to write to. Note that when AES module is in the CFB
          operation mode with the data segment size less than 128 bits, the input data must be written to the first
          (DATABUFPTR = 0) and/or second (DATABUFPTR = 1) input buffer registers (see Table 42-1).
          The input to the encryption processes of the CBC, CFB and OFB modes includes, in addition to the
          plaintext, a 128-bit data block called the Initialization Vector (IV), which must be set in the Initialization
          Vector Registers (INTVECT). Additionally, the GCM mode 128-bit authentication data needs to be
          programmed. The Initialization Vector is used in the initial step in the encryption of a message and in the
          corresponding decryption of the message. The Initialization Vector Registers are also used by the
          Counter mode to set the counter value.
          It is necessary to notify AES module whenever the next data block it is going to process is the beginning
          of a new message. This is done by writing a one to the New Message bit in the Control B register
          (CTRLB.NEWMSG).
          The AES modes of operation are selected by setting the AESMODE field in the Control A Register
          (CTRLA.AESMODE). In Cipher Feedback Mode (CFB), five data sizes are possible (8, 16, 32, 64 or 128
          bits), configurable by means of the CFBS field in the Control A Register (CTRLA.CFBS). In Counter
          mode, the size of the block counter embedded in the module is 16 bits. Therefore, there is a rollover after
          processing 1 megabyte of data. The data pre-processing, post-processing and data chaining for the
          concerned modes are automatically performed by the module.
          When data processing has completed, the Encryption Complete bit in the Interrupt Flag register
          (INTFLAG.ENCCMP) is set by hardware (which triggers an interrupt request if the corresponding interrupt
          is enabled). The processed output data is read out through the Output Data register (DATA) address from
          the data buffer consisting of four 32-bit registers. The data buffer register that is read from when the next




         © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1416
                                                           SAM D5x/E5x Family Data Sheet
                                                                    AES – Advanced Encryption Standard

        read is performed is indicated by the Data Pointer field in the Data Buffer Pointer register
        (DATABUFPTR). This field is incremented by one or wrapped by hardware when a read from the DATA
        register address is performed. This field can also be programmed, giving the user direct control over
        which output buffer register to read from. Note that when AES module is in the CFB operation mode with
        the data segment size less than 128 bits, the output data must be read from the first (DATABUFPTR = 0)
        and/or second (DATABUFPTR = 1) output buffer registers (see Table 42-1). The Encryption Complete bit
        (INTFLAG.ENCCMP) is cleared by hardware after the processed data has been read from the relevant
        output buffer registers.
        Table 42-1. Relevant Input/Output Data Registers for Different Confidentiality Modes

         Confidentiality Mode                   Relevant Input / Output Data Registers
         ECB                                    All
         CBC                                    All
         OFB                                    All
         128-bit CFB                            All
         64-bit CFB                             First and Second
         32-bit CFB                             First
         16-bit CFB                             First
         8-bit CFB                              First
         CTR                                    All

42.6.2.4 Start Modes
        The Start mode field in the Control A Register (CTRLA.STARTMODE) allows the selection of encryption
        start mode.
          1.   Manual Start Mode
               In the Manual Start Mode the sequence is as follows:
               1.1.    Write the 128/192/256 bit key in the Key Register (KEYWORD)
               1.2.    Write the initialization vector or counter in the Initialization Vector Register (INTVECT). The
                       initialization vector concerns all modes except ECB
               1.3.    Enable interrupts in Interrupt Enable Set Register (INTENSET), depending on whether an
                       interrupt is required or not at the end of processing.
               1.4.    Write the data to be encrypted or decrypted in the Data Registers (DATA).
               1.5.    Set the START bit in Control B Register (CTRLB.START) to begin the encryption or the
                       decryption process.
               1.6.    When the processing completes, the Encryption Complete bit in the Interrupt Flag Register
                       (INTFLAG.ENCCMP) raises. If Encryption Complete interrupt has been enabled, the
                       interrupt line of the AES is activated.
               1.7.    When the software reads one of the Output Data Registers (DATA), INTFLAG.ENCCMP bit
                       is automatically cleared.
          2.   Auto start Mode
               The Auto Start Mode is similar to the manual one, except in this mode, as soon as the correct
               number of input data registers is written, processing is automatically started without setting the
               START bit in the Control B Register. DMA operation uses this mode.




        © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1417
                                                            SAM D5x/E5x Family Data Sheet
                                                                    AES – Advanced Encryption Standard

          3.   Last Output Data Mode (LOD)
               This mode is used to generate message authentication code (MAC) on data in CCM mode of
               operation. The CCM mode combines counter mode for encryption and CBC-MAC generation for
               authentication.
        When LOD is disabled in CCM mode then counter mode of encryption is performed on the input data
        block.
        When LOD is enabled in CCM mode then CBC-MAC generation is performed. Zero block is used as the
        initialization vector by the hardware. Also software read from the Output Data Register (DATA) is not
        required to clear the ENCCMP flag. The ENCCMP flag is automatically cleared by writing into the Input
        Data Register (DATA). This allows retrieval of only the last data in several encryption/decryption
        processes. No output data register reads are necessary between each block of encryption/decryption
        process.
        Note that assembling message depending on the security level identifier in CCM* has to be done in
        software.
42.6.2.5 Computation of last Nk words of expanded key
        The AES algorithm takes the cryptographic key provided by the user and performs a Key Expansion
        routine to generate an expanded key. The expanded key contains a total of 4(Nr + 1) 32-bit words, where
        the first Nk (4/6/8 for a 128-/192-/256-bit key) words are the user-provided key. For data encryption, the
        expanded key is used in the forward direction, i.e., the first four words are used in the initial round of data
        processing, the second four words in the first round, the third four words in the second round, and so on.
        On the other hand, for data decryption, the expanded key is used in the reverse direction, i.e.,the last four
        words are used in the initial round of data processing, the last second four words in the first round, the
        last third four words in the second round, and so on.
        To reduce gate count, the AES module does not generate and store the entire expanded key prior to data
        processing. Instead, it computes on-the-fly the round key (four 32-bit words) required for the current
        round of data processing. In general, the round key for the current round of data processing can be
        computed from the Nk words of the expanded key generated in the previous rounds. When AES module
        is operating in the encryption mode, the round key for the initial round of data processing is simply the
        user-provided key written to the KEY registers. On the other hand, when AES module is operating in the
        decryption mode, the round key for the initial round of data processing is the last four words of the
        expanded key, which is not available unless AES module has performed at least one encryption process
        prior to operating in the decryption mode.
        In general, the last Nk words of the expanded key must be available before decryption can start. If
        desired, AES module can be instructed to compute the last Nk words of the expanded key in advance by
        writing a one to the Key Generate (KEYGEN) bit in the CTRLA register (CTRLA.KEYGEN). The
        computation takes Nr clock cycles. Alternatively, the last Nk words of the expanded key can be
        automatically computed by AES module when a decryption process is initiated if they have not been
        computed in advance or have become invalid. Note that this will introduce a latency of Nr clock cycles to
        the first decryption process.
42.6.2.6 Hardware Countermeasures against Differential Power Analysis Attacks
        The AES module features four types of hardware countermeasures that are useful for protecting data
        against differential power analysis attacks:
          • Type 1: Randomly add one cycle to data processing
          • Type 2: Randomly add one cycle to data processing (other version)




        © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1418
                                                         SAM D5x/E5x Family Data Sheet
                                                                 AES – Advanced Encryption Standard

           • Type 3: Add a random number of clock cycles to data processing, subject to a maximum of 11/13/15
             clock cycles for key sizes of 128/192/256 bits
           • Type 4: Add random spurious power consumption during data processing
         By default, all countermeasures are enabled. One or more of the countermeasures can be disabled by
         programming the Countermeasure Type field in the Control A (CTRLA.CTYPE) register. The
         countermeasures use random numbers generated by a deterministic random number generator
         embedded in AES module. The seed for the random number generator is written to the RANDSEED
         register. Note also that a new seed must be written after a change in the keysize. Note that enabling
         countermeasures reduces AES module’s throughput. In short, the throughput is highest with all the
         countermeasures disabled. On the other hand, with all of the countermeasures enabled, the best
         protection is achieved but the throughput is worst.

42.6.3   Galois Counter Mode (GCM)
         GCM is comprised of the AES engine in CTR mode along with a universal hash function (GHASH engine)
         that is defined over a binary Galois field to produce a message authentication tag. The GHASH engine
         processes data packets after the AES operation. GCM provides assurance of the confidentiality of data
         through the AES Counter mode of operation for encryption. Authenticity of the confidential data is
         assured through the GHASH engine. Refer to the NIST Special Publication 800-38D Recommendation
         for more complete information.




         © 2019 Microchip Technology Inc.                  Datasheet                        DS60001507E-page 1419
                                                     SAM D5x/E5x Family Data Sheet
                                                                 AES – Advanced Encryption Standard




                 Counter 0            Incr32       Counter 1            Incr32               Counter 2




                 CIPH(K)                            CIPH(K)                                   CIPH(K)




                                    Plaintext 1        +               Plaintext 2               +



                                                  Ciphertext 1                              Ciphertext 2
    Encryption




                                                       +                                         +



                              GF128Mult(H)        GF128Mult(H)                              GF128Mult(H)




                               Auth Data 1                             Len (A) || Len (C)        +



                                                                                            GF128Mult(H)



                                                                                                 +



                                                                                              Auth Tag
   Authentication




© 2019 Microchip Technology Inc.                       Datasheet                               DS60001507E-page 1420
                                                            SAM D5x/E5x Family Data Sheet
                                                                    AES – Advanced Encryption Standard

42.6.3.1 GCM Operation
42.6.3.1.1 Hashkey Generation
           • Configure CTRLA register as follows:
              1. CTRLA.STARTMODE as Manual (Auto for DMAC)
              2. CTRLA.CIPHER as Encryption
              3. CTRLA.KEYSIZE as per the key used
              4. CTRLA.AESMODE as ECB
              5. CTRLA.CTYPE as per the countermeasures required.
           • Set CTRLA.ENABLE
           • Write zero to CIPLEN reg.
           • Write the key in KEYWORD register
           • Write the zeros to DATA reg
           • Set CTRLB.Start.
           • Wait for INTFLAG.ENCCMP to be set
           • AES Hardware generates Hash Subkey in HASHKEY register.
42.6.3.1.2 Authentication Header Processing
           • Configure CTRLA register as follows:
              1. CTRLA.STARTMODE as Manual
              2. CTRLA.CIPHER as Encryption
              3. CTRLA.KEYSIZE as per the key used
              4. CTRLA.AESMODE as GCM
              5. CTRLA.CTYPE as per the countermeasures required.
           • Set CTRLA.ENABLE
           • Write the key in KEYWORD register
           • Set CTRLB.GFMUL
           • Write the Authdata to DATA reg
           • Set CTRLB.START as1
           • Wait for INTFLAG.GFMCMP to be set.
           • AES Hardware generates output in GHASH register
           • Continue steps 4 to 7 for remaining Authentication Header.
             Note: If the Auth data is less than 128 bit, it has to be padded with zero to make it 128 bit aligned.




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1421
                                                            SAM D5x/E5x Family Data Sheet
                                                                    AES – Advanced Encryption Standard


                                                                             GHASH




                                             AUTHDAT                            +




                                                                           GF128Mult(H)




                                                                             GHASH



42.6.3.1.3 Plain text Processing
           •   Set CTRLB.NEWMSG for the new set of plain text processing.
           •   Load CIPLEN reg.
           •   Load (J0+1) in INTVECT register.
           •   As described in NIST documentation J 0 = IV || 0 31 || 1 when len(IV)=96 and J0 =GHASHH (IV || 0 s
               +64 || [len(IV)] 64 ) (s is the minimum number of zeroes that should be padded with the Initialization
               Vector to make it a multiple of 128) if len(IV) != 96.
           •   Load plain text in DATA register.
           •   Set CTRLB.START as 1.
           •   Wait for INTFLAG.ENCCMP to be set.
           •   AES Hardware generates output in DATA register.
           •   Intermediate GHASH is stored in GHASH register and Cipher Text available in DATA register.
           •   Continue 3 to 6 till the input of plain text to get the cipher text and the Hash keys.
           •   At the last input, set CTRLB.EOM.
           •   Write last in-data to DATA reg.
           •   Set CTRLB.START as 1.
           •   Wait for INTFLAG.ENCCMP to be set.
           •   AES Hardware generates output in DATA register and final Hash key in GHASH register.
           •   Load [LEN(A)]64||[LEN(C)]64 in DATA register and set CTRLB.GFMUL and CTRLB.START as 1.
           •   Wait for INTFLAG.GFMCMP to be set.
           •   AES Hardware generates final GHASH value in GHASH register.
42.6.3.1.4 Plain text processing with DMAC
           •   Set CTRLB.NEWMSG for the new set of plain text processing.
           •   Load CIPLEN reg.
           •   Load (J0+1) in INTVECT register.
           •   Load plain text in DATA register.
           •   Wait for INTFLAG.ENCCMP to be set.




         © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1422
                                                        SAM D5x/E5x Family Data Sheet
                                                                AES – Advanced Encryption Standard

           •   AES Hardware generates output in DATA register.
           •   Intermediate GHASH is stored in GHASH register and Cipher Text available in DATA register.
           •   Continue 3 to 5 till the input of plain text to get the cipher text and the Hash keys.
           •   At the last input, set CTRLB.EOM.
           •   Write last in-data to DATA reg.
           •   Wait for INTFLAG.ENCCMP to be set.
           •   AES Hardware generates output in DATA register and final Hash key in GHASH register.
           •   Load [LEN(A)]64||[LEN(C)]64 in DATA register and set CTRLB.GFMUL and CTRLB.START as 1.
           •   Wait for INTFLAG.GFMCMP to be set.
           •   AES Hardware generates final GHASH value in GHASH register.
42.6.3.1.5 Tag Generation
           • Configure CTRLA
              1. Set CTRLA.ENABLE to 0
              2. Set CTRLA.AESMODE as CTR
              3. Set CTRLA.ENABLE to 1
           • Load J0 value to INITVECTV reg.
           • Load GHASH value to DATA reg.
           • Set CTRLB.NEWMSG and CTRLB.START to start the Counter mode operation.
           • Wait for INTFLAG.ENCCMP to be set.
           • AES Hardware generates the GCM Tag output in DATA register.

42.6.4   Synchronization
         Not applicable.




         © 2019 Microchip Technology Inc.                 Datasheet                      DS60001507E-page 1423
                                                             SAM D5x/E5x Family Data Sheet
                                                                   AES – Advanced Encryption Standard


42.7      Register Summary

 Offset        Name        Bit Pos.

                              7:0            CFBS[2:0]                    AESMODE[2:0]              ENABLE         SWRST
                             15:8            XORKEY      KEYGEN   LOD     STARTMODE      CIPHER            KEYSIZE[1:0]
 0x00         CTRLA
                             23:16                                                           CTYPE[3:0]
                             31:24
 0x04         CTRLB           7:0                                           GFMUL         EOM      NEWMSG           START
 0x05        INTENCLR         7:0                                                                   GFMCMP         ENCCMP
 0x06        INTENSET         7:0                                                                   GFMCMP         ENCCMP
 0x07        INTFLAG          7:0                                                                   GFMCMP         ENCCMP
 0x08      DATABUFPTR         7:0                                                                         INDATAPTR[1:0]
 0x09        DBGCTRL          7:0                                                                                  DBGRUN
 0x0A
   ...       Reserved
 0x0B
                              7:0                                  KEYWORD[7:0]
                             15:8                                  KEYWORD[15:8]
  0C        KEYWORD0
                             23:16                                 KEYWORD[23:16]
                             31:24                                 KEYWORD[31:24]
                              7:0                                  KEYWORD[7:0]
                             15:8                                  KEYWORD[15:8]
  10        KEYWORD1
                             23:16                                 KEYWORD[23:16]
                             31:24                                 KEYWORD[31:24]
                              7:0                                  KEYWORD[7:0]
                             15:8                                  KEYWORD[15:8]
  14        KEYWORD2
                             23:16                                 KEYWORD[23:16]
                             31:24                                 KEYWORD[31:24]
                              7:0                                  KEYWORD[7:0]
                             15:8                                  KEYWORD[15:8]
  18        KEYWORD3
                             23:16                                 KEYWORD[23:16]
                             31:24                                 KEYWORD[31:24]
                              7:0                                  KEYWORD[7:0]
                             15:8                                  KEYWORD[15:8]
  1C        KEYWORD4
                             23:16                                 KEYWORD[23:16]
                             31:24                                 KEYWORD[31:24]
                              7:0                                  KEYWORD[7:0]
                             15:8                                  KEYWORD[15:8]
  20        KEYWORD5
                             23:16                                 KEYWORD[23:16]
                             31:24                                 KEYWORD[31:24]
                              7:0                                  KEYWORD[7:0]
                             15:8                                  KEYWORD[15:8]
  24        KEYWORD6
                             23:16                                 KEYWORD[23:16]
                             31:24                                 KEYWORD[31:24]




          © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 1424
                                                 SAM D5x/E5x Family Data Sheet
                                                      AES – Advanced Encryption Standard

...........continued

  Offset               Name    Bit Pos.

                                  7:0                 KEYWORD[7:0]
                                 15:8                 KEYWORD[15:8]
     28          KEYWORD7
                                 23:16                KEYWORD[23:16]
                                 31:24                KEYWORD[31:24]
   0x2C
     ...           Reserved
   0x37
                                  7:0                    DATA[7:0]
                                 15:8                   DATA[15:8]
   0x38                DATA
                                 23:16                  DATA[23:16]
                                 31:24                  DATA[31:24]
                                  7:0                  INTVECTV[7:0]
                                 15:8                 INTVECTV[15:8]
     3C           INTVECTV0
                                 23:16                INTVECTV[23:16]
                                 31:24                INTVECTV[31:24]
                                  7:0                  INTVECTV[7:0]
                                 15:8                 INTVECTV[15:8]
     40           INTVECTV1
                                 23:16                INTVECTV[23:16]
                                 31:24                INTVECTV[31:24]
                                  7:0                  INTVECTV[7:0]
                                 15:8                 INTVECTV[15:8]
     44           INTVECTV2
                                 23:16                INTVECTV[23:16]
                                 31:24                INTVECTV[31:24]
                                  7:0                  INTVECTV[7:0]
                                 15:8                 INTVECTV[15:8]
     48           INTVECTV3
                                 23:16                INTVECTV[23:16]
                                 31:24                INTVECTV[31:24]
   0x4C
     ...           Reserved
   0x5B
                                  7:0                  HASHKEY[7:0]
                                 15:8                 HASHKEY[15:8]
   0x5C           HASHKEY0
                                 23:16                HASHKEY[23:16]
                                 31:24                HASHKEY[31:24]
                                  7:0                  HASHKEY[7:0]
                                 15:8                 HASHKEY[15:8]
   0x60           HASHKEY1
                                 23:16                HASHKEY[23:16]
                                 31:24                HASHKEY[31:24]
                                  7:0                  HASHKEY[7:0]
                                 15:8                 HASHKEY[15:8]
   0x64           HASHKEY2
                                 23:16                HASHKEY[23:16]
                                 31:24                HASHKEY[31:24]




              © 2019 Microchip Technology Inc.   Datasheet               DS60001507E-page 1425
                                                                 SAM D5x/E5x Family Data Sheet
                                                                          AES – Advanced Encryption Standard

...........continued

  Offset                Name    Bit Pos.

                                  7:0                                      HASHKEY[7:0]
                                 15:8                                     HASHKEY[15:8]
   0x68           HASHKEY3
                                 23:16                                    HASHKEY[23:16]
                                 31:24                                    HASHKEY[31:24]
                                  7:0                                       GHASH[7:0]
                                 15:8                                      GHASH[15:8]
   0x6C                GHASH0
                                 23:16                                     GHASH[23:16]
                                 31:24                                     GHASH[31:24]
                                  7:0                                       GHASH[7:0]
                                 15:8                                      GHASH[15:8]
   0x70                GHASH1
                                 23:16                                     GHASH[23:16]
                                 31:24                                     GHASH[31:24]
                                  7:0                                       GHASH[7:0]
                                 15:8                                      GHASH[15:8]
   0x74                GHASH2
                                 23:16                                     GHASH[23:16]
                                 31:24                                     GHASH[31:24]
                                  7:0                                       GHASH[7:0]
                                 15:8                                      GHASH[15:8]
   0x78                GHASH3
                                 23:16                                     GHASH[23:16]
                                 31:24                                     GHASH[31:24]
   0x7C
     ...           Reserved
   0x7F
                                  7:0                                       CIPLEN[7:0]
                                 15:8                                      CIPLEN[15:8]
     80                CIPLEN
                                 23:16                                     CIPLEN[23:16]
                                 31:24                                     CIPLEN[31:24]
                                  7:0                                     RANDSEED[7:0]
                                 15:8                                     RANDSEED[15:8]
   0x84           RANDSEED
                                 23:16                                   RANDSEED[23:16]
                                 31:24                                   RANDSEED[31:24]




42.8           Register Description
               Registers can be 8, 16, or 32 bits wide. Atomic 8-, 16- and 32-bit accesses are supported. In addition, the
               8-bit quarters and 16-bit halves of a 32-bit register, and the 8-bit halves of a 16-bit register can be
               accessed directly.
               Some registers are optionally write-protected by the Peripheral Access Controller (PAC). Optional PAC
               write protection is denoted by the "PAC Write-Protection" property in each individual register description.
               For details, refer to 42.5.8 Register Access Protection.
               Some registers are enable-protected, meaning they can only be written when the peripheral is disabled.
               Enable-protection is denoted by the "Enable-Protected" property in each individual register description.




              © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1426
                                                               SAM D5x/E5x Family Data Sheet
                                                                        AES – Advanced Encryption Standard

42.8.1         Control A

               Name:       CTRLA
               Offset:     0x00
               Reset:      0x00000000
               Property:   PAC Write-Protection, Enable-protected


         Bit        31           30             29        28             27          26                 25                  24


   Access
    Reset


         Bit        23           22             21        20             19          18                 17                  16
                                                                                           CTYPE[3:0]
   Access                                                               R/W         R/W                 R/W             R/W
    Reset                                                                0             0                 0                  0


         Bit        15           14             13        12             11          10                  9                  8
                              XORKEY          KEYGEN     LOD        STARTMODE      CIPHER                    KEYSIZE[1:0]
   Access                       R/W            R/W       R/W            R/W         R/W                 R/W             R/W
    Reset                         0             0         0              0             0                 0                  0


         Bit        7             6             5         4              3             2                 1                  0
                              CFBS[2:0]                             AESMODE[2:0]                   ENABLE             SWRST
   Access          R/W          R/W            R/W       R/W            R/W         R/W                 R/W             R/W
    Reset           0             0             0         0              0             0                 0                  0


               Bits 19:16 – CTYPE[3:0] Counter Measure Type
               Value       Name                             Description
               XXX0        CTYPE1 disabled                  Countermeasure1 disabled
               XXX1        CTYPE1 enabled                   Countermeasure1 enabled
               XX0X        CTYPE2 disabled                  Countermeasure2 disabled
               XX1X        CTYPE2 enabled                   Countermeasure2 enabled
               X0XX        CTYPE3 disabled                  Countermeasure3 disabled
               X1XX        CTYPE3 enabled                   Countermeasure3 enabled
               0XXX        CTYPE4 disabled                  Countermeasure4 disabled
               1XXX        CTYPE4 enabled                   Countermeasure4 enabled

               Bit 14 – XORKEY XOR Key Operation
               Value      Description
               0          No effect
               1          The user keyword gets XORed with the previous keyword register content.

               Bit 13 – KEYGEN Last Key Generation
               Value      Description
               0          No effect
               1          Start Computation of the last NK words of the expanded key




           © 2019 Microchip Technology Inc.                    Datasheet                                DS60001507E-page 1427
                                                SAM D5x/E5x Family Data Sheet
                                                        AES – Advanced Encryption Standard

Bit 12 – LOD Last Output Data Mode
Value      Description
0          No effect
1          Start encryption in Last Output Data mode

Bit 11 – STARTMODE Start Mode Select
Value      Name              Description
0          Manual Mode       Start Encryption / Decryption in Manual mode
1          Auto Mode         Start Encryption / Decryption in Auto mode

Bit 10 – CIPHER Cipher Mode Select
Value       Description
0           Decryption
1           Encryption

Bits 9:8 – KEYSIZE[1:0] Encryption Key Size
Value       Name                Description
0           128-bit Key         128-bit Key for Encryption / Decryption
1           192-bit Key         192-bit Key for Encryption / Decryption
2           256-bit Key         256-bit Key for Encryption / Decryption
3           Reserved            Reserved

Bits 7:5 – CFBS[2:0] Cipher Feedback Block Size
Value       Name               Description
0           128-bit data block 128-bit Input data block for Encryption/Decryption in Cipher Feedback
                               mode
1           64-bit data block 64-bit Input data block for Encryption/Decryption in Cipher Feedback
                               mode
2           32-bit data block 32-bit Input data block for Encryption/Decryption in Cipher Feedback
                               mode
3           16-bit data block 16-bit Input data block for Encryption/Decryption in Cipher Feedback
                               mode
4           8-bit data block   8-bit Input data block for Encryption/Decryption in Cipher Feedback mode
5-7         Reserved           Reserved

Bits 4:2 – AESMODE[2:0] AES Modes of Operation
Value       Name               Description
0           ECB                Electronic code book mode
1           CBC                Cipher block chaining mode
2           OFB                Output feedback mode
3           CFB                Cipher feedback mode
4           Counter            Counter mode
5           CCM                CCM mode
6           GCM                Galois counter mode
7           Reserved           Reserved

Bit 1 – ENABLE Enable
Value      Description
0          The peripheral is disabled




© 2019 Microchip Technology Inc.                  Datasheet                        DS60001507E-page 1428
                                                     SAM D5x/E5x Family Data Sheet
                                                              AES – Advanced Encryption Standard

 Value        Description
 1            The peripheral is enabled

Bit 0 – SWRST Software Reset
Writing a '0' to this bit has no effect.
Writing a '1' to this bit resets all registers in the AES module to their initial state, and the module will be
disabled.
Writing a '1' to SWRST will always take precedence, meaning that all other writes in the same write
operation will be discarded.
 Value        Description
 0            There is no reset operation ongoing
 1            The reset operation is ongoing




© 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 1429
                                                                  SAM D5x/E5x Family Data Sheet
                                                                          AES – Advanced Encryption Standard

42.8.2         Control B

               Name:        CTRLB
               Offset:      0x04
               Reset:       0x00
               Property:    PAC Write-Protection


         Bit         7             6            5             4             3            2             1             0
                                                                         GFMUL          EOM        NEWMSG         START
   Access                                                                 R/W           R/W           R/W           R/W
    Reset                                                                   0            0             0             0


               Bit 3 – GFMUL GF Multiplication
               This bit is applicable only to GCM mode.
                Value       Description
                0           No action
                1           Setting this bit calculates GF multiplication with data buffer content and hashkey register
                            content.

               Bit 2 – EOM End of Message
               This bit is applicable only to GCM mode.
                Value       Description
                0           No action
                1           Setting this bit generates final GHASH value for the message.

               Bit 1 – NEWMSG New Message
               This bit is used in cipher block chaining (CBC), cipher feedback (CFB) and output feedback (OFB),
               counter (CTR) modes to indicate the hardware to use Initialization vector for encrypting the first block of
               message.
                Value       Description
                0            No action
                1            Setting this bit indicates start of new message to the module.

               Bit 0 – START Start Encryption/Decryption
               Value      Description
               0          No action
               1          Start encryption / decryption in manual mode.




           © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 1430
                                                                   SAM D5x/E5x Family Data Sheet
                                                                           AES – Advanced Encryption Standard

42.8.3         Interrupt Enable Clear

               Name:        INTENCLR
               Offset:      0x05
               Reset:       0x00
               Property:    PAC Write-Protection
               This register allows the user to disable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Set (INTENSET) register.


         Bit         7             6             5             4             3             2             1              0
                                                                                                     GFMCMP        ENCCMP
   Access                                                                                               R/W            R/W
    Reset                                                                                                0              0


               Bit 1 – GFMCMP GF Multiplication Complete Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the GF Multiplication Complete Interrupt Enable bit, which disables the GF
               Multiplication Complete interrupt.
               Value         Description
               0             The GF Multiplication Complete interrupt is disabled.
               1             The GF Multiplication Complete interrupt is enabled.

               Bit 0 – ENCCMP Encryption Complete Interrupt Enable
               Writing a '0' to this bit has no effect.
               Writing a '1' to this bit will clear the Encryption Complete Interrupt Enable bit, which disables the
               Encryption Complete interrupt.
               Value         Description
               0             The Encryption Complete interrupt is disabled.
               1             The Encryption Complete interrupt is enabled.




           © 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 1431
                                                                     SAM D5x/E5x Family Data Sheet
                                                                              AES – Advanced Encryption Standard

42.8.4         Interrupt Enable Set

               Name:        INTENSET
               Offset:      0x06
               Reset:       0x00
               Property:    PAC Write-Protection
               This register allows the user to enable an interrupt without doing a read-modify-write operation. Changes
               in this register will also be reflected in the Interrupt Enable Clear (INTENCLR) register.


         Bit         7              6             5              4             3              2             1                 0
                                                                                                        GFMCMP         ENCCMP
   Access                                                                                                  R/W           R/W
    Reset                                                                                                   0                 0


               Bit 1 – GFMCMP GF Multiplication Complete Interrupt Enable
               Writing a '0' to this bit has no effect. Writing a '1' to this bit will clear the GF Multiplication Complete
               Interrupt Enable bit, which enables the GF Multiplication Complete interrupt.
                Value        Description
                0            The GF Multiplication Complete interrupt is disabled.
                1            The GF Multiplication Complete interrupt is enabled.

               Bit 0 – ENCCMP Encryption Complete Interrupt Enable
               Writing a '0' to this bit has no effect. Writing a '1' to this bit will clear the Encryption Complete Interrupt
               Enable bit, which enables the Encryption Complete interrupt.
               Value         Description
               0             The Encryption Complete interrupt is disabled.
               1             The Encryption Complete interrupt is enabled.




           © 2019 Microchip Technology Inc.                            Datasheet                            DS60001507E-page 1432
                                                                 SAM D5x/E5x Family Data Sheet
                                                                        AES – Advanced Encryption Standard

42.8.5         Interrupt Flag Status and Clear

               Name:       INTFLAG
               Offset:     0x07
               Reset:      0x00


         Bit         7            6            5             4            3            2            1             0
                                                                                                 GFMCMP       ENCCMP
   Access                                                                                          R/W           R/W
    Reset                                                                                           0             0


               Bit 1 – GFMCMP GF Multiplication Complete
               This flag is cleared by writing a '1' to it.
               This flag is set when GHASH value is available on the Galois Hash Registers (GHASHx) in GCM mode.
               Writing a '0' to this bit has no effect.
               This flag is also automatically cleared in the following cases.
                1. Manual encryption/decryption occurs (START in CTRLB register).
                2.   Reading from the GHASHx register.

               Bit 0 – ENCCMP Encryption Complete
               This flag is cleared by writing a '1' to it.
               This flag is set when encryption/decryption is complete and valid data is available on the Data Register.
               Writing a '0' to this bit has no effect.
               This flag is also automatically cleared in the following cases:
                1. Manual encryption/decryption occurs (START in CTRLA register). (This feature is needed only if we
                      do not support double buffering of DATA registers).
                2.   Reading from the data register (DATAx) when LOD = 0.
                3.   Writing into the data register (DATAx) when LOD = 1.
                4.   Reading from the Hash Key register (HASHKEYx).




           © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1433
                                                                  SAM D5x/E5x Family Data Sheet
                                                                          AES – Advanced Encryption Standard

42.8.6         Data Buffer Pointer

               Name:        DATABUFPTR
               Offset:      0x08
               Reset:       0x00
               Property:    PAC Write-Protection


         Bit         7            6             5             4            3             2             1            0
                                                                                                       INDATAPTR[1:0]
   Access                                                                                            R/W           R/W
    Reset                                                                                              0            0


               Bits 1:0 – INDATAPTR[1:0] Input Data Pointer
               Writing to this field changes the value of the input data pointer, which determines which of the four data
               registers is written to/read from when the next write/read to the DATA register address is performed.




           © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 1434
                                                                 SAM D5x/E5x Family Data Sheet
                                                                         AES – Advanced Encryption Standard

42.8.7         Debug

               Name:       DBGCTRL
               Offset:     0x09
               Reset:      0x00
               Property:   PAC Write-Protection


         Bit         7            6             5            4             3            2            1             0
                                                                                                               DBGRUN
   Access                                                                                                         W
    Reset                                                                                                          0


               Bit 0 – DBGRUN Debug Run
               Writing a '0' to this bit causes the AES to halt during debug mode.
               Writing a '1' to this bit allows the AES to continue normal operation during debug mode. This bit can only
               be changed while the AES is disabled.




           © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 1435
                                                                SAM D5x/E5x Family Data Sheet
                                                                       AES – Advanced Encryption Standard

42.8.8         Keyword

               Name:       KEYWORD
               Offset:     0x0C + n*0x04 [n=0..7]
               Reset:      0x00000000
               Property:   PAC Write-Protection


         Bit        31           30           29           28           27          26           25           24
                                                           KEYWORD[31:24]
   Access           W            W            W            W            W            W           W            W
    Reset           0             0           0            0            0            0            0            0


         Bit        23           22           21           20           19          18           17           16
                                                           KEYWORD[23:16]
   Access           W            W            W            W            W            W           W            W
    Reset           0             0           0            0            0            0            0            0


         Bit        15           14           13           12           11          10            9            8
                                                           KEYWORD[15:8]
   Access           W            W            W            W            W            W           W            W
    Reset           0             0           0            0            0            0            0            0


         Bit        7             6           5            4            3            2            1            0
                                                            KEYWORD[7:0]
   Access           W            W            W            W            W            W           W            W
    Reset           0             0           0            0            0            0            0            0


               Bits 31:0 – KEYWORD[31:0] Key Word Value
               The four/six/eight 32-bit Key Word registers set the 128-bit/192-bit/256-bit cryptographic key used for
               encryption/decryption. KEYWORD0.KEYWORD corresponds to the first word of the key and KEYWORD3/
               KEYWORD5/KEYWORD7.KEYWORD to the last one.
               Note: By setting the XORKEY bit of CTRLA register, keyword will update with the resulting XOR value of
               user keyword and previous keyword content.




           © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 1436
                                                                   SAM D5x/E5x Family Data Sheet
                                                                               AES – Advanced Encryption Standard

42.8.9         Data

               Name:        DATA
               Offset:      0x38
               Reset:       0x00000000


         Bit          31          30            29           28                 27       26           25            24
                                                                  DATA[31:24]
   Access           R/W          R/W           R/W          R/W                R/W      R/W          R/W           R/W
    Reset             0           0             0             0                 0        0             0            0


         Bit          23          22            21           20                 19       18           17            16
                                                                  DATA[23:16]
   Access           R/W          R/W           R/W          R/W                R/W      R/W          R/W           R/W
    Reset             0           0             0             0                 0        0             0            0


         Bit          15          14            13           12                 11       10            9            8
                                                                  DATA[15:8]
   Access           R/W          R/W           R/W          R/W                R/W      R/W          R/W           R/W
    Reset             0           0             0             0                 0        0             0            0


         Bit          7           6             5             4                 3        2             1            0
                                                                   DATA[7:0]
   Access           R/W          R/W           R/W          R/W                R/W      R/W          R/W           R/W
    Reset             0           0             0             0                 0        0             0            0


               Bits 31:0 – DATA[31:0] Data Value
               A write to or read from this register corresponds to a write to or read from one of the four data registers.
               The four 32-bit Data registers set the 128-bit data block used for encryption/decryption. The data register
               that is written to or read from is given by the DATABUFPTR.DATPTR field.
               Note: Both input and output shares the same data buffer. Reading DATA register will return 0’s when
               AES is performing encryption or decryption operation.




           © 2019 Microchip Technology Inc.                          Datasheet                        DS60001507E-page 1437
                                                               SAM D5x/E5x Family Data Sheet
                                                                       AES – Advanced Encryption Standard

42.8.10 Initialization Vector Register

            Name:        INTVECTV
            Offset:      0x3C + n*0x04 [n=0..3]
            Reset:       0x00000000
            Property:    PAC Write-Protection


      Bit        31            30            29           28            27            26            25           24
                                                           INTVECTV[31:24]
   Access        W             W             W             W            W             W             W            W
    Reset         0             0            0             0             0            0             0             0


      Bit        23            22            21           20            19            18            17           16
                                                           INTVECTV[23:16]
   Access        W             W             W             W            W             W             W            W
    Reset         0             0            0             0             0            0             0             0


      Bit        15            14            13           12            11            10            9             8
                                                           INTVECTV[15:8]
   Access        W             W             W             W            W             W             W            W
    Reset         0             0            0             0             0            0             0             0


      Bit         7             6            5             4             3            2             1             0
                                                            INTVECTV[7:0]
   Access        W             W             W             W            W             W             W            W
    Reset         0             0            0             0             0            0             0             0


            Bits 31:0 – INTVECTV[31:0] Initialization Vector Value
            The four 32-bit Initialization Vector registers INTVECTVn set the 128-bit Initialization Vector data block
            that is used by some modes of operation as an additional initial input. INTVECTV0.INTVECTV
            corresponds to the first word of the Initialization Vector, INTVECTV3.INTVECTV to the last one. These
            registers are write-only to prevent the Initialization Vector from being read by another application. For
            CBC, OFB, and CFB modes, the Initialization Vector corresponds to the initialization vector. For CTR
            mode, it corresponds to the counter value.




        © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 1438
                                                            SAM D5x/E5x Family Data Sheet
                                                                    AES – Advanced Encryption Standard

42.8.11 Hash Key (GCM mode only)

           Name:       HASHKEY
           Offset:     0x5C + n*0x04 [n=0..3]
           Reset:      0x00000000
           Property:   PAC Write-protection


     Bit        31           30           29         28              27       26           25           24
                                                      HASHKEY[31:24]
  Access       R/W          R/W           R/W        R/W            R/W       R/W         R/W          R/W
   Reset        0             0            0          0                  0     0           0            0


     Bit        23           22           21         20              19       18           17           16
                                                      HASHKEY[23:16]
  Access       R/W          R/W           R/W        R/W            R/W       R/W         R/W          R/W
   Reset        0             0            0          0                  0     0           0            0


     Bit        15           14           13         12              11       10           9            8
                                                      HASHKEY[15:8]
  Access       R/W          R/W           R/W        R/W            R/W       R/W         R/W          R/W
   Reset        0             0            0          0                  0     0           0            0


     Bit        7             6            5          4                  3     2           1            0
                                                          HASHKEY[7:0]
  Access       R/W          R/W           R/W        R/W            R/W       R/W         R/W          R/W
   Reset        0             0            0          0                  0     0           0            0


           Bits 31:0 – HASHKEY[31:0] Hash Key Value
           The four 32-bit HASHKEY registers contain the 128-bit Hash Key value computed from the AES KEY. The
           Hash Key value can also be programmed offering single GF128 multiplication possibilities.




       © 2019 Microchip Technology Inc.                       Datasheet                    DS60001507E-page 1439
                                                             SAM D5x/E5x Family Data Sheet
                                                                     AES – Advanced Encryption Standard

42.8.12 Galois Hash (GCM mode only)

           Name:       GHASH
           Offset:     0x6C + n*0x04 [n=0..3]
           Reset:      0x00000000
           Property:   PAC Write-Protection


     Bit        31           30           29          28                 27    26           25           24
                                                          GHASH[31:24]
  Access       R/W          R/W           R/W        R/W             R/W      R/W          R/W          R/W
   Reset        0             0            0          0                  0     0            0            0


     Bit        23           22           21          20                 19    18           17           16
                                                          GHASH[23:16]
  Access       R/W          R/W           R/W        R/W             R/W      R/W          R/W          R/W
   Reset        0             0            0          0                  0     0            0            0


     Bit        15           14           13          12                 11    10           9            8
                                                           GHASH[15:8]
  Access       R/W          R/W           R/W        R/W             R/W      R/W          R/W          R/W
   Reset        0             0            0          0                  0     0            0            0


     Bit        7             6            5          4                  3     2            1            0
                                                           GHASH[7:0]
  Access       R/W          R/W           R/W        R/W             R/W      R/W          R/W          R/W
   Reset        0             0            0          0                  0     0            0            0


           Bits 31:0 – GHASH[31:0] Galois Hash Value
           The four 32-bit Hash Word registers GHASHcontain the GHASH value after GF128 multiplication in GCM
           mode. Writing a new key to KEYWORD registers causes GHASH to be initialized with zeroes. These
           registers can also be programmed.




       © 2019 Microchip Technology Inc.                       Datasheet                     DS60001507E-page 1440
                                                                SAM D5x/E5x Family Data Sheet
                                                                        AES – Advanced Encryption Standard

42.8.13 Galois Hash x (GCM mode only)

           Name:       CIPLEN
           Offset:     0X80
           Reset:      0x00000000
           Property:   PAC Write-Protection


     Bit        31            30           29            28                  27     26           25            24
                                                             CIPLEN[31:24]
  Access       R/W           R/W          R/W           R/W              R/W       R/W          R/W           R/W
   Reset         0            0             0            0                   0      0             0            0


     Bit        23            22           21            20                  19     18           17            16
                                                             CIPLEN[23:16]
  Access       R/W           R/W          R/W           R/W              R/W       R/W          R/W           R/W
   Reset         0            0             0            0                   0      0             0            0


     Bit        15            14           13            12                  11     10            9            8
                                                              CIPLEN[15:8]
  Access       R/W           R/W          R/W           R/W              R/W       R/W          R/W           R/W
   Reset         0            0             0            0                   0      0             0            0


     Bit         7            6             5            4                   3      2             1            0
                                                              CIPLEN[7:0]
  Access       R/W           R/W          R/W           R/W              R/W       R/W          R/W           R/W
   Reset         0            0             0            0                   0      0             0            0


           Bits 31:0 – CIPLEN[31:0] Cipher Length
           This register contains the length in bytes of the Cipher text that is to be processed. This is programmed
           by the user in GCM mode for Tag generation.




       © 2019 Microchip Technology Inc.                          Datasheet                       DS60001507E-page 1441
                                                            SAM D5x/E5x Family Data Sheet
                                                                   AES – Advanced Encryption Standard

42.8.14 Random Seed

           Name:       RANDSEED
           Offset:     0x84
           Reset:      0x00000000
           Property:   PAC Write-Protection


     Bit        31           30           29           28           27           26           25           24
                                                       RANDSEED[31:24]
  Access       R/W          R/W           R/W         R/W          R/W          R/W          R/W          R/W
   Reset        0             0            0           0            0            0            0            0


     Bit        23           22           21           20           19           18           17           16
                                                       RANDSEED[23:16]
  Access       R/W          R/W           R/W         R/W          R/W          R/W          R/W          R/W
   Reset        0             0            0           0            0            0            0            0


     Bit        15           14           13           12           11           10           9            8
                                                       RANDSEED[15:8]
  Access       R/W          R/W           R/W         R/W          R/W          R/W          R/W          R/W
   Reset        0             0            0           0            0            0            0            0


     Bit        7             6            5           4            3            2            1            0
                                                        RANDSEED[7:0]
  Access       R/W          R/W           R/W         R/W          R/W          R/W          R/W          R/W
   Reset        0             0            0           0            0            0            0            0


           Bits 31:0 – RANDSEED[31:0] Random Seed
           A write to this register corresponds to loading a new seed into the Random number generator.




       © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 1442
