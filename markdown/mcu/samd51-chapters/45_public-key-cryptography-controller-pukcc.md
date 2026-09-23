# 43. Public Key Cryptography Controller (PUKCC)

*Source: `Atmel-SAMD51.pdf`, pages 1443-1573 — SAMD51 family datasheet*

                                                          SAM D5x/E5x Family Data Sheet
                                                         Public Key Cryptography Controller (PUKCC)


43.      Public Key Cryptography Controller (PUKCC)

43.1     Overview
         The Public Key Cryptography Controller (PUKCC) processes public key cryptography algorithm calculus
         in both GF(p) and GF(2n) fields.
         The PUKCL (PUblic Key Cryptography Library) is stored in ROM inside the device. This library can be
         used in applications to access features of PUKCC.
         The Public Key Cryptography Library includes complete implementation of the following public key
         cryptography algorithms:
           • RSA (Rivest-Shamir-Adleman public key cryptosystem), DSA (Digital Signature Algorithm):
              – Modular Exponentiation with CRT up to 7168 bits
              – Modular Exponentiation without CRT up to 5376 bits
              – Prime generation
              – Utilities: GCD/modular Inverse, Divide, Modular reduction, Multiply, ...
           • Elliptic Curves:
              – ECDSA GF(p) up to 521 bits for common curves (up to 1120 bits for future use)
              – ECDSA GF(2n) up to 571 bits for common curves (up to 1440 bits for future use)
              – Choice of the curves parameters so compatibility with NIST Curves or other curves in
                  Weierstrass equation
              – Point Multiply
              – Point Add/Doubling
              – Other high level elliptic curves algorithms (ECDH, ...) can be implemented by user using library
                  functions
           • Deterministic Random Number Generation (DRNG ANSI X9.31) for DSA


43.2     Product Dependencies

43.2.1   I/O Lines
         Not applicable.

43.2.2   Power Management
         The PUKCC will continue to operate in any sleep mode, as long as its source clock is running.

43.2.3   Clocks
         The bus clock (CLK_PUKCC_AHB) can be enabled and disabled by the Main Clock Controller.
         Related Links
         15. MCLK – Main Clock

43.2.4   DMA
         Not applicable.

43.2.5   Interrupts
         Not applicable.




         © 2019 Microchip Technology Inc.                  Datasheet                         DS60001507E-page 1443
                                                            SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

43.2.6   Events
         Not applicable.



43.3     Functional Description

43.3.1   Public Key Cryptography Library (PUKCL) Application Programming Interface (API)
         The Public Key Cryptography Controller (PUKCC) is a peripheral that can be used to accelerate public
         key cryptography, and processes public key cryptography algorithm calculus in both Prime field (GF(p))
         and Binary field (GF(2n)). Different functionalities of the PUKCC are accessed with the help of the Public
         Key Cryptography Library (PUKCL), which is embedded into a dedicated ROM inside the microcontroller.
         The PUKCL provides access to many algorithms and functions. The features provided, start from basic
         addition or comparison, up to the RSA or ECDSA complete computation. The library can be utilized by
         including the PUKCL Driver in the application and passing parameters through a common Application
         Programming Interface (API). The PUKCC Driver is available in Atmel START within Drivers >
         Cryptography. This library can be used in conjunction with a SSL software stack to improve performance
         and helps to reduce the RAM usage and time taken to perform different cryptographic functions.

43.3.2   PUKCL Features
         PUKCL features include:
          • 43.3.4 Basic Arithmetic and Cryptographic Services - PUKCL self-test, GCD, integral division, etc.
          • 43.3.5 Modular Arithmetic Services - Modular reduction, modular exponentiation, probable prime
            generation and modular exponentiation
          • 43.3.6 Elliptic Curves Over GF(p) Services - Point addition and doubling on an elliptic curve in a
            prime field, ECDSA signature generation and verification on an elliptic curve over GF(p)
          • 43.3.7 Elliptic Curves Over GF(2n) Services - Point addition and doubling on an elliptic curve in a
            prime field, ECDSA signature generation and verification on an elliptic curve over GF(2n)

43.3.3   PUCKL Usage
         The following sections provide details on accessing the PUKCL and its features.
43.3.3.1 Initializing the PUKCC and PUKCL
         For a project created with Atmel START, the clock initialization is handled by the initialization function
         atmel_start_init. After a power-on reset, and when the PUKCC Clock is enabled, a Crypto RAM
         clear process is launched. It is mandatory to wait until the end of this process before using the Crypto
         Library.
         The following code shows how to wait for the Crypto RAM clear process.

           while ((PUKCCSR & BIT_PUKCCSR_CLRRAM_BUSY) != 0);

         The next task to be done is self-test. From the generated project in Atmel Studio, copy the example for
         the PUKCC Driver SelfTest and add it to the main source file. This is a mandatory step before using the
         library. The return values from the SelfTest service must be compared against known values mentioned in
         the service description (see the Description section in 43.3.4.1 SelfTest).

                   Example 43-1. PUKCC Initialization

                    void PUKCC_self_test(void)
                    {




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1444
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

                        // Clear contents of PUKCLParam
                        memset(&PUKCLParam, 0, sizeof(PUKCL_PARAM));

                        pvPUKCLParam = &PUKCLParam;
                        vPUKCL_Process(SelfTest, pvPUKCLParam);

                        // In case of error, loop here
                        while (PUKCL(u2Status) != PUKCL_OK) {
                        ;
                        }
                        while (pvPUKCLParam->P.PUKCL_SelfTest.u4Version != PUKCL_VERSION) {
                        ;
                        }
                        while (pvPUKCLParam->P.PUKCL_SelfTest.u4CheckNum1 != 0x6E70DDD2) {
                        ;
                        }
                        while (pvPUKCLParam->P.PUKCL_SelfTest.u4CheckNum2 != 0x25C8D64F) {
                        ;
                        }
                   }

                   int main(void)
                   {
                       /* Initializes MCU, drivers and middleware */
                       atmel_start_init();

                        // Wait for Crypto RAM clear process
                        while ((PUKCCSR & BIT_PUKCCSR_CLRRAM_BUSY) != 0);

                        // Initialize PUKCC and perform self test
                        PUKCC_self_test();
                        while(1)
                        {
                        }
                   }


         Note: It may also be necessary to initialize the Random Number Generator (RNG) on the
         microcontroller, as some services in the library use the peripheral. Before calling such services, be sure to
         follow the directives given for random number generation on the selected microcontroller (particularly
         initialization and seeding) and compulsorily start the RNG. For details refer to each service.
43.3.3.2 Accessing Different Library Services
         All cryptographic services in the library are accessed by the macro vPUKCL_Process. All of these
         services use the same process for receiving and returning parameters. PUKCL receives two arguments:
         the requested service and a pointer to a structure called the parameter block. The parameter block
         contains two structures, a common parameter structure for all commands and specific parameter
         structure for each service. A specific service is accessed with vPUKCL_Process by passing the service
         name as the first argument. For example, to perform SelfTest, use vPUKCL_Process(SelfTest,
         pvPUKCLParam).

                  Example 43-2. PUKCL Parameter Block

                   typedef struct _PUKCL_param {
                       PUKCL_HEADER PUKCL_Header;
                       union {
                       _PUKCL_CLEARFLAGS PUKCL_ClearFlags;
                       _PUKCL_COMP       PUKCL_Comp;
                       _PUKCL_CONDCOPY   PUKCL_CondCopy;
                       _PUKCL_CRT        PUKCL_CRT;
                       _PUKCL_DIV        PUKCL_Div;
                       _PUKCL_EXPMOD     PUKCL_ExpMod;
                       _PUKCL_FASTCOPY   PUKCL_FastCopy;
                       _PUKCL_FILL       PUKCL_Fill;
                       _PUKCL_FMULT      PUKCL_Fmult;
                       _PUKCL_GCD        PUKCL_GCD;
                       _PUKCL_PRIMEGEN   PUKCL_PrimeGen;
                       _PUKCL_REDMOD     PUKCL_RedMod;
                       _PUKCL_RNG        PUKCL_Rng;




        © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1445
                                                               SAM D5x/E5x Family Data Sheet
                                                              Public Key Cryptography Controller (PUKCC)

                           _PUKCL_SELFTEST      PUKCL_SelfTest;
                           _PUKCL_SMULT         PUKCL_Smult;
                           _PUKCL_SQUARE        PUKCL_Square;
                           _PUKCL_SWAP          PUKCL_Swap;

                           // ECC
                           _PUKCL_ZPECCADD                   PUKCL_ZpEccAdd;
                           _PUKCL_ZPECCDBL                   PUKCL_ZpEccDbl;
                           _PUKCL_ZPECCADDSUB                PUKCL_ZpEccAddSub;
                           _PUKCL_ZPECCMUL                   PUKCL_ZpEccMul;
                           _PUKCL_ZPECDSAGENERATE            PUKCL_ZpEcDsaGenerate;
                           _PUKCL_ZPECDSAVERIFY              PUKCL_ZpEcDsaVerify;
                           _PUKCL_ZPECDSAQUICKVERIFY         PUKCL_ZpEcDsaQuickVerify;
                           _PUKCL_ZPECCQUICKDUALMUL          PUKCL_ZpEccQuickDualMul;
                           _PUKCL_ZPECCONVPROJTOAFFINE       PUKCL_ZpEcConvProjToAffine;
                           _PUKCL_ZPECCONVAFFINETOPROJECTIVE PUKCL_ZpEcConvAffineToProjective;
                           _PUKCL_ZPECRANDOMIZECOORDINATE    PUKCL_ZpEcRandomiseCoordinate;
                           _PUKCL_ZPECPOINTISONCURVE         PUKCL_ZpEcPointIsOnCurve;

                       // ECC
                       _PUKCL_GF2NECCADD                   PUKCL_GF2NEccAdd;
                       _PUKCL_GF2NECCDBL                   PUKCL_GF2NEccDbl;
                       _PUKCL_GF2NECCMUL                   PUKCL_GF2NEccMul;
                       _PUKCL_GF2NECDSAGENERATE            PUKCL_GF2NEcDsaGenerate;
                       _PUKCL_GF2NECDSAVERIFY              PUKCL_GF2NEcDsaVerify;
                       _PUKCL_GF2NECCONVPROJTOAFFINE       PUKCL_GF2NEcConvProjToAffine;
                       _PUKCL_GF2NECCONVAFFINETOPROJECTIVE PUKCL_GF2NEcConvAffineToProjective;
                       _PUKCL_GF2NECRANDOMIZECOORDINATE    PUKCL_GF2NEcRandomiseCoordinate;
                       _PUKCL_GF2NECPOINTISONCURVE         PUKCL_GF2NEcPointIsOnCurve;
                       } P;
                   } PUKCL_PARAM,



43.3.3.2.1 PUKCL_HEADER Structure
        The PUKCL_HEADER is common for all services of the library. This header includes standard fields to
        indicate the requested service, sub-service, options, return status, and so on, as shown in the following
        tables.
        Different terms used in the below description to be understood, are as follows:
         • Parameter – Represents a variable used by the PUKCL. Every parameter belongs to either
             PUKCL_HEADER or PUKCL Service Specific Header
         • Type – Indicates the data type. For details on data type, please refer to
             CryptoLib_typedef_pb.h file in the library
          • Dir – Direction. Indicates whether PUKCL considers the variable as input or output. Input means that
            the application passes data to the PUKCL using the variable. Output means that the PUKCL uses the
            variable to pass data to the application.
          • Location – Suggests whether the parameter need to be stored in Crypto RAM or device SRAM. The
            PUKCL driver has macros for placing parameters into Crypto RAM, so that the user does not have to
            worry about the addresses
          • Data Length – If a parameter is a pointer variable, the Data Length column shows the size of the data
            pointed by the pointer
        Table 43-1. PUKCL_HEADER Structure
               Parameter              Type        Direction Location Data Length Before Executing the     After Executing the
                                                                                       Service                  Service

               u1Service                   u1         I        –          –      Required service        Executed service

             u1SubService                  u1         I        –          –      Required sub-service    Executed sub-service

                u2Option                   u2         I        –          –      Required option         Executed option

                Specific         PUKCL_STATUS        I/O       –          –      See Table 43-2          See Table 43-2




        © 2019 Microchip Technology Inc.                           Datasheet                            DS60001507E-page 1446
                                                                   SAM D5x/E5x Family Data Sheet
                                                                Public Key Cryptography Controller (PUKCC)

         ...........continued
                Parameter               Type       Direction Location Data Length Before Executing the              After Executing the
                                                                                        Service                           Service

              u2Status (see
             43.3.3.6 Return               u2           I/O        –          –         –                       Output Status
                 Codes)

                 Reserved                  u2           –          –          –         –                       –

                 Reserved                  u4           –          –          –         –                       –


         The Specific field in the PUKCL_HEADER structure is another structure named PUKCL_STATUS. The
         following table describes this structure. The details of the use of these bits are provided in the individual
         service descriptions.
43.3.3.2.2 PUKCL_STATUS Structure
         Members of the PUKCL_STATUS structure are shown in the following table.
         Table 43-2. PUKCL_STATUS Structure
               Parameter         Type Direction Location Data Length Before Executing the Service After Executing the Service

          CarryIn (see Note 1)    bit       I       –          –         CarryIn                          –

                CarryOut          bit      O        –          –         –                                CarryOut

                                                                                                          1: Result is zero
                   Zero           bit      O        –          –         –
                                                                                                          0: Result is not zero

                                                                         Mathematical field 0: Integers
           Gf2n (see Note 1)      bit       I       –          –         (Zp)                             –
                                                                         1: Field GF(2n)

                Violation         bit      O        –          –         –                                Indicates a violation


         Note:
          1. Two of these fields must be filled in to avoid problems during computations. If the Gf2n and CarryIn
               fields are not reset or initialized properly, problems may be encountered during computations. For
               instance, not initializing the Gf2n field may result in getting a correct mathematical result, but
               computed over GF(2n) instead of Zp.
43.3.3.2.3 PUKCL Service Specific Header
         Details about each service specific header are provided with service descriptions in a subsequent
         section. Such structures may contain input or output parameters. A parameter is considered as an input
         parameter when it used for passing information to the PUKCL, and it is considered as an output
         parameter when the PUKCL uses it to pass a result back to the application code.
         The following code provides the service specific header example for the SelfTest service.

          typedef struct _PUKCL_selftest {
              u4 u4Version;
              u4 u4PUKCCVersion;
              u4 u4CheckNum1;
              u4 u4CheckNum2;
              u1 u1Step;
          } _PUKCL_SELFTEST;

         After the SelfTest service is invoked (with vPUKCL_Process(SelfTest, pvPUKCLParam)), the service
         specific return values can be checked using pvPUKCLParam.




        © 2019 Microchip Technology Inc.                               Datasheet                              DS60001507E-page 1447
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

         To check whether the version returned by the PUKCL is correct, the following code can be used.

          while (pvPUKCLParam->P.PUKCL_SelfTest.u4Version != PUKCL_VERSION);

         In a similar way, other returns can also be accessed.
43.3.3.3 Parameter Passing (Special Considerations)
         Most of the PUKCL services work with memory area and accept pointers and lengths as parameters to
         define input and output areas. Most of the time, the pointers and lengths are untouched by the services,
         while the defined areas are read, filled, or overwritten. These memory areas are defined with an initial
         pointer and a byte length. For most of the commands, the memory area location must be in the PUKCC
         Cryptographic RAM. The Cryptographic RAM is the memory area for parameter exchange with the
         PUKCL and is 4 Kbytes large. Sometimes memory areas can be located in Embedded SRAM, which is
         detailed in the Location column of the parameters description tables.
         When working with binary fields, polynomials in GF(2n) need no transformation to be written in an area:
          • Each bit represents a polynomial coefficient 0 or 1
          • The polynomials must be written Low Significant Byte First
          • A zero padding on the Most Significant Bytes may be added if the area is larger than the real size of
            the polynomial


                       Important: The Cryptographic RAM is 4 Kbytes in size and is dedicated to PUKCC. However,
                       to ensure correct library operation, the two last 32-bit words must not be used. Unless otherwise
                       specified, these memory areas contain integers in GF(p) or polynomials in GF(2n) with the Less
                       Significant Byte first.


         Unless otherwise specified, the length must be a multiple of four and the pointers must be four bytes
         aligned. This is because most of the services work with 32-bit words.
43.3.3.4 Aligned Significant Length
         Parameters in memory areas can have any Significant Length in bytes. As the lengths in PUKCL must be
         a multiple of four, a padding is processed on the Most Significant Side with zero to three bytes cleared to
         zero. Now the parameter can be considered to meet the Aligned Significant Length requirement for
         PUKCL.
43.3.3.5 Processing Field GF(p) and GF(2n)
         The library can process arithmetic functions over GF(p) (or Zp integers) and GF(2n), when applicable.
         The choice of these processing fields is made using the following rules:
          • If a processing field is not applicable to the function, it is not mentioned and the Specific.GF2n bit has
            no effect.
          • If the function can support both processing fields, the choice is mentioned and the Specific.GF2n bit
            must be filled according to the choice.
          • If the function supports only one of the processing fields, the processing field is mentioned and the
            Specific.GF2n bit has no effect.
43.3.3.6 Return Codes
         Each call to one of the PUKCL services returns a status code indicating whether or not the execution is
         correct, which can be decoded, as shown in the following figure.




        © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1448
                                                        SAM D5x/E5x Family Data Sheet
                                                      Public Key Cryptography Controller (PUKCC)

Figure 43-1. Return Code Status Decoding




The following table shows how the severity indicators should be decoded.
Table 43-3. Severity Indicators

    Value for Bits 14–15            Severity                                Comment
            0xC000                   Severe       Indicates a blocking error condition
            0x8000                  Warning       Indicates a cautionary use of the return values
            0x4000                 Information    Indicates the result is correct and gives information
            0x0000                     –          No error or no severity given

The following table contains the exhaustive list of all reason codes.
Table 43-4. Return Codes

     Value for Bits 00–13            Severity Code                            Reason Code
             0x0000                        –             PUKCL_OK
             0x4001                    Informative       PUKCL_NUMBER_IS_NOT_PRIME
             0x4002                    Informative       PUKCL_NUMBER_IS_PRIME
             0xC001                      Severe          PUKCL_COMPUTATION_NOT_STARTED
             0xC002                      Severe          PUKCL_UNKNOWN_SERVICE
             0xC003                      Severe          PUKCL_UNEXPLOITABLE_OPTIONS
             0xC004                      Severe          PUKCL_HARDWARE_ISSUE
             0xC005                      Severe          PUKCL_WRONG_HARDWARE
             0xC006                      Severe          PUKCL_LIBRARY_MALFORMED
             0xC007                      Severe          PUKCL_ERROR
             0xC008                      Severe          PUKCL_UNKNOWN_SUBSERVICE
             0xC101                      Severe          PUKCL_DIVISION_BY_ZERO
             0xC102                      Severe          PUKCL_MALFORMED_MODULUS
             0xC103                      Severe          PUKCL_FAULT_DETECTED
             0xC104                      Severe          PUKCL_MALFORMED_KEY




© 2019 Microchip Technology Inc.                         Datasheet                           DS60001507E-page 1449
                                                             SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

          Please note the following rules about return codes:
           • A status value indicating a severe error, means that an expected operation has not been executed or
             has been corrupted. Therefore, the result of such an operation should never be used.
           • A status value indicating a warning should be looked at precisely, as the expected correctness of the
             result cannot be guaranteed.
           • A status value indicating an information always means that the result is correct with no possible
             misinterpretation of the values.
           • A status value zero indicates that there is no error or no severity.
          In the following sections, for each service, the constraints on the parameters placement are detailed. For
          reduced code size and higher execution speed, tests are processed on these constraints. It is important
          that PUKCL users take these placement constraints into consideration at the development and test
          stages to ensure the correct functioning of the library.

43.3.4    Basic Arithmetic and Cryptographic Services
43.3.4.1 SelfTest
43.3.4.1.1 Purpose
          This service is used to initialize the PUKCL. It resets the PUKCC, clears the Crypto RAM, and returns the
          library and PUKCC version numbers.
          It must be called before using any other services in the library and the user must verify the return status
          at the end of the service execution.
43.3.4.1.2 How to Use the Service
43.3.4.1.3 Description
          This service processes internal tests and returns information and status codes as described in 43.3.4.1.7
          Status Returned Values. The service name for this operation is SelfTest.
43.3.4.1.4 Parameters Definition
          It is possible to directly address this service through the PUKCL_SelfTest() macro.
          Table 43-5. SelfTest Service Parameters

          Parameter              Type Dir. Location Data Length Before Executing After Executing the
                                                                the Service      Service
          u4Version              u4         O   –     –              –                    PUKCL version
          u4PUKCCVersion u4                 O   –     –              –                    PUKCC Version
          u4CheckNum1            u4         O   –     –              –                    Test result value 1
          u4CheckNum2            u4         O   –     –              –                    Test result value 2
          u1Step                 u1         O   –     –              –                    Latest correctly executed
                                                                                          step

43.3.4.1.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library
           vPUKCL_Process(SelfTest,pvPUKCLParam);

           if (PUKCL(u2Status) == PUKCL_OK)




         © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1450
                                                             SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

                          {
                          // The Library version is available
                          // in PUKCL_SelfTest(u4Version)
                          // The PUKCL version is available
                          // in PUKCL_SelfTest(u4PUKCCVersion)
                          }

43.3.4.1.6 Returned Values
          The expected u4Version value depends on the version of PUKCL being used, and the u4PUKCCVersion
          value depends on the version of PUKCC being used.
          The expected u4CheckNum1 value is 0x6e70ddd2 and the expected one for u4CheckNum2 is
          0x25c8d64f. The expected final u1Step value is 3.
43.3.4.1.7 Status Returned Values
          Table 43-6. SelfTest Service Return Codes

          Returned Status                   Importance           Meaning
          PUKCL_OK                          –                    Service functioned correctly.
          PUKCL_ERROR                       Severe               An issue has been encountered.

43.3.4.2 Clear Flags
43.3.4.2.1 Purpose
          This service can be used to clear parameter structure flags.
43.3.4.2.2 How to Use the Service

43.3.4.2.3 Description
          This service clears CarryOut, CarryIn, Zero and Violation flags in the Specific bit field. The Gf2n flag is
          untouched.
          The service name for this operation is ClearFlags.
43.3.4.2.4 Parameters Definition
          It is possible to directly address this service through the PUKCL_ClearFlags() macro.
          Table 43-7. Clear Flags Service Parameters

              Parameter          Type Direction Location Data Length Before Executing               After Executing
                                                                       the Service                    the Service
          Specific/CarryOut        Bit      O        –             –                  –                  Cleared
           Specific/CarryIn        Bit      O        –             –                  –                  Cleared
             Specific/Zero         Bit      O        –             –                  –                  Cleared
           Specific/Violation      Bit      O        –             –                  –                  Cleared

43.3.4.2.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(ClearFlags,pvPUKCLParam);
           if (PUKCL(u2Status) == PUKCL_OK)
                       {
                       // Success




         © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1451
                                                             SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

                       }
           else // Manage the error


43.3.4.2.6 Status Returned Values
          Table 43-8. ClearFlags Service Return Codes

          Returned Status                    Importance             Meaning
          PUKCL_OK                           –                      Service functioned correctly.

43.3.4.3 Swap

43.3.4.3.1 Purpose
          This service performs swapping of two buffers.
43.3.4.3.2 How to Use the Service

43.3.4.3.3 Description
          This service swaps two buffers, X and Y, of the same size in memory.
          The service name for this operation is Swap.

43.3.4.3.4 Parameters Definition
          This service can easily be accessed through the use of the PUKCL_Swap() macro.
          Table 43-9. Swap Service Parameters

          Parameter Type Direction           Location       Data        Before Executing        After Executing the
                                                           Length         the Service                 Service
           nu1XBase       nu1         I     Crypto RAM     u2Length     Base of the number     Base of X filled with Y
                                                                                 X
           nu1YBase       nu1         I     Crypto RAM     u2Length     Base of the number     Base of Y filled with X
                                                                                 Y
           u2XLength      u2          I          –            –          Length of X and Y          Length of X and Y

43.3.4.3.5 Code Example
           _PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // Initialize parameters
           PUKCL_Swap(nu1XBase) = <Base of the X number>;
           PUKCL_Swap(nu1YBase) = <Base of the Y number>;
           PUKCL_Swap(u2XLength) = <Length of the numbers>;

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(Swap,pvPUKCLParam);
           if (PUKCL(u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error


43.3.4.3.6 Constraints
          The following conditions must be avoided to ensure that the service works correctly:
           • nu1XBase or nu1YBase are not aligned on 32-bit boundaries
           • u2XLength is either <4, > 0xffc, or not a 32-bit length
           • {nu1XBase, u2XLength} or {nu1YBase, u2XLength} do not entirely lie in PUKCCRAM




         © 2019 Microchip Technology Inc.                     Datasheet                             DS60001507E-page 1452
                                                               SAM D5x/E5x Family Data Sheet
                                                              Public Key Cryptography Controller (PUKCC)

           • {nu1XBase, u2XLength} overlaps {nu1YBase,u2YLength}
43.3.4.3.7 Status Returned Values
          Table 43-10. Swap Service Return Codes

                  Returned status                Importance                                 Meaning
                     PUKCL_OK                           –                      Service functioned correctly

43.3.4.4 Fill
43.3.4.4.1 Purpose
          This service performs a memory fill operation, with a given 32-bit constant.
43.3.4.4.2 How to Use the Service

43.3.4.4.3 Description
          This service fills a Crypto RAM space with a provided 32-bit constant: Fill (R, FillValue)
          The service name for this operation is Fill.
43.3.4.4.4 Parameters Definition
          This service can easily be accessed through the use of the PUKCL_Fill() macro.
          Table 43-11. Fill Service Parameters

          Parameter Type Direction.          Location       Data Length Before Executing         After Executing the
                                                                          the Service                  Service
           nu1RBase       nu1         I     Crypto RAM      u2RLength        Base of R           Base of R value filled
                                                                                                   repetitively with
                                                                                                     u4FillValue
          u2RLength       u2          I     Crypto RAM          –           Length of R                Length of R
          u4FillValue     u4          I         –               –           Filling value              Filling value

43.3.4.4.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // Initialize parameters
           PUKCL_Fill(nu1RBase) = <Base of the R number>;
           PUKCL_Fill(u2RLength) = <Length of the R number>;
           PUKCL_Fill(u4FillValue) = <32-bits value to fill with>;

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(Fill,pvPUKCLParam);
           if (PUKCL(u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error

43.3.4.4.6 Constraints
          The following conditions must be avoided to ensure that the service works correctly:
           • nu1RBase are not aligned on 32-bit boundaries
           • u2RLength is either: <4, >0xffc or not a 32-bit length
           • {nu1RBase, u2RLength} do not entirely lie in Crypto RAM




         © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 1453
                                                               SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

43.3.4.4.7 Status Returned Values
          Table 43-12. Fill Service Return Codes

          Returned Status                    Importance               Meaning
          PUKCL_OK                           –                        Service functioned correctly.

43.3.4.5 Fast Copy/Clear
43.3.4.5.1 Purpose
          This service performs a copy from a memory area to another or a memory area clear.
43.3.4.5.2 How to Use the Service
43.3.4.5.3 Description
          This service copies a number X into another number R, padding with zero on the MSB side up to the
          length specified for R.
          R=X
          If the lengths of R and X are equal, a complete fast copy is processed.
          If the length of R is strictly greater than the length of X, X is first copied in the Low Significant Bytes side
          of R, and R is padded with zeros on the Most Significant Bytes side.
          If the pointer on the X area equals zero, R is filled with zeros. This operation can also be made by using
          the Fill service (see 43.3.4.4 Fill).
          The service name for this operation is FastCopy.


                         Important: The length of R must be greater or equal to the length of X.




43.3.4.5.4 Parameters Definition
          This service can easily be accessed through the use of the PUKCL_FastCopy() macro.
          Table 43-13. FastCopy Service Parameters

          Parameter Type Direction           Location     Data Length      Before Executing        After Executing the
                                                                             the Service                 Service
           nu1XBase       nu1         I     Crypto RAM     u2XLength            Base of X            Base of X number
                                                                                                        untouched
           nu1RBase       nu1         I     Crypto RAM     u2RLength            Base of R         Base of R filled with X
          u2RLength       u2          I          –              –              Length of R              Length of R
           u2XLength      u2          I          –              –              Length of X              Length of X

43.3.4.5.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // Initialize parameters
           PUKCL_FastCopy(nu1XBase) = <Base of the X number>;
           PUKCL_FastCopy(nu1RBase) = <Base of the R number>;
           PUKCL_FastCopy(u2XLength) = <Length of the X number>;
           PUKCL_FastCopy(u2RLength) = <Length of the R number>;




         © 2019 Microchip Technology Inc.                        Datasheet                            DS60001507E-page 1454
                                                              SAM D5x/E5x Family Data Sheet
                                                              Public Key Cryptography Controller (PUKCC)

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(FastCopy,pvPUKCLParam);
           if (PUKCL(u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error

43.3.4.5.6 Constraints
          The parameter placements that are not allowed are are as follows.
          If nu1XBase equals zero, no checks are made on nu1XBase (fixed) and u2XLength (unused).
          The following conditions must be avoided to ensure that the service works correctly:
           •   nu1XBase or nu1RBase are not aligned on 32-bit boundaries
           •   u2XLength or u2RLength is either: <4, >0xffc or not a 32-bit length or u2XLength >u2RLength
           •   {nu1XBase, u2XLength} or {nu1RBase, u2RLength} do not entirely lie in Crypto RAM
           •   {nu1XBase, u2XLength} overlaps {nu1RBase,u2RLength}
43.3.4.5.7 Status Returned Values
          Table 43-14. FastCopy Service Return Codes

          Returned status                        Importance           Meaning
          PUKCL_OK                                       –            Service functioned correctly

43.3.4.6 Conditional Copy/Clear
43.3.4.6.1 Purpose
          This service conditionally performs a copy from a memory area to another or a memory area clear.
43.3.4.6.2 How to Use the Service

43.3.4.6.3 Description
          This service copies a number X into another number R, padding with zero on the MSB side up to the
          length specified for R. This copy operation is performed under the conditions specified in the options.
          If the condition is verified, R = X.
          The copy or clear action is made under condition.
          The four possible options for the condition are described in the following table. Two of the conditions
          check the Specific.CarryIn bit (see 43.3.3.2 Accessing Different Library Services).
          The processing is done as follows:
           • If the condition is not verified, nothing is processed.
           • If the condition is verified the copy or clear follows the rules:
                – If the lengths of R and X are equal, a complete fast copy is processed
                – If the length of R is strictly greater than the length of X, X is first copied in the Low Significant
                   Bytes side of R, and R is padded with zeros on the Most Significant Bytes side.
                – If the pointer on the X area equals zero, R is filled with zeros.
          The service name for this operation is CondCopy.




         © 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 1455
                                                                SAM D5x/E5x Family Data Sheet
                                                               Public Key Cryptography Controller (PUKCC)

                          Important: If the condition is verified, the length of R must be greater or equal to the length of
                          X.



43.3.4.6.4 Parameters Definition
          This service can easily be accessed through the use of the PUKCL_CondCopy() and PUKCL() macros.
          Table 43-15. CondCopy Service Parameters

            Parameter        Type Direction      Location      Data Length Before Executing After Executing the
                                                                             the Service          Service
             u2Options         u2           I         –              –              Option for       Option for condition
                                                                                condition (see the    (see the following
                                                                                 following table)           table)
              Specific/        Bit          I         –              –             Bit CarryIn           Bit CarryIn
              CarryIn
            nu1XBase           nu1          I   Crypto RAM      u2XLength           Base of X        Base of X number
                                                                                                        untouched
            nu1RBase           nu1          I   Crypto RAM      u2RLength          Base of R         Base of R filled with
                                                                                                     X if condition holds
            u2RLength          u2           I         –              –             Length of R           Length of R
            u2XLength          u2           I         –              –             Length of X           Length of X

43.3.4.6.5 Available Options
          The option for the condition is set by the u2Options input parameter that must take one of the values
          listed in the following table.
          Table 43-16. CondCopy Service Options

          Option                                          Purpose               Needed parameters
          PUKCL_CONDCOPY_ALWAYS                           Always perform the    nu1XBase,u2XLength,nu1RBase,
                                                          copy                  u2RLength
          PUKCL_CONDCOPY_NEVER                            Never perform the     None
                                                          copy
          PUKCL_CONDCOPY_IF_CARRY                         Perform the copy if   Specific/CarryIn
                                                          CarryIn is 1          nu1XBase,u2XLength,nu1RBase,
                                                                                u2RLength
          PUKCL_CONDCOPY_IF_NOT_CARRY Perform the copy if                       Specific/CarryIn
                                      CarryIn is zero                           nu1XBase,u2XLength,nu1RBase,
                                                                                u2RLength

43.3.4.6.6 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // CarryIn shall be beforehand filled (with zero or one) PUKCL(Specific).CarryIn = ...;




         © 2019 Microchip Technology Inc.                         Datasheet                          DS60001507E-page 1456
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

           // Condition Option PUKCL(u2Options) = ...;

           // Initialize parameters
           PUKCL_CondCopy(nu1XBase) = <Base of the X number>;
           PUKCL_CondCopy(nu1RBase) = <Base of the R number>;
           PUKCL_CondCopy(u2XLength) = <Length of the X number>;
           PUKCL_CondCopy(u2RLength) = <Length of the R number>;

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(CondCopy,pvPUKCLParam);
           if (PUKCL(u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error


43.3.4.6.7 Constraints
          The parameters placement that are not allowed are listed below.
          If the conditional option and the CarryIn do not lead to execute the copy, no checks are made on the
          constraints to be respected.
          If nu1XBase equals zero, no checks are made on nu1XBase (fixed) and u2XLength (unused).
          The following conditions must be avoided to ensure that the service works correctly:
           •   nu1XBase or nu1RBase are not aligned on 32-bit boundaries
           •   u2XLength or u2RLength is either: <4, >0xffc or not a 32-bit length or u2XLength >u2RLength
           •   {nu1XBase, u2XLength} or {nu1RBase, u2RLength} do not entirely lie in Crypto RAM
           •   {nu1XBase, u2XLength} overlaps {nu1RBase,u2RLength}
43.3.4.6.8 Status Returned Values
          Table 43-17. CondCopy Service Return Codes

          Returned status                   Importance Meaning
          PUKCL_WRONG_SERVICE Severe                   An inconsistency has been detected between the called
                                                       service and the provided service number.
          PUKCL_OK                          –          Service functioned correctly

43.3.4.7 Small Multiply, Add, Subtract, Exclusive OR

43.3.4.7.1 Purpose
          This purpose of this service is to multiply a large number X by a single-word number, MulValue, and
          perform an optional accumulation/subtract with a large number Z, returning the result R.
          The following options are available:
           •   Work in the GF(2n) or in the standard GF(p) arithmetic integer field
           •   Add of a supplemental CarryOperand
           •   Overlap of the operands is possible, taking into account some constraints
           •   Modulo-reduction of the computation result (see 43.3.5.1 Modular Reduction)
          In addition to a multiply, possible uses of this service can include:
            • Copy a block of data from one place to another (if u4MulValue is 1). This operation can alternatively
               be made by using the Fast Copy service (see 43.3.4.5 Fast Copy/Clear).
            • Adding/Subtracting two numbers (if u4MulValue is1)
            • Xoring two blocks of data (if u4MulValue is 1 and the selected mathematical field is GF(2n))




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 1457
                                                            SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

43.3.4.7.2 How to Use the Service

43.3.4.7.3 Description
          This service processes the following operation (if not computing a modular reduction of the result):
          R = [Z] ± (MulValue × X + CarryOperand)
          Or (if computing a modular reduction of the result):
          R = ([Z] ± (MulValue × X + CarryOperand))mod N
          The service name for this operation is Smult.
          The result of the Small Multiply Operation is stored on u2RLength bytes, so the choice of this length
          compared to u2XLength may lead to:
           • A truncation if the result is too big to be stored on u2RLengthbytes.
           • A padding on the MSB side if the result does not take all the u2RLengthbytes.
             However, in all cases this rule must be followed:


                             Important: The length of R must be greater than or equal to the length of X.




          In these computations, the following parameters need to be provided:
           •   R the result (pointed by{nu1RBase,u2Rlength})
           •   X one input number or GF(2n) polynomial (pointed by{nu1XBase,u2XLength})
           •   Z one optional input number or GF(2n) polynomial (pointed by{nu1ZBase,u2Rlength}).
           •   MulValue one input number or GF(2n)polynomial on one word (provided in u4MulValue)
           •   CarryOperand (provided through the CarryOptions and Carry values).


                             Important: Even if neither accumulation nor subtraction is specified, the nu1ZBase must
                             always be filled and point to a Crypto RAM space. It this case, nu1ZBase can point to the
                             same space as the nu1RBase.


          If using the modular reduction option, the Multiply operation is followed by a reduction (see 43.3.5.1
          Modular Reduction) and the following parameters must be additionally provided:
           • N—the modulus (pointed by {nu1ModBase,u2Modlength +4})
           • Cns—the reduction constant
              – In case of Big reduction, Cns is pointed by {nu1CnsBase,64bytes}.
              – In case of Fast or Normalized reduction, Cns is pointed by {nu1CnsBase,u2ModLength +8}




         © 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 1458
                                                             SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

                             Important:
                             The result buffer R must first be padded with zero bytes until its length is sufficient to
                             perform the reduction (2*u2ModLength + 8) to be used by the Modular Reduction service
                             as an input parameter.
                             The result of the reduction is written in the area X pointed by {nu1XBase, u2ModLength
                             + 4}.


           • For example, if relevant u2ModLength is 0x80 bytes and u2XLength is 0x80 too, the length of the
             Rspace may be 2*(u2ModLength + 4) = 0x108 bytes.
             In case of fast or normalized reduction, the length of the result may be u2ModLength + 4 so 0x84
             bytes. Therefore, the zone X may lengths 0x84 bytes (at least). The multiplication of X by 1 word
             provide a result in the zone R which MSB bytes will be padded with zero bytes.
              In that example, the length of the zone R will be 2*u2ModLength + 8 = 0x108 bytes.
43.3.4.7.4 Parameters Definition
          Table 43-18. Smult Service Parameters

             Parameter         Type Direction     Location      Data Length          Before          After Executing
                                                                                  Executing the        the Service
                                                                                    Service
              u2Options          u2         I         –               –            Options (see        Options (see
                                                                                     below)              below)
            Specific/Gf2n       Bits        I         –               –           GF(2n) Bit and             –
              CarryIn                                                               Carry In
             Specific/          Bits        I         –               –                  –           Carry Out, Zero
           CarryOut Zero                                                                             Bit and Violation
             Violation                                                                                    Bit filled
                                                                                                     according to the
                                                                                                           result
            nu1ModBase          nu1         I      Crypto       u2ModLength         Base of N           Base of N
                                                    RAM             +4                                  untouched
            nu1CnsBase          nu1         I      Crypto       u2ModLength        Base of Cns         Base of Cns
                                                    RAM             +8                                  untouched
            u2ModLength          u2         I         –               –            Length of N          Length of N
              nu1XBase          nu1         I      Crypto      u2XLength or         Base of X         Base of X ( see
                                                    RAM        u2ModLength                               Note 2)
                                                              + 4 (see Note 1)
             u2XLength           u2         I         –               –            Length of X          Length of X
              nu1ZBase          nu1         I      Crypto        u2RLength          Base of Z           Base of Z
                                                    RAM                                                 untouched
              nu1RBase          nu1         I      Crypto        u2RLength          Base of R         Base of R (see
                                                    RAM                                                  Note 3)
             u2RLength           u2         I         –               –            Length of R          Length of R




         © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1459
                                                               SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

          ...........continued
             Parameter           Type Direction   Location        Data Length          Before          After Executing
                                                                                    Executing the        the Service
                                                                                      Service
             u4MulValue           u4        I          –                –              Value of        Value of MulValue
                                                                                       MulValue            untouched

          Note:
           1. If a reduction option is specified, the area X will be, if necessary, extended to u2ModLength + 4
                bytes.
           2. If Smult is without reduction, X is untouched. If Smult is with reduction, X is filled with the final
                result.
           3. If Smult is without reduction, R is filled with the final result. If Smult is with reduction, R is corrupted.
43.3.4.7.5 Available Options
          The options are set by the u2Options input parameter, which is composed of:
           • the mandatory Small Multiplication operation option described in Table 43-19
           • the mandatory CarryOperand option described in Table 43-20 and Table 43-21
           • the facultative Modular Reduction option (see 43.3.5.1 Modular Reduction). If the Modular Reduction
             is not requested, this option is absent.
          The u2Options number is calculated by an “Inclusive OR” of the options. Some examples in C language
          are:
           • Operation: Small Multiply only without carry and without Modular Reduction
             PUKCL(u2Options) = SET_MULTIPLIEROPTION(PUKCL_SMULT_ONLY) |
             SET_CARRYOPTION(CARRY_NONE);
           • Operation: Small Multiply with addition with Specific/CarryIn addition and with Fast Modular
             Reduction
             PUKCL(u2Options) =SET_MULTIPLIEROPTION(PUKCL_SMULT_ADD) |
             SET_CARRYOPTION(ADD_CARRY) | PUKCL_REDMOD_REDUCTION |
             PUKCL_REDMOD_USING_FASTRED;
          The following table lists all of the necessary parameters for the Small Multiply option. When the Addition
          or Subtraction option is not chosen, it is not necessary to fill in the nu1ZBase parameter.
          Table 43-19. Smult Service Operation Options

          Option                                                Purpose                    Required Parameters
          SET_MULTIPLIEROPTION(PUKCL_SMULT_                     Perform R =                nu1RBase, u2RLength,
          ONLY)                                                 MulValue*X +               nu1XBase, u2XLength,
                                                                CarryOperand               u4MulValue
          SET_MULTIPLIEROPTION(PUKCL_SMULT_                     Perform R = Z +            nu1RBase, u2RLength,
          ADD)                                                  MulValue*X +               nu1ZBase, nu1XBase,
                                                                CarryOperand               u2XLength,u4MulValue
          SET_MULTIPLIEROPTION(PUKCL_SMULT_                     Perform R = Z -            nu1RBase, u2RLength,
          SUB)                                                  (MulValue*X +              nu1ZBase, nu1XBase,
                                                                CarryOperand)              u2XLength,u4MulValue




         © 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 1460
                                                             SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

43.3.4.7.6 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // Gf2n and CarryIn shall be beforehand filled (with zero or one)
           PUKCL(Specific).Gf2n = ...;
           PUKCL(Specific).CarryIn = ...; PUKCL(u2Options) =...;

           // Depending on the option specified, not all fields should be filled
           PUKCL_Smult(nu1XBase) = <Base of the X number>;
           PUKCL_Smult(u2XLength) = <Length of the X number>;
           PUKCL_Smult(nu1RBase) = <Base of the R number>;
           PUKCL_Smult(u2RLength) = <Length of the R number>;
           PUKCL_Smult(nu1ZBase) = <Base of the Z number>;
           PUKCL_Smult(u4MulValue) = <Value to be multiplied with>;

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(Smult,pvPUKCLParam);
           if (PUKCL(u2Status) == PUKCL_OK)
                       {
                       // The Small multiplication has been executed correctly
                       ...
                       }
           else // Manage the error

          Note:
          The length of R must be greater or equal to the length of X. Additional options are available through the
          use of a modular reduction to be executed at the end of this operation. Some important considerations
          have to be taken into account concerning the length of resulting operands to get a mathematically correct
          result.
          The output of this operation is not obviously compatible with the modular reduction, as it may be either
          smaller or bigger. In the case (most of the time) where the result (pointed by nu1RBase) is smaller in size
          than twice the modulus plus one word, it is mandatory to add padding bytes to zero. Otherwise, the
          reduced value will be taken considering the high order words (potentially uninitialized) as part of the
          number, thus resulting in a mathematically correct but unexpected result.
          In the case that the result is bigger than twice the modulus plus one word, the modular reduction feature
          has to be executed as a separate operation, using an Euclidean division.
43.3.4.7.7 Constraints
          For the case of a small multiplication with an option indicating either subtraction or accumulation, the
          following conditions must be avoided to ensure the service works correctly:
           • nu1XBase, nu1RBase or nu1ZBase are not aligned on 32-bit boundaries
           • {nu1XBase, u2XLength}, {nu1ZLength, u2RLength} or {nu1RBase, u2RLength} do not entirely lie in
             Crypto RAM
           • u2XLength or u2RLength is either: < 4, > 0xffc or not a 32-bit length or u2XLength >u2RLength
           • {nu1RBase, u2RLength} overlaps {nu1XBase, u2XLength} or nu1R < nu1Z and
             {nu1RBase,u2RLength} overlaps {nu1ZBase, u2RLength}
          If the nu1R value is greater or equals to the nu1Z one, the overlapping between R and Z is allowed.
          If a modular reduction is specified, the relevant parameters must be defined according to the chosen
          reduction and follow the description in 43.3.5.1 Modular Reduction. Additional constraints to be
          respected and error codes are described in this section and in Table 43-22.
          Multiplication with Accumulation or Subtraction
          When the options bits specify that either an Accumulation or a Subtraction should be performed, this
          service performs the following operation:




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1461
                                                          SAM D5x/E5x Family Data Sheet
                                                         Public Key Cryptography Controller (PUKCC)

         R = (Z ± (MulValue × X + CarryOperand))mod BRLength
         Table 43-20. Smult Service (with Accumulate/Subtract From) Carry Settings

          Carry Options                                       CarryOperand Resulting Operation
          SET_CARRYOPTION(ADD_CARRY)                          CarryIn              R = Z ± (MulValue*X + CarryIn)
          SET_CARRYOPTION(SUB_CARRY)                          - CarryIn            R = Z ± (MulValue*X - CarryIn)
          SET_CARRYOPTION(ADD_1_PLUS_CARRY)                   1 + CarryIn          R = Z ± (MulValue*X + 1 + CarryIn)
          SET_CARRYOPTION(ADD_1_MINUS_CARRY)                  1 - CarryIn          R = Z ± (MulValue*X + 1 - CarryIn)
          SET_CARRYOPTION(CARRY_NONE)                         0                    R = Z ± (MulValue*X)
          SET_CARRYOPTION(ADD_1)                              1                    R = Z ± (MulValue*X + 1)
          SET_CARRYOPTION(SUB_1)                              -1                   R = Z ± (MulValue*X - 1)
          SET_CARRYOPTION(ADD_2)                              2                    R = Z ± (MulValue*X + 2)

         Multiplication without Accumulation or Subtraction
         When the case the options bits specify that neither an Accumulation nor a Subtraction should be
         performed, this service performs the following operation:

         R = (MulValue × X + CarryOperand)mod BRLength
         Table 43-21. Smult Service Carry Settings

          Carry Options                                            CarryOperand        Resulting Operation
          SET_CARRYOPTION(ADD_CARRY)                               CarryIn             R = MulValue*X + CarryIn
          SET_CARRYOPTION(SUB_CARRY)                               - CarryIn           R = MulValue*X - CarryIn
          SET_CARRYOPTION(ADD_1_PLUS_CARRY)                        1 + CarryIn         R = MulValue*X + 1 + CarryIn
          SET_CARRYOPTION(ADD_1_MINUS_CARRY)                       1 - CarryIn         R = MulValue*X + 1 - CarryIn
          SET_CARRYOPTION(CARRY_NONE)                              0                   R = MulValue*X
          SET_CARRYOPTION(ADD_1)                                   1                   R = MulValue*X + 1
          SET_CARRYOPTION(SUB_1)                                   -1                  R = MulValue*X - 1
          SET_CARRYOPTION(ADD_2)                                   2                   R = MulValue*X + 2

43.3.4.7.8 Status Returned Values
         Table 43-22. Smult Service Return Codes

          Returned Status                   Importance                 Meaning
          PUKCL_OK                          –                          Service functioned correctly

43.3.4.8 Compare
43.3.4.8.1 Purpose
         The purpose of this service is to compare two numbers in classical arithmetic GF(p).




         © 2019 Microchip Technology Inc.                     Datasheet                               DS60001507E-page 1462
                                                               SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

                         Important: This service works only with integers.




43.3.4.8.2 How to Use the Service

43.3.4.8.3 Description
          This service accepts two numbers in classical arithmetic in input and performs a comparison, virtually
          subtracting (X + CarryIn) from Y:
          CompareGetFlags (Y - (X + CarryIn))
          The numbers X and Y are untouched but the resulting flags CarryOut and the Zero Bit are filled. If the
          lengths of Y and X are equal, a comparison is processed.
          If the length of Y is strictly greater than the length of X, X is first virtually padded with zeros on the Most
          Significant Bytes side, then a comparison is processed.
          Note: The length of Y must be greater or equal to the length of X.
          In this computation, the following data need to be provided:
           • X (pointed by{nu1XBase,u2XLength})
           • Y (pointed by{nu1YBase,u2YLength})
          The service name for this operation is Comp.

43.3.4.8.4 Parameters Definition
          Table 43-23. Comp Service Parameters

          Parameter           Type Direction Location          Data Length Before Executing After Executing the
                                                                           the Service      Service
          Specific/Gf2n       Bits    I         –              –               GF(2n) Bit and       –
          CarryIn                                                              Carry In
          Specific/           Bits    I         –              –               –                    Carry Out, Zero Bit
          CarryOut Zero                                                                             and Violation Bit
          Violation                                                                                 filled according to
                                                                                                    the result
          nu1XBase            nu1     I         Crypto RAM u2XLength           Base of X            Base of X
          u2XLength           u2      I         –              –               Length of X          Length of X
          nu1YBase            nu1     I         Crypto RAM u2YLength           Base of Y            Base of Y
          u2YLength           u2      I         –              –               Length of Y          Length of Y

43.3.4.8.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // CarryIn shall be beforehand filled (with zero or one) PUKCL(Specific).CarryIn = ...;

           // Initializing parameters
           PUKCL_Comp(nu1XBase) = <Base of the ram location of X>;
           PUKCL_Comp(u2XLength) = <Length of X>;
           PUKCL_Comp(nu1YBase) = <Base of the ram location of Y>;
           PUKCL_Comp(u2YLength) = <Length of Y>;




         © 2019 Microchip Technology Inc.                          Datasheet                         DS60001507E-page 1463
                                                            SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

           // vPUKCL_Process() is a macro command,
           // and then calls the library...
           vPUKCL_Process(Comp,pvPUKCLParam);
           if (PUKCL(u2Status) == PUKCL_OK)
                       {
                       // The COMPARE has been executed correctly
                       // CarryOut, Zero ... are available
                       ... = PUKCL(Specific).CarryOut;
                       ... = PUKCL(Specific).Zero;
                       }
           else // Manage the error

43.3.4.8.6 Constraints
          The following conditions must be avoided to ensure that the service works correctly:
           • nu1XBase or nu1YBase are not aligned on 32-bit boundaries
           • {nu1XBase, u2XLength} or {nu1YLength, u2YLength} are not in Crypto RAM
           • u2XLength or u2YLength is either: < 4, > 0xffc or not a 32-bit length or u2XLength >u2YLength
43.3.4.8.7 Status Returned Values
          Table 43-24. Comp Service Return Codes

          Returned Status                   Importance               Meaning
          PUKCL_OK                          –                        Service functioned correctly

43.3.4.9 Full Multiply
43.3.4.9.1 Purpose
          The purpose of this service is to multiply two large numbers, X and Y, and optionally accumulate/subtract
          from a third large number, Z, returning the result, R.
          The available options are as follows:
           •   Work in the GF(2n) field or in the standard arithmetic field
           •   Add of a supplemental CarryOperand
           •   Overlap of the operands is possible, taking into account some constraints
           •   Modular Reduction of the computation result (see 43.3.5.1 Modular Reduction)
43.3.4.9.2 How to Use the Service

43.3.4.9.3 Description
          This service provides the following (if not computing a modular reduction of the result):

          R = [Z] ± (X × Y + CarryOperand)
          Or (if computing a modular reduction of the result):

          R = ([Z] ± (X × Y + CarryOperand))mod N
          The service name for this operation is Fmult.
          In these computations, the following data has to be provided:
           •   R the result (pointed by {nu1RBase,u2Xlength +u2YLength})
           •   X one input number or GF(2n) polynomial (pointed by{nu1XBase,u2XLength})
           •   Y one input number or GF(2n) polynomial (pointed by{nu1YBase,u2YLength})
           •   Z one optional input number or GF(2n) polynomial (pointed by {nu1ZBase,u2Xlength +u2YLength})




         © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 1464
                                                            SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

           • CarryOperand (provided through the Carry Options and Carry values)


                        Important: Even if neither accumulation nor subtraction is specified, the nu1ZBase must
                        always be filled and point to a Crypto RAM space. It this case, nu1ZBase can point to the same
                        space as the nu1RBase.


          If using the big modular reduction option, the Multiply operation is followed by a reduction (see 43.3.5.1
          Modular Reduction). In this case, the length of Cns is 64 bytes.
          If using the modular reduction option, the Multiply operation is followed by a reduction (see 43.3.5.1
          Modular Reduction). In this case the following parameters must be additionally provided:
           • N—the modulus (pointed by {nu1ModBase,u2Modlength +4})
           • Cns—the reduction constant
              – In case of Big reduction, Cns is pointed by {nu1CnsBase,64bytes}.
              – In case of Fast or Normalized reduction, Cns is pointed by (pointed by
                {nu1CnsBase,u2ModLength+ 8})
          Note:
          The result buffer R must first be padded with zero bytes until its length is sufficient to perform the
          reduction (2*u2ModLength + 8) to be used by the Modular Reduction service as an input parameter.
          The result of the reduction is written in the area X pointed by {nu1XBase, u2ModLength + 4}.
          For example, if u2ModLength, u2XLength and u2YLength are 0x80 bytes, the length of the R space is
          2*(u2ModLength + 4) = 0x108 bytes because of the constraints of modular reduction.
          In case of Fast or Normalized Reduction, the length of the result is u2ModLength + 4 so 0x84 bytes.
          Thus, the zone X has a length of 0x84 bytes (at least). The multiplication of X by Y provides a result of
          length 0x100 bytes in the zone R so the 8 MSB bytes must be previously padded with zero bytes (in
          offsets 0x100 to 0x107).
43.3.4.9.4 Parameters Definition
          Table 43-25. Fmult Service Parameters

          Parameter            Type Direction Location       Data Length         Before             After Executing
                                                                                 Executing the      the Service
                                                                                 Service
          u2Options            u2      I       –             –                   Options (see       Options (see
                                                                                 below)             below)
          Specific/Gf2n        Bits    I       –             –                   GF(2n) Bit and     –
          CarryIn                                                                Carry In
          Specific/            Bits    I       –             –                   –                  Carry Out, Zero
          CarryOut Zero                                                                             Bit and Violation
          Violation                                                                                 Bit filled
                                                                                                    according to the
                                                                                                    result
          nu1ModBase           nu1     I       Crypto        u2ModLength + 4 Base of N              Base of N
                                               RAM                                                  untouched




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1465
                                                               SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

          ...........continued
          Parameter              Type Direction Location        Data Length          Before            After Executing
                                                                                     Executing the     the Service
                                                                                     Service
          nu1CnsBase             nu1   I         Crypto         u2ModLength + 8 Base of Cns            Base of Cns
                                                 RAM            or 64 bytes                            untouched
          u2ModLength            u2    I         –              –                    Length of N       Length of N
          nu1XBase               nu1   I         Crypto         u2XLength or    Base of X              Base of X (see
                                                 RAM            u2ModLength + 4                        Note 2)
                                                                (see Note 1)
          u2XLength              u2    I         –              –                    Length of X       Length of X
          nu1YBase               nu1   I         Crypto         u2YLength            Base of Y         Base of Y
                                                 RAM
          u2YLength              u2    I         –              –                    Length of Y       Length of Y
          nu1ZBase               nu1   I         Crypto         u2XLength +          Base of Z         Base of Z
                                                 RAM            u2YLength                              untouched
          nu1RBase               nu1   I         Crypto         u2XLength +          Base of R         Base of R (see
                                                 RAM            u2YLength                              Note 3)

          Note:
           1. In case of a reduction option is specified, if necessary, the area X will be extended to u2ModLength
                + 4 bytes.
           2. If FMult is without reduction, X is untouched. If FMult is with reduction, X is filled with the final
                result.
           3. If FMult is without reduction, R is filled with the final result. If FMult is with reduction, R is corrupted.
43.3.4.9.5 Available Options
          The options are set by the u2Options input parameter, which is composed of:
           • the mandatory Full Multiplication operation option described in Table 43-26
           • the mandatory CarryOperand option described in Table 43-27 and Table 43-28
           • the facultative Modular Reduction option (see 43.3.5.1 Modular Reduction). If the Modular Reduction
             is not requested, this option is absent.
          The u2Options number is calculated by an Inclusive OR of the options.
          Some Examples in C language are:
           • Operation: Full Multiply only without carry and without Modular Reduction
             PUKCL(u2Options) = SET_MULTIPLIEROPTION(PUKCL_FMULT_ONLY) |
             SET_CARRYOPTION(CARRY_NONE);
           • Operation: Full Multiply with addition with Specific/CarryIn addition and with Fast Modular Reduction
             PUKCL(u2Options) = SET_MULTIPLIEROPTION(PUKCL_FMULT_ADD) |
              SET_CARRYOPTION(ADD_CARRY) |
              PUKCL_REDMOD_REDUCTION |
              PUKCL_REDMOD_USING_FASTRED;




         © 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 1466
                                                          SAM D5x/E5x Family Data Sheet
                                                         Public Key Cryptography Controller (PUKCC)

         The following table shows all of the necessary parameters for the Full Multiply option. When the Addition
         or Subtraction option is not chosen, it is not necessary to fill in the nu1ZBase parameter.
         Table 43-26. Fmult Service Options

          Option                                              Purpose                      Required
                                                                                           Parameters
          SET_MULTIPLIEROPTION(PUKCL_FMUL_ONLY) Perform R = X*Y +                          nu1RBase,
                                                CarryOperand                               nu1YBase,
                                                                                           u2YLength,
                                                                                           nu1XBase, u2XLength
          SET_MULTIPLIEROPTION(PUKCL_FMUL_ADD)                Perform R = Z + X*Y +        nu1RBase,
                                                              CarryOperand                 nu1ZBase, nu1YBase,
                                                                                           u2YLength,
                                                                                           nu1XBase, u2XLength
          SET_MULTIPLIEROPTION(PUKCL_FMUL_SUB)                Perform R = Z - (X*Y +       nu1RBase,
                                                              CarryOperand)                nu1ZBase, nu1YBase,
                                                                                           u2YLength,
                                                                                           nu1Xlength,
                                                                                           u2XLength

43.3.4.9.6 Code Example
          PUKCL_PARAM PUKCLParam;
          PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;


          // Gf2n and CarryIn shall be beforehand filled (with zero or one)
          PUKCL(Specific).Gf2n = ...;
          PUKCL(Specific).CarryIn = ...;

          PUKCL(u2Option) =...;
          // Depending on the option specified, not all fields should be filled
          PUKCL_Fmult(nu1XBase) = <Base of the ram location of X>;
          PUKCL_Fmult(u2XLength) = <Length of X>;
          PUKCL_Fmult(nu1YBase) = <Base of the ram location of Y>;
          PUKCL_Fmult(u2YLength) = <Length of Y>;
          PUKCL_Fmult(nu1ZBase) = <Base of the ram location of Z>;
          PUKCL_Fmult(nu1RBase) = <Base of the ram location of R>;

          // vPUKCL_Process() is a macro command, which populates the service name
          // and then calls the library...
          vPUKCL_Process(Fmult,pvPUKCLParam);
          if (PUKCL(u2Status) == PUKCL_OK)
                      {
                      // The Full multiply has been executed correctly
                      ...
                      }
          else // Manage the error




        © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1467
                                                            SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

43.3.4.9.7 Important Considerations for Modular Reduction of a Fmult Computation Result
          Note:
          Additional options are available through the use of a modular reduction to be executed at the end of this
          operation. Some important considerations have to be taken into account concerning the length of
          resulting operands to get a mathematically correct result.
          The output of this operation is not always compatible with the modular reduction as it may be either
          smaller or bigger. In the case (most of the time) the result (pointed by nu1RBase) is smaller in size than
          “twice the modulus plus one word” by one word, a padding word must be added to zero. Otherwise, the
          reduced value will be taken considering the high order words (potentially uninitialized) as part of the
          number, thus resulting in getting a mathematically correct but unexpected result.
          In the case that the result is bigger than twice the modulus plus one word, the modular reduction feature
          has to be executed as a separate operation, using an Euclidean division.
43.3.4.9.8 Constraints
          The following conditions must be avoided to ensure that the service works correctly:
           • nu1XBase, nu1YBase, nu1RBase or nu1ZBase are not aligned on 32-bit boundaries
           • {nu1XBase, u2XLength}, {nu1YLength, u2YLength}, {nu1ZBase, u2XLength+u2YLength}
             or{nu1RBase, u2XLength+u2YLength} are not in Crypto RAM
           • u2XLength, u2YLength is either: < 4, > 0xffc or not a 32-bit length
           • {nu1RBase, u2XLength+u2YLength} overlaps {nu1YBase, u2YLength} or{nu1RBase, u2XLength
             +u2YLength} overlaps {nu1XBase, u2XLength}
           • {nu1RBase, u2XLength+u2YLength} overlaps {nu1ZBase, u2XLength+u2YLength} and nu1RBase>
             nu1ZBase
          If a modular reduction is specified, the relevant parameters must be defined according to the chosen
          reduction and follow the description in 43.3.5.1 Modular Reduction. Additional constraints to be
          respected and error codes are described in this section and in Table 43-49.
          Multiplication with Accumulation or Subtraction
          In the case where the options bits specify that either an Accumulation or a subtraction should be
          performed, this service performs the following operation:
          R = (Z ± (X × Y + CarryOperand))mod BXLength + YLength
          Table 43-27. Fmult Service (with Accumulate/Subtract From) Carry Settings

          Option AND CARRYOPTIONS                                  CarryOperand       Resulting Operation
          SET_CARRYOPTION(ADD_CARRY)                               CarryIn            R = Z ± (X*Y + CarryIn)
          SET_CARRYOPTION(SUB_CARRY)                               - CarryIn          R = Z ± (X*Y - CarryIn)
          SET_CARRYOPTION(ADD_1_PLUS_CARRY)                        1 + CarryIn        R = Z ± (X*Y + 1 + CarryIn)
          SET_CARRYOPTION(ADD_1_MINUS_CARRY)                       1 - CarryIn        R = Z ± (X*Y + 1 - CarryIn)
          SET_CARRYOPTION(CARRY_NONE)                              0                  R = Z ± (X*Y)
          SET_CARRYOPTION(ADD_1)                                   1                  R = Z ± (X*Y + 1)
          SET_CARRYOPTION(SUB_1)                                   -1                 R = Z ± (X*Y - 1)
          SET_CARRYOPTION(ADD_2)                                   2                  R = Z ± (X*Y + 2)




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1468
                                                             SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

          Multiplication without Accumulation or Subtraction
          In the case the options bits specify that either an Accumulation or a subtraction should be performed, this
          service performs the following operation:
          R = (X × Y + CarryOperand)mod BXLength + YLength
          Table 43-28. Fmult Service Carry Settings

          Option AND CARRYOPTIONS                                       CarryOperand       Resulting Operation
          SET_CARRYOPTION(ADD_CARRY)                                    CarryIn            R = X*Y + CarryIn
          SET_CARRYOPTION(SUB_CARRY)                                    - CarryIn          R = X*Y - CarryIn
          SET_CARRYOPTION(ADD_1_PLUS_CARRY)                             1 + CarryIn        R = X*Y + 1 + CarryIn
          SET_CARRYOPTION(ADD_1_MINUS_CARRY)                            1 - CarryIn        R = X*Y + 1 - CarryIn
          SET_CARRYOPTION(CARRY_NONE)                                   0                  R = X*Y
          SET_CARRYOPTION(ADD_1)                                        1                  R = X*Y + 1
          SET_CARRYOPTION(SUB_1)                                        -1                 R = X*Y - 1
          SET_CARRYOPTION(ADD_2)                                        2                  R = X*Y + 2

43.3.4.9.9 Status Returned Values
          Table 43-29. Fmult Service Return Codes

          Returned Status                   Importance               Meaning
          PUKCL_OK                          –                        Service functioned correctly

43.3.4.10 Square
43.3.4.10.1 Purpose
          The purpose of this service is to compute the square of a big number and optionally accumulate/subtract
          from a second big number.
          Please note that this service uses an optimized implementation of the squaring. It also means that when
          the GF(2n) flag is set, the execution time will be smaller than when not set (in that case, the squaring
          execution time will still be smaller than for a standard multiplication).
          The available options are as follows:
           •   Work in the GF(2n) or in the standard integer arithmetic field
           •   Add of a supplemental CarryOperand
           •   Overlapping of the operands is possible, taking into account some constraints
           •   Modular Reduction of the computation result
43.3.4.10.2 How to Use the Service

43.3.4.10.3 Description
          This service provides the following (if not computing a modular reduction of the result):

          R = [Z] ± (X2 + CarryOperand)
          Or (if computing a modular reduction of the result):
          R = ([Z] ± (X2 + CarryOperand))mod N




         © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 1469
                                                            SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

         The service name for this operation is Square.
         In these computations, the following data has to be provided:
           •   R the result (pointed by {nu1RBase,2 *u2Xlength})
           •   X one input number or GF(2n) polynomial (pointed by{nu1XBase,u2XLength})
           •   Z one optional input number or GF(2n) polynomial (pointed by {nu1ZBase,2 *u2Xlength})
           •   CarryOperand (provided through the CarryOptions and Carry values)


                        Important: Even if neither accumulation nor subtraction is specified, the nu1ZBase must
                        always be filled and point to a Crypto RAM space. It this case, nu1ZBase can point to the same
                        space as the nu1RBase.


         If using the big modular reduction option, the Multiply operation is followed by a reduction (see 43.3.5.1
         Modular Reduction). In this case, the length of Cns is 64 bytes.
         If using the modular reduction option the Square operation is followed by a reduction (see 43.3.5.1
         Modular Reduction). In this case the following parameters must be additionally provided:
           • N—the modulus (pointed by {nu1ModBase,u2Modlength +4}).
           • Cns—the reduction constant (pointed by {nu1CnsBase,u2Modlength +8})
              – In case of big reduction option, the length of Cns is 64bytes.
         Note:
         The result buffer R must first be padded with zero bytes until its length is sufficient to perform the
         reduction (2*u2ModLength + 8) to be used by the Modular Reduction service as an input parameter.
         The result of the reduction is written in the area X pointed by {nu1XBase, u2ModLength + 4}.
         For example, if u2ModLength, u2XLength is 0x80 bytes, the length of the R space is 2*(u2ModLength
         + 4) = 0x108 bytes because of the constraints of modular reduction.
         In case of Fast or Normalized Reduction, the length of the result is u2ModLength + 4 so 0x84 bytes.
         Thus, the zoneX has a length of 0x84 bytes (at least). The square of X provides a result of length 0x100
         bytes in the zone R so the 8 MSB bytes previously must be previously padded with zero bytes (in offsets
         0x100 to 0x107).
43.3.4.10.4 Parameters Definition
         Table 43-30. Square Service Parameters

          Parameter            Type Direction Location      Data Length          Before             After Executing
                                                                                 Executing the      the Service
                                                                                 Service
          u2Options            u2      I       –            –                    Options (see       Options (see
                                                                                 below)             below)
          Specific/Gf2n        Bits    I       –            –                    GF(2n) Bit and     –
          CarryIn                                                                Carry In




         © 2019 Microchip Technology Inc.                    Datasheet                            DS60001507E-page 1470
                                                            SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

          ...........continued
          Parameter              Type Direction Location    Data Length         Before            After Executing
                                                                                Executing the     the Service
                                                                                Service
          Specific/              Bits   I       –           –                   –                 Carry Out, Zero
          CarryOut Zero                                                                           Bit and Violation
          Violation                                                                               Bit filled
                                                                                                  according to the
                                                                                                  result
          nu1ModBase             nu1    I       Crypto      u2ModLength + 4 Base of N             Base of N
                                                RAM                                               untouched
          nu1CnsBase             nu1    I       Crypto      u2ModLength + 8 Base of Cns           Base of Cns
                                                RAM         or 64 bytes                           untouched
          u2ModLength            u2     I       –           –                   Length of N       Length of N
          nu1XBase               nu1    I       Crypto      u2XLength or    Base of X             Base of X ( see
                                                RAM         u2ModLength + 4                       Note 2)
                                                            (see Note 1)
          u2XLength              u2     I       –           –                   Length of X       Length of X
          nu1ZBase               nu1    I       Crypto      2 * u2XLength       Base of Z         Base of Z
                                                RAM
          nu1RBase               nu1    I       Crypto      2 * u2XLength       Base of R         Base of R (see
                                                RAM                                               Note 3)

          Note:
           1. In case of a reduction option is specified, the area X will be, if necessary, extended to u2ModLength
                + 4 bytes.
           2. If Square is without reduction, X is untouched. If Square is with reduction, X is filled with the final
                result.
           3. If Square is without reduction, R is filled with the final result. If Square is with reduction, R is
                corrupted.
43.3.4.10.5 Available Options
          The options are set by the u2Options input parameter, which is composed of:
           • the mandatory Square operation option described in Table 43-31
           • the mandatory CarryOperand option described in Table 43-32 and Table 43-33
           • the facultative Modular Reduction option (see 43.3.5.1 Modular Reduction). If the Modular Reduction
             is not requested, this option is absent.
          The u2Options number is calculated by an Inclusive OR of the options. Some Examples in C language
          are:
           • Operation: Square only without carry and without Modular Reduction
             PUKCL(u2Options) = SET_MULTIPLIEROPTION(PUKCL_SQUARE_ONLY) |
             SET_CARRYOPTION(CARRY_NONE);
           • Operation: Square with addition with Specific/CarryIn addition and with Fast Modular Reduction




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1471
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

              PUKCL(u2Options) = SET_MULTIPLIEROPTION(PUKCL_SQUARE_ADD) |
              SET_CARRYOPTION(ADD_CARRY) | PUKCL_REDMOD_REDUCTION |
              PUKCL_REDMOD_USING_FASTRED;
         The following table lists all of the necessary parameters for the Square option. When the Addition or
         Subtraction option is not chosen it is not necessary to fill in the nu1ZBase parameter.
         Table 43-31. Square Service Options

          Option                                       Purpose                              Required Parameters
          SET_MULTIPLIEROPTION(PUKCL_                  Perform R = X2 + CarryOperand        nu1RBase, nu1ZBase,
          SQUARE_ONLY)
                                                                                            nu1XBase, u2XLength

          SET_MULTIPLIEROPTION(PUKCL_                  Perform R = Z + X2 +                 nu1RBase, nu1ZBase,
          SQUARE_ADD)                                  CarryOperand
                                                                                            nu1XBase, u2XLength

          SET_MULTIPLIEROPTION(PUKCL_                  Perform R = Z - (X2 +                nu1RBase, nu1ZBase,
          SQUARE_SUB)                                  CarryOperand)
                                                                                            nu1Xlength, u2XLength

43.3.4.10.6 Code Example
          PUKCL_PARAM PUKCLParam;
          PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;


          // Gf2n and CarryIn shall be beforehand filled (with zero or one)
          PUKCL(Specific).Gf2n = ...;
          PUKCL(Specific).CarryIn = ...;

          PUKCL(u2Option) =...;
          // Depending on the option specified, not all fields should be filled
          PUKCL_Fmult(nu1XBase) = <Base of the ram location of X>;
          PUKCL_Fmult(u2XLength) = <Length of X>;
          PUKCL_Fmult(nu1ZBase) = <Base of the ram location of Z>;

          // vPUKCL_Process() is a macro command, which populates the service name
          // and then calls the library...
          vPUKCL_Process(Square,pvPUKCLParam);
          if (PUKCL(u2Status) == PUKCL_OK)
                      {
                      // The Squaring has been executed correctly
                      ...
                      }
          else // Manage the error

43.3.4.10.7 Important Considerations for Modular Reduction of a Square Computation
         Note:
         Additional options are available through the use of a modular reduction to be executed at the end of this
         operation. Some important considerations have to be taken into account concerning the length of
         resulting operands to get a mathematically correct result.
         The output of this operation is not obviously compatible with the modular reduction as it may be either
         smaller or bigger. In the case (most of the time) the result (pointed by nu1RBase) is smaller in size than
         “twice the modulus plus one word” by one word, a padding word must be added to zero. Otherwise, the
         reduced value will be taken considering the high order words (potentially uninitialized) as part of the
         number, thus resulting in getting a mathematically correct but unexpected result.
         In the case that the result is greater than twice the modulus plus one word, the modular reduction feature
         has to be executed as a separate operation, using an Euclidean division.




        © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1472
                                                            SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

43.3.4.10.8 Constraints
          When the options only indicate a square, the constraints involving nu1ZBase are not checked. The
          following conditions must be avoided to ensure that the service works correctly:
           • nu1XBase, nu1RBase or nu1ZBase are not aligned on 32-bit boundaries
           • {nu1XBase, u2XLength}, {nu1ZBase, 2*u2XLength} or {nu1RBase, 2*u2XLength} are not in Crypto
             RAM
           • u2XLength is either: < 4, > 0xffc or not a 32-bit length
           • {nu1RBase, 2*u2XLength} overlaps {nu1XBase,u2XLength}
           • {nu1RBase, 2*u2XLength} overlaps {nu1ZBase, 2*u2XLength} and nu1RBase >nu1ZBase
          If a modular reduction is specified, the relevant parameters must be defined according to the chosen
          reduction and follow the description in 43.3.5.1 Modular Reduction. Additional constraints to be
          respected and error codes are described in this section and in Table 43-49.
          Multiplication with Accumulation or Subtraction
          Where the options bits specify that either an Accumulation or a subtraction should be performed, this
          command performs the following operation:
          R = (Z ± (X2 + CarryOperand))mod B2 ˟ XLength
          Table 43-32. Multiplication with Accumulation or Subtraction

          Option AND CARRYOPTIONS                                     CarryOperand        Resulting Operation
          SET_CARRYOPTION(ADD_CARRY)                                  CarryIn             R = Z ± (X2 + CarryIn)
          SET_CARRYOPTION(SUB_CARRY)                                  - CarryIn           R = Z ± (X2 - CarryIn)
          SET_CARRYOPTION(ADD_1_PLUS_CARRY)                           1 + CarryIn         R = Z ± (X2 + 1 + CarryIn)
          SET_CARRYOPTION(ADD_1_MINUS_CARRY)                          1 - CarryIn         R = Z ± (X2 + 1 - CarryIn)
          SET_CARRYOPTION(CARRY_NONE)                                 0                   R = Z ± (X2)
          SET_CARRYOPTION(ADD_1)                                      1                   R = Z ± (X2 + 1)
          SET_CARRYOPTION(SUB_1)                                      -1                  R = Z ± (X2 - 1)
          SET_CARRYOPTION(ADD_2)                                      2                   R = Z ± (X2 + 2)

43.3.4.10.9 Multiplication without Accumulation or Subtraction
          Where the options bits specify that either an accumulation or a subtraction should be performed, this
          command performs the following operation:
          R = (X2 + CarryOperand)mod B2 ˟ XLength
          Table 43-33. Square Service Carry Settings

          Option AND CARRYOPTIONS                                          CarryOperand      Resulting Operation
          SET_CARRYOPTION(ADD_CARRY)                                       CarryIn           R = X2 + CarryIn
          SET_CARRYOPTION(SUB_CARRY)                                       - CarryIn         R = X2 - CarryIn
          SET_CARRYOPTION(ADD_1_PLUS_CARRY)                                1 + CarryIn       R = X2 + 1 + CarryIn
          SET_CARRYOPTION(ADD_1_MINUS_CARRY)                               1 - CarryIn       R = X2 + 1 - CarryIn
          SET_CARRYOPTION(CARRY_NONE)                                      0                 R = X2




         © 2019 Microchip Technology Inc.                        Datasheet                         DS60001507E-page 1473
                                                            SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

          ...........continued
          Option AND CARRYOPTIONS                                      CarryOperand       Resulting Operation
          SET_CARRYOPTION(ADD_1)                                       1                  R = X2 + 1
          SET_CARRYOPTION(SUB_1)                                       -1                 R = X2 - 1
          SET_CARRYOPTION(ADD_2)                                       2                  R = X2 + 2

43.3.4.10.10 Status Returned Values
          Table 43-34. Square Service Return Codes

          Returned status                    Importance            Meaning
          PUKCL_OK                           –                     Service functioned correctly

43.3.4.11 Integral (Euclidean) Division
43.3.4.11.1 Purpose
          The purpose of this service is to compute the Euclidean Division of two multiple precision numbers in
          GF(p) or polynomial in GF(2n). The Numerator is divided by the Denominator giving the Quotient “Quo”
          and the Remainder “R”.
          The following options are available:
           • Work in the GF(2n) field or in the standard integer arithmetic field GF(p)
43.3.4.11.2 How to Use the Service

43.3.4.11.3 Description
          This service processes the calculus corresponding to:
                                                                          ���
          ��� = ��� × ��� + � ���ℎ          0 ≤ � < ��� ���    ��� =
                                                                          ���
          The Numerator is Num.
          The Divisior (Modulus) is Mod.
          The Quotient is Quo.
          The Remainder is R.
          The Inputs are, the Numerator Num, and the Denominator Mod. The service calculates the Quotient and
          the Remainder. The Remainder overwrites the Numerator and is copied to the R area.
          If the parameter nu1QuoBase equals zero, the Quotient is not stored in memory.
          If nu1QuoBase is different from zero, the Quotient length is (<Numerator Length> - <Denominator
          Length>) + 4 bytes.
          In this computation, the following areas need to be provided:
           •   Num (pointed by {nu1NumBase,u2NumLength}) filled with the Numerator (with MSB word to zero).
           •   Mod (pointed by {nu1ModBase,u2ModLength}) filled with the Denominator.
           •   Workspace (pointed by {nu1CnsBase,64 or68}).
           •   Quo (pointed by {nu1QuoBase,u2NumLength - u2ModLength + 4}) to contain calculated Quotient.
                – When the quotient is not needed, the nu1QuoBase pointer can be provided as NULL. In that
                  case, only the remainder will be provided as a result.




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1474
                                                               SAM D5x/E5x Family Data Sheet
                                                               Public Key Cryptography Controller (PUKCC)

           • R (pointed by {nu1RBase,u2ModLength}) to contain the calculated Remainder.
          The service name for this operation is Div.
43.3.4.11.4 Parameters Definition
          Table 43-35. Div Service Parameters

          Parameter               Type Dir. Location       Data Length       Before Executing After Executing
                                                                             the Service      the Service
          Specific/Gf2n           Bit       I   –          –                 GF(2n) Bit         –
          nu1NumBase              nu1       I   Crypto RAM u2NumLength       Base of Num        Base of Num
                                                                             Filled with the    Filled with the
                                                                             Numerator          Remainder

          u2NumLength             u2        I   –          –                 Length of the      Length of the
                                                                             Numerator          Numerator
          nu1ModBase              nu1       I   Crypto RAM u2ModLengt        Base of the        Base of the
                                                                             Divisor            Divisor untouched

          u2ModLength             u2        I   –          –                 Length of the      Length of the
                                                                             Divisor            Divisor
          nu1QuoBase (see nu1               I   Crypto RAM u2NumLength -   Base of the          Base of the
          Note 1)                                          u2ModLength + 4 Quotient             Quotient
          nu1WorkSpace            nu1       I   Crypto RAM GF(p): 64         Base of the        Base of the
                                                                             WorkSpace          WorkSpace
                                                           GF(2n): 68
                                                                                                corrupted
          nu1RBase ( see          nu1       I   Crypto RAM u2ModLength       Base of the        Base of the
          Note 2)                                                            Remainder          Remainder

          Note:
           1. If the quotient is not needed, set nu1QuoBase to zero and the quotient will not be written to
                memory. If the quotient is needed, set the nu1QuoBase to the beginning of an area of size
                (u2NumLength - u2ModLength + 4) to write the whole quotient.
           2. The Remainder is present in the area {nu1NumBase, u2NumLength} at the end of the calculus. The
                nu1RBase parameter makes it possible to copy this result in the other area {nu1RBase,
                u2ModLength}, if this copy is not needed, set nu1RBase to the same value as nu1NumBase and
                the copy will not be done.




         © 2019 Microchip Technology Inc.                        Datasheet                     DS60001507E-page 1475
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

          Note: The parameter Num must have its most significant 32-bit word cleared to zero. The length
          u2NumLength is the length of Num including this zero word.
          One additional word is used on the LSB side of the Num parameter, this word is restored at the end of the
          calculus. As a consequence the parameter nu1NumBase must never been at the beginning of the Crypto
          RAM, i.e., ensure that nu1NumBase ≥ <Crypto RAM Base> + 4 bytes.
          One additional word is used on the MSB side of the Num parameter, this word is not corrupted. As a
          consequence the Area {nu1NumBase, u2NumLength} must not be at the end of the Crypto RAM, i.e., en
          sure that nu1NumBase+u2NumLength ≤ <Crypto RAM End> - 4.
          u2ModLength must be the true length of the Modulus, i.e., the MSB word of the area {nu1ModBase,
          u2ModLength} must be different from zero.
          The minimum value for u2ModLength is 8 bytes, so the significant length of Num must be at least 8 bytes.
          To divide by a 32-bit value, the divider and numerator shall be multiplied by 232. The resulting remainder
          will have to be divided by 232, the quotient will be exact.
43.3.4.11.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // Fill all the fields
           // In that case, the quotient will be computed
           // If it was not needed, set nu1QuoBase to NULL
           PUKCL_Div(nu1NumBase) = <Base of the ram location of Num>;
           PUKCL_Div(nu1ModBase) = <Base of the ram location of Mod>;
           PUKCL_Div(nu1QuoBase) = <Base of the ram location of Quo>;
           PUKCL_Div(nu1WorkSpace) = <Base of the workspace>;
           PUKCL_Div(nu1RBase) = <Base of the ram location of R>;
           PUKCL_Div(u2NumLength) = <Length of Num>;
           PUKCL_Div(u2ModLength) = <Length of Mod>;

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(Div,pvPUKCLParam);
           if (PUKCL(u2Status) == PUKCL_OK)
                       {
                       // The Division has been executed correctly
                       ...
                       }
           else // Manage the error


43.3.4.11.6 Constraints
          The following conditions must be avoided to ensure the service works correctly:
           • nu1ModBase, nu1RBase, nu1QuoBase, nu1WorkSpace or nu1NumBase are not aligned on 32-bit
             boundaries
           • {nu1ModBase, u2ModLength}, {nu1RBase, u2ModLength}, {nu1WorkSpace, 64} or{nu1NumBase,
             u2NumLength} are not in Crypto RAM
           • u2ModLength, u2NumLength is either: < 4, > 0xffc or not a 32-bit length
           • One or more overlaps exist between two of the areas: {nu1ModBase,u2ModLength},{nu1RBase,
             u2ModLength} {nu1NumBase, u2NumLength}(1) or {nu1WorkSpace,64}
           • If nu1QuoBase is different from zero and: {nu1QuoBase, u2NumLength - u2ModLength + 4} are not
             in Crypto RAM
           • If nu1QuoBase is different from zero and one or more overlaps exist between two of the areas:
             {nu1QuoBase, u2NumLength - u2ModLength + 4}, {nu1ModBase, u2ModLength}, {nu1RBase,
             u2ModLength}, {nu1NumBase, u2NumLength} or {nu1WorkSpace, 64}
          Overlaps between {nu1RBase, u2ModLength} and {nu1NumBase, u2NumLength} are forbidden, but the
          equality between nu1RBase and nu1NumBase is authorized




         © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1476
                                                             SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

43.3.4.11.7 Status Returned Values
          Table 43-36. Div Service Return Codes

          Returned Status                     Importance Meaning
          PUKCL_OK                            –           Service functioned correctly.
          PUKCL_DIVISION_BY_ZERO Severe                   The operation was not performed because the
                                                          Denominator value is zero.

43.3.4.12 GCD, Modular Inverse

43.3.4.12.1 Purpose
          The purpose of this command is to compute the Greatest Common Divisor (GCD) and the Modular
          Inverse. The algorithm used is the Extended Euclidean Algorithm for the GCD.
          This command accepts as input two multiple precision numbers in GF(p) or two polynomials in GF(2n) X
          and Y and computes their GCD (D), if D equals one, the command also supplies the inverse of X modulo
          Y.
          The available options are as follows:
           • Work in the GF(2n) field or in the standard integer arithmetic field GF(p)
43.3.4.12.2 How to Use the Service

43.3.4.12.3 Description
          This command calculates:
          D = GCD(X,Y).
          and parameter A in the Bezout equation:
          A × X + B × Y = D.
          The first input, or input to inverse is X.
          The second input, or modulus is Y.
          The GCD is output in D.
          The modular inverse if X and Y are co-primes is output A:
          A = X–1mod(Y)
          The command calculates the GCD and the value A. The value A is the multiplicative inverse of X, only if
          X and Y are co-prime. As a supplemental result, Z is given back, being the quotient of Y divided by D only
          if D is different from zero:
               �
          �=
               �
          At the end of the command: X is overwritten by D.
          Y is cleared.
          The value of A is calculated and stored.
          The value of Z is calculated and stored if D is different from zero.
          The service name for this operation is GCD.
          In this computation, the following areas have to be provided:




         © 2019 Microchip Technology Inc.                      Datasheet                       DS60001507E-page 1477
                                                             SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

           •   X (pointed by {nu1XBase,u2Length}) filled with X (with MSB word to zero)
           •   Y (pointed by {nu1YBase,u2Length}) filled with Y (with MSB word to zero)
           •   A (pointed by {nu1ABase,u2Length}) to contain calculated A
           •   Z (pointed by {nu1ZBase,u2Length}) to contain calculated Z
           •   The workspace (pointed by {nu1WorkSpace,32})
43.3.4.12.4 Parameters Definition
         Table 43-37. GCD Service Parameters

          Parameter           Type Dir. Location       Data Length    Before Executing      After Executing the
                                                                      the Service           Service
          Specific/Gf2n       Bit     I     –          –              GF(2n) Bit            –
          nu1XBase            nu1     I     Crypto RAM u2Length       Base of X Number X Base of X
                                                                                            Filled with the GCD D

          u2Length            u2      I     –          –              Length of the Areas   Length of the Areas X,
                                                                      X, Y, A, Z            Y, A, Z
          nu1YBase            nu1     I     Crypto RAM u2Length       Base of Y Number Y Base of Y Cleared area
          nu1ABase            nu1     I     Crypto RAM u2Length       Base of A             Base of A
                                                                                            Filled with the result

          nu1ZBase            nu1     I     Crypto RAM u2Length + 4   Base of Z             Base of Z
                                                       (see Note 1)
                                                                                            Filled with the result

          nu1WorkSpace nu1            I     Crypto RAM 32 bytes       Base of the           Base of the workspace
                                                                      workspace             corrupted

         Note:
          1. The additional word is 4 zero bytes.
         The parameters X and Y must have their most significant 32-bit word cleared to zero. The length
         u2Length is the length of the longer of the parameters X and Y including this zero word.
         To clarify here is an example:
           • X is an 8 bytes number.
           • Y is a 12 bytes number.
         This example is processed this way before the use of the GCD service:
           • The longer number is Y so its length is taken and increased by 4 bytes for the 32-bit word cleared to
             zero, this gives u2Length = 16 bytes. Therefore, X, Y, A and Z areas have a length of 16 bytes.
           • Y is padded with 4 bytes cleared to zero on the MSB side and the u2Length = 16 bytes are written in
             memory (LSB first).
           • X is padded with 8 bytes cleared to zero on the MSB side and the u2Length = 16 bytes are written in
             memory (LSB first).
           • The areas A and Z are mapped in memory with a size of u2Length = 16 bytes.
           • The workspace is mapped in memory with its constant size of 32 bytes




         © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1478
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

43.3.4.12.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;
           // Fill all the fields
           PUKCL(u2Option) = 0;
           PUKCL_GCD(nu1XBase) = <Base of the ram location of X>;
           PUKCL_GCD(nu1YBase) = <Base of the ram location of Y>;
           PUKCL_GCD(nu1ABase) = <Base of the ram location of A>;
           PUKCL_GCD(nu1ZBase) = <Base of the ram location of Z>;
           PUKCL_GCD(nu1WorkSpace) = <Base of the workspace>;
           PUKCL_GCD(u2Length) = <Length of X, Y, A and Z>;
           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(GCD, pvPUKCLParam);
           if (PUKCL_Param.Status == PUKCL_OK)
                          {
                          // The GCD has been executed correctly
                          ...
                          }
           else // Manage the error

43.3.4.12.6 Constraints
          The following conditions must be avoided to ensure that the service works correctly:
           • nu1XBase, nu1YBase, nu1ABase or nu1ZBase are not aligned on 32-bit boundaries
           • {nu1XBase, u2Length}, {nu1YBase, u2Length}, {nu1ABase, u2Length} or {nu1ZBase, u2Length} are
             not in Crypto RAM
           • u2Length is either: < 4, > 0xffc or not a 32-bit length
           • {nu1XBase, u2Length} overlaps {nu1YBase, u2Length} or {nu1XBase, u2Length} overlaps
             {nu1ABase, u2Length} or {nu1XBase, u2Length} overlaps {nu1ZBase, u2Length} or {nu1YBase,
             u2Length}overlaps
          {nu1ABase, u2Length} or {nu1YBase, u2Length} overlaps {nu1ZBase, u2Length} or {nu1ABase,
          u2Length} overlaps {nu1ZBase, u2Length}
43.3.4.12.7 Status Returned Values
          Table 43-38. GCD Service Return Codes

          Returned Status                   Importance            Meaning
          PUKCL_OK                          –                     Service functioned correctly

43.3.4.13 Get Random Number
43.3.4.13.1 Purpose
          The purpose of this command is to provide the user with a source of entropy. The options available for
          this service are:
           • Generation of random numbers from a Hardware Random Number Generator (TRNG).
           • Generation of random numbers from a Deterministic Random Number Generator (DRNG).




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 1479
                                                                SAM D5x/E5x Family Data Sheet
                                                              Public Key Cryptography Controller (PUKCC)

                          Important:
                          When using this service, be sure to strictly follow the directives given for the RNG on the chip
                          you use (particularly initialization, seeding) and compulsorily start the RNG. If the directives
                          require not to use this service, follow them and use the proposed method to get random
                          numbers.
                          This service only has the option to get random numbers and does not seed, initialize or start the
                          RNG. Other options are reserved for future use.
                          Neither continuous testing nor entropy testing is included in this service. If this is needed (FIPS
                          140, ZKA, ...), this service should not be used and the users shall develop their own command.


          The DRNG is compatible with both ANSI X9.31 and FIPS 186-2 standards (see the important note
          below). The DRNG is designed according to:
           • The algorithm described in the document ANSI Digital Signatures Using Reversible Public Key
             Cryptography for the Financial Services Industry (rDSA) X9.31 dated September 9, 1998.
           • The Change recommendation for ANSI X9.0 - 1995 (Part 1) and ANSI X9.31 -1998:
          The algorithm B.2.1 Algorithm for computing m Values of x is the one applied in the Toolbox 3 X9.31
          DRNG. The DRNG is compatible with:
           • The DRNG is described in the document NIST Digital Signature Standard (DSS) FIPS Pub 186-2
             January 27, 2000 Appendix 3.1
           • The FIPS 186-2 Change Notice 1 dated October 5, 2001 modifies this algorithm.


                          Important: To apply the FIPS 186-2 algorithm, the parameters XSeed[0] and XSeed[1] must
                          be set to the same value.



43.3.4.13.2 How to Use the Service
43.3.4.13.3 Description
          This service has four possible options described in Table 43-41. Two of these options are reserved for
          future use. This service performs the following operations:
           • Generation of a random number from the Hardware RNG
           • Generation of a random number from the Deterministic RNG
          Generation of a Random Number from the Hardware RNG
          This service, activated with the option PUKCL_RNG_GET, makes it possible to get a random number R
          from the Hardware RNG:
          R = HardwareRandomGenerate()
          In the Generation of random from the RNG service, the following parameters need to be provided:
           • R the generated number area (pointed by{nu1RBase,u2RLength})
43.3.4.13.4 Generation of a Random Number from the Deterministic RNG
          This service, activated with the option PUKCL_RNG_X931_GET, makes it possible to get a random
          number R from the Deterministic Random Number Generator with input parameters the Key XKey and
          the Seed XSeed:
          (XKey, R) = DeterministicRandomGenerateFromSeed ( XKey, XSeed, Q)




         © 2019 Microchip Technology Inc.                        Datasheet                           DS60001507E-page 1480
                                                            SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

         In the generation of a random number from the Deterministic RNG service, the following parameters need
         to be provided:
           •   XKey the input and output Key (pointed by {nu1XKeyBase,u2XKeyLength})
           •   XSeed the input Seed (pointed by {nu1XseedBase,u2XKeyLength})
           •   Q the prime number (pointed by {nu1QBase, 20bytes})
           •   R the generated number area (pointed by {nu1RBase, 20bytes})
43.3.4.13.5 Hardware RNG Parameters Definition
         The parameters for the generation of random from the Hardware RNG are described in the following
         table. This service can easily be accessed through the use of the PUKCL_Rng() and PUKCL() macros.
         Table 43-39. RNG Service Hardware Generated Parameters

          Parameter Type Dir. Location                Data Length Before Executing     After Executing the
                                                                  the Service          Service
          u2Options u2          I     –               –            Option (see Table   Option (see Table 43-41)
                                                                   43-41)
          nu1RBase nu1          I     Crypto RAM or u2RLength      Base of R           Base of R filled with
                                      Device RAM                                       random values
                                                                                       depending on the option
          u2RLength u2          I     –               –            Length of R         Length of R

43.3.4.13.6 Deterministic RNG Parameters Definition
         The parameters for the generation of random from the Deterministic RNG are described in the following
         table. This service can easily be accessed through the use of the PUKCL_Rng() and PUKCL() macros.
         Table 43-40. RNG Service Deterministic Generated Parameters

          Parameter            Type Direction Location     Data Length           Before        After
                                                                                 Executing the Executing the
                                                                                 Service       Service
          u2Options            u2      I       –           –                     Option (see       Option (see
                                                                                 Table 43-41)      Table 43-41)
          nu1XKeyBase          nu1     I/O     Crypto      u2XKeyLength          Base of XKey      Base of XKey
                                               RAM                                                 filled with the
                                                                                                   resulting XKey
          nu1Workspace         nu1     NA      Crypto      64 bytes              Base of the       Base of the
                                               RAM                               workspace         workspace
                                                                                                   corrupted
          nu1Workspace2 nu1            NA      Crypto      2*u1XKeyLength + 4 Base of the          Base of the
                                               RAM                            workspace 2          workspace
          (see Note 1)
                                                                                                   corrupted
          nu1XSeedBase nu1             I/O     Crypto      max                   Base of the       Base of XSeed
                                               RAM                               values            filled with the
                                                           ( 2*u2XKeyLength,
                                                                                 XSeed[0] and      result on 20
                                                           44 bytes)
                                                                                 XSeed[1]          bytes




         © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 1481
                                                               SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

         ...........continued
          Parameter             Type Direction Location       Data Length         Before        After
                                                                                  Executing the Executing the
                                                                                  Service       Service
          u2XKeyLength          u2     I           –          –                   Length of        Length of XKey,
                                                                                  XKey,            Xseed[0] and
                                                                                  Xseed[0] and     Xseed[1]
                                                                                  Xseed[1]
          nu1QBase              nu1    I           Crypto     20 bytes            Base of Q        Base of Q
                                                   RAM
          nu1RBase              nu1    I           Crypto     u2RLength           Base of R        Base of R filled
                                                   RAM                                             with the result
                                                                                                   on 20 bytes

         Note:
          1. The nu1 Workspace2 must be a multiple of 256.
43.3.4.13.7 Options
         The option is set by the u2Options input parameter that must take one of the values listed in the following
         table. Please note that the values, OPTION_RNG_SEED and OPTION_RNG_GETSEED, are reserved
         for future use.
         Table 43-41. RNG Service Options

          Option                            Purpose                              Required Parameters
          PUKCL_RNG_SEED                    Reserved                             Reserved
          PUKCL_RNG_GET                     Generation of a random number from   nu1RBase, u2RLength
                                            the RNG
          PUKCL_RNG_X931_GET Generation of a random number from                  nu1XKeyBase, nu1Workspace,
                             the Deterministic RNG                               nu1XSeedBase, u2XKeyLength,
                                                                                 nu1QBase, nu1RBase
          PUKCL_RNG_GETSEED Reserved                                             Reserved

43.3.4.13.8 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // ! The Random Number Generator must be initialized and started
           // ! following the directives given for the RNG on the chip

           PUKCL(u2Option) =...;

           // Initializing parameters
           PUKCL_Rng(nu1RBase) = <Base of the ram location to store the rng>;
           PUKCL_Rng(u2RLength) = <Length of the rng to get>;

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(Rng,pvPUKCLParam);
           if (PUKCL(u2Status) == PUKCL_OK)
                       {
                       // The RNG generation has been executed correctly
                       ...




         © 2019 Microchip Technology Inc.                         Datasheet                    DS60001507E-page 1482
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

                       }
           else // Manage the error


43.3.4.13.9 Constraints

          Random Number Generation
          The following conditions must be avoided to ensure that the service works correctly:
           • {nu1RBase,u2RLength} not in RAM
           • {nu1RBase,u2RLength} not accessible or authorized for writing
          Deterministic Random Number Generation
          The length of the parameter nu1XSeedbase is: XSeedLength = max( 2*u2XKeyLength, 44 bytes) The
          max() macro takes a maximum of two values.
          The following conditions must be avoided to ensure that the service works correctly:
           • nu1XKeyBase,nu1Workspace, nu1Workspace2, nu1XSeedBase, nu1QBase, nu1RBase are not
             aligned on 32-bit boundaries
           • {nu1XKeyBase, u2XKeyLength}, {nu1Workspace, 64 bytes}, {nu1Workspace2, 2*u1XKeyLength +4},
             {nu1XSeedBase, XSeedLength}, {nu1QBase, 24 bytes} or {nu1RBase, 20 bytes} are not in PUKCC
             RAM
           • u2XKeyLength is either: < 20, > 64 or not a 32-bit length
           • nu1Workspace2 not multiple of 256.
           • Overlaps exist between two or more of the areas: {nu1XKeyBase, u2XKeyLength}, {nu1Workspace,
             64 bytes}, {nu1XSeedBase, XSeedLength}, {nu1QBase, 24 bytes} or {nu1RBase, 20 bytes}
             The area {nu1RBase, 20} can overlap with {nu1Workspace, 64 bytes} or {nu1QBas, 24 bytes}. The
             pointer nu1RBase can equal the pointer nu1XSeedBase.
43.3.4.13.10 Status Returned Values
          Table 43-42. RNG Service Return Codes

          Returned status                   Importance            Meaning
          PUKCL_OK                          Information           Service functioned correctly

43.3.5    Modular Arithmetic Services
          This section provides a complete description of the modular arithmetic services, which consists of two
          sets:
           • Modular reductions, which can be used as stand alone operations, or used as a final step of most
             arithmetic operations (full and small multiplications, squaring).
           • Modular operations, which include modular exponentiations (with or without using the CRT) and a
             probabilistic prime number generation.
          These operations work on general data so the modulus has no special form. The modular services are
          available through:
           • a Fast form (may return a congruence of the result, with a high probability to have a Normalized
             result)
           • a Normalized form (returns the exact result, strictly lower than the modulus)
           • a Euclidean form (returns the exact result, strictly lower than the modulus)
          The following table describes the modes of the modular reduction with the hypothesis:
           • In GF(p): The modulus is N with length NLength in bytes




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 1483
                                                                SAM D5x/E5x Family Data Sheet
                                                              Public Key Cryptography Controller (PUKCC)

           • In GF(2n): The modulus is P[X] with length NLength in bytes
         For the exact calculus of NLength see below.
         Table 43-43. Modular Reduction Modes

          Modular             Input Dynamic                 Result Dynamic              Comments
          Reduction
          Form
          Fast                GF(p): 0 ≤ Input < (N2) *     GF(p): 0 ≤ Res < N * 4      The fastest reduction available,
                              (232)                                                     needs a precomputed constant.
                                                            GF(2n): Res < P[X] * (X2)
                              GF(2n): Input < ((P[x])2) *
                              (X32)

          Normalized          InputLength < NLength         GF(p): 0 ≤ Res < N          The correction step does not
                              + 4 bytes                     GF(2n): Res < P[X]          runs in constant time. Needs a
                                                                                        precomputed constant.
                                                                                        The Normalize function cannot
                                                                                        be applied to the product of two
                                                                                        numbers of length u2NLength.

          Using               InputLength < 2 *             GF(p): 0 ≤ Res < N          Does not need any
          Euclidean           NLength + 4 bytes                                         precomputed constant.
                                                            GF(2n): Res < P[X]
          division

         To be able to use these modular reduction services (except the Euclidean division), first the implementer
         shall call the setup service, providing the modulus as well as one free memory space for the constant
         (this constant is used to speed up the modular reduction). In most commands (except the modular
         exponentiation), the quotient is stored in the high order bytes of the number to be reduced, using only
         eight bytes more than the maximum size of the number to be reduced.
         The following rules must be respected to ensure the modular reduction services function correctly:
           • The numbers to be reduced can have any significant length, given the fact it CANNOT BE GREATER
             than 2*u2ModLength + 4 bytes.
           • The modulus SHALL ALWAYS HAVE a significant length of <u2ModLength> bytes. The modulus
             must be provided as a <u2ModLength + 4> bytes long number, padded on the most significant side
             with a 32-bit word cleared to zero. Not respecting this rule leads to unexpected and wrong results
             from the modular reduction.
           • The normalization operation ALWAYS performs a modular reduction step, and will therefore have the
             same memory usage as this one.
           • The very first operation before any modular operation SHALL BE a modular setup.

43.3.5.1 Modular Reduction

43.3.5.1.1 Purpose
         This service is used to perform the various steps necessary to perform a modular reduction and accepts
         as input numbers in GF(p) or polynomials in GF(2n) .
         The available options for this service are:
           • Work in the GF(2n) or in the standard integer arithmetic field GF(p)
           • Operation is the generation of the reduction constant.




         © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 1484
                                                            SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

           • Operation is a Modular Reduction.
           • Operation is a Normalization.
43.3.5.1.2 How to Use the Service

43.3.5.1.3 Description
          This service performs one of the following operations:
           •   Setup of the Fast or Normalize functions: generation of the reduction constant
           •   Fast Modular Reduction
           •   Big Modular Reduction (using Euclide’s division)
           •   Normalization
          The service name for this operation is RedMod.

43.3.5.1.4 Modular Reduction Setup
          This service calculates the constant Cns, computed from the modulus and used to speed up the modular
          reduction:
          Cns = SetupConstant(N)
          This service must be processed before the use of the Fast or Normalize functions. In the Setup
          computations, the following data must be provided:
           • N the modulus (pointed by {nu1ModBase,u2ModLength +4}).
           • Cns the Setup Constant Result (pointed by {nu1CnsBase,u2ModLength +12}).
           • X used as a workspace (pointed by {nu1XBase,2 * u2ModLength + 8}) (include the supplementary
             bytes; see Note 2 in Table 43-44
           • R used as a workspace (pointed by {nu1RBase,64 or 68bytes}).
           • u2ModLength is the Aligned Significant Length of the modulus and is not the byte Significant Length
             (see 43.3.3.4 Aligned Significant Length).
43.3.5.1.5 Fast Reductions and Normalization
          These commands calculate an approximated or exact Modular Reduction, that is, the result may be
          greater than the modulus, but is always congruent to the true result.


                         Important: Before using these functions, ensure that the constant Cns has been calculated
                         with the setup for the Modular Reduction service.


          Input and Result significant values verify:
           • For the Fast Modular Reduction:

          0 ≤ � < �2 × 232
          � = ���� � + � × �          ���ℎ   0≤�≤4
           • For the Normalize:
          ������ℎ < ������ℎ + 4 ����� �
          = ���� �
          In these Fast Modular Reduction and Normalize computations, the following data have to be provided:
           • X (pointed by {nu1XBase,2 * u2ModLength +8})




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1485
                                                            SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

                 – The Normalize computation accept as entry a value whose length is lower or equal to
                   u2ModLength + 4 (that is, for example, a value yet reduced but not normalized.). The
                   u2ModLength + 4 MSB bytes are cleared at the beginning of the computation.
                 – in case of Fast RedMod computations, the value X mayverify: X < (N2) *(232).
                 – include the supplementary bytes; see Note 3 in Table 43-45)
           •   R (pointed by {nu1RBase,u2Modlength +4})
           •   N (pointed by {nu1ModBase,u2ModLength +4})
           •   Cns (pointed by {nu1CnsBase,u2ModLength +12})
           •   u2ModLength is the Aligned Significant Length of the modulus and is not the byte Significant Length
               (see 43.3.3.4 Aligned Significant Length).
         The Fast Modular Reduction is able to reduce inputs up to <2*u2ModLength + 4> bytes. The input can
         come from a multiplication of 2 <u2ModLength + 4> bytes numbers. The input X is considered as a
         <2*u2ModLength + 8> bytes number.


                        Important: Additionally the Fast Reduction and Normalize functions need supplemental bytes
                        located on the MSB side of the number to be reduced but these bytes are restored at the end of
                        the operation and are therefore unchanged. However, these bytes are to be taken into account
                        when the mapping is created, and could lead to unexpected results if overlapping with other
                        area used by the function.


         The Fast Modular Reduction returns a <u2ModLength + 4> bytes number, but this number is in fact a
         <u2ModLength + 2> significant bytes number. When using the Fast Modular Reduction, the two MSB
         bytes of the <u2ModLength + 2> can have a maximum of two lsb bits set (depending on the reduced
         number and the modulo).
         The Normalize computation accepts as entry a resulting value of Fast Modular Reduction and computes
         an exact result. It can not be applied to the result of the product of two numbers of size NLength: a Fast
         Modular Reduction must be applied before.
         For the Normalize computation, the X value is limited by the preceding formula but the area in memory is
         bigger as described in Table 43-45.
         As input, the Normalize sub-service only accept values, which length is lower or equal to u2ModLength
         + 4. The Most Significant u2ModLength + 4 bytes are firstly cleared by this service.
43.3.5.1.6 Big Modular Reduction Using Euclide's Division
         This command calculates:
         ������ℎ < 2 × ������ℎ + 4 ����� �
         = ���� �
         In this Big Modular Reduction computations, the following data must be provided:
           • X (pointed by {nu1XBase,2 * u2ModLength + 8}) (include the supplementary bytes; see Note 1 in
             Table 43-46)
           • R (pointed by {nu1RBase,u2Modlength +4})
           • N (pointed by {nu1ModBase,u2ModLength +4})
           • u2ModLength is the Aligned Significant Length of the modulus and is not the byte Significant Length
             (see 43.3.3.4 Aligned Significant Length)
           • Workspace (pointed by {nu1CnsBase,64 or 68}).




         © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 1486
                                                              SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

43.3.5.1.7 Modular Reductions Service Parameters Definition
         Table 43-44. RedMod Service Parameters

          Parameter             Type Direction Location       Data Length        Before            After Executing
                                                                                 Executing the     the Service
                                                                                 Service
          u2Options             u2     I       –              –                  Options (see      Options (see
                                                                                 below)            below)
          Specific/CarryIn      Bits   I       –              –                  Must be set to    –
                                                                                 zero.
          Specific/Gf2n         Bit    I       –              –                  GF(2n) Bit        –
          Specific/             Bits   I       –              –                  –                 Carry Out, Zero
          CarryOut Zero                                                                            Bit and Violation
          Violation                                                                                Bit filled
                                                                                                   according to the
                                                                                                   result
          nu1ModBase            nu1    I       Crypto         u2ModLength + 4    Base of N         Base of N
          ( see Note 1)                        RAM                                                 untouched
          nu1CnsBase            nu1    I       Crypto         u2ModLength + 12 Base of Cns         Base of Cns
                                               RAM                                                 filled with the
                                                                                                   Setup Constant
          u2ModLength           u2     I       –              –                  Length of N       Length of N
          nu1RBase              nu1    I       Crypto         GF(p): 64 bytes    Base of R      Base of R
                                               RAM                                              workspace
                                                              GF(2n): 68 bytes   as a workspace
                                                                                                corrupted
          nu1XBase (see         nu1    I       Crypto         2*u2ModLength      Base of X as a    Base of X
          Note 2)                              RAM            +8                 workspace         workspace
                                                                                                   corrupted

         Note:
          1. The Modulus is to be given as a u2ModLength Aligned Significant Length Bytes however, it has to
               be provided as a u2ModLength + 4 bytes long number, having the four high-order bytes set to zero.
          2. Before the X (pointed by {nu1XBase,2 * u2ModLength + 8}) LSB bytes, four supplementary bytes
               will be saved/restored. Other four supplementary bytes will also be saved/restored after the X MSB
               bytes. All these supplementary bytes may be entirely in the Crypto RAM (therefore, do not place
               the X area too near the end of the Crypto RAM) and shall not overlap with other area used by the
               service.




         © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1487
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

43.3.5.1.8 Fast Modular Reductions Service Parameters Definition
         Table 43-45. Fast RedMode and Normalize Service Parameters

          Parameter             Type Direction Location      Data Length       Before        After Executing
                                                                               Executing the the Service
                                                                               Service
          u2Options             u2         I   –             –                 Options (see       Options (see
                                                                               below)             below)
          Specific/CarryIn      Bits       I   –             –                 Must be set to     –
                                                                               zero.
          Specific/Gf2n         Bit        I   –             –                 GF(2n) Bit         –
          Specific/             Bits       I   –             –                 –                  Carry Out, Zero
          CarryOut Zero                                                                           Bit and Violation
          Violation                                                                               Bit filled
                                                                                                  according to the
                                                                                                  result
          nu1ModBase            nu1        I   Crypto        u2ModLength + 4   Base of N          Base of N
          (see Note 1)                         RAM                                                untouched
          nu1CnsBase            nu1        I   Crypto        u2ModLength       Base of Cns        Base of Cns
                                               RAM           + 12                                 untouched
          u2ModLength           u2         I   –             –                 Length of N        Length of N
          nu1RBase (see         nu1        I   Crypto        u2ModLength + 4   Base of R          Base of R filled
          Note 2)                              RAM                                                with the result
          nu1XBase (see         nu1        I   Crypto        2*u2ModLength     Base of X the      Base of X
          Note 3)                              RAM           +8                number to          corrupted
                                                                               reduce

         Note:
          1. The Modulus is to be given as a u2ModLength Aligned Significant Length Bytes however, it has to
               be provided as a u2ModLength + 4 bytes long number, having the four high-order bytes set to zero.
          2. To make profitable the space memory, it is possible to set nu1RBase exactly equal to nu1XBase.
          3. After the X (pointed by {nu1XBase,2 * u2ModLength + 8}) MSB bytes, supplementary bytes will be
               saved/restored (8 bytes in case of Fast RedMod, otherwise; 12 bytes). These supplementary bytes
               may be entirely in the Crypto RAM (therefore, do not place the X area too near the end of the
               Crypto RAM) and shall not overlap with other area used by the service.
43.3.5.1.9 Big Modular Reduction Parameters Definition
         Table 43-46. Big RedMod Service Parameters

          Parameter            Type Direction Location      Data Length        Before             After Executing
                                                                               Executing the      the Service
                                                                               Service
          u2Options            u2      I       –            –                  Options (see       Options (see
                                                                               below)             below)




         © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1488
                                                          SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

         ...........continued
          Parameter             Type Direction Location    Data Length         Before              After Executing
                                                                               Executing the       the Service
                                                                               Service
          Specific/CarryIn Bits        I       –           –                   Must be set to      –
                                                                               zero
          Specific/Gf2n         Bit    I       –           –                   GF(2n) Bit          –
          Specific/             Bits   I       –           –                   –                   Carry Out, Zero
          CarryOut Zero                                                                            Bit and Violation
          Violation                                                                                Bit filled
                                                                                                   according to the
                                                                                                   result
          nu1ModBase            nu1    I       Crypto      u2ModLength + 4     Base of N           Base of N
                                               RAM                                                 untouched
          nu1CnsBase            nu1    I       Crypto      GF(p): 64 bytes     Base of Cns as Base of Cns
                                               RAM                             a workspace    corrupted
                                                           GF(2n): 68 bytes

          u2ModLength           u2     I       –           –                   Length of N         Length of N
          nu1RBase              nu1    I       Crypto      u2ModLength + 4     Base of R           Base of R filled
                                               RAM                                                 with the result
          nu1XBase (see         nu1    I       Crypto      2*u2ModLength       Base of X the       Base of X filled
          Note 1)                              RAM         +8                  number to           with the result
                                                                               reduce

         Note:
          1. Before the X (pointed by {nu1XBase,2 * u2ModLength + 8}) LSB bytes, four supplementary bytes
               will be saved/restored. Other four supplementary bytes will also be saved/restored after the X MSB
               bytes. All of these supplementary bytes may be entirely in the Crypto RAM (therefore, do not place
               the X area too near the end of the Crypto RAM) and shall not overlap with other area used by the
               service.
43.3.5.1.10 Options
         The options are set by the u2Options input parameter, which is composed of:
           • the mandatory Operation Option described in Table 43-47
           • if the Operation Option is PUKCL_REDMOD_REDUCTION, the Modular Reduction Sub-Option
             described in Table 43-48
         The u2Options number is calculated by an Inclusive OR of the options. Some Examples in C language
         are:
           • Operation: Setup for the ModularReductions.
             PUKCL(u2Options) = PUKCL_ REDMOD_SETUP;
           • Operation: Fast ModularReduction.
             PUKCL(u2Options) = PUKCL_REDMOD_REDUCTION | PUKCL_REDMOD_USING_FASTRED;




         © 2019 Microchip Technology Inc.                   Datasheet                           DS60001507E-page 1489
                                                            SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

          For this command three exclusive options can be specified. The following table lists the operations that
          can be performed.
          Table 43-47. RedMod Service Options

          Option                              Purpose                               Required Parameters
          PUKCL_REDMOD_SETUP                  Perform the Cns value computation nu1ModBase, u2ModLength,
                                                                                nu1CnsBase, nu1XBase
          PUKCL_REDMOD_REDUCTION Perform R ≡ X Mod N, see sub-                      nu1ModBase, u2ModLength,
                                 option for details                                 nu1CndBase, nu1XBase,
                                                                                    nu1RBase
          PUKCL_REDMOD_NORMALIZE Perform R = X Mod N                                nu1ModBase, u2ModLength,
                                                                                    nu1CndBase, nu1XBase,
                                                                                    nu1RBase

          When selecting the PUKCL_REDMOD_REDUCTION option, one of the two sub-options listed in the
          following table must be selected.
          Table 43-48. RedMode Service Options with PUKCL_RED_MOD_REDUCTION

          Option                            Purpose                            Required Parameters
          PUKCL_REDMOD                      Perform R = X Mod N                nu1ModBase, u2ModLength,
          _USING_DIVISION                                                      nu1CndBase, nu1XBase
          PUKCL_REDMOD                      Perform R ≡ X Mod N                nu1ModBase, u2ModLength,
          _USING_FASTRED                                                       nu1CndBase, nu1XBase,
                                            The entropy is minimized (~2 bits)
                                                                               nu1RBase

43.3.5.1.11 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           PUKCL(Specific).CarryIn = 0;
           PUKCL(Specific).GF2n = ...;

           PUKCL(u2Option) =...;

           // Depending on the option specified, not all fields should be filled
           PUKCL_RedMod(nu1ModBase) = <Base of the ram location of N>;
           PUKCL_RedMod(u2ModLength) = <Length of N>;
           PUKCL_RedMod(nu1CnsBase) = <Base of the ram location of Cns>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(RedMod,pvPUKCLParam);
           if (PUKCL_Param.Status == PUKCL_OK)
                       {
                       // operation has correctly been performed
                       ...
                       }
           else // Manage the error

43.3.5.1.12 Constraints
          Depending on the options chosen the lengths of the R area and Cns area differ:
           • For the Setup:
              – RLength = 64bytes




         © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1490
                                                            SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

              – CnsLength = u2ModLength +12
           • For the Fast Reduction and Normalize:
              – RLength = u2ModLength +4
              – CnsLength = u2ModLength +8
           • For the BigRedMod:
              – RLength = u2ModLength +4
              – CnsLength =64
         The following combinations of input values should be avoided in the case of a modular reduction ‘alone’,
         meaning that it has not been requested as an option of any other command:
           • nu1ModBase, nu1CnsBase, nu1RBase, nu1XBase are not aligned on 32-bit boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2CnsLength}, {nu1XBase, 2*u2XLength + 8 + s}
             or {nu1RBase, u2RLength} are not in Crypto RAM
           • u2ModLength is either: < 4, > 0xffc or not a 32-bit length
           • Overlaps exist between two or more of the areas: {nu1ModBase, u2ModLength + 4},{nu1CnsBase,
             u2CnsLength}, {nu1XBase, 2*u2XLength + 8 + s} or {nu1RBase, u2RLength}
         Note: Overlaps between {nu1RBase, RLength} and {nu1XBase, 2*u2XLength + 8} are forbidden; but if
         the operation is the Fast, Normalized or Big Modular Reduction, the equality between nu1RBase and
         nu1XBase is authorized.
43.3.5.1.13 Status Returned Values
         Table 43-49. RedMod Service Return Codes

          Returned Status                          Importance Meaning
          PUKCL_OK                                 –            Service functioned correctly
          PUKCL_DIVISION_BY_ZERO                   Severe       When computing an Euclidean division, the
                                                                Modulus was found to be zero. This occurs ONLY
                                                                when either reducing using an Euclidean division
                                                                or computing the reduction constant usable for a
                                                                Fast or Normalize Reduction.
          PUKCL_UNEXPLOITABLE_OPTIONS Severe                    A bad combination of options has been detected.
          PUKCL_MALFORMED_MODULUS                  Severe       The Msw of the modulus is not zero.

43.3.5.2 Modular Exponentiation (Without CRT)
43.3.5.2.1 Purpose
         This service is used to perform the Modular Exponentiation computation. This service processes integers
         in GF(p) only.
         The options available for this service are:
           •   Fast implementation
           •   Regular implementation
           •   Exponent is located in Crypto RAM or not in Crypto RAM
           •   Exponent window size




         © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 1491
                                                             SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

43.3.5.2.2 How to Use the Service

43.3.5.2.3 Description


                         Important: Before using these functions, ensure that the constant Cns has been calculated
                         with the Setup of the Modular Reductions service.


          This service processes the following operation:
          The service name for this operation is ExpMod.
          R = XExpmod(N)
          In this computation, the following parameters need to be provided:
           •   X: input number (pointed by {nu1XBase,u2ModLength +16})
           •   N: modulus (pointed by {nu1ModBase,u2ModLength +4}).
           •   Exp: exponent (pointed by {pfu1ExpBase,u2ExpLength +4})
           •   Cns: Fast Modular Constant (pointed by {nu1CnsBase,u2ModLength +8})
           •   Precomp: precomputation workspace (pointed by{nu1PrecompBase,PrecompLen})
           •   Blinding: exponent blinding value (provided inu1Blinding)
          The length PrecompLen depends on the lengths and options chosen; its calculus is detailed in Options
          below.
          Note: The minimum value for u2ModLength is 12 bytes. Therefore, the significant length of N must be at
          least three 32-bit words.
43.3.5.2.4 Parameters Definition
          Table 43-50. ExpMod Service Parameters

          Parameter                 Type Direction Location      Data Length      Before        After
                                                                                  Executing the Executing the
                                                                                  Service       Service
          u2Options                 u2      I       –            –                Options (see      Options (see
                                                                                  below)            below)
          nu1ModBase                nu1     I       Crypto       u2ModLength      Base of N         Base of N
                                                    RAM          +4                                 untouched
          nu1CnsBase                nu1     I       Crypto       u2ModLength      Base of Cns       Base of Cns
                                                    RAM          +8                                 untouched
          u2ModLength               u2      I       –            –                Length of N       Length of N
          nu1XBase (see             nu1     I       Crypto       u2ModLength      Base of X         Base of X
          Note 1)                                   RAM          + 16
                                                                                                    Filled with the
                                                                                                    result

          nu1PrecompBase            nu1     I       Crypto       See below        Base of           Base of
                                                    RAM                           Precomp as a      Precomp
                                                                                  workspace         workspace
                                                                                                    corrupted




         © 2019 Microchip Technology Inc.                      Datasheet                        DS60001507E-page 1492
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

          ...........continued
          Parameter                 Type Direction Location      Data Length       Before        After
                                                                                   Executing the Executing the
                                                                                   Service       Service
          pfu1ExpBase (see          pfu1 I         Any place     u2ExpLength       Base of the       Base of the
          Note 2)                                  (see Note     +4                Exponent          Exponent
                                                   3)                                                untouched
          u2ExpLength (see          u2      I      –             –                 Significant       Significant
          Note 4)                                                                  length of         length of
                                                                                   Exponent          Exponent
          u1Blinding (see           u1      I      –             –                 Exponent          Exponent
          Note 5)                                                                  unblinding        unblinding
                                                                                   value             value
                                                                                                     untouched

         Note:
          1. This zone contains the number to be exponentiated (u2ModLength bytes) and is used during the
               computations as a workspace (four 32-bit words longer than the number to be exponentiated). At
               the end of the computation, it contains the correct result of the operation.
          2. The exponent must be given with a supplemental word on the LSB side (low addresses). This word
               shall be set to zero.
          3. If the PUKCL_EXPMOD_EXPINPUKCCRAM option is not set, the location of the exponent MUST
               NOT be the Crypto RAM, even partially.
          4. The u2ExpLength parameter does not take into account the supplemental word needed on the LSB
               side of the exponent.
          5. It is possible to mask the exponent in memory using an 8-bits XOR mask value. Be aware that not
               only the exponent, but also the supplemental word has to be masked. If masking is not desired,
               then this parameter should be set to 0.
43.3.5.2.5 Options
          The options are set by the u2Options input parameter, which is composed of:
           • the mandatory Calculus Mode Option described in Table 43-51
           • the mandatory Window Size Option described in Table 43-52
           • the indication of the presence of the exponent in Crypto RAM
          Note: Please check precisely if one part of the exponent is in Crypto RAM. If this is the case the
          PUKCL_EXPMOD_EXPINPUKCCRAM must be used.
         The u2Options number is calculated by an “Inclusive OR” of the options. Some examples in C language
         are:
           • Operation:Fast Modular Exponentiation with the window size equal to 1 and with no part of the
             Exponent in the Crypto RAM
             PUKCL(u2Options) = PUKCL_EXPMOD_FASTRSA | PUKCL_EXPMOD_WINDOWSIZE_1;
           • Operation: Regular Modular Exponentiation with the window size equal to 2 and with one part of the
             Exponent in the Crypto RAM
             PUKCL(u2Options) = PUKCL_EXPMOD_REGULARRSA | PUKCL_EXPMOD_WINDOWSIZE_2 |
             PUKCL_EXPMOD_EXPINPUKCCRAM;




         © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1493
                                                            SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

         There is no difference on the final result when using any of the options for this service. The choice has to
         be made according to the available resources (RAM, Time) and also taking into account the expected
         security level.
         For this service, two exclusive Calculus Modes are possible. The following table describes the Calculus
         Mode Options.
         Table 43-51. ExpMod Service Calculus Mode Option

          Option                               Explanation
          PUKCL_EXPMOD_FASTRSA                 Performs a Fast computation
          PUKCL_EXPMOD_REGULARRSA Performs a Regular computation, slower than the Fast version, but
                                  using Regular calculus methods

         For this service, four window sizes are possible. The window size in bits is those of the windowing
         method used for the exponent.
         The choice of the window size is a balance between the size of the parameters and the computation time:
          • Increasing the window size increases the precomputation workspace.
          • Increasing the window size reduces the computation time (may not be relevant for very small
            exponents).
         The following table details the size of the precomputation workspace, depending on the chosen window
         size option.
         Table 43-52. ExpMode Service Window Size Options and Precomputation Space Size

          Option specified                       Size of the PrecompBase                Content of the Workspace
                                                 Workspace (bytes)
          PUKCL_EXPMOD_WINDOWSIZE_1 3*(u2ModLength + 4) + 8                             x
          PUKCL_EXPMOD_WINDOWSIZE_2 4*(u2ModLength + 4) + 8                             x x3
          PUKCL_EXPMOD_WINDOWSIZE_3 6*(u2ModLength + 4) + 8                             x x3 x5 x7
          PUKCL_EXPMOD_WINDOWSIZE_4 10*(u2ModLength + 4) + 8                            x x3 x5 x7 x9 x11 x13 x15

         The exponent can be located in RAM or in the data space. If one part of the exponent is in Crypto RAM
         this must be mandatory signaled by using the option PUKCL_EXPMOD_EXPINPUKCCRAM.
         The following table describes this option.
         Table 43-53. ExpMod Service Exponent in Crypto RAM Option

          Option                                      Purpose
          PUKCL_EXPMOD_EXPINPUKCCRAM The exponent can be read from any data space of memory,
                                     including Flash, RAM or even Crypto RAM. When at least one
                                     word the exponent is in Crypto RAM, this option has to be set.

43.3.5.2.6 Code Example
          PUKCL_PARAM PUKCLParam;
          PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;


          PUKCL(u2Option) =...;




        © 2019 Microchip Technology Inc.                        Datasheet                       DS60001507E-page 1494
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

           // Depending on the option specified, not all fields should be filled
           PUKCL_ExpMod(nu1ModBase) = <Base of the ram location of N>;
           PUKCL_ExpMod(u2ModLength) = <Length of N>;
           PUKCL_ExpMod(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL_ExpMod(nu1XBase) = <Base of the ram location of X>;
           PUKCL_ExpMod(nu1PrecompBase) = <Base of the ram location of Precomp>;
           PUKCL_ExpMod(pfu1ExpBase) = <Base of the location of Exp>;
           PUKCL_ExpMod(u2ExpLength) = <Length of Exp>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(ExpMod, pvPUKCLParam);
           if (PUKCL_Param.Status == PUKCL_OK)
                       {
                       // operation has been performed correctly
                       ...
                       }
           else // Manage the error

43.3.5.2.7 Constraints
          The following combinations of input values should be avoided in the case of a modular reduction ‘alone’,
          meaning that it has not been requested as an option of any other command:
           • nu1ModBase,nu1CnsBase, nu1XBase,nu1PrecompBase,nu1ExpBase are not aligned on 32-bit
             boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1XBase, u2ModLength
             +16},{nu1PrecompBase, <PrecompLength>} are not in Crypto RAM
           • {nu1ExpBase,u2ExpLength + 4} has no part in Crypto RAM and
             PUKCL_EXPMOD_EXPINPUKCCRAM is specified
           • u2ModLength or u2ExpLength are either: < 4, > 0xffc or not a 32-bit length
           • None or both PUKCL_EXPMOD_REGULARRSA and PUKCL_EXPMOD_FASTRSA are specified.
           • {nu1PrecompBase,<PrecompLength>} overlaps with either: {nu1ModBase, u2ModLength +4},
             {nu1CnsBase, u2ModLength + 8} {nu1XBase, u2ModLength + 16} or {nu1ExpBase, u2ExpLength
             + 4}
           • {nu1XBase,u2ModLength + 16} overlaps with either: {nu1ModBase, u2ModLength + 4},
             {nu1CnsBase, u2ModLength + 8} or {nu1ExpBase, u2ExpLength + 4}
           • {nu1ModBase, u2ModLength + 4} overlaps {nu1CnsBase, u2ModLength +8}
43.3.5.2.8 Maximum Sizes for the Modular Exponentiation
          The following table provides the maximum sizes for the Modular Exponentiation, depending on the
          window size and the presence of the exponent in Crypto RAM.
           • The figures below are calculated supposing that u2ExpLength =u2ModLength.
           • In case of the PUKCL_EXPMOD_EXPINPUKCCRAM option is specified, for the computation of the
             maximum acceptable size, it is assumed the Exponent is entirely in the Crypto RAM and its length is
             equal to the Modulus one.
           • Otherwise, the Exponent is entirely out of the Crypto RAM and so the computation do not depend on
             its length.
          Table 43-54. Maximum Exponentiation Sizes

          Option Specified                             Maximum Modulus Size           Maximum Modulus Size
                                                       (bytes)                        (bits)
          Exponent in Crypto RAM, 1 bit window         576                            4608




         © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1495
                                                             SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

          ...........continued
          Option Specified                               Maximum Modulus Size          Maximum Modulus Size
                                                         (bytes)                       (bits)
          Exponent in Crypto RAM, 2 bits window          504                           4032
          Exponent in Crypto RAM, 3 bits window          400                           3200
          Exponent in Crypto RAM, 4 bits window          284                           2272
          Exponent not in Crypto RAM, 1 bit window       672                           5376
          Exponent not in Crypto RAM, 2 bits window 576                                4608
          Exponent not in Crypto RAM, 3 bits window 448                                3584
          Exponent not in Crypto RAM, 4 bits window 308                                2464

43.3.5.2.9 Status Returned Values
          Table 43-55. ExpMod Service Return Codes

          Returned Status                   Importance              Meaning
          PUKCL_OK                          –                       Service functioned correctly

43.3.5.3 Probable Prime Generation (Using Rabin-Miller)
43.3.5.3.1 Purpose
          This service is used to perform probable prime generation or test. This service processes integers in
          GF(p) only.
          The options available for this service are:
           •   Choice of the number of iterations of the Rabin-Miller test
           •   Generation or Test of a probable prime number
           •   Fast Implementation
           •   Regular Implementation
           •   Exponent Window Size
43.3.5.3.2 Additional Information
          The Rabin-Miller test is a probable-primality testing algorithm. As a consequence, the primality of the
          generated number is not guaranteed at 100%, however, numerous publications have been issued
          explaining how to estimate the probability of getting a composite number, giving the size of the number
          and the number of iterations (the T parameter).
          Useful information can be found in the “Handbook of Applied Cryptography (Discrete Mathematics and Its
          Applications” by Alfred J. Menezes, Paul C. van Oorschot, and Scott A. Vanstone, in the following
          sections:
           • 4.2.3. “Rabin-Miller Test”
           • 4.4. “Prime Number Generation”
43.3.5.3.3 How to Use the Service

43.3.5.3.4 Description
          This service processes a test for probable primality or a generation of a probable prime number.




         © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1496
                                                                       SAM D5x/E5x Family Data Sheet
                                                                   Public Key Cryptography Controller (PUKCC)

          Note: When using this service be sure to follow the directives given for the RNG on the chip you use
          (particularly initialization, seeding) and compulsorily start the RNG.
          This service processes one of the following operations: CheckProbablePrimality(N)
          or
          N = GenerateProbablePrimeFromSeed (NSeed)
          In this computation, the following parameters need to be provided:
           • N the input number (pointed by {nu1NBase,u2NLength +4})
              – If the requested operation is a test, it is untouched after the operation.
              – If the requested operation is a generation and a probable prime number was found before
                 reaching the Maximum Increment, it contains the resulting probable prime after the operation.
              – If the requested operation was a generation and Maximum Increment was reached before a
                 probable prime number was found, it contains no relevant information.
           • Cns as a workspace (pointed by {nu1CnsBase,u2NLength +12})
           • Rnd as a workspace (pointed by {nu1RndBase,u2NLength +16})
           • Precomp the precomputation workspace (pointed by{nu1PrecompBase,PrecompLen})
           • Exp as a workspace (pointed by {pfu1ExpBase,u2ExpLength +4})
           • u1MillerRabinIterations the number of Miller Rabin Iterations requested
           • u2MaxIncrement, maximum increment of the number in case of probable prime generation
          The length PrecompLen depends on the lengths and options chosen; its calculus is detailed in Options
          below.
          The service name for this operation is PrimeGen.
43.3.5.3.5 Parameters Definition
          Table 43-56. PrimeGen Service Parameters
          Parameter                  Typ    Direction   Location   Data Length      Before Executing the     After Executing the
                                     e                                              Service                  Service

          nu1NBase (see Note 1)      nu1    I           Crypto     u2NLength + 4    Base of N                Base of N unchanged if
                                                        RAM                                                  test or generation result
                                                                                    Number to test or Seed
                                                                                                             ( see Note 1)
                                                                                    for the generation

          nu1CnsBase                 nu1    I           Crypto     u2NLength + 12   Base of Cns as a         Base of Cns workspace
                                                        RAM                         workspace                corrupted

          u2NLength                  u2     I           –          –                Length of N              Length of N

          nu1RndBase                 nu1    I           Crypto     Max (u2NLength   Internal Workspace       Internal Workspace
                                                        RAM        + 16,64)                                  corrupted

          nu1PrecompBase             nu1    I           Crypto     See Options      Base of Precomp          Base of Precomp
                                                        RAM        below            workspace                workspace corrupted

          nu1RBase (see Note 2)      nu1    –           Crypto     –                –                        –
                                                        RAM

          nu1ExpBase (see Note       nu1    I           Crypto     u2NLength + 4    Base of Exponent (R)     Base of Exponent (R)
          3)                                            RAM

          u1MillerRabin-Iterations   u1     I           –          –                Miller Rabin’s T         Miller Rabin’s T
                                                                                    parameter                parameter




         © 2019 Microchip Technology Inc.                              Datasheet                             DS60001507E-page 1497
                                                                       SAM D5x/E5x Family Data Sheet
                                                                   Public Key Cryptography Controller (PUKCC)

          ...........continued
          Parameter                 Typ     Direction   Location   Data Length     Before Executing the   After Executing the
                                    e                                              Service                Service

          u2MaxIncrement            u2      I           –          –               Maximum Increment      Maximum Increment
                                                                                   (see Note 4)


         Note:
          1. This zone contains the number to be either tested or used as a seed for generation. It has to be
               provided with one zero word on the MSB side. This area has supplementary constraints (see the
               following Important note).
            1.    This parameter does not have to be provided and is used as an internal value for computing the
                  reduction’s constant.
            2.    The area {nu1ExpBase, u2NLength + 4} must be entirely in the Crypto RAM.
            3.    The generation starts from the number in {nu1NBase,u2NLength + 4} and increments it until a
                  number is found as probable prime. However, the generation may stop for two reasons: The
                  number has been incremented in a way it is bigger than <u2NLength> bytes, or the original number
                  has been incremented by more than <u2MaxIncrement>.
         In case of probable prime generation, ensure that the addition of NSeed and Maximum Increment is not a
         number with more bytes than u2NLength, as this would produce an overflow.


                            Important:
                            One additional word is used on the LSB side of the NBase parameter; this word is restored at
                            the end of the calculus. As a consequence, the parameter nu1NBase must never be at the
                            beginning of the Crypto RAM, but at least at one word from the beginning.
                            One additional word is used on the MSB side of the NBase parameter; this word is not
                            corrupted. As a consequence the Area {nu1NBase, u2NLength} must not be at the end of the
                            Crypto RAM but at least at one word from the end.
                            Prime numbers of a size lower than 96 bits (three 32-bit words) cannot be generated or tested
                            by this service.


43.3.5.3.6 Options
          Some of the Prime Generation options configure the Modular Exponentiation steps and so are very
          similar to the Modular Exponentiation options.
          The options are set by the u2Options input parameter, which is composed of:
            • the mandatory Operation Option described in Table 43-57
            • the mandatory Calculus Mode Option described in Table 43-58
            • the mandatory Window Size Option described in Table 43-59
          The u2Options number is calculated by an “Inclusive OR” of the options. Some Examples in C language
          are:
            • Operation: Probable Prime Testing with Fast Modular Exponentiation and the window size equal to 1
              PUKCL(u2Options) = PUKCL_PRIMEGEN_TEST | PUKCL_EXPMOD_FASTRSA |
              PUKCL_EXPMOD_WINDOWSIZE_1;
            • Operation: Probable Prime Generate with Regular Modular Exponentiation and the window size
              equal to 2




         © 2019 Microchip Technology Inc.                              Datasheet                          DS60001507E-page 1498
                                                 SAM D5x/E5x Family Data Sheet
                                                Public Key Cryptography Controller (PUKCC)

     PUKCL(u2Options) = PUKCL_EXPMOD_REGULARRSA | PUKCL_EXPMOD_WINDOWSIZE_2;
The following table describes the PrimeGen service features available from the various options.
Table 43-57. PrimeGen Service Options

 Option                                       Method Used
 PUKCL_PRIMEGEN_TEST                          This option is used to specify that only tests will be made
                                              on the provided number.
                                              When this option is not specified, a prime generation
                                              algorithm is selected, starting from the given seed and
                                              incrementing it.

 PUKCL_EXPMOD_WINDOWSIZE_1,2,3 or             Depending on this option, different bit-window sizes will
 4                                            be used. For long exponents, the bigger the window, the
                                              faster the computation. However, this has also an impact
                                              on the size of the precomputations table.

For this service, two exclusive Calculus Modes are possible. The following table describes the Calculus
Mode Options.
Table 43-58. PrimeGen Service Calculus Mode Options

 Option                              Explanation
 PUKCL_EXPMOD_FASTRSA                Perform a Fast computation.
 PUKCL_EXPMOD_REGULARRSA Performs a Regular computation, slower than the Fast version, but
                         using regular calculus methods.

The length of the Precomp area depends on the window size W and u2NLength. The Precomp area
length is:
PrecompLen = max( 2*(u2NLength + 4) + 2W-1 * (u2NLength + 4), u2NLength + 8 + 64) + 8
Note: Please calculate precisely the length PrecompLen with the formula and the max() macro, which
takes a maximum of two values.
The following table shows the size of the precomputation workspace (PrecompLen), depending on the
chosen window size option.
Table 43-59. PrimeGen Service Precomputation Space Size

 Option Specified                      Size of the PrecompBase                  Content of the
                                       Workspace (bytes)                        Workspace
 PUKCL_EXPMOD_WINDOWSIZE_1 max( 3*(u2NLength + 4), u2NLength                    x
                           + 72) + 8
 PUKCL_EXPMOD_WINDOWSIZE_2 max( 4*(u2NLength + 4), u2NLength                    x x3
                           + 72) + 8
 PUKCL_EXPMOD_WINDOWSIZE_3 max( 6*(u2NLength + 4), u2NLength                    x x3 x5 x7
                           + 72) + 8




© 2019 Microchip Technology Inc.                   Datasheet                           DS60001507E-page 1499
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

          ...........continued
          Option Specified                       Size of the PrecompBase                 Content of the
                                                 Workspace (bytes)                       Workspace
          PUKCL_EXPMOD_WINDOWSIZE_4 max( 10*(u2NLength + 4) u2NLength                    x x3 x5 x7 x9 x11 x13 x15
                                    + 72) + 8

          The following table provides the maximum sizes for the Prime Generation depending on the window size.
          Table 43-60. PrimeGen Service Maximum Sizes

          Characteristics of the Operation                         Maximum Prime Sizes (bits)
          1 bit window                                             4608
          2 bits window                                            4032
          3 bits window                                            3200
          4 bits window                                            2272

43.3.5.3.7 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // ! The Random Number Generator must be initialized and started
           // ! following the directives given for the RNG on the chip PUKCL(u2Option) =...;
           // Depending on the option specified, not all fields should be filled
           PUKCL_PrimeGen(nu1NBase) = <Base of the ram location of N>;
           PUKCL_PrimeGen(u2NLength) = <Length of N>;
           PUKCL_PrimeGen(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL_PrimeGen(nu1PrecompBase) = <Base of the ram location of Precomp>;
           PUKCL_PrimeGen(pfu1ExpBase) = <Base of the location of Exp>;
           PUKCL_PrimeGen(u2ExpLength) = <Length of Exp>;
           PUKCL_PrimeGen(u1MillerRabinIterations) = <Number of iterations>;
           PUKCL_PrimeGen(u2MaxIncrement) = <Maximum Increment>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(PrimeGen, pvPUKCLParam);
           if (PUKCL_Param.Status == PUKCL_NUMBER_IS_PRIME)
                       {
                       // The number is probably prime
                       ...
                       }
           else if (PUKCL_Param.Status == PUKCL_NUMBER_IS_NOT_PRIME)
                       {
                       // The number is not prime
                       ...
                       }
           else // Manage the error

43.3.5.3.8 Constraints
          The following combinations of input values should be avoided in the case of a modular reduction ‘alone’,
          meaning that it has not been requested as an option of any other service:
           • nu1NBase,nu1CnsBase, nu1RndBase,nu1PrecompBase,nu1ExpBase are not aligned on 32-bit
             boundaries
           • {nu1NBase, u2NLength + 4}, {nu1CnsBase, u2NLength + 12}, {nu1RndBase, u2NLength +12},
             {nu1PrecompBase, <PrecompLength>} are not in Crypto RAM
           • u2NLength is either: < 12, > 0xffc or not a 32-bit length
           • Both PUKCL_EXPMOD_REGULARRSA and PUKCL_EXPMOD_FASTRSA are specified.




         © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1500
                                                             SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

           • {nu1PrecompBase,<PrecompLength>} overlaps with either: {nu1NBase, u2NLength + 4},
             {nu1CnsBase, u2NLength + 12} {nu1RndBase, u2NLength + 12} or {nu1ExpBase, u2ExpLength + 4}
           • {nu1RndBase,3*u2NLength + 24} overlaps with either: {nu1NBase, u2NLength + 4},{nu1CnsBase,
             u2NLength + 12} {nu1XBase, u2NLength + 12} or {nu1ExpBase, u2ExpLength + 4}
           • {nu1NBase, u2NLength + 4} overlaps {nu1CnsBase, u2NLength +12}
43.3.5.3.9 Status Returned Values
          Table 43-61. PrimeGen Service Return Codes

          Returned Status                         Importance Meaning
          PUKCL_NUMBER_IS_PRIME                   Information    The generated or tested number has been detected
                                                                 as probably prime.
          PUKCL_NUMBER_IS_NOT_PRIME Information                  The generated or tested number has been detected
                                                                 as composite.

43.3.5.4 Modular Exponentiation (With CRT)

43.3.5.4.1 Purpose
          The purpose of this service is to perform the Modular Exponentiation with the Chinese Remainders
          Theorem (CRT). This service processes integers in GF(p) only.
          The options available for this service are:
           •   Fast implementation
           •   Regular implementation
           •   Exponent is located in Crypto RAM or not
           •   Exponent window size
43.3.5.4.2 How to Use the Service

43.3.5.4.3 Description
          This service processes a Modular Exponentiation with the Chinese Remainder Theorem:
          R = XDmod(N) with N = P *Q


                         Important: For this service, be sure to follow the directives given for the RSA implementation
                         on the chip you use.


          This service requires that the modulus N is the product of two co-primes P and Q and that the decryption
          exponents D is co-prime with the product ((P-1)*(Q-1)).
          The Input data are P, Q, EP, EQ, Rvalue, and X. P and Q are the co-primes so that N = P*Q.
          X is the number to exponentiate.
          EP, EQ and Rval are calculated as follows:
          EP = Dmod(P – 1) EQ = Dmod(Q – 1) Rval = P–1mod(Q)
          In some cases, the decryption exponent D may not be available and the encryption exponent E may be
          available instead. The possibilities to calculate the parameters are:
           • Calculate D from E with the formula:
             D = E–1mod((P – 1) × (Q – 1))




         © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 1501
                                                             SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

           • Calculate the parameters from E:
             EP = E–1mod(P – 1) EQ = E–1mod(Q – 1) Rval = P–1mod(Q)
          In this computation, the following parameters need to be provided:
           •   X the input number (pointed by {nu1XBase,2*u2ModLength +16})
           •   P and Q the primes (pointed by {nu1ModBase,2*u2ModLength +8}).
           •   EP and EQ the reduced exponents (pointed by {pfu1ExpBase,2*u2ExpLength +8})
           •   Rval and Precomp (pointed by{nu1PrecompBase,RAndPrecompLen})
           •   Blinding the exponent blinding value (provided inu1Blinding)
          The length RAndPrecompLen depends on the lengths and options chosen; its calculus is detailed in
          Options below.
          The service for this operation is CRT.
          Note: The minimum value for u2ModLength is 12 bytes. Therefore, the significant length of P or Q must
          be at least three 32-bit words.
43.3.5.4.4 Parameters Definition
          The following table shows the parameter block for the CRT service.
          Many parameters have complex placement in memory; therefore, detailed figures are provided in CRT
          Service Placement below.
          Table 43-62. CRT Service Parameters

          Parameter                Type Direction Location      Data Length     Before              After
                                                                                Executing the       Executing
                                                                                Service             the Service
          u2Options                u2       I      –            –               Options (see        Options (see
                                                                                below)              below)
          nu1ModBase               nu1      I      Crypto       2*u2ModLength   Base of P, Q        Base of P, Q
                                                   RAM          +8                                  untouched
          u2ModLength              u2       I      –            –               Length of P or Q    Length of P or
                                                                                greater than or     Q
                                                                                equal to 12
          nu1XBase (see            nu1      I      Crypto       2*u2ModLength   Base of X           Base of X
          Note 1)                                  RAM          + 16
                                                                                                    Filled with the
                                                                                                    result

          nu1PrecompBase           nu1      I      Crypto       See Options     Base of Rvalue      Corrupted
                                                   RAM          below           and Pre
                                                                                computations
                                                                                workspace
          pfu1ExpBase (see         pfu1 I          Any place    2*u2ExpLength   Base of EP, EQ      Base of EP,
          Note 2)                                               +8                                  EQ untouched
          u2ExpLength              u2       I      –            –               Significant length Significant
                                                                                of EP or EQ        length of EP
                                                                                                   or EQ




         © 2019 Microchip Technology Inc.                      Datasheet                       DS60001507E-page 1502
                                                             SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

          ...........continued
          Parameter                Type Direction Location     Data Length       Before             After
                                                                                 Executing the      Executing
                                                                                 Service            the Service
          u1Blinding (see          u4       I     –            –                 Exponent           Exponent
          Note 3)                                                                unblinding value   unblinding
                                                                                                    value

          Note:
           1. This zone contains the number to be exponentiated (u2ModLength bytes) and is used during the
                computations as a workspace (four 32-bit words longer than the number to be exponentiated). At
                the end of the computation, it contains the correct result of the operation.
           2. If the PUKCL_EXPMOD_EXPINPUKCCRAM option is not set, the location of the exponent MUST
                NOT be placed in the Crypto RAM, even partially.
           3. It is possible to mask the exponent in memory using a 32-bit XOR mask value. Be aware that not
                only the exponent, but also the supplemental spill word has to be masked. If masking is not
                desired, the parameter should be set to 0.
43.3.5.4.5 Options
          Most of the CRT options configure the Modular Exponentiation steps of the CRT and so are very similar
          to the Fast Modular Exponentiation options.
          The options are set by the u2Options input parameter, which is composed of:
           • the mandatory Calculus Mode Option described in Table 43-63
           • the mandatory Window Size Option described in Table 43-64
           • the indication of the presence of the exponent in Crypto RAM


                        Important: Please check precisely if one part of the exponent area (containing EP and EQ) is
                        in Crypto RAM. If this is the case, the PUKCL_EXPMOD_EXPINPUKCCRAM option must be
                        used.


          The u2Options number is calculated by an “Inclusive OR” of the options. Some Examples in C language
          are:
           • Operation: CRT using the Fast Modular Exponentiation with the window size equal to 1 and with no
             part of the Exponent area in the Crypto RAM
             PUKCL(u2Options) = PUKCL_EXPMOD_FASTRSA | PUKCL_EXPMOD_WINDOWSIZE_1;
           • Operation:CRT using the Regular Modular Exponentiation with the window size equal to 2 and with
             one part the Exponent area in the Crypto RAM
             PUKCL(u2Options) = PUKCL_EXPMOD_REGULARRSA | PUKCL_EXPMOD_WINDOWSIZE_2 |
             PUKCL_EXPMOD_EXPINPUKCCRAM;
          For this service, two exclusive Calculus Modes for the Modular Exponentiation steps of the CRT are
          possible. The following table describes the Calculus Mode Options.
          Table 43-63. CRT Service Calculus Mode Options

          Option                                Explanation
          PUKCL_EXPMOD_FASTRSA                  Perform a Fast computation.




         © 2019 Microchip Technology Inc.                     Datasheet                       DS60001507E-page 1503
                                                 SAM D5x/E5x Family Data Sheet
                                                Public Key Cryptography Controller (PUKCC)

...........continued
 Option                               Explanation
 PUKCL_EXPMOD_REGULARRSA Performs a Regular computation, slower than the Fast version, but
                         using regular calculus methods.

For this service, four window sizes for the Modular Exponentiation Steps are possible. The window size in
bits is those of the windowing method used for the exponent.
The choice of the window size is a balance between the size of the parameters and the computation time:
  • Increasing the window size increases the precomputation workspace.
  • Increasing the window size reduces the computation time (may not be relevant for very small
    exponents). The length of the Rval and Precomp area depends on the window size W and
    u2ModLength.
The Rval and Precomp area length is:
RandPrecompLen = 4 * (u2ModLength + 4) + max(64 , 2(W-1) * (u2ModLength + 4)) + 8


               Important: Please calculate precisely the length RandPrecompLen with the formula and the
               max() macro, which takes the maximum of two values.


The following table shows the size of the Rval and Precomp area, depending on the chosen window size
option.
Table 43-64. CRT Service Window Size Options and Rval and Precomp Area Size

 Option Specified                       Size of the Rval and Precomp Area      Precomputation Values
                                        (bytes)
 PUKCL_EXPMOD_WINDOWSIZE_1 4*(u2ModLength + 4) + max(64 ,                      x
                           (u2ModLength + 4)) + 8
 PUKCL_EXPMOD_WINDOWSIZE_2 4*(u2ModLength + 4) + max(64 ,                      x x3
                           2*(u2ModLength + 4)) + 8
 PUKCL_EXPMOD_WINDOWSIZE_3 4*(u2ModLength + 4) + max(64 ,                      x x3 x5 x7
                           4*(u2ModLength + 4)) + 8
 PUKCL_EXPMOD_WINDOWSIZE_4 10*(u2ModLength + 4) + max(64 ,                     x x3 x5 x7 x9 x11 x13 x15
                           8*(u2ModLength + 4)) + 8

The exponent area can be located in RAM or in the data space. If one part of the exponent area is in
Crypto RAM this must be mandatory signaled by using the PUKCL_EXPMOD_EXPINPUKCCRAM
option.
The following table describes this option.




© 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1504
                                                            SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

          Table 43-65. CRT Service Crypto RAM Option Exponent Area

          Option                                    Purpose
          PUKCL_EXPMOD_EXPINPUKCCRAM The exponent area can be read from any data space of
                                     memory, including Crypto RAM. When at least one word the
                                     exponent is in Crypto RAM, this option has to be set.

43.3.5.4.6 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;


           PUKCL(u2Option) =...;

           // Depending on the option specified, not all fields should be filled PUKCL_CRT(nu1ModBase) =
           <Base of the ram location of P and Q>; PUKCL_CRT(u2ModLength) = <Length of P or Q>;
           PUKCL_CRT(nu1XBase) = <Base of the ram location of X>;
           PUKCL_CRT(nu1PrecompBase) = <Base of the ram location of RVal and Precomp>;
           PUKCL_CRT(pfu1ExpBase) = <Base of the ram location of EP and EQ>;
           PUKCL_CRT(u2ExpLength) = <Length of EP or EQ>;
           PUKCL_CRT(u1Blinding) = <Blinding value>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(CRT, pvPUKCLParam);
           if (PUKCL_Param.Status == PUKCL_OK)
                       {
                       // operation has been performed correctly
                       ...
                       }
           else // Manage the error

43.3.5.4.7 Constraints
          The following conditions must be avoided to ensure that the service works correctly:
           • nu1ModBase, nu1XBase, nu1PrecompBase, pfu1ExpBase are not aligned on 32-bit boundaries
           • {nu1XBase, 2*u2ModLength + 16}, {nu1ModBase, 2*u2ModLength + 8},
             {nu1PrecompBase,<PrecompLength>} are not in Crypto RAM
           • {nu1ExpBase,2*u2ExpLength + 8} is not in Crypto RAM and PUKCL_EXPMOD_EXPINPUKCCRAM
             is specified
           • u2ModLength or u2ExpLength are either: < 4, > 0xffc or not a 32-bit length
           • None or both PUKCL_EXPMOD_REGULARRSA and PUKCL_EXPMOD_FASTRSA are specified.
           • {nu1XBase,2*u2ModLength + 16} overlaps with either: {nu1ModBase, 2*u2ModLength +8},
             {nu1PrecompBase, <PrecompLength>} or {pfu1ExpBase, 2*u2ExpLength + 8}
           • {nu1ModBase,2*u2ModLength + 8} overlaps with either: {nu1PrecompBase, <PrecompLength>} or
             {pfu1ExpBase, 2*u2ExpLength + 8}
           • {nu1PrecompBase, <PrecompLength>} overlaps {pfu1ExpBase, 2*u2ExpLength +8}
43.3.5.4.8 CRT Service Parameter Placement
          The parameters’ placements are described in detail in the following figures.




         © 2019 Microchip Technology Inc.                     Datasheet                          DS60001507E-page 1505
                                           SAM D5x/E5x Family Data Sheet
                                          Public Key Cryptography Controller (PUKCC)

Figure 43-2. Modulus P and Q in {nu1ModBase, 2*u2ModLength + 8}




Figure 43-3. Value X in {nu1XBase, 2*u2ModLength + 16}




Figure 43-4. Exponents EP and EQ in {fnu1ExpBase, 2*u2ExpLength + 8}




© 2019 Microchip Technology Inc.             Datasheet                 DS60001507E-page 1506
                                                          SAM D5x/E5x Family Data Sheet
                                                         Public Key Cryptography Controller (PUKCC)

         Figure 43-5. Value Rval and Precomp in {nu1PrecompBase, RandPrecompLen}




43.3.5.4.9 CRT Service Modular Exponentiation Maximum Size
         The following table details the maximum size in bits of P or Q, of N and of EP or EQ.
          • The maximum size in bits of P or Q equals:
            <Max Size Bits P> = <Max Size Bits Q> = 8 * <Max u2ModLength bytes>
          • The maximum size in bits of N=P*Q equals:
            <Max Size Bits N> = 2 * <Max Size Bits P>
          • The maximum size in bits of EP or EQ equals:
            <Max Size Bits EP> = <Max Size Bits EQ> = 8 * <Max u2ExpLength bytes>
          • In case of the PUKCL_EXPMOD_EXPINPUKCCRAM option is specified, for the computation of the
            maximum acceptable size, it is assumed the Exponent is entirely in the Crypto RAM and its length
            equal the Modulus one.
          • Otherwise, the Exponent is entirely out of the Crypto RAM and so the computation do not depend on
            its length.
         Table 43-66. CRT Service Maximum Sizes

          Characteristics of the Operation             P or Q Max Bit     N Max Bit      EP or EQ Max Bit Sizes
                                                       Sizes              Sizes
          Exponent in Crypto RAM, 1 bit window         2912               5824           2912
          Exponent in Crypto RAM, 2 bits window        2688               5376           2688
          Exponent in Crypto RAM, 3 bits window        2464               4928           2464
          Exponent in Crypto RAM, 4 bits window        2304               4608           2304
          Exponent not in Crypto RAM, 1 bit window     3584               7168           <application dependent>
          Exponent not in Crypto RAM, 2 bits window 3232                  6464           <application dependent>
          Exponent not in Crypto RAM, 3 bits window 2912                  5824           <application dependent>




        © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1507
                                                             SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

         ...........continued
          Characteristics of the Operation                P or Q Max Bit   N Max Bit       EP or EQ Max Bit Sizes
                                                          Sizes            Sizes
          Exponent not in Crypto RAM, 4 bits window 2688                   5376            <application dependent>

43.3.5.4.10 Status Returned Values
         Table 43-67. CRT Service Return Codes

          Returned Status                   Importance             Meaning
          PUKCL_OK                          Information            Service functioned correctly

43.3.6   Elliptic Curves Over GF(p) Services
         This section provides a complete description of the currently available elliptic curve over Prime Fields
         services. These services process integers in GF(p) only.
         The offered services cover the basic operations over elliptic curves such as:
           • Adding two points over a curve
           • Doubling a point over a curve
           • Multiplying a point by an integral constant
           • Converting a point’s projective coordinates (resulting from a doubling or an addition) to the affine
             coordinates, and oppositely converting a point’s affine coordinates to the projective coordinates.
           • Testing the point presence on the curve.
         Additionally, some higher level services covering the needs for signature generation and verification are
         offered:
           • Generating an ECDSA signature (compliant with FIPS186-2)
           • Verifying an ECDSA signature (compliant with FIPS186-2) The supported curves use the following
             curve equation:
         Y2 = X3 + aX + b
43.3.6.1 Coordinate Systems
43.3.6.1.1 General Considerations
         In this implementation, several choices have been made related to the coordinate systems managed by
         the elliptic curve primitives.
         There are two systems currently managed by the library:
           • Affine Coordinates System where each curve point has two coordinates (X, Y)
           • Projective Coordinates System where each point is represented with three coordinates (X,Y, Z)
         Converting from the affine coordinates system to a projective coordinates system is performed by
         extending its representation with Z = 1:

         (X, Y) ⇒ (X, Y, Z= 1)

         Converting from a projective coordinate to an affine one is a service offered by the PUKCL. The formula
         to perform this conversion is:
         (X, Y, Z) ⇒ (X / Z2, Y / Z3)




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1508
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

43.3.6.1.2 Points Representations
         Depending on the representation (Projective or Affine), points are represented tn memory, as shown in
         the following figure.
         Figure 43-6. Points Representation in Memory




         In this figure, the modulus is represented as a reference, and to show that coordinates are always to be
         provided on the length of the modulus plus one 32-bit word.
         The different types of representations are as follows:




         Note:
          1. The minimum value for u2ModLength is 12 bytes. Therefore, the significant length of the modulus
               must be at least three 32-bit words.
          2. In some cases the point can be the infinite point. In this case, it is represented with its Z
               coordinates equal or congruent to zero.
43.3.6.1.3 Modulus and Modular Constant Parameters
         In most of the services the following parameters must be provided:
           • P the Modulus (often pointed by {nu1ModBase,u2ModLength + 4}): This parameter contains the
             Modulus Integer prime P defining the Galois Field used in points coordinates computations. The
             Modulus must be u2ModLength bytes long, while having a supplemental zeroed 32-bit word on the
             MSB side.




         © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1509
                                                            SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

             Note: Most of the Elliptic Curve computations are reduced modulo P. In many functions the
             reductions are made with the Fast Reduction.
           • Cns the Modular Constant (often pointed by {nu1CnsBase,u2ModLength + 12}): This parameter
             contains the Modular Constant associated to the Modulus


                         Important: The Modular Constant must be calculated before using the GF(p) Elliptic Curves
                         functions by a call to the Setup for Modular Reductions with the GF(p) option (see Modular
                         Reduction Setup in the 43.3.5.1 Modular Reduction section).


43.3.6.2 Point Addition
43.3.6.2.1 Purpose
          This service is used to perform a point addition, based on a given elliptic curve over GF(p). Please note
          that:
           • This service is not intended to add the same point twice. In this particular case, use the doubling
             service
             (see 43.3.6.4 Fast Point Doubling).
43.3.6.2.2 How to Use the Service

43.3.6.2.3 Description
          The operation performed is:
          PtC = PtA + PtB
          In this computation, the following parameters need to be provided:
           • A the input point is filled in projective coordinates (X,Y,Z) (pointed by {nu1PointABase,
             3*u2ModLength + 12}). This point can be the Infinite Point.
           • B the input point is filled in projective coordinates (X,Y,Z) (pointed by {nu1PointBBase,
             3*u2ModLength + 12}). This point can be the Infinite Point.
           • Cns the Fast Modular Constant filled (pointed by {nu1CnsBase,u2ModLength +8})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength +4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 5*u2ModLength +32}
          The resulting C point is represented in projective coordinates (X,Y,Z) and is stored at the very same place
          than the input point A. This Point can be the Infinite Point.
          The service name for this operation is ZpEccAddFast. This service uses Fast mode and Fast Modular
          Reduction for computations.


                         Important: Before using this service, ensure that the constant Cns has been calculated with
                         the Setup of the Modular Reduction functions.




         © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1510
                                                          SAM D5x/E5x Family Data Sheet
                                                         Public Key Cryptography Controller (PUKCC)

43.3.6.2.4 Parameters Definition
          Table 43-68. ZpEccAddFast Service Parameters

          Parameter           Type Direction Location     Data Length         Before             After Executing
                                                                              Executing the      the Service
                                                                              Service
          nu1ModBase          nu1     I      Crypto       u2ModLength + 4     Base of Modulus Base of
                                             RAM                              P               Modulus P
          nu1CnsBase          nu1     I      Crypto       u2ModLength + 8     Base of Cns        Base of Cns
                                             RAM
          u2ModLength         u2      I      –            –                   Length of          Length of
                                                                              modulo             modulo
          nu1PointABase nu1           I/O    Crypto       3*u2ModLength       Input point A      Resulting point
                                             RAM          + 12                (projective        C (projective
                                                                              coordinates)       coordinates)
          nu1PointBBase nu1           I      Crypto       3*u2ModLength       Input point B      Input point B
                                             RAM          + 12                (projective
                                                                              coordinates)
          nu1Workspace nu1            I      Crypto       5*u2ModLength       –                  Corrupted
                                             RAM          + 32                                   workspace

43.3.6.2.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           PUKCL (u2Option) = 0;

           PUKCL _ZpEccAdd(nu1ModBase) = <Base of the ram location of P>;
           PUKCL _ZpEccAdd(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL _ZpEccAdd(u2ModLength) = <Byte length of P>;
           PUKCL _ZpEccAdd(nu1PointABase) = <Base of the ram location of the A point>;
           PUKCL _ZpEccAdd(nu1PointBBase) = <Base of the ram location of the B point>;
           PUKCL _ZpEccAdd(nu1Workspace) = <Base of the ram location of the workspace>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(ZpEccAddFast,&PUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error

43.3.6.2.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure that the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1PointBBase, nu1Workspace are not aligned on 32-
             bit boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointABase,
             3*u2ModLength + 12}, {nu1PointBBase, 3*u2ModLength + 12}, {nu1Workspace,
             <WorkspaceLength>} are not in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length




         © 2019 Microchip Technology Inc.                     Datasheet                       DS60001507E-page 1511
                                                               SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength +8},
             {nu1PointABase, 3*u2ModLength + 12}, {nu1PointBBase, 3*u2ModLength + 12} and
             {nu1Workspace, 5*u2ModLength + 32}
43.3.6.2.7 Status Returned Values
          Table 43-69. ZpEccAddFast Service Return Codes

          Returned Status                   Importance      Meaning
          PUKCL_OK                          –               The computation passed without problem.

43.3.6.3 Point Addition and Subtraction

43.3.6.3.1 Purpose
          This service is used to perform a point addition and point subtraction, based on a given elliptic curve over
          GF(p). Please note that:
           • This service is not intended to add the same point twice. In this particular case, use the doubling
             service (see 43.3.6.4 Fast Point Doubling).
43.3.6.3.2 How to Use the Service

43.3.6.3.3 Description
          The operation performed is:

          PtC = PtA ± PtB
          In this computation, the following parameters need to be provided:
           • A the input point is filled in projective coordinates (X,Y,Z) (pointed by {nu1PointABase,
             3*u2ModLength + 12}). This point can be the Infinite Point.
           • B the input point is filled in projective coordinates (X,Y,Z) (pointed by {nu1PointBBase,
             3*u2ModLength + 12}). This point can be the Infinite Point.
           • Cns the Fast Modular Constant filled (pointed by {nu1CnsBase,u2ModLength +8})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength +4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 5*u2ModLength +32}
           • The operator filled with the operation to perform (Addition or Subtraction)
          The resulting C point is represented in projective coordinates (X,Y,Z) and is stored at the very same place
          than the input point A. This Point can be the Infinite Point.
          The service name for this operation is ZpEccAddSubFast. This service uses Fast mode and Fast
          Modular Reduction for computations.
          Note: Before using this service, ensure that the constant Cns has been calculated with the setup of the
          modular reduction functions.
43.3.6.3.4 Parameters Definition
          Table 43-70. ZpEccAddSubFast Service Parameters

          Parameter           Type Direction Location         Data Length        Before               After Executing
                                                                                 Executing the        the Service
                                                                                 Service
          nu1ModBase          nu1     I            Crypto     u2ModLength + 4    Base of Modulus Base of Modulus
                                                   RAM                           P               P




         © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1512
                                                           SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

          ...........continued
          Parameter              Type Direction Location   Data Length        Before             After Executing
                                                                              Executing the      the Service
                                                                              Service
          nu1CnsBase             nu1   I        Crypto     u2ModLength + 8    Base of Cns        Base of Cns
                                                RAM
          u2ModLength            u2    I        –          –                  Length of          Length of
                                                                              modulo             modulo
          nu1PointABase nu1            I/O      Crypto     3*u2ModLength      Input point A      Resulting point
                                                RAM        + 12               (projective        C (projective
                                                                              coordinates)       coordinates)
          nu1PointBBase nu1            I        Crypto     3*u2ModLength      Input point B      Input point B
                                                RAM        + 12               (projective
                                                                              coordinates)
          u2Operator             u2    I        -          -                  Addition or        Addition or
                                                                              Subtraction        Subtraction
          nu1Workspace nu1             I        Crypto     5*u2ModLength      –                  Corrupted
                                                RAM        + 32                                  workspace

43.3.6.3.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;


           PUKCL (u2Option) = 0;

           PUKCL _ZpEccAddSub(nu1ModBase) = <Base of the ram location of P>;
           PUKCL _ZpEccAddSub(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL _ZpEccAddSub(u2ModLength) = <Byte length of P>;
           PUKCL _ZpEccAddSub(nu1PointABase) = <Base of the ram location of the A point>;
           PUKCL _ZpEccAddSub(nu1PointBBase) = <Base of the ram location of the B point>;
           PUKCL _ZpEccAddSub(nu1Workspace) = <Base of the ram location of the workspace>;
           PUKCL _ZpEccAddSub(u2Operator) = <Operation to perform (PUKCL_ZPECCADD or PUKCL_ZPECCSUB)>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(ZpEccAddSubFast,&PUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                   {
                   ...
                   }
           else // Manage the error

43.3.6.3.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure that the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1PointBBase, nu1Workspace are not aligned on 32-
             bit boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointABase,
             3*u2ModLength + 12}, {nu1PointBBase, 3*u2ModLength + 12}, {nu1Workspace,
             <WorkspaceLength>} are not in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length




         © 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 1513
                                                               SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength +8},
             {nu1PointABase, 3*u2ModLength + 12}, {nu1PointBBase, 3*u2ModLength + 12} and
             {nu1Workspace, 5*u2ModLength + 32}
43.3.6.3.7 Status Returned Values
          Table 43-71. ZpEccAddFast Service Return Codes

          Returned Status                   Importance      Meaning
          PUKCL_OK                          –               The computation passed without problem.

43.3.6.4 Fast Point Doubling
43.3.6.4.1 Purpose
          This service is used to perform a Point Doubling, based on a given elliptic curve over GF(p).
43.3.6.4.2 How to Use the Service

43.3.6.4.3 Description
          These two services process the Point Doubling:

          PtC = 2 × PtA
          In this computation, the following parameters need to be provided:
           • A the input point is filled in projective coordinates (X,Y,Z) (pointed by {nu1PointABase,
             3*u2ModLength + 12}). This point can be the Infinite Point.
           • Cns the Fast Modular Constant filled (pointed by {nu1CnsBase,u2ModLength +8})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength +4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 4*u2ModLength +28}
           • The a parameter relative to the elliptic curve (pointed by {nu1ABase,u2ModLength +4})
           • The resulting C point is represented in projective coordinates (X,Y,Z) and is stored at the same
             location than the input point A. This point can be the Infinite Point.
          The service name for this operation is ZpEccDblFast. This service uses Fast mode and Fast Modular
          Reduction for computations.


                         Important: Before using this service, ensure that the constant Cns has been calculated with
                         the setup of the Fast Modular Reduction service.



43.3.6.4.4 Parameters Definition
          Table 43-72. ZpEccDblFastService

          Parameter           Type Direction Location         Data Length        Before             After Executing
                                                                                 Executing the      the Service
                                                                                 Service
          nu1ModBase          nu1     I            Crypto     u2ModLength + 4    Base of modulus Base of modulus
                                                   RAM                           P               P
          nu1CnsBase          nu1     I            Crypto     u2ModLength + 8    Base of Cns        Base of Cns
                                                   RAM




         © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1514
                                                           SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

          ...........continued
          Parameter              Type Direction Location   Data Length        Before             After Executing
                                                                              Executing the      the Service
                                                                              Service
          u2ModLength            u2   I         –          –                  Length of          Length of
                                                                              modulus P          modulus P
          nu1ABase               u2   I         Crypto     u2ModLength + 4    Parameter a of     Parameter a of
                                                RAM                           the elliptic curve the elliptic curve
          nu1PointABase nu1           I/O       Crypto     3*u2ModLength      Input point A      Resulting point
                                                RAM        + 12               (projective        C (projective
                                                                              coordinates)       coordinates)
          nu1Workspace nu1            I         Crypto     4*u2ModLength      –                  Corrupted
                                                RAM        + 28                                  workspace

43.3.6.4.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;


           PUKCL (u2Option) = 0;

           PUKCL _ZpEccDbl(nu1ModBase) = <Base of the ram location of P>;
           PUKCL _ZpEccDbl(u2ModLength) = <Byte length of P>;
           PUKCL _ZpEccDbl(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL _ZpEccDbl(nu1PointABase) = <Base of the ram location of the A point>;
           PUKCL _ZpEccDbl(nu1ABase) = <Base of the a parameter of the elliptic curve>;
           PUKCL _ZpEccDbl(nu1Workspace) = <Base of the ram location of the workspace>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(ZpEccDblFast,&PUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error

43.3.6.4.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure that the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1ABase, nu1Workspace are not aligned on 32-bit
             boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointABase,
             3*u2ModLength+ 12}, {nu1ABase, u2ModLength + 4}, {nu1Workspace, <WorkspaceLength>} are not
             in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength +8},
             {nu1PointABase, 3*u2ModLength + 12}, {nu1ABase, u2ModLength + 4} and {nu1Workspace,
             4*u2ModLength + 28}




         © 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 1515
                                                               SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

43.3.6.4.7 Status Returned Values

          Returned Status                   Importance      Meaning
          PUKCL_OK                          –               The computation passed without problem.

43.3.6.5 Fast Multiplying by a Scalar Number of a Point
43.3.6.5.1 Purpose
          This service is used to multiply a point by an integral constant K on a given elliptic curve over GF(p).
43.3.6.5.2 How to Use the Service

43.3.6.5.3 Description
          These two services process the Multiplying by a scalar number:
          PtC = K × PtA
          In this computation, the following parameters need to be provided:
           • A the input point is filled in projective coordinates (X,Y,Z) (pointed by {nu1PointABase,
             3*u2ModLength + 12}). This point can be the Infinite Point.
           • Cns the Fast Modular Constant filled (pointed by {nu1CnsBase,u2ModLength +8})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength +4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 8*u2ModLength +44}
           • The a parameter relative to the elliptic curve (pointed by {nu1ABase,u2ModLength +4})
           • K the scalar number (pointed by {nu1ScalarNumber,u2ScalarLength +4})
          The resulting C point is represented in projective coordinates (X,Y,Z) and is stored at the very same place
          than the input point A. This point can be the Infinite Point.
          The service name for this operation is ZpEccMulFast. This service uses Fast mode and Fast Modular
          Reduction for computations.
          Note: Before using this service, ensure that the constant Cns has been calculated with the setup of the
          Fast Modular Reduction service.
43.3.6.5.4 Parameters Definition
          Table 43-73. ZpEccMulFast Service Parameters

          Parameter           Type Direction Location         Data Length         Before              After
                                                                                  Executing the       Executing the
                                                                                  Service             Service
          nu1ModBase          nu1     I            Crypto     u2ModLength + 4     Base of modulus     Base of
                                                   RAM                            P                   modulus P
          nu1CnsBase          nu1     I            Crypto     u2ModLength + 8     Base of Cns         Base of Cns
                                                   RAM
          u2ModLength         u2      I            –          –                   Length of           Length of
                                                                                  modulus P           modulus P
          nu1KBase            nu1     I            Crypto     u2KLength           Scalar number       Unchanged
                                                   RAM                            used to multiply
                                                                                  the point A




         © 2019 Microchip Technology Inc.                         Datasheet                       DS60001507E-page 1516
                                                           SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

          ...........continued
          Parameter              Type Direction Location   Data Length        Before               After
                                                                              Executing the        Executing the
                                                                              Service              Service
          u2KLength              u2    I        –          –                  Length of scalar     Length of scalar
                                                                              K                    K
          nu1PointABase nu1            I/O      Crypto     3*u2ModLength      Input point A        Resulting point
                                                RAM        + 12               (projective          C (projective
                                                                              coordinates)         coordinates)
          nu1ABas                nu1   I        Crypto     u2ModLength + 4    Parameter a of       Unchanged
                                                RAM                           the elliptic curve
          nu1Workspace nu1             I        Crypto     8*u2ModLength      –                    Corrupted
                                                RAM        + 44                                    workspace

43.3.6.5.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;


           PUKCL (u2Option) = 0;

           PUKCL _ZpEccMul(nu1ModBase) = <Base of the ram location of P>;
           PUKCL _ZpEccMul(u2ModLength) = <Byte length of P>;
           PUKCL _ZpEccMul(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL _ZpEccMul(nu1PointABase) = <Base of the ram location of the A point>;
           PUKCL _ZpEccMul(nu1ABase) = <Base of the ram location of the parameter A of the elliptic
           curve>;
           PUKCL _ZpEccMul(nu1KBase) = <Base of the ram location of the scalar number>;
           PUKCL _ZpEccMul(nu1Workspace) = <Base of the ram location of the workspace>;
           PUKCL_ZpEccMul(u2KLength) = <Byte length of the Scalar Number K>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(ZpEccMulFast,&PUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error

43.3.6.5.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure that the service works correctly:
           • nu1ModBase,nu1CnsBase, nu1PointABase, nu1ABase, nu1ScalarNumber, nu1Workspace are not
             aligned on 32-bit boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointABase,
             3*u2ModLength+ 12}, {nu1ABase, u2ModLength + 4}, {nu1ScalarNumber, u2ScalarLength} or
             {nu1Workspace, 8*u2ModLength + 44} are not in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength +8},
             {nu1PointABase, 3*u2ModLength + 12}, {nu1ABase, u2ModLength + 4}, {nu1ScalarNumber,
             u2ScalarLength} and {nu1Workspace, 8*u2ModLength + 44}




         © 2019 Microchip Technology Inc.                      Datasheet                       DS60001507E-page 1517
                                                             SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

43.3.6.5.7 Status Returned Values

          Returned Status                   Importance   Meaning
          PUKCL_OK                          –            The computation passed without problem.

43.3.6.6 Quick Dual Multiplying by Two Scalar Numbers and Two Points
43.3.6.6.1 Purpose
          This service is used to multiply two points by two integral constants K1 and K2, and then provide the
          addition of these multiplications results.


                         Important: This service has a quick implementation without additional security.




43.3.6.6.2 How to Use the Service

43.3.6.6.3 Description
          This service processes the dual Multiplying by two scalar numbers:

          PtC = K1 × PtA + K2 × PtB
          In this computation, the following parameters need to be provided:
           • A the first input point is filled in projective coordinates (X,Y,Z) (pointed by {pu1PointABase,
             (3*(u2ModLength + 4)) * (2(WA-2))}). This point can be the Infinite Point.
           • B the 2nd input point is filled in projective coordinates (X,Y,Z) (pointed by {pu1PointBBase,
             (3*(u2ModLength + 4)) * (2(WB-2))}). This point can be the Infinite Point.
           • P the modulus filled and Cns the Fast Modular Constant filled (pointed by {pu1ModCnsBase,
             2*u2ModLength + 16})
           • The a parameter filled and the workspace not initialized (pointed by {pu1AWorkBase,
             9*u2ModLength +48}
           • KAB the scalar numbers (pointed by {pu1KABBase, 2*u2KLength +8})
           • The options are set by the u2Options input parameter, which is composed of:
               – wA: Size of window for Point A between 2 and15
               – wB: Size of window for Point B between 2 and15
               – PUKCL_ZPECCMUL_SCAL_IN_CLASSIC_RAM flag: to set only if the scalars are entirely in
                  Classic RAM with no part in PUKCC RAM
          The resulting C point is represented in projective coordinates (X,Y,Z) and is stored at (pu1AWorkBase +
          u2ModLength + 4). This point can be the Infinite Point.


                         Important: Before using this service, ensure that the constant Cns has been calculated with
                         the setup of the Fast Modular Reduction service.



43.3.6.6.4 Parameters Definition
          WA is the Point A window size and WB is the Point B window size (see Options below for details).




         © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1518
                                                             SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

                        Important: Please calculate precisely the length of areas with the formulas. Ensure that the
                        pu1 type is a pointer on 4 bytes and contains the full address (see 43.3.3.4 Aligned Significant
                        Length ).


         Table 43-74. ZpEccQuickDualMulFast Service Parameters

          Parameter             Type Direction Location      Data Length             Before              After Executing
                                                                                     Executing the       the Service
                                                                                     Service
          pu1ModCnsBase pu1             I       Crypto       2 * u2ModLength         Base of             Base of modulus
                                                RAM          + 16                    modulus P,          P, Base of Cns
                                                                                     Base of Cns
          u2Option              u2      I       –            –                       Option related      –
                                                                                     to the called
                                                                                     service (see
                                                                                     below)
          u2ModLength           u2      I       –            –                       Length of           Length of
                                                                                     modulus P           modulus P
          pu1KABBase            pu1     I       Any RAM      2 * u2KLength + 8       Scalar              Unchanged
                                                                                     numbers used
                                                                                     to multiply the
                                                                                     points A and B
          u2KLength             u2      I       –            –                       Length of      Length of scalars
                                                                                     scalars KA and KA and KB
                                                                                     KB
          pu1PointABase         pu1     I/O     Crypto       (3*(u2ModLength         Input point A       Unchanged
                                                RAM          + 4)) * (2(WA-2)) (1)   (projective
                                                                                     coordinates)
          pu1PointBBase         pu1     I       Crypto       (3*(u2ModLength         Input point B       Unchanged
                                                RAM          + 4)) * (2(WB-2)) (2)   (projective
                                                                                     coordinates)
          pu1AWorkBase          pu1     I       Crypto       9*u2ModLength           Parameter a of Resulting point C
                                                RAM          + 48                    the elliptic   (projective
                                                                                     curve          coordinates) in
                                                                                                    pu1AWorkBase
                                                                                                    Base +
                                                                                                    u2ModLength + 4

         Note:
          1. The precalculus table size for the point A is calculated from chosen window size “WA”.
          2. The precalculus table size for the point B is calculated from chosen window size “WB”.
43.3.6.6.5 Options
         The options are set by the u2Options input parameter, which is composed of:
           • the mandatory windows sizes WA and WB




         © 2019 Microchip Technology Inc.                        Datasheet                             DS60001507E-page 1519
                                                  SAM D5x/E5x Family Data Sheet
                                                 Public Key Cryptography Controller (PUKCC)

  • the indication of the presence of the scalars in system RAM
Note: Please check precisely if one part of the scalars is in Crypto RAM. If this is the case, the
PUKCL_ZPECCMUL_SCAL_IN_CLASSIC_RAM option must not be used.
The u2Options number is calculated by an “Inclusive OR” of the options. Some Examples in C language
are:
  • // Scalars are in system RAM
    // The Point A window size is 3
     // The Point B window size is 4
     PUKCL(u2Options) = PUKCL_ZPECCMUL_SCAL_IN_CLASSIC_RAM |
     PUKCL_ZPECCMUL_WINSIZE_A_VAL_TO_OPT(3) |
     PUKCL_ZPECCMUL_WINSIZE_B_VAL_TO_OPT(4);
  • // Scalars are in the PUKCC Cryptographic RAM
    // The Point A window size is 2
     // The Point B window size is 5
     PUKCL(u2Options) = PUKCL_ZPECCMUL_WINSIZE_A_VAL_TO_OPT(2) |
     PUKCL_ZPECCMUL_WINSIZE_B_VAL_TO_OPT(5);
For this service, many window sizes are possible. The window sizes in bits are those of the windowing
method used for the scalar multiplying.
The choice of the window sizes is a balance between the size of the parameters and the computation
time:
  • Increasing the window size increases the precomputation table size.
  • Increasing the window size to the optimum reduces the computation time.
The following table details the size of the point and the precomputation table, depending on the chosen
window size option.
Table 43-75. ZpEccQuickDualMulFast Service Window Size Options and Precomputation Table
Size

 Option Specified                                                      Size of the Point and the
                                                                       Precomputation Table
 PUKCL_ZPECCMUL_WINSIZE_A_VAL_TO_OPT(WA) WA in [2,                     (3*(u2ModLength + 4)) * (2(WA-2))
 15]
 PUKCL_ZPECCMUL_WINSIZE_B_VAL_TO_OPT(WB) WB in [2,                     (3*(u2ModLength + 4)) * (2(WB-2))
 15]

The scalars can be located in PUKCC RAM or in system RAM. If both scalars are entirely in system RAM
with no part in PUKCC RAM this can be signaled by using the option
PUKCL_ZPECCMUL_SCAL_IN_CLASSIC_RAM. In all other cases this option must not be used.
The following table describes this option.




© 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1520
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

          Table 43-76. ZpEccQuickDualMulFast Service System RAM Scalar Options

          Option                                             Purpose
          PUKCL_ZPECCMUL_SCAL_IN_CLASSIC_RAM The scalars can be located in Crypto RAM or in
                                             system RAM.
                                                             If both scalars are entirely in system RAM with no
                                                             part in Crypto RAM this can be signaled by using this
                                                             option . In all other cases this option must not be
                                                             used.

43.3.6.6.6 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           PUKCL(u2Option) = <Configure scalar numbers location and windows sizes>;
           PUKCL_ZpEccQuickDualMulFast(pu1ModCnsBase) = <Base of the ram location of P and Cns>;
           PUKCL_ZpEccQuickDualMulFast(u2ModLength) = <Byte length of P>;
           PUKCL_ZpEccQuickDualMulFast(u2KLength) = <Byte length of scalars>;
           PUKCL_ZpEccQuickDualMulFast(pu1PointABase) = <Base of the ram location of the A point>;
           PUKCL_ZpEccQuickDualMulFast(pu1PointBBase) = <Base of the ram location of the B point>;
           PUKCL_ZpEccQuickDualMulFast(pu1AWorkBase) = <Base of the ram location of the parameter A of
           the elliptic curve and workspace>;
           PUKCL_ZpEccQuickDualMulFast(pu1KABBase) = <Base of the ram location of the scalar numbers KA
           and KB>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(ZpEccQuickDualMulFast, pvPUKCLParam);
           if (PUKCL(u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error

43.3.6.6.7 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure that the service works correctly:
           • pu1ModCnsBase,pu1PointABase, pu1PointBBase, pu1AWorkBase, pu1KABBase are not aligned on
             32-bit boundaries
           • {pu1ModCnsBase, 2*u2ModLength + 16}, {pu1PointABase, (3*(u2ModLength + 4)) *(2(WA-2))},
             {pu1PointBBase, (3*(u2ModLength + 4)) * (2(WB-2))} or { pu1AWorkBase, 9*u2ModLength + 48} are
             not in PUKCC RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • Alloverlapping between {pu1ModCnsBase, 2*u2ModLength + 16}, {pu1PointABase,
             (3*(u2ModLength + 4)) * (2(WA-2))}, {pu1PointBBase, (3*(u2ModLength + 4)) * (2(WB-2))} or
             {pu1AWorkBase, 9*u2ModLength + 48}.
43.3.6.6.8 Parameters Placement
          The parameters’ placement is described in the following figures.




         © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1521
                                             SAM D5x/E5x Family Data Sheet
                                            Public Key Cryptography Controller (PUKCC)

Figure 43-7. Modulus P and Cns{pu1ModCnsBase, 2*u2ModLength + 16}




Figure 43-8. Points A and B {pu1PointABase, [(3*(u2ModLength + 4)) * (2(WA-2))] Or
[(3*(u2ModLength + 4)) * (2(WB-2))]}




© 2019 Microchip Technology Inc.               Datasheet                      DS60001507E-page 1522
                                          SAM D5x/E5x Family Data Sheet
                                         Public Key Cryptography Controller (PUKCC)

Figure 43-9. Scalars KA and KB {pu1KABBase, 2 * u2KLength + 8}




Figure 43-10. The a parameter and Workspace {pu1AWorkBase, 9*u2ModLength + 48}




© 2019 Microchip Technology Inc.            Datasheet                  DS60001507E-page 1523
                                                                      SAM D5x/E5x Family Data Sheet
                                                                      Public Key Cryptography Controller (PUKCC)

43.3.6.6.9 Status Returned Values

          Returned Status                   Importance           Meaning
          PUKCL_OK                          –                    The computation passed without problem.

43.3.6.7 Projective to Affine Coordinates Conversion
43.3.6.7.1 Purpose
          This service is used to perform a point coordinates conversion from projective representation to affine.
43.3.6.7.2 How to Use the Service

43.3.6.7.3 Description
          The operation performed is:

                                          ���Pr�������� ����������
          ��� ������ ���������� =
                                      ��� Pr�������� ���������� 2

                                          ��� Pr�������� ����������
          ��� ������ ���������� =
                                      ��� Pr�������� ���������� 3

          In this computation, the following parameters need to be provided:
           • A the input point is filled in projective coordinates (X,Y,Z) or affine coordinates for X and Y, and
             setting Z to 1(pointed by {nu1PointABase,3*u2ModLength + 12}). The Point A can be the point at
             infinity. In this case, the u2Status returned is PUKCL_POINT_AT_INFINITY.
           • Cns the Fast Modular Constant filled (pointed by {nu1CnsBase,u2ModLength +8})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength +4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 4*u2ModLength +48}
          The result is the point A with its (X,Y) coordinates converted to affine, and the Z coordinate set to 1. The
          service for this operation is ZpEcConvProjToAffine.


                         Important: Before using this service, ensure that the constant Cns has been calculated with
                         the Setup of the fast Modular Reductions service.



43.3.6.7.4 Parameters Definition
          Table 43-77. ZpEccConvAffineToProjective Service Parameters

          Parameter           Type Direction Location                 Data Length       Before        After Executing
                                                                                        Executing the the Service
                                                                                        Service
          nu1ModBase          nu1     I              Crypto           u2ModLength + 4   Base of         Base of modulus
                                                     RAM                                modulus P       P
          nu1CnsBase          nu1     I              Crypto           u2ModLength + 8   Base of Cns     Base of Cns
                                                     RAM
          u2ModLength         u2      I              –                –                 Length of       Length of
                                                                                        modulus P       modulus P




         © 2019 Microchip Technology Inc.                                 Datasheet                   DS60001507E-page 1524
                                                              SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

          ...........continued
          Parameter              Type Direction Location      Data Length            Before        After Executing
                                                                                     Executing the the Service
                                                                                     Service
          nu1PointABase nu1           I          Crypto       3*u2ModLength          Input point A     Resulting point A
                                                 RAM          + 12                                     in affine
                                                                                                       coordinates
          nu1Workspace nu1            I          Crypto       4*u2ModLength          –                 Workspace
                                                 RAM          + 48

43.3.6.7.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;


           PUKCL (u2Option) = 0;

           PUKCL _ZpEcConvProjToAffine(nu1ModBase) = <Base of the ram location of P>;
           PUKCL _ZpEcConvProjToAffine(u2ModLength) = <Byte length of P>;
           PUKCL _ZpEcConvProjToAffine(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL _ZpEcConvProjToAffine(nu1PointABase) = <Base of the ram location of the A point>;
           PUKCL _ZpEcConvProjToAffine(nu1Workspace) = <Base of the ram location of the workspace>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(ZpEcConvProjToAffine,&PUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error

43.3.6.7.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure that the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1Workspace are not aligned on 32-bit boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8},{nu1PointABase,
             3*u2ModLength+ 12}, {nu1Workspace, <WorkspaceLength>} are not in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength +8},
          {nu1PointABase, 3*u2ModLength + 12} and {nu1Workspace, 4*u2ModLength + 48}
43.3.6.7.7 Status Returned Values
          Table 43-78. ZpEccConvAffineToProjective Service Return Codes

          Returned Status                    Importance Meaning
          PUKCL_OK                           –             The computation passed without problem.
          PUKCL_POINT_AT_INFINITY Warning                  The input point has its Z equal to zero, so it’s a
                                                           representation of the infinite point.




         © 2019 Microchip Technology Inc.                       Datasheet                            DS60001507E-page 1525
                                                              SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

43.3.6.8 Affine to Projective Coordinates Conversion
43.3.6.8.1 Purpose
          This service is used to perform a point coordinates conversion from an affine point representation to
          projective.
43.3.6.8.2 How to Use the Service

43.3.6.8.3 Description
          The operation performed is:
          affine(Xa, Ya) → projective(Xp, Yp, Zp)
          In this computation, the following parameters need to be provided:
           • A the input point is filled in affine coordinates for X and Y, and setting Z to 1 (pointed by
             {nu1PointABase,3*u2ModLength + 4}).
           • Cns the Fast Modular Constant filled (pointed by {nu1CnsBase,u2ModLength +8})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength +4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 2*u2ModLength +16}
          The result is the point A with its (X,Y,Z) projective coordinates.
          The service for this operation is ZpEcConvAffineToProjective


                         Important: Before using this service, ensure that the constant Cns has been calculated with
                         the setup of the Fast Modular Reductions service.



43.3.6.8.4 Parameters Definition
          Table 43-79. ZpEccConvAffineToProjective Service Parameters

          Parameter           Type Direction Location         Data Length           Before        After Executing
                                                                                    Executing the the Service
                                                                                    Service
          nu1ModBase          nu1     I        Crypto         u2ModLength + 4       Base of           Base of modulus
                                               RAM                                  modulus P         P
          nu1CnsBase          nu1     I        Crypto         u2ModLength + 8       Base of Cns       Base of Cns
                                               RAM
          u2ModLength         u2      I        –              –                     Length of         Length of
                                                                                    modulus P         modulus P
          nu1PointABase nu1           I        Crypto         3*u2ModLength         Input point A     Resulting point A
                                               RAM            + 12                                    in affine
                                                                                                      coordinates
          nu1Workspace nu1            I        Crypto         2*u2ModLength         –                 Workspace
                                               RAM            + 16

43.3.6.8.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;




         © 2019 Microchip Technology Inc.                         Datasheet                         DS60001507E-page 1526
                                                               SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

           PUKCL (u2Option) = 0;

           PUKCL _ZpEcConvAffineToProjective(nu1ModBase) = <Base of the ram location of P>;
           PUKCL _ZpEcConvAffineToProjective(u2ModLength) = <Byte length of P>;
           PUKCL _ZpEcConvAffineToProjective(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL _ZpEcConvAffineToProjective(nu1PointABase) = <Base of the ram location of the A point>;
           PUKCL _ZpEcConvAffineToProjective(nu1Workspace) = <Base of the ram location of the workspace>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(ZpEcConvAffineToProjective,&PUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error


43.3.6.8.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure that the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1Workspace are not aligned on 32-bit boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointABase,
             3*u2ModLength+ 12}, {nu1Workspace, <WorkspaceLength>} are not in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength +8},
             {nu1PointABase, 3*u2ModLength + 12}, and {nu1Workspace, 2*u2ModLength + 16}
43.3.6.8.7 Status Returned Values
          Table 43-80. ZpEccConvAffineToProjective Service Return Codes

          Returned Status                   Importance      Meaning
          PUKCL_OK                          –               The computation passed without problem.

43.3.6.9 Randomize a Coordinate

43.3.6.9.1 Purpose
          This service is used to convert the projective representation of a point to another projective
          representation.
43.3.6.9.2 How to Use the Service

43.3.6.9.3 Description
          The operation performed is:
          Projective(X1, Y1, Z1) → Projective(X2, Y2, Z2)
          In this computation, the following parameters need to be provided:
           • The input point is filled in projective coordinates (X,Y,Z) (pointed by {nu1PointBase,3*u2ModLength
             + 12}). This Point must not be the point at infinity.
           • Cns the Fast Modular Constant filled (pointed by {nu1CnsBase,u2ModLength +8})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength +4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 3*u2ModLength +28}
           • The random number (pointed by {nu1RandomBase, u2ModLength +4}).
          The result is the point nu1PointBase with its (X,Y,Z) coordinates randomized.
          The service for this operation is ZpEcRandomiseCoordinate.




         © 2019 Microchip Technology Inc.                       Datasheet                         DS60001507E-page 1527
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

                        Important: Before using this service:
                         • Ensure that the constant Cns has been calculated with the setup of the Modular Reduction
                           service.
                         • Be sure to follow the directives given for the RNG on the chip you use (particularly
                           initialization, seeding) and compulsorily start the RNG
                        .


43.3.6.9.4 Parameters Definition
          Table 43-81. ZpEccRandomiseCoordinate Service Parameters

          Parameter             Type Direction Location     Data Length          Before        After
                                                                                 Executing the Executing the
                                                                                 Service       Service
          nu1ModBase            nu1     I      Crypto RAM u2ModLength + 4        Base of           Base of
                                                                                 modulus P         modulus P
          nu1CnsBase            nu1     I      Crypto RAM u2ModLength + 8        Base of Cns       Base of Cns
          u2ModLength           u2      I      –            –                    Length of         Length of
                                                                                 modulus P         modulus P
          nu1PointBase          nu1     I      Crypto RAM 3*u2ModLength          Input point       Resulting point
                                                          + 12
          nu1RandomBase nu1             I      Crypto RAM u2ModLength + 4        Random            Corrupted
          nu1Workspace          nu1     I      Crypto RAM 3*u2ModLength          –                 Workspace
                                                          + 28

43.3.6.9.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // ! The Random Number Generator must be initialized and started
           // ! following the directives given for the RNG on the chip

           PUKCL (u2Option) = 0;

           // Depending on the option specified, not all fields should be filled
           PUKCL _ZpEccRandomiseCoordinate(nu1ModBase) = <Base of the ram location of P>;
           PUKCL _ZpEccRandomiseCoordinate(u2ModLength) = <Byte length of P>;
           PUKCL _ZpEccRandomiseCoordinate(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL_ZpEccRandomiseCoordinate(nu1RandomBase) = <Base of the ram location where the the RNG
           is stored>;
           PUKCL _ZpEccRandomiseCoordinate(nu1PointBase) = <Base of the ram location of the point>;
           PUKCL _ZpEccRandomiseCoordinate(nu1Workspace) = <Base of the ram location of the workspace>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(ZpEccRandomiseCoordinate,&PUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error




         © 2019 Microchip Technology Inc.                   Datasheet                          DS60001507E-page 1528
                                                             SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

43.3.6.9.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure that the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1RandomBase, nu1Workspace are not aligned on
             32-bit boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointABase,
             3*u2ModLength + 12}, {nu1RandomBase, u2ModLength + 4}, {nu1Workspace, <WorkspaceLength>}
             are not in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength +8},
             {nu1PointABase, 3*u2ModLength + 12}, {nu1RandomBase, u2ModLength + 4} and {nu1Workspace,
             3*u2ModLength + 28}
43.3.6.9.7 Status Returned Values
          Table 43-82. ZpEccRandomiseCoordinate Service Return Codes

          Returned Status                   Importance    Meaning
          PUKCL_OK                          –             The computation passed without problem.

43.3.6.10 Point is on Elliptic Curve

43.3.6.10.1 Purpose
          This service is used to test whether or not the point is on the curve.
43.3.6.10.2 How to Use the Service

43.3.6.10.3 Description
          The operation performed is:
          Status = IsPointOnCurve(X, Y, Z)
          In this computation, the following parameters need to be provided:
           • The input point is filled in projective coordinates (X,Y,Z) (pointed by {nu1PointBase,3*u2ModLength
             + 4}). This Point can be the point at infinity.
           • AParam and BParam are the Elliptic Curve Equation parameters. (pointed by{nu1AParam,
             u2ModLength+4} and {nu1BParam, u2ModLength+4}).
           • Cns the Fast Modular Constant filled (pointed by{nu1CnsBase,u2ModLength+8}).
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength +4}).
           • The workspace not initialized (pointed by {nu1WorkSpace, 4*u2ModLength +28}.
          The result is the status of the point (X,Y,Z) regarding the Elliptic Curve Equation.
          The service name for this operation is ZpEcPointIsOnCurve.
          Note: Before using this service, ensure that the constant Cns has been calculated with the setup of the
          Fast Modular Reduction service.
43.3.6.10.4 Parameters Definition
          Table 43-83. ZpEcPointIsOnCurve Service Parameters

          Parameter          Type Direction Location        Data Length            Before             After Executing
                                                                                   Executing the      the Service
                                                                                   Service




         © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1529
                                                            SAM D5x/E5x Family Data Sheet
                                                         Public Key Cryptography Controller (PUKCC)

          nu1ModBase         nu1     I      Crypto RAM u2ModLength + 4         Base of          Base of modulus
                                                                               modulus P        P
          nu1CnsBase         nu1     I      Crypto RAM u2ModLength + 8         Base of Cns      Base of Cns
          u2ModLength        u2      I      –           –                      Length of        Length of
                                                                               modulus P        modulus P
          nu1PointBase       nu1     I      Crypto RAM 3*u2ModLength + 12 Input point           unchanged
          nu1AParam          nu1     I      Crypto RAM u2ModLength + 4         The parameter    The parameter a
                                                                               a
          nu1BParam          nu1     I      Crypto RAM u2ModLength + 4         The parameter    The parameter b
                                                                               b
          nu1Workspace nu1           I      Crypto RAM 4*u2ModLength + 28 –                     Workspace

43.3.6.10.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;


           PUKCL (u2Option) = 0;

           PUKCL _ZpEcPointIsOnCurve(nu1ModBase) = <Base of the ram location of P>;
           PUKCL _ZpEcPointIsOnCurve(u2ModLength) = <Byte length of P>;
           PUKCL _ZpEcPointIsOnCurve(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL _ZpEcPointIsOnCurve(nu1AParam) = <Base of the ram location of the parameter a>;
           PUKCL _ZpEcPointIsOnCurve(nu1BParam) = <Base of the ram location of the parameter b>;
           PUKCL _ZpEcPointIsOnCurve(nu1PointBase) = <Base of the ram location of the point>;
           PUKCL _ZpEcPointIsOnCurve(nu1Workspace) = <Base of the ram location of the workspace>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(ZpEcPointIsOnCurve,&PUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error

43.3.6.10.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure that the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1AParam, nu1BParam, nu1Workspace are not
             aligned on 32-bit boundaries
           • {nu1ModBase, u2ModLength+4}, {nu1CnsBase, u2ModLength+8}, {nu1PointABase, 3*u2ModLength
             +12}, {nu1AParam, u2ModLength + 4}, {nu1BParam, u2ModLength + 4}, {nu1Workspace,
             <WorkspaceLength>} are not in Crypto RAM.
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length.
           • All overlapping between {nu1ModBase, u2ModLength+4}, {nu1CnsBase,u2ModLength+8},
             {nu1PointABase, 3*u2ModLength+12}, {nu1AParam, u2ModLength+4}, {nu1AParam, u2ModLength
             + 4} and {nu1Workspace, 4*u2ModLength+28}.




         © 2019 Microchip Technology Inc.                   Datasheet                        DS60001507E-page 1530
                                                            SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

43.3.6.10.7 Status Returned Values
          Table 43-84. ZpEcPointIsOnCurve Service Return Codes

          Returned Status                           Importance Meaning
          PUKCL_OK                                  –             The point is on the curve.
          PUKCL_POINT_IS_NOT_ON_                    Warning       The point is not on the curve.
          CURVE
          PUKCL_POINT_AT_INFINITY                   Warning       The input point has its Z equal to zero, so it’s a
                                                                  representation of the infinite point.

43.3.6.11 Generating an ECDSA Signature (Compliant with FIPS 186-2)

43.3.6.11.1 Purpose
          This service is used to generate an ECDSA signature following the FIPS 186-2. It performs the second
          step of the Signature Generation. A hash value (HashVal) must be provided as input, it has to be
          previously computed from the message to be signed using a secure hash algorithm.
          A scalar number must be provided too as described in the FIPS 186-2. The result (R,S) is computed by
          this service.
43.3.6.11.2 How to Use the Service

43.3.6.11.3 Description
          The operation performed is:

          (R, S) = EcDsaSign(PtA, HashVal, k, CurveParameters, PrivateKey)

          This service processes the following checks:
           • If the Scalar Number k is out of the range [1, PointOrder -1], the calculus is stopped and the status is
             set to PUKCL_WRONG_SELECT_NUMBER.
           • If R equals zero, the calculus is stopped and the status is set to
             PUKCL_WRONG_SELECT_NUMBER.
           • If S equals zero, the calculus is stopped and the status is set to
             PUKCL_WRONG_SELECT_NUMBER.
          In this computation, the following parameters need to be provided:
           • A the input point is filled in “mixed” coordinates (X,Y) with the affine values and Z = 1 (pointed by
             {nu1PointABase,3*u2ModLength + 12})
           • Cns the working space for the Fast Modular Constant not initialized (pointed by
             {nu1CnsBase,u2ScalarLength + 8})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength + 4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 8*u2ModLength + 44}
           • The a parameter relative to the elliptic curve (pointed by {nu1ABase, u2ModLength + 4})
           • The order of the Point A on the elliptic curve (pointed by {nu1OrderPointBase, u2ScalarLength + 4})
           • k the input Scalar Number beforehand generated and filled (pointed
             by{nu1ScalarNumber,u2ScalarLength + 4})
           • HashVal the hash value beforehand generated and filled (pointed by {nu1HashBase, u2ScalarLength
             + 4})
           • The Private Key (pointed by {nu1PrivateKey, u2ScalarLength +4})




         © 2019 Microchip Technology Inc.                     Datasheet                            DS60001507E-page 1531
                                                    SAM D5x/E5x Family Data Sheet
                                                   Public Key Cryptography Controller (PUKCC)

  • Generally, u2ScalarLength is equal to (u2ModLength) or (u2ModLength + 4)


               Important:
               For the ECDSA signature generation be sure to follow the directives given for the RNG on the
               chip you use (particularly initialization, seeding) and compulsorily start the RNG.
               The scalar number k must be selected at random. This random must be generated before the
               call of the ECDSA signature. For this random generation be sure to follow the directives given
               for the RNG on the chip you use (particularly initialization, seeding) and compulsorily start the
               RNG.


The operation performed is:
  • Compute the ECDSA (R,S) as described in FIPS 186-2, but leaving the user the role of computing
    the input Hash Value, thus leaving the freedom of using any other algorithm than SHA-1.
  • Compute a R value using the input A point and the scalar number.
  • Compute a S value using R, the scalar number, the private key and the provided hash value. Note
    that the resulting signature (R,S) is stored at the place of the input A point.
  • If all is correct and S is different from zero, the status is set to PUKCL_OK. If all is correct and S
    equals zero,the status is set to PUKCL_WRONG_SELECT_NUMBER. If an error occurs, the status
    is set to the corresponding error value (see Status Returned Values below).
The service name for this operation is ZpEcDsaGenerateFast. This service uses Fast mode and Fast
Modular Reduction for computation.
  • The signature (R,S), when resulting from a computation is given back at address of the A point:
     – R output is at offset 0 and has length (u2ScalarLength + 4)bytes.
     – S output is at offset (u2ScalarLength + 4) bytes and has length (u2ScalarLength + 4) bytes.
     – The MSB 4 zero bytes may be suppressed to get the R and S values on u2ScalarLength bytes




© 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1532
                                                             SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

43.3.6.11.4 Parameters Definition
          Table 43-85. ZpEcDsaGenerateFast Service Parameters

          Parameter                  Type Direction Location     Data Length      Before             After
                                                                                  Executing the      Executing
                                                                                  Service            the Service
          nu1ModBase                 nu1    I       Crypto       u2ModLength + 4 Base of             Base of
                                                    RAM                          modulus P           modulus P
          nu1CnsBase                 nu1    I       Crypto       u2ScalarLength   Base of Cns        Base of Cns
                                                    RAM          +8
          u2ModLength                u2     I       –            –                Length of          Length of
                                                                                  modulus P          modulus P
          nu1ScalarNumber            nu1    I       Crypto       u2ScalarLength   Scalar Number Unchanged
                                                    RAM          +4               used to multiply
                                                                                  the point A
          nu1OrderPointBase          nu1    I       Crypto       u2ScalarLength   Order of the       Unchanged
                                                    RAM          +4               Point A in the
                                                                                  elliptic curve
          nu1PrivateKey              nu1    I/O     Crypto       u2ScalarLength   Base of the        Unchanged
                                                    RAM          +4               Private Key
          nu1HashBase (see           nu1    I       Crypto       u2ScalarLength   Base of the        Unchanged
          Note 1)                                   RAM          +4               hash value
                                                                                  resulting from
                                                                                  the previous
                                                                                  SHA
          u2ScalarLength             u2     I       –            –                Length of scalar Length of
                                                                                  (same length as scalar
                                                                                  the length of
                                                                                  order)
          nu1PointABase (see nu1            I/O     Crypto       3*u2ModLength    Input point A      Resulting
          Note 2)                                   RAM          + 12             (three             signature
                                                                                  coordinates        (R,S,0)
                                                                                  (X,Y) affine and
                                                                                  Z = 1)
          nu1ABase                   nu1    I       Crypto       u2ModLength + 4 Parameter a of Unchanged
                                                    RAM                          the elliptic curve
          nu1Workspace               nu1    I       Crypto       8*u2ModLength    –                  Corrupted
                                                    RAM          + 44                                workspace

          Note:
           1. The hash value calculus is defined by the ECDSA norm and depends on the elliptic curve domain
                parameters. To construct the input parameter, the 4 Most Significant Bytes must be set to zero.
           2. The resulting signature format is different from the point A format (see Description above for
                information on the point A format).




         © 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 1533
                                                          SAM D5x/E5x Family Data Sheet
                                                         Public Key Cryptography Controller (PUKCC)

43.3.6.11.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // ! The Random Number Generator must be initialized and started
           // ! following the directives given for the RNG on the chip


           PUKCL (u2Option) = 0;

           // Depending on the option specified, not all fields should be filled PUKCL
           _ZpEcDsaGenerate(nu1ModBase) = <Base of the ram location of P>; PUKCL
           _ZpEcDsaGenerate(u2ModLength) = <Byte length of P>;
           PUKCL _ZpEcDsaGenerate(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL _ZpEcDsaGenerate(nu1PointABase) = <Base of the A point>;
           PUKCL _ZpEcDsaGenerate(nu1PrivateKey) = <Base of the Private Key>;
           PUKCL _ZpEcDsaGenerate(nu1ScalarNumber) = <Base of the ScalarNumber>;
           PUKCL _ZpEcDsaGenerate(nu1OrderPointBase) = <Base of the order of A point>;
           PUKCL _ZpEcDsaGenerate(nu1ABase) = <Base of the a parameter of the curve>;
           PUKCL _ZpEcDsaGenerate(nu1Workspace) = <Base of the workspace>;
           PUKCL _ZpEcDsaGenerate(nu1HashBase) = <Base of the SHA resulting hash>;
           PUKCL_ZpEcDsaGenerate(u2ScalarLength)    = < Length of ScalarNumber>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(ZpEcDsaGenerateFast, pvPUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error

43.3.6.11.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure that the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1PrivateKey, nu1ScalarNumber,
             nu1OrderPointBase,nu1ABase, nu1Workspace or nu1HashBase are not aligned on 32-bit
             boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointABase,
             3*u2ModLength+ 12},{nu1PrivateKey, u2ScalarLength + 4},{nu1ScalarNumber, u2ScalarLength + 4},
             {nu1OrderPointBase, u2ScalarLength + 4}, {nu1ABase, u2ModLength + 4}, {nu1Workspace,
             <WorkspaceLength>} or {nu1HashBase, u2ScalarLength + 4} are not in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength +8},
             {nu1PointABase, 3*u2ModLength + 12}, {nu1PrivateKey, u2ScalarLength + 4}, {nu1ScalarNumber,
             u2ScalarLength + 4}, {nu1OrderPointBase, u2ScalarLength + 4}, {nu1ABase, u2ModLength + 4},
             {nu1Workspace, <WorkspaceLength>} and {nu1HashBase, u2ScalarLength + 4}
43.3.6.11.7 Status Returned Values
          Table 43-86. ZpEcDsaGenerateFast Service Return Codes

          Returned Status                        Importance Meaning
          PUKCL_OK                               –            The computation passed without problem. The
                                                              signature is the good one.
          PUKCL_WRONG_SELECTNUMBER Warning                    The given value for nu1ScalarNumber is not good
                                                              to perform this signature generation.




         © 2019 Microchip Technology Inc.                   Datasheet                        DS60001507E-page 1534
                                                            SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

43.3.6.12 Verifying an ECDSA Signature (Compliant with FIPS186-2)
43.3.6.12.1 Purpose
          This service is used to verify an ECDSA signature following the FIPS 186-2. It performs the second step
          of the Signature Verification.
          A hash value (HashVal) must be provided as input, it has to be previously computed from the message to
          be signed using a secure hash algorithm.
          As second significant input, the Signature is provided to be checked. This service checks the signature
          and fills the status accordingly.
43.3.6.12.2 How to Use the Service

43.3.6.12.3 Description
          The operation performed is:
          Verify = EcDsaVerifySignature(PtA, HashVal, Signature, CurveParameters, PublicKey)
          The points used for this operation are represented in different coordinate systems. In this computation,
          the following parameters need to be provided:
           • A the input point is filled with the affine values (X,Y) and Z = 1 (pointed by{nu1PointABase,
             3*u2ModLength + 12})
           • Cns the working space for the Fast Modular Constant not initialized (pointed by
             {nu1CnsBase,u2ScalarLength + 8})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength + 4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 8*u2ModLength + 44}
           • The a parameter relative to the elliptic curve (pointed by {nu1ABase,u2ModLength + 4})
           • The order of the Point A on the elliptic curve (pointed by {nu1OrderPointBase,u2ScalarLength + 4})
           • HashVal the hash value is generated prior and filled (pointed by {nu1HashBase,u2ScalarLength + 4})
           • The Public Key point is filled in “mixed” coordinates (X,Y) with the affine values and Z = 1 (pointed by
             {nu1PointPublicKeyGen, 3*u2ModLength + 12})
           • The input signature (R,S), even if it is not a Point, is represented in memory like a point in affine
             coordinates (X,Y) (pointed by {nu1PointSignature, 2*u2ScalarLength + 8})
             Note: For the ECDSA signature verification be sure to follow the directives given for the RNG on the
             chip you use (particularly initialization, seeding) and compulsorily start the RNG.
           • The operation consists in obtaining a V value with all these input parameters and checking that V
             equals the provided R. If all is correct and the signature is the good one, the status is set to
             PUKCL_OK. If all is correct and the signature is wrong, the status is set to
             PUKCL_WRONG_SIGNATURE. If an error occurs, the status is set to the corresponding error value
             (see Status Returned Values below).
43.3.6.12.4 Parameters Definition
          Table 43-87. ZpEcDsaVerifyFast Service Parameters

          Parameter                     Type Direction Location     Data Length         Before         After
                                                                                        Executing      Executing
                                                                                        the Service    the Service
          nu1ModBase                    nu1   I        Crypto       u2ModLength + 4     Base of        Base of
                                                       RAM                              modulus P      modulus P




         © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 1535
                                                          SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

         ...........continued
          Parameter                    Type Direction Location     Data Length        Before            After
                                                                                      Executing         Executing
                                                                                      the Service       the Service
          nu1CnsBase                   nu1   I        Crypto       u2ScalarLength     Base of Cns       Base of Cns
                                                      RAM          + 12
          u2ModLength                  u2    I        –            –                  Length of         Length of
                                                                                      modulus P         modulus P
          nu1OrderPointBase            nu1   I        Crypto       u2ScalarLength     Order of the Unchanged
                                                      RAM          +4                 Point A in the
                                                                                      elliptic curve
          nu1PointSignature            nu1   I        Crypto       2*u2ScalarLength   Signature(r,      Corrupted
                                                      RAM          +8                 s)
          nu1HashBase (see             nu1   I        Crypto       u2ScalarLength     Base of the    Corrupted
          Note 1)                                     RAM          +4                 hash value
                                                                                      resulting from
                                                                                      the previous
                                                                                      SHA
          u2ScalarLength               u2    I        –            –                  Length of         Length of
                                                                                      scalar            scalar
          nu1PointABase                nu1   I/O      Crypto       3*u2ModLength      Generator         Corrupted
                                                      RAM          + 12               point
          nu1PointPublicKeyGen         nu1   I/O      Crypto       3*u2ModLength      Public point      Corrupted
                                                      RAM          + 12
          nu1ABase                     nu1   I        Crypto       u2ModLength + 4    Parameter a       Unchanged
                                                      RAM                             of the elliptic
                                                                                      curve
          nu1Workspace                 nu1   I        Crypto       8*u2ModLength      –                 Corrupted
                                                      RAM          + 44                                 workspace

         Note:
          1. The hash value calculus is defined by the ECDSA norm and depends on the elliptic curve domain
               parameters. To construct the input parameter, the 4 Most Significant Bytes must be set to zero.
43.3.6.12.5 Code Example
          PUKCL_PARAM PUKCLParam;
          PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

          // ! The Random Number Generator must be initialized and started
          // ! following the directives given for the RNG on the chip

          PUKCL(u2Option) = 0;

          // Depending on the option specified, not all fields should be filled
          PUKCL_ZpEcDsaVerify(nu1ModBase) = <Base of the ram location of P>;
          PUKCL_ZpEcDsaVerify(u2ModLength) = <Byte length of P>;
          PUKCL_ZpEcDsaVerify(nu1CnsBase) = <Base of the ram location of Cns>;
          PUKCL_ZpEcDsaVerify(nu1PointABase) = <Base of the A point>;
          PUKCL_ZpEcDsaVerify(nu1PrivateKey) = <Base of the Private Key>;




        © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 1536
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

           PUKCL_ZpEcDsaVerify(nu1ScalarNumber) = <Base of the ScalarNumber>;
           PUKCL_ZpEcDsaVerify(nu1OrderPointBase) = <Base of the order of A point>;
           PUKCL_ZpEcDsaVerify(nu1ABase) = <Base of the a parameter of the curve>;
           PUKCL_ZpEcDsaVerify(nu1Workspace) = <Base of the workspace>;
           PUKCL_ZpEcDsaVerify(nu1HashBase) = <Base of the SHA resulting hash>;
            PUKCL_ZpEcDsaVerify(u2ScalarLength)    = < Length of ScalarNumber>;

           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(ZpEcDsaVerifyFast, pvPUKCLParam);
           if (PUKCL(u2Status) == PUKCL_OK)
                       {
                       ...
                       }ou
           else
                       if(PUKCL(u2Status) == PUKCL_WRONG_SIGNATURE)
                                   {
                                   ...
                                   }
                       else // Manage the error


43.3.6.12.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure that the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1PointPublicKeyGen, nu1PointSignature,
             nu1OrderPointBase,nu1ABase, nu1Workspace or nu1HashBase are not aligned on 32-bit
             boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointABase,
             3*u2ModLength+ 12}, {nu1PointPublicKeyGen, 3*u2ModLength + 12}, {nu1PointSignature,
             2*u2ScalarLength + 8}, {nu1OrderPointBase, u2ScalarLength + 4}, {nu1ABase, u2ModLength + 4},
             {nu1Workspace, <WorkspaceLength>} or {nu1HashBase, u2ScalarLength + 4} are not in Crypto
             RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength +8},
             {nu1PointABase, 3*u2ModLength + 12}, {nu1PointPublicKeyGen, 3*u2ModLength + 12},
             {nu1PointSignature, 2*u2ScalarLength + 8}, {nu1OrderPointBase, u2ScalarLength + 4}, {nu1ABase,
             u2ModLength + 4}, {nu1Workspace, <WorkspaceLength>} and {nu1HashBase, u2ScalarLength + 4}
43.3.6.12.7 Status Returned Values
          Table 43-88. ZpEcDsaVerifyFast Service Return Codes

          Returned Status                   Importance Meaning
          PUKCL_OK                          –             The computation passed without problem. The signature
                                                          is the good one.
          PUKCL_WRONG_SIGNATURE Warning                   The signature is wrong.

43.3.6.13 Quick Verifying an ECDSA Signature (Compliant with FIPS 186-2)

43.3.6.13.1 Purpose
          This service is used to verify an ECDSA signature following the FIPS 186-2. It performs the second step
          of the Signature Verification using Quick Dual Multiplying to perform computation.
          A hash value (HashVal) must be provided as input, it has to be previously computed from the message
          whose signature is verified using a secure hash algorithm.
          As second significant input, the Signature is provided to be checked.




         © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1537
                                                              SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

          This service checks the signature and fills the status accordingly.


                          Important: This service has a quick implementation without additional security.




43.3.6.13.2 How to Use the Service

43.3.6.13.3 Description
          The operation performed is:
          Verify = EcDsaVerifySignature(PtA, HashVal, Signature, CurveParameters, PublicKey)
          The points used for this operation are represented in different coordinate systems.
          In this computation, the following parameters need to be provided (such that u2MaxLength =
          max(u2ModLength, u2ScalarLength)):
           • A the input point is filled with the affine values (X,Y) and Z = 1 (pointed by {pu1PointABase,
             (3*(u2ModLength + 4)) * (2(WA-2))})
           • P the modulus filled and Cns the working space for the Fast Modular Constant not initialized (pointed
             by {pu1ModBase, u2ModLength + u2MaxLength + 16})
           • The a parameter relative to the elliptic curve filled and workspace not initialized (pointed by
             {pu1AWorkBase,8*u2MaxLength + u2ModLength + 48})
           • The order of the Point A on the elliptic curve (pointed by {pu1OrderPointBase,u2ScalarLength +4})
           • HashVal the hash value beforehand generated and filled (pointed by {pu1HashBase,u2MaxLength
             +4})
           • The Public Key point is filled in “mixed” coordinates (X,Y) with the affine values and Z = 1 (pointed by
             {nu1PointPublicKeyGen, (3*(u2ModLength + 4)) * (2(WB-2))})
           • The input signature (R,S), even if it is not a Point, is represented in memory like a point in affine
             coordinates (X,Y) (pointed by {nu1PointSignature, 2*u2ScalarLength + 8})
          The operation consists of obtaining a V value with all input parameters and checks that V equals the
          provided R. If all is correct and the signature is the good one, the status is set to PUKCL_OK. If all is
          correct and the signature is wrong, the status is set to PUKCL_WRONG_SIGNATURE. If an error occurs,
          the status is set to the corresponding error value (see Status Returned Values below).
43.3.6.13.4 Parameters Definition
          To place the parameters correctly the maximum of u2ModLength and u2ScalarLength must be calculated:
          u2MaxLength = max(u2ModLength, u2ScalarLength)
          WA is the Point A window size and WB is the Point Public Key window size (see Options below for
          details).


                          Important: Please calculate precisely the length of areas with the formulas and the max()
                          service which takes the maximum of two values. Ensure that the pu1 type is a pointer on 4
                          bytes and contains the full address (see 43.3.3.4 Aligned Significant Length for details).




         © 2019 Microchip Technology Inc.                      Datasheet                         DS60001507E-page 1538
                                                  SAM D5x/E5x Family Data Sheet
                                                  Public Key Cryptography Controller (PUKCC)

Table 43-89. ZpEcDsaQuickVerify Service Parameters

 Parameter                     Type Direction Location    Data Length         Before         After
                                                                              Executing      Executing
                                                                              the Service    the Service
 pu1ModCnsBase                 pu1   I        Crypto      u2ModLength + 4 + Base of          Base of
                                              RAM         u2MaxLength + 12 modulus P         modulus P

 u2Option                      u2    I        –           –                   Option         –
                                                                              related to the
                                                                              called service
                                                                              (see below)
 u2ModLength                   u2    I        –           –                   Length of      Length of
                                                                              modulus P      modulus P
 pu1OrderPointBase             pu1   I        Crypto      u2ScalarLength      Order of the   Unchanged
                                              RAM         +4                  Point A in the
                                                                              elliptic curve
 pu1PointSignature             pu1   I        Any RAM 2*u2ScalarLength        Signature(r,   Corrupted
                                                      +8                      s)
 pu1HashBase (see              pu1   I        Crypto      u2MaxLength + 4     Base of the    Corrupted
 Note 1)                                      RAM                             hash value
                                                                              resulting from
                                                                              the previous
                                                                              SHA
 u2ScalarLength                u2    I        –           –                   Length of      Length of
                                                                              scalar         scalar
 pu1PointABase                 pu1   I/O      Crypto      (3*u2ModLength      Generator      Corrupted
                                              RAM         + 12) * (2(WA-2))   point

 pu1PointPublicKeyGen pu1            I/O      Crypto      (3*u2ModLength      Public Key     Corrupted
                                              RAM         + 12) * (2(WB-2))   point

 pu1AWorkBase                  pu1   I        Crypto      (u2ModLength + 4) Parameter a      Corrupted
                                              RAM         + (8*u2MaxLength of the elliptic
                                                          + 44)             curve and
                                                                            Workspace

Note:
 1. 1. The hash value calculus is defined by the ECDSA norm and depends on the elliptic curve
      domain parameters. To construct the input parameter, the 4 Most Significant Bytes must be set to
      zero.
A suggested parameters placement in Crypto RAM is:
  •   ModCnsBase
  •   OrderPointBase
  •   Signature may be placed here or in Classical RAM
  •   HashBase




© 2019 Microchip Technology Inc.                       Datasheet                      DS60001507E-page 1539
                                                            SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

           • PointABase
           • PointPublicKeyGen
           • AWorkBase
43.3.6.13.5 Options
         The options are set by the u2Options input parameter, which is composed of:
           • the mandatory windows sizes WA (window for Point A) and WB (window for Point Public Key)
           • the indication of the presence of the Point Signature in system RAM


                        Important: Please check precisely if the Point Signature is in Crypto RAM. If this is the case
                        the PUKCL_ZPECCMUL_SCAL_IN_CLASSIC_RAM must not be used.


         The u2Options number is calculated by an “Inclusive OR” of the options. Some Examples in C language
         are:
           • // Point Signature in system RAM
             // The Point A window size is 3
              // The Point Public Key window size is 4
              PUKCL(u2Options) = PUKCL_ZPECCMUL_SCAL_IN_CLASSIC_RAM |
              PUKCL_ZPECCMUL_WINSIZE_A_VAL_TO_OPT(3) |
              PUKCL_ZPECCMUL_WINSIZE_B_VAL_TO_OPT(4);
           • // Point Signature in the Cryptographic RAM
             // The Point A window size is 2
              // The Point Public Key window size is 5
              PUKCL(u2Options) = PUKCL_ZPECCMUL_WINSIZE_A_VAL_TO_OPT(2) |
              PUKCL_ZPECCMUL_WINSIZE_B_VAL_TO_OPT(5);
         For this service, many window sizes are possible. The window sizes in bits are those of the windowing
         method used for the scalar multiplying.
         The choice of the window sizes is a balance between the size of the parameters and the computation
         time:
           • Increasing the window size increases the precomputation table size.
           • Increasing the window size to the optimum reduces the computation time.
         The following table details the estimated windows WA and WB optimum and possible for some curves.
         Table 43-90. ZpEcDsaQuickVerify Service Estimated WA and WB Window Size

          Curve Size (bits)        Optimum Window size       Possible Window Sizes (WA, WB) or (WB, WA)
          192                      5                         5, 5
          256                      5                         5, 5
          384                      6                         5, 5
          521                      6                         4, 5




         © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1540
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

          The following table details the size of the point and the precomputation table, depending on the chosen
          window size option.
          Table 43-91. ZpEcDsaQuickVerify Service Window Size and Precomputation Table Size Options

          Option Specified                                                       Point and Precomputation
                                                                                 Table Size
          PUKCL_ZPECCMUL_WINSIZE_A_VAL_TO_OPT(WA) WA in [2, 15] (3*(u2ModLength + 4)) * (2(WA-2))
          PUKCL_ZPECCMUL_WINSIZE_B_VAL_TO_OPT(WB) WB in [2,                      (3*(u2ModLength + 4)) * (2(WB-2))
          15]

          The Point Signature can be located in PUKCC RAM or in system RAM. If the Point Signature is entirely in
          system RAM with no part in PUKCC RAM this can be signaled by us ing the option
          PUKCL_ZPECCMUL_SCAL_IN_CLASSIC_RAM. In all other cases this option must not be used.
          The following table describes this option.
          Table 43-92. ZpEcDsaQuickVerify Service Point Signature in Classical RAM Option

          Option                                             Purpose
          PUKCL_ZPECCMUL_SCAL_IN_CLASSIC_RAM The Point Signature can be located in Crypto RAM or
                                             in system RAM. If the Point Signature is entirely in
                                             system RAM with no part in PUKCC RAM this can be
                                             signaled by using this option. In all other cases this
                                             option must not be used.

43.3.6.13.6 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;
           PUKCL(u2Option) = <Point Signature location and windows sizes>;
           PUKCL_ZpEcDsaQuickVerify(pu1ModCnsBase) = <Base of the ram location of P and Cns>;
           PUKCL_ZpEcDsaQuickVerify(u2ModLength) = <Byte length of P>;
           PUKCL_ZpEcDsaQuickVerify(pu1PointABase) = <Base of the ram location of the A point>;
           PUKCL_ZpEcDsaQuickVerify(pu1PointPublicKeyGen) = <Base of the Public Key>;
           PUKCL_ZpEcDsaQuickVerify(pu1PointSignature) = <Base of the Signature (r, s)>;
           PUKCL_ZpEcDsaQuickVerify(pu1OrderPointBase) = <Base of the order of the A point>;
           PUKCL_ZpEcDsaQuickVerify(pu1AWorkBase) = <Base of the ram location of the parameter A of the
           elliptic curve and workspace>;
           PUKCL_ZpEcDsaQuickVerify(pu1HashBase) = <Base of the SHA resulting hash>;
           PUKCL_ZpEcDsaQuickVerify(u2ScalarLength) = <Byte length of R and S in Point Signature>;
           . . .
           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(ZpEcDsaQuickVerify, pvPUKCLParam);
           if (PUKCL(u2Status) == PUKCL_OK)
                          {
                          ...
                          }
           else
                          if ( PUKCL(u2Status) = PUKCL_WRONG_SIGNATURE )
                                          {
                                          ...
                                          }
                          else // Manage the error

43.3.6.13.7 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure that the service works correctly:




         © 2019 Microchip Technology Inc.                    Datasheet                        DS60001507E-page 1541
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

           • pu1ModCnsBase, pu1PointABase, pu1PointPublicKeyGen, pu1PointSignature,pu1OrderPointBase,
             pu1AWorkBase or pu1HashBase are not aligned on 32-bit boundaries
           • {pu1ModCnsBase, u2ModLength + 4 + u2MaxLength + 12}, {pu1PointABase, (3 * u2ModLength
             + 12)* (2(WA-2))}, {pu1PointPublicKeyGen, (3 * u2ModLength + 12) * (2(WPub-2))},
             {pu1OrderPointBase, u2ScalarLength + 4}, {nu1ABase, u2ModLength + 4}, {pu1AWorkBase,
             (u2ModLength + 4) + (8 * u2MaxLength + 44)} or {nu1HashBase, u2ScalarLength + 4} are not in
             Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {pu1ModCnsBase, u2ModLength + 4 + u2MaxLength + 12},
             {pu1PointABase, (3 * u2ModLength + 12) * (2(WA-2))}, {pu1PointPublicKeyGen, (3 * u2ModLength
             + 12) *(2(WPub-2))}, {pu1OrderPointBase, u2ScalarLength + 4}, {pu1PointSignature, 2 *
             u2ScalarLength + 8}, {nu1ABase, u2ModLength + 4}, {pu1AWorkBase, (u2ModLength + 4) + (8 *
             u2MaxLength + 44)} and {nu1HashBase, u2ScalarLength + 4}
43.3.6.13.8 Status Returned Values
         Table 43-93. ZpEcDsaQuickVerify Service Return Codes

          Returned Status                   Importance Meaning
          PUKCL_OK                          –             The computation passed without problem. The signature
                                                          is the good one.
          PUKCL_WRONG_SIGNATURE Warning                   The signature is wrong.

43.3.6.13.9 Parameter Placement
         The parameters’ placement is described in detail in the following figures.
         Figure 43-11. Modulus P and Cns{pu1ModCnsBase, u2ModLength + 4 + u2MaxLength + 12}




         © 2019 Microchip Technology Inc.                    Datasheet                      DS60001507E-page 1542
                                             SAM D5x/E5x Family Data Sheet
                                           Public Key Cryptography Controller (PUKCC)

Figure 43-12. Points A {pu1PointABase, (3*(u2ModLength + 4)) * (2(WA-2))} and Public Key Gen
{pu1PointPublicKeyGen, (3*(u2ModLength + 4)) * (2(WB-2))}




Figure 43-13. PointSignature {pu1PointSignature, 2 * u2ScalarLength + 8}




© 2019 Microchip Technology Inc.              Datasheet                      DS60001507E-page 1543
                                                            SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

         Figure 43-14. The a parameter and Workspace {pu1AWorkBase, 9*u2ModLength + 48}




43.3.7   Elliptic Curves Over GF(2n) Services
         This section provides a complete description of the currently available elliptic curve over Polynomials in
         GF(2n) services.
         These services process Polynomials in GF(2n) only.
         The offered services cover the basic operations over elliptic curves such as:
           • Adding two points over a curve
           • Doubling a point over a curve
           • Multiplying a point by an integral constant
           • Converting a point’s projective coordinates (resulting from a doubling or an addition) to the affine
             coordinates, and oppositely converting a point’s affine coordinates to the projective coordinates.
           • Testing the point presence on the curve.
         Additionally, some higher level services covering the needs for signature generation and verification are
         offered:
           • Generating an ECDSA signature (compliant with FIPS186-2)
           • Verifying an ECDSA signature (compliant with FIPS 186-2) The supported curves use the following
             curve equation in GF(2n):
         Y2 + XY = X3 + aX + b

43.3.7.1 Parameters Format

43.3.7.1.1 Polynomials in GF(2n)
         Polynomials in GF(2n) are binary polynomials reduced modulo the polynomial P[X]. This polynomial is
         called the modulus and may be abbreviated to P in this document. The storage of these polynomials in
         memory area is described in 43.3.3.4 Aligned Significant Length.
         For notation simplicity the comparison signs “<“ or “>” may be used for polynomials, this is to be
         interpreted as a comparison between the degree of the polynomials.




         © 2019 Microchip Technology Inc.                    Datasheet                          DS60001507E-page 1544
                                                               SAM D5x/E5x Family Data Sheet
                                                               Public Key Cryptography Controller (PUKCC)

         In GF(2n) fully reduced polynomials are of degree strictly lower than degree(P[X]). In many cases the
         polynomials used in this library are only partially reduced and so have a degree higher or equal than
         degree(P[X]), but this degree is maintained strictly lower than (degree(P[X]) + 15).
43.3.7.1.2 Coordinates System
         In this implementation, several choices have been made related to the coordinate systems managed by
         the elliptic curve primitives.
         There are two systems currently managed by the library:
           • Affine Coordinates System where each curve point has two coordinates (X,Y)
           • Projective Coordinates System where each point is represented with three coordinates (X,Y,Z)
         Converting from the affine coordinates system to a projective coordinates system and is performed by
         extending its representation having Z = 1:
         (X,Y) ⇒ (X,Y, Z= 1)
         Converting from a projective coordinate to an affine one is a service offered by the library. The formula to
         perform this conversion is:
         (X,Y, Z) ⇒ (X ⇒ Z,Y/Z2)
43.3.7.1.3 Points Representation in Memory
         Depending on the representation (Projective or Affine), points are represented in memory as shown in the
         following figure.
         Figure 43-15. Point Representation in Memory




         In this figure, the modulus is represented as a reference, and to show that coordinates are always to be
         provided on the length of the modulus plus one 32-bit word.
         Different types of representations are listed here:
                                           ������� < � × �15
         Affine representation: �� =
                                           ������� < � × �15




        © 2019 Microchip Technology Inc.                         Datasheet                      DS60001507E-page 1545
                                                               SAM D5x/E5x Family Data Sheet
                                                              Public Key Cryptography Controller (PUKCC)

                                            �Pr�������� < � × �15
         Projective representation: �� = �Pr�������� < � × �15
                                            �Pr�������� < � × �15

         Note:
          1. The minimum value for u2ModLength is 12 bytes. Therefore, the significant length of the modulus
               must be at least three 32-bit words.
          2. In some cases the point can be the infinite point. In this case it is represented with its Z coordinates
               equal or congruent to zero.
43.3.7.1.4 Modulus and Modular Constant Parameters
         In most of the services the following parameters must be provided:
           • P the Modulus (often pointed by {nu1ModBase,u2ModLength + 4}): This parameter contains the
             Modulus Polynomial P[X] defining the Galois Field used in points coordinates computations. The
             Modulus must be u2ModLength bytes long, while having a supplemental zeroed 32-bit word on the
             MSB side.
             Note: Most of the Elliptic Curve computations are reduced modulo P. In many functions the
             reductions are made with the Fast Reduction.
           • Cns the Modular Constant (often pointed by {nu1CnsBase,u2ModLength + 12}): This parameter
             contains the Modular Constant associated to the Modulus.


                        Important: The Modular Constant must be calculated before using the GF(2n) Elliptic Curves
                        functions by a call to the Setup for Modular Reductions with the GF(2n) option (see 43.3.5.1
                        Modular Reduction).


43.3.7.1.5 Curve Parameters in Memory
         Some services need one or both of the Elliptic Curve Equation Parameters a and b. In this case these
         values are organized in memory as follows:
           • The a Parameter relative to the Elliptic Curve Equation (often pointed by {nu1ABase,u2ModLength
             +4}). The a Parameter is written in a classical way in memory. It is u2ModLength bytes long and has
             a supplemental zeroed 32-bit word on the MSB side.
           • The a and b Parameters relative to the Elliptic Curve Equation (often pointed by {nu1ABBase,
             2*u2ModLength + 8}):
               – The a Parameter is written in memory on u2ModLength bytes long, with a supplemental zeroed
                  32-bit word on the MSB side.
               – The b Parameter is written in memory after the a Parameter at an offset of (u2ModLength + 4)
                  bytes. It is written in memory on u2ModLength bytes long, with a supplemental zeroed 32-bit
                  word on the MSB side.
43.3.7.2 Point Addition
43.3.7.2.1 Purpose
         This service is used to perform a point addition, based on a given elliptic curve over GF(2n).
         Please note that this service is not intended to add the same point twice. In this particular case, use the
         doubling service (see 43.3.7.3 Point Doubling).




         © 2019 Microchip Technology Inc.                           Datasheet                    DS60001507E-page 1546
                                                            SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

43.3.7.2.2 How to Use the Service

43.3.7.2.3 Description
          The operation performed is:
          PtC = PtA + PtB
          In this computation, the following parameters need to be provided:
           • Point A the input point is filled in projective coordinates (X,Y,Z) (pointed by {nu1PointABase,
             3*u2ModLength + 12}). This point can be the Infinite Point.
           • Point B the input point is filled in projective coordinates (X,Y,Z) (pointed by {nu1PointBBase,
             3*u2ModLength + 12}). This point can be the Infinite Point.
           • Cns the Fast Modular Constant filled (pointed by {nu1CnsBase,u2ModLength + 12})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength + 4})
           • The a parameter relative to the elliptic curve equation (pointed by {nu1ABase,u2ModLength + 4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 7*u2ModLength + 40}
          The resulting C point is represented in projective coordinates (X,Y,Z) and is stored at the same place than
          the input point A. This Point can be the Infinite Point.
          The services for this operation are:
           • Service GF2NEccAddFast: The fast mode is used, the fast modular reduction is used in the
              computations.


                         Important: Before using this service, ensure that the constant Cns has been calculated with
                         the setup of the Modular Reductions service.



43.3.7.2.4 Parameters Definition
          Table 43-94. GF2NEccAddFast Service Parameters

          Parameter           Type Direction Location       Data Length         Before             After
                                                                                Executing the      Executing the
                                                                                Service            Service
          nu1ModBase          nu1     I        Crypto       u2ModLength + 4     Base of Modulus Base of
                                               RAM                              P               Modulus P
          nu1CnsBase          nu1     I        Crypto       u2ModLength + 12 Base of Cns           Base of Cns
                                               RAM
          u2ModLength         u2      I        –            –                   Length of          Length of
                                                                                modulo             modulo
          nu1PointABase nu1           I/O      Crypto       3*u2ModLength       Input point A      Resulting point
                                               RAM          + 12                (projective        C (projective
                                                                                coordinates)       coordinates)
          nu1PointBBase nu1           I        Crypto       3*u2ModLength       Input point B      Input point B
                                               RAM          + 12                (projective
                                                                                coordinates)




         © 2019 Microchip Technology Inc.                       Datasheet                       DS60001507E-page 1547
                                                            SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

          ...........continued
          Parameter              Type Direction Location    Data Length         Before               After
                                                                                Executing the        Executing the
                                                                                Service              Service
          nu1ABBase              nu1   I          Crypto    u2ModLength + 4     Parameter a of       Unchanged
                                                  RAM                           the elliptic curve
          nu1Workspace nu1             I          Crypto    7*u2ModLength       –                    Corrupted
                                                  RAM       + 40                                     workspace

43.3.7.2.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;
           //Depending on the function the Random Number Generator
           //must be initialized and started
           //following the directives given for the RNG on the chip
           PUKCL(u2Option) = 0;
           PUKCL_GF2NEccAdd(nu1ModBase) = <Base of the ram location of P>;
           PUKCL_GF2NEccAdd(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL_GF2NEccAdd(u2ModLength) = <Byte length of P>;
           PUKCL_GF2NEccAdd(nu1PointABase) = <Base of the ram location of the A point>;
           PUKCL_GF2NEccAdd(nu1PointBBase) = <Base of the ram location of the B point>;
           PUKCL_GF2NEccAdd(nu1ABBase) = <Base of the ram location of the a Parameter>;
           PUKCL_GF2NEccAdd(nu1Workspace) = <Base of the ram location of the workspace>;
           . . .
           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(GF2NEccAddFast, pvPUKCLParam);
           if (PUKCL(u2Status) == PUKCL_OK)
                          {
                          ...
                          }
           else // Manage the error


43.3.7.2.6 Constraints
          No overlapping between either input and output are allowed The following conditions must be avoided to
          ensure the service works correctly:
           • nu1ModBase,nu1CnsBase, nu1PointABase, nu1PointBBase, nu1ABBase, nu1Workspace are not
             aligned on 32-bit boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointABase,
             3*u2ModLength+ 12}, {nu1PointBBase, 3*u2ModLength + 12}, {nu1ABase,u2ModLength + 4},
             {nu1Workspace, <WorkspaceLength>} are not in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength +8},
             {nu1PointABase, 3*u2ModLength + 12}, {nu1PointBBase, 3*u2ModLength + 12},
             {nu1ABase,u2ModLength + 4} and {nu1Workspace, 5*u2ModLength + 32}
43.3.7.2.7 Status Returned Values
          Table 43-95. GF2NEccAddFast Service Return Codes

          Returned Status                   Importance     Meaning
          PUKCL_OK                          –              The computation passed without errors.

43.3.7.3 Point Doubling

43.3.7.3.1 Purpose
          This service is used to perform a Point Doubling, based on a given elliptic curve over GF(2n).




         © 2019 Microchip Technology Inc.                     Datasheet                         DS60001507E-page 1548
                                                            SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

43.3.7.3.2 How to Use the Service

43.3.7.3.3 Description
          The operation performed is:
          PtC = 2 × PtA
          In this computation, the following parameters need to be provided:
           • A the input point is filled in projective coordinates (X,Y,Z) (pointed by {nu1PointABase,
             3*u2ModLength + 12}). This point can be the Infinite Point.
           • Cns the Fast Modular Constant filled (pointed by {nu1CnsBase,u2ModLength +8})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength +4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 4*u2ModLength +28}
           • The a and b Parameters relative to the Elliptic Curve Equation (pointed by {nu1ABBase,
             2*u2ModLength+ 8})
           • The resulting C point is represented in projective coordinates (X,Y,Z) and is stored at the very same
             place than the input point A. This point can be the Infinite Point.
          The service name for this operation is GF2NEccDblFast. This service uses Fast mode and Fast Modular
          Reduction for computation.


                         Important: Before using this service, ensure that the constant Cns has been calculated with
                         the setup of the Fast Modular Reductions service.



43.3.7.3.4 Parameters Definition
          Table 43-96. GF2NEccDblFast Service Parameters

          Parameter           Type Direction Location       Data Length         Before             After Executing
                                                                                Executing the      the Service
                                                                                Service
          nu1ModBase          nu1     I        Crypto       u2ModLength + 4     Base of modulus Base of modulus
                                               RAM                              P               P
          nu1CnsBase          nu1     I        Crypto       u2ModLength + 12 Base of Cns           Base of Cns
                                               RAM
          u2ModLength         u2      I        –            –                   Length of          Length of
                                                                                modulus P          modulus P
          nu1ABBase           u2      I        Crypto       2*u2ModLength       Parameters a       Parameter a and
                                               RAM          +8                  and b of the       b of the elliptic
                                                                                elliptic curve     curve
          nu1PointABase nu1           I/O      Crypto       3*u2ModLength       Input point A      Resulting point
                                               RAM          + 12                (projective        C (projective
                                                                                coordinates)       coordinates)
          nu1Workspace nu1            I        Crypto       4*u2ModLength       –                  Corrupted
                                               RAM          + 28                                   workspace




         © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1549
                                                             SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

43.3.7.3.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           PUKCL (u2Option) = 0;

           PUKCL _GF2NEccDbl(nu1ModBase) = <Base of the ram location of P>;
           PUKCL _GF2NEccDbl(u2ModLength) = <Byte length of P>;
           PUKCL _GF2NEccDbl(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL _GF2NEccDbl(nu1PointABase) = <Base of the ram location of the A point>;
           PUKCL _GF2NEccDbl(nu1ABBase) = <Base of the a and b parameters of the elliptic curve>;
           PUKCL _GF2NEccDbl(nu1Workspace) = <Base of the ram location of the workspace>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(GF2NEccDblFast,&PUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error


43.3.7.3.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1ABBase, nu1Workspace are not aligned on 32-bit
             boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointABase,
             3*u2ModLength+ 12}, {nu1ABBase, 2*u2ModLength + 8}, {nu1Workspace, <WorkspaceLength>} are
             not in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8},
             {nu1PointABase, 3*u2ModLength + 12}, {nu1ABase, u2ModLength + 4} and {nu1Workspace,
             4*u2ModLength + 28}
43.3.7.3.7 Status Returned Values
          Table 43-97. GF2NEccDblFast Service Return Codes

          Returned Status                   Importance   Meaning
          PUKCL_OK                          –            The computation passed without problem.

43.3.7.4 Scalar Point Multiply

43.3.7.4.1 Purpose
          This service is used to multiply a point by an integral constant K on a given elliptic curve over GF(2n).
43.3.7.4.2 How to Use the Service

43.3.7.4.3 Description
          The operation performed is:
          PtC = K × PtA
          In this computation, the following parameters need to be provided:
           • A the input point is filled in projective coordinates (X,Y,Z) (pointed by {nu1PointABase,
             3*u2ModLength + 12}). This point can be the Infinite Point.
           • Cns the Fast Modular Constant filled (pointed by {nu1CnsBase,u2ModLength + 8})




         © 2019 Microchip Technology Inc.                      Datasheet                          DS60001507E-page 1550
                                                            SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

           •   P the modulus filled (pointed by {nu1ModBase,u2ModLength + 4})
           •   The workspace not initialized (pointed by {nu1WorkSpace, 8*u2ModLength + 44}
           •   The a and b parameters relative to the elliptic curve (pointed by {nu1ABBase,2*u2ModLength + 8})
           •   K the scalar number (pointed by {nu1ScalarNumber,u2ScalarLength + 4})
          The resulting C point is represented in projective coordinates (X,Y,Z) and is stored at the very same place
          than the input point A. This point can be the Infinite Point.
          The service name for this operation is GF2NEccMulFast. This service uses Fast mode and Fast Modular
          Reduction for computation.


                        Important: Before using this service, ensure that the constant Cns has been calculated with
                        the setup of the Fast Modular Reductions service.



43.3.7.4.4 Parameters Definition
          Table 43-98. GF2NEccMulFast Service Parameters

          Parameter          Type Direction Location       Data Length          Before                After
                                                                                Executing the         Executing the
                                                                                Service               Service
          nu1ModBase         nu1     I       Crypto        u2ModLength + 4      Base of modulus       Base of
                                             RAM                                P                     modulus P
          nu1CnsBase         nu1     I       Crypto        u2ModLength + 12 Base of Cns               Base of Cns
                                             RAM
          u2ModLength        u2      I       –             –                    Length of             Length of
                                                                                modulus P             modulus P
          nu1KBase           nu1     I       Crypto        u2KLength            Scalar number         Unchanged
                                             RAM                                used to multiply
                                                                                the point A
          u2KLength          u2      I       –             –                    Length of scalar      Length of scalar
                                                                                K                     K
          nu1PointBase       nu1     I/O     Crypto        3*u2ModLength        Input point A         Resulting point
                                             RAM           + 12                 (projective           C (projective
                                                                                coordinates)          coordinates)
          nu1ABase           nu1     I       Crypto        2*u2ModLength        Parameters a and Unchanged
                                             RAM           +8                   b of the elliptic
                                                                                curve
          nu1Workspace nu1           I       Crypto        8*u2ModLength        –                     Corrupted
                                             RAM           + 44                                       workspace

43.3.7.4.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           PUKCL (u2Option) = 0;




         © 2019 Microchip Technology Inc.                      Datasheet                           DS60001507E-page 1551
                                                                    SAM D5x/E5x Family Data Sheet
                                                                   Public Key Cryptography Controller (PUKCC)

           PUKCL _GF2NEccMul(nu1ModBase) = <Base of the ram location of P>;
           PUKCL _GF2NEccMul(u2ModLength) = <Byte length of P>;
           PUKCL _GF2NEccMul(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL _GF2NEccMul(nu1PointBase) = <Base of the ram location of the A point>;
           PUKCL _GF2NEccMul(nu1ABase) = <Base of the ram location of the parameters a and b of the
           elliptic
           curve>;
           PUKCL _GF2NEccMul(nu1KBase) = <Base of the ram location of the scalar number>;
           PUKCL _GF2NEccMul(nu1Workspace) = <Base of the ram location of the workspace>;
           PUKCL _GF2NEccMul(u2KLength) = <Length of the ram location of the scalar number>;

           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(GF2NEccMulFast,&PUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error


43.3.7.4.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointBase, nu1ABase, nu1KBase, nu1Workspace are not aligned
             on 32-bit boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointBase,
             3*u2ModLength+ 12}, {nu1ABase, 2*u2ModLength + 8}, {nu1KBase, u2KLength} or {nu1Workspace,
             8*u2ModLength + 44} are not in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength +8},
             {nu1PointBase, 3*u2ModLength + 12}, {nu1ABase, 2*u2ModLength + 8}, {nu1KBase, u2KLength}
             and {nu1Workspace, 8*u2ModLength + 44}
43.3.7.4.7 Status Returned Values
          Table 43-99. GF2NEccMulFast Service Return Codes

          Returned Status                   Importance        Meaning
          PUKCL_OK                          –                 The computation passed without problem.

43.3.7.5 Projective to Affine Coordinates Conversion

43.3.7.5.1 Purpose
          This service is used to perform a point coordinates conversion from a projective representation to an
          affine.
43.3.7.5.2 How to Use the Service

43.3.7.5.3 Description
          The operation performed is:

                                       ���Pr�������� ����������
          ��� ������ ���������� =
                                      ��� Pr�������� ����������

                                       ��� Pr�������� ����������
          ��� ������ ���������� =
                                      ��� Pr�������� ���������� 2

          In this computation, the following parameters need to be provided:




         © 2019 Microchip Technology Inc.                            Datasheet                    DS60001507E-page 1552
                                                             SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

           • A the input point is filled in projective coordinates (X,Y,Z) or affine coordinates for X and Y, and
             setting Z to 1 (pointed by {nu1PointABase,3*u2ModLength + 12}). The Point A can be the point at
             infinity. In this case, the u2Status returned is PUKCL_POINT_AT_INFINITY.
           • Cns the Modular Constant filled (pointed by {nu1CnsBase,u2ModLength + 8})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength + 4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 4*u2ModLength + 48}
          The result is the point A with its (X,Y) coordinates converted to affine, and the Z coordinate set to 1.
          The service name for this operation is GF2NEcConvProjToAffine.


                        Important: Before using this service, ensure that the constant Cns has been calculated with
                        the setup of the Fast Modular Reductions service.



43.3.7.5.4 Parameters Definition
          Table 43-100. GF2NEcConvProjToAffine Service Parameters

          Parameter           Type Direction Location        Data Length            Before        After Executing
                                                                                    Executing the the Service
                                                                                    Service
          nu1ModBase          nu1     I        Crypto        u2ModLength + 4        Base of           Base of modulus
                                               RAM                                  modulus P         P
          nu1CnsBase          nu1     I        Crypto        u2ModLength + 12       Base of Cns       Base of Cns
                                               RAM
          u2ModLength         u2      I        –             –                      Length of         Length of
                                                                                    modulus P         modulus P
          nu1PointABase nu1           I        Crypto        3*u2ModLength          Input point A     Resulting point A
                                               RAM           + 12                                     in affine
                                                                                                      coordinates
          nu1Workspace nu1            I        Crypto        4*u2ModLength          –                 Workspace
                                               RAM           + 48

43.3.7.5.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // ! The Random Number Generator must be initialized and started
           // ! following the directives given for the RNG on the chip

           PUKCL (u2Option) = 0;

           PUKCL _GF2NEcConvProjToAffine(nu1ModBase) = <Base of the ram location of P>;
           PUKCL _GF2NEcConvProjToAffine(u2ModLength) = <Byte length of P>;
           PUKCL _GF2NEcConvProjToAffine(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL _GF2NEcConvProjToAffine(nu1PointABase) = <Base of the ram location of the A point>;
           PUKCL _GF2NEcConvProjToAffine(nu1Workspace) = <Base of the ram location of the workspace>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(GF2NEcConvProjToAffine,&PUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                       {




         © 2019 Microchip Technology Inc.                        Datasheet                          DS60001507E-page 1553
                                                            SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

                       ...
                       }
           else // Manage the error

43.3.7.5.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1Workspace are not aligned on 32-bit boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8},{nu1PointABase,
             3*u2ModLength + 12}, {nu1Workspace, <WorkspaceLength>} are not in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8},
             {nu1PointABase, 3*u2ModLength + 12} and {nu1Workspace, 4*u2ModLength + 48}
43.3.7.5.7 Status Returned Values
          Table 43-101. GF2NEcConvProjToAffine Service Return Codes

          Returned Status                   Importance Meaning
          PUKCL_OK                          –            The computation passed without problem.
          PUKCL_POINT_AT_INFINITY Warning                The input point has its Z equal to zero, so it is a
                                                         representation of the infinite point.

43.3.7.6 Affine to Projective Coordinates Conversion
43.3.7.6.1 Purpose
          This service is used to perform a point coordinates conversion from an affine point representation to
          projective.
43.3.7.6.2 How to Use the Service

43.3.7.6.3 Description
          The operation performed is:
          affine(Xa, Ya) → projective(Xp, Yp, Zp)
          In this computation, the following parameters need to be provided:
           • A the input point is filled in affine coordinates for X and Y, and setting Z to 1 (pointed by
             {nu1PointABase,3*u2ModLength + 4}).
           • Cns the Fast Modular Constant filled (pointed by {nu1CnsBase,u2ModLength + 8})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength + 4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 2*u2ModLength +16} The result is the
             point A with its (X,Y,Z) projective coordinates.
          The service name for this operation is GF2NEcConvAffineToProjective.


                         Important: Before using this service, ensure that the constant Cns has been calculated with
                         the setup of the Fast Modular Reductions service.




         © 2019 Microchip Technology Inc.                     Datasheet                           DS60001507E-page 1554
                                                          SAM D5x/E5x Family Data Sheet
                                                         Public Key Cryptography Controller (PUKCC)

43.3.7.6.4 Parameters Definition
          Table 43-102. GF2NEcConvAffineToProjective Service Parameters

          Parameter           Type Direction Location     Data Length          Before        After Executing
                                                                               Executing the the Service
                                                                               Service
          nu1ModBase          nu1     I      Crypto       u2ModLength + 4      Base of           Base of modulus
                                             RAM                               modulus P         P
          nu1CnsBase          nu1     I      Crypto       u2ModLength + 8      Base of Cns       Base of Cns
                                             RAM
          u2ModLength         u2      I      –            –                    Length of         Length of
                                                                               modulus P         modulus P
          nu1PointABase nu1           I      Crypto       3*u2ModLength        Input point A     Resulting point A
                                             RAM          + 12                                   in affine
                                                                                                 coordinates
          nu1Workspace nu1            I      Crypto       2*u2ModLength        –                 Workspace
                                             RAM          + 16

43.3.7.6.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // ! The Random Number Generator must be initialized and started
           // ! following the directives given for the RNG on the chip

           PUKCL (u2Option) = 0;

           PUKCL _GF2NEcConvAffineToProjective(nu1ModBase) = <Base of the ram location of P>;
           PUKCL _GF2NEcConvAffineToProjective(u2ModLength) = <Byte length of P>;
           PUKCL _GF2NEcConvAffineToProjective(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL _GF2NEcConvAffineToProjective(nu1PointABase) = <Base of the ram location of the A
           point>;
           PUKCL _GF2NEcConvAffineToProjective(nu1Workspace) = <Base of the ram location of the
           workspace>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(GF2NEcConvAffineToProjective,&PUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error

43.3.7.6.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure that the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1Workspace are not aligned on 32-bit boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointABase,
             3*u2ModLength + 12}, {nu1Workspace, <WorkspaceLength>} are not in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8},
             {nu1PointABase, 3*u2ModLength + 12}, and {nu1Workspace, 2*u2ModLength + 16}




         © 2019 Microchip Technology Inc.                     Datasheet                        DS60001507E-page 1555
                                                               SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

43.3.7.6.7 Status Returned Values
          Table 43-103. GF2NEcConvAffineToProjective Service Return Codes

          Returned Status                   Importance      Meaning
          PUKCL_OK                          –               The computation passed without problem.

43.3.7.7 Randomize Coordinate
43.3.7.7.1 Purpose
          This service is used to convert the Projective representation of a point to another Projective
          representation.
43.3.7.7.2 How to Use the Service

43.3.7.7.3 Description
          The operation performed is:
          Projective(X1, Y1, Z1) → Projective(X2, Y2, Z2)
          In this computation, the following parameters need to be provided:
           • The input point is filled in projective coordinates (X,Y,Z) (pointed by {nu1PointBase,3*u2ModLength
             + 12}). This Point must not be the point at infinity.
           • Cns the Fast Modular Constant filled (pointed by {nu1CnsBase,u2ModLength + 8})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength + 4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 3*u2ModLength + 28}
           • The random number (pointed by {nu1RandomBase, u2ModLength + 4}) The result is the point
             nu1PointBase with its (X,Y,Z) coordinates randomized. The service for this operation is
             GF2NEcRandomiseCoordinate.


                         Important:
                         Before using this service:
                          • Ensure that the constant Cns has been calculated with the Setup of the fast Modular
                            Reductions service.
                          • Be sure to follow the directives given for the RNG on the chip you use (particularly
                            initialization, seeding) and compulsorily start the RNG.


43.3.7.7.4 Parameters Definition
          Table 43-104. GF2NEcRandomiseCoordinate Service Parameters

          Parameter             Type Direction Location         Data Length          Before        After
                                                                                     Executing the Executing the
                                                                                     Service       Service
          nu1ModBase            nu1     I           Crypto RAM u2ModLength + 4       Base of          Base of
                                                                                     modulus P        modulus P
          nu1CnsBase            nu1     I           Crypto RAM u2ModLength + 8       Base of Cns      Base of Cns
          u2ModLength           u2      I           –           –                    Length of        Length of
                                                                                     modulus P        modulus P




         © 2019 Microchip Technology Inc.                       Datasheet                        DS60001507E-page 1556
                                                           SAM D5x/E5x Family Data Sheet
                                                           Public Key Cryptography Controller (PUKCC)

          ...........continued
          Parameter              Type Direction Location     Data Length         Before        After
                                                                                 Executing the Executing the
                                                                                 Service       Service
          nu1PointBase           nu1    I       Crypto RAM 3*u2ModLength         Input point       Resulting point
                                                           + 12
          nu1RandomBase nu1             I       Crypto RAM u2ModLength + 4       Random            Corrupted
          nu1Workspace           nu1    I       Crypto RAM 3*u2ModLength         –                 Workspace
                                                           + 28

43.3.7.7.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // ! The Random Number Generator must be initialized and started
           // ! following the directives given for the RNG on the chip

           PUKCL (u2Option) = 0;

           // Depending on the option specified, not all fields should be filled
           PUKCL _GF2NEcRandomiseCoordinate(nu1ModBase) = <Base of the ram location of P>;
           PUKCL _GF2NEcRandomiseCoordinate(u2ModLength) = <Byte length of P>;
           PUKCL _GF2NEcRandomiseCoordinate(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL_GF2NEcRandomiseCoordinate(nu1RandomBase) = <Base of the ram location where the the rng
           is stored>;
           PUKCL _GF2NEcRandomiseCoordinate(nu1PointBase) = <Base of the ram location of the point>;
           PUKCL _GF2NEcRandomiseCoordinate(nu1Workspace) =
           <Base of the ram location of the workspace>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(GF2NEcRandomiseCoordinate,&PUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error

43.3.7.7.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure that the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1RandomBase, nu1Workspace are not aligned on
             32-bit boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointABase,
             3*u2ModLength + 12}, {nu1RandomBase, u2ModLength + 4}, {nu1Workspace, <WorkspaceLength>}
             are not in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8},
             {nu1PointABase, 3*u2ModLength + 12}, {nu1RandomBase, u2ModLength + 4} and {nu1Workspace,
             3*u2ModLength + 28}




         © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1557
                                                                   SAM D5x/E5x Family Data Sheet
                                                                 Public Key Cryptography Controller (PUKCC)

43.3.7.7.7 Status Returned Values
          Table 43-105. GF2NEcRandomiseCoordinate Service Return Codes

          Returned Status                   Importance          Meaning
          PUKCL_OK                          –                   The computation passed without problem.

43.3.7.8 Point is on Elliptic Curve
43.3.7.8.1 Purpose
          This service is used to test whether the point is on the curve.
43.3.7.8.2 How to Use the Service

43.3.7.8.3 Description
          The operation performed is:
          Status = IsPointOnCurve(X, Y, Z);
          In this computation, the following parameters need to be provided:
           • The input points filled in projective coordinates (X, Y, Z) (pointed by {nu1PointBase, 3*U2ModLength
             + 4}). This point can be point at infinity.
           • AParam and BParam are the Elliptic Curve Equation parameters (pointed by {nu1AParam,
             u2ModLength+ 4} and {nu1BParam, u2ModLength + 4}).
           • Cns the Fast Modular Constant filled (pointed by {nu1CnsBase, u2ModLength + 8})
           • P the modulus filled (pointed by {nu1ModBase, u2ModLength + 8})
           • The workspace not initialized (pointed by {nu1WorkSpace, 4*u2ModLength + 28})
          The service name for this operation is GF2NEcPointIsOnCurve.


                         Important: Before using this service, the constant Cns must have been calculated with the
                         Fast Modular Reduction service.



43.3.7.8.4 Parameters Definition
          Table 43-106. GF2NEcPointIsOnCurve Service Parameters

          Parameter          Type Dir. Location             Data Length          Before Executing     After Executing
                                                                                 the Service          the Service
          nu1ModBase         nu1     I          Crypto RAM u2ModLength + 4       Base of modulus P Base of modulus
                                                                                                   P
          nu1CnsBase         nu1     I          Crypto RAM u2ModLength + 8       Base of Cns          Base of Cns
          u2ModLength        u2      I          –           –                    Length of modulus    Length of
                                                                                 P                    modulus P
          nu1PointBase       nu1     I          Crypto RAM 3*u2ModLength + 12 Input point             Unchanged
          nu1AParam          nu1     I          Crypto RAM u2ModLength + 4       The parameter a      Unchanged
          nu1BParam          nu1     I          Crypto RAM u2ModLength + 4       The parameter b      Unchanged
          nu1Workspace nu1           I          Crypto RAM 4*u2ModLength + 28 N/A                     Workspace




         © 2019 Microchip Technology Inc.                           Datasheet                        DS60001507E-page 1558
                                                          SAM D5x/E5x Family Data Sheet
                                                         Public Key Cryptography Controller (PUKCC)

43.3.7.8.5 Code Example
           PUKCL_PARAM PUKCLParam;
           PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

           // ! The Random Number Generator must be initialized and started
           // ! following the directives given for the RNG on the chip

           PUKCL (u2Option) = 0;

           // Depending on the option specified, not all fields should be filled
           PUKCL _GF2NEcPointIsOnCurve(nu1ModBase) = <Base of the ram location of P>;
           PUKCL _GF2NEcPointIsOnCurve(u2ModLength) = <Byte length of P>;
           PUKCL _GF2NEcPointIsOnCurve(nu1CnsBase) = <Base of the ram location of Cns>;
           PUKCL _GF2NEcPointIsOnCurve(nu1PointABase) = <Base of the A point>;
           PUKCL _GF2NEcPointIsOnCurve(nu1AParam) = <Base of the ram location of the parameter a>;
           PUKCL _GF2NEcPointIsOnCurve(nu1BParam) = <Base of the ram location of the parameter b>;
           PUKCL _GF2NEcPointIsOnCurve(nu1PointBase) = <Base of the ram location of the point>;
           PUKCL _GF2NEcPointIsOnCurve(nu1Workspace) = <Base of the ram location of the workspace>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKC L_Process(GF2NEcPointIsOnCurve,
           pvPUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error


43.3.7.8.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure that the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1AParam, nu1BParam and nu1Workspace are not
             aligned on 32-bit boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointABase,
             3*u2ModLength + 12}, {nu1AParam, u2ModLength + 4}, {nu1BParam, u2ModLength + 4},
             {nu1Workspace, 4*u2ModLength + 28} are not in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8},
             {nu1PointABase, 3*u2ModLength + 12}, {nu1AParam, u2ModLength + 4}, {nu1BParam,
             u2ModLength + 4} and {nu1Workspace, 4*u2ModLength + 28}
43.3.7.8.7 Status Returned Values
          Table 43-107. GF2NEcPointIsOnCurve Service Return Codes

          Returned Status                         Importance Meaning
          PUKCL_OK                                –            The point is on the curve.
          PUKCL_POINT_IS_NOT_ON_CURVE Warning                  The point is not on the curve.
          PUKCL_POINT_AT_INFINITY                 Warning      The input point has its Z equal to zero, so it’s a
                                                               representation of the infinite point.

43.3.7.9 Generating an ECDSA Signature (Compliant with FIPS 186-2)

43.3.7.9.1 Purpose
          This service is used to generate an ECDSA signature following the FIPS 186-2. It performs the second
          step of the Signature Generation. A hash value (HashVal) must be provided as input, it has to be
          previously computed from the message to be signed using a secure hash algorithm.




         © 2019 Microchip Technology Inc.                   Datasheet                           DS60001507E-page 1559
                                                              SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

          A scalar number must be provided, as described in the FIPS 186-2.
          The result (R,S) is computed by this service. If S equals zero, the status is set to
          PUKCL_WRONG_SELECT_NUMBER.
43.3.7.9.2 How to Use the Service

43.3.7.9.3 Description
          The operation performed is:
          (R, S) = EcDsaSign(PtA, HashVal, k, CurveParameters, PrivateKey)
          This service processes the following checks:
           • If the Scalar Number k is out of the range [1, PointOrder -1], the calculus is stopped and the status is
             set to PUKCL_WRONG_SELECT_NUMBER.
           • If R equals zero, the calculus is stopped and the status is set to
             PUKCL_WRONG_SELECT_NUMBER.
           • If S equals zero, the calculus is stopped and the status is set to
             PUKCL_WRONG_SELECT_NUMBER. In this computation, the following parameters need to be
             provided:
           • A the input point is filled in “mixed” coordinates (X,Y) with the affine values and Z = 1 (pointed by
             {nu1PointABase,3*u2ModLength + 12})
           • Cns the working space for the Fast Modular Constant not initialized (pointed by
             {nu1CnsBase,u2ScalarLength + 8})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength + 4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 8*u2ModLength + 44}
           • The a and b parameters relative to the elliptic curve equation (pointed by {nu1ABBase,
             2*u2ModLength + 8})
           • The order of the Point A on the elliptic curve (pointed by {nu1OrderPointBase, u2ScalarLength + 4})
           • k the input Scalar Number beforehand generated and filled (pointed
             by{nu1ScalarNumber,u2ScalarLength + 4})
           • HashVal the hash value beforehand generated and filled (pointed by {nu1HashBase, u2ScalarLength
             +4})
           • The Private Key (pointed by {nu1PrivateKey, u2ScalarLength +4})
           • Generally u2ScalarLength is equal to (u2ModLength) or (u2ModLength + 4)


                         Important:
                         For the ECDSA signature generation be sure to follow the directives given for the RNG on the
                         chip you use (particularly initialization, seeding) and compulsorily start the RNG.
                         The scalar number k must be selected at random. This random must be generated before the
                         call of the ECDSA signature. For this random generation be sure to follow the directives given
                         for the RNG on the chip you use (particularly initialization, seeding) and compulsorily start the
                         RNG.


          The operation performed is:
           • Compute the ECDSA (R,S) as described in FIPS 186-2, but leaving the user the role of computing
             the input Hash Value, thus leaving the freedom of using any other algorithm than SHA-1.
           • Compute a R value using the input A point and the scalar number.




         © 2019 Microchip Technology Inc.                       Datasheet                          DS60001507E-page 1560
                                                             SAM D5x/E5x Family Data Sheet
                                                             Public Key Cryptography Controller (PUKCC)

           • Compute a S value using R, the scalar number, the private key and the provided hash value. Note
             that the resulting signature (R,S) is stored at the place of the input A point.
           • If all is correct and S is different from zero, the status is set to PUKCL_OK. If all is correct and S
             equals zero,the status is set to PUKCL_WRONG_SELECT_NUMBER. If an error occurs, the status
             is set to the corresponding error value (see Status Returned Values below).
          The service name for this operation is GF2NEcDsaGenerateFast. The fast mode is used, the fast
          modular reduction is used in the computations.
           • The signature (R,S), when resulting from a computation is given back at address of the A point:
              – The R value result with u2ModLength + 4 bytes (padded with zeros).
              – The S value result with u2ModLength + 4 bytes (padded with zeros)
              – The u2NLength + 4 following bytes (space for the third coordinate of A) are filled with zeros.




43.3.7.9.4 Parameters Definition
          Table 43-108. GF2NEcDsaGenerateFast Service Parameters

          Parameter                  Type Direction Location     Data Length       Before             After
                                                                                   Executing the      Executing
                                                                                   Service            the Service
          nu1ModBase                 nu1    I       Crypto       u2ModLength + 4 Base of              Base of
                                                    RAM                          modulus P            modulus P
          nu1CnsBase                 nu1    I       Crypto       u2ScalarLength    Base of Cns        Base of Cns
                                                    RAM          + 12
          u2ModLength                u2     I       –            –                 Length of          Length of
                                                                                   modulus P          modulus P




         © 2019 Microchip Technology Inc.                      Datasheet                       DS60001507E-page 1561
                                                            SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

         ...........continued
          Parameter                 Type Direction Location     Data Length      Before             After
                                                                                 Executing the      Executing
                                                                                 Service            the Service
          nu1ScalarNumber           nu1    I       Crypto       u2ScalarLength   Scalar Number      Unchanged
                                                   RAM          +4               used to multiply
                                                                                 the point A
          nu1OrderPointBase         nu1    I       Crypto       u2ScalarLength   Order of the       Unchanged
                                                   RAM          +4               Point A in the
                                                                                 elliptic curve
          nu1PrivateKey             nu1    I/O     Crypto       u2ScalarLength   Base of the        Unchanged
                                                   RAM          +4               Private Key
          nu1HashBase (see          nu1    I       Crypto       u2ScalarLength   Base of the        Unchanged
          Note 1)                                  RAM          +4               hash value
                                                                                 resulting from
                                                                                 the previous
                                                                                 SHA
          u2ScalarLength            u2     I       –            –                Length of scalar Length of
                                                                                 (same length as scalar
                                                                                 the length of
                                                                                 order)
          nu1PointABase             nu1    I/O     Crypto       3*u2ModLength    Input point A      Resulting
                                                   RAM          + 12             (three             signature
                                                                                 coordinates        (R,S,0)
                                                                                 (X,Y) affine and
                                                                                 Z = 1)
          nu1ABase                  nu1    I       Crypto       2*u2ModLength    Parameter a of Unchanged
                                                   RAM          +8               the elliptic curve
          nu1Workspace              nu1    I       Crypto       8*u2ModLength    –                  Corrupted
                                                   RAM          + 44                                workspace

         Note:
          1. Whatever the chosen SHA, the resulting hash value may have a length inferior or equal to the
               modulo length and be padded with zeros until its total length is u2ModLength + 4.
43.3.7.9.5 Code Example
          PUKCL_PARAM PUKCLParam;
          PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

          // ! The Random Number Generator must be initialized and started
          // ! following the directives given for the RNG on the chip

          PUKCL (u2Option) = 0;

          // Depending on the option specified, not all fields should be filled
          PUKCL _GF2NEcDsaGenerate(nu1ModBase) = <Base of the ram location of P>;
          PUKCL _GF2NEcDsaGenerate(u2ModLength) = <Byte length of P>;
          PUKCL _GF2NEcDsaGenerate(nu1CnsBase) = <Base of the ram location of Cns>;
          PUKCL _GF2NEcDsaGenerate(nu1PointABase) = <Base of the A point>;
          PUKCL _GF2NEcDsaGenerate(nu1PrivateKey) = <Base of the Private Key>;




        © 2019 Microchip Technology Inc.                      Datasheet                      DS60001507E-page 1562
                                                           SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

           PUKCL _GF2NEcDsaGenerate(nu1ScalarNumber) = <Base of the ScalarNumber>;
           PUKCL _GF2NEcDsaGenerate(nu1OrderPointBase) = <Base of the order of A point>;
           PUKCL _GF2NEcDsaGenerate(nu1ABase) = <Base of the a parameter of the curve>; PUKCL
           _GF2NEcDsaGenerate(nu1Workspace) = <Base of the workspace>;
           PUKCL _GF2NEcDsaGenerate(nu1HashBase) = <Base of the SHA resulting hash>;
           ...

           // vPUKCL_Process() is a macro command, which populates the service name
           // and then calls the library...
           vPUKCL_Process(GF2NEcDsaGenerateFast, pvPUKCLParam);
           if (PUKCL (u2Status) == PUKCL_OK)
                       {
                       ...
                       }
           else // Manage the error

43.3.7.9.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1PrivateKey, nu1ScalarNumber,
             nu1OrderPointBase,nu1ABase, nu1Workspace or nu1HashBase are not aligned on 32-bit
             boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointABase,
             3*u2ModLength+ 12},{nu1PrivateKey, u2ScalarLength + 4},{nu1ScalarNumber, u2ScalarLength + 4},
             {nu1OrderPointBase, u2ScalarLength + 4}, {nu1ABase, u2ModLength + 4}, {nu1Workspace,
             <WorkspaceLength>} or {nu1HashBase, u2ScalarLength + 4} are not in Crypto RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength +8},
             {nu1PointABase, 3*u2ModLength + 12}, {nu1PrivateKey, u2ScalarLength + 4}, {nu1ScalarNumber,
             u2ScalarLength + 4}, {nu1OrderPointBase, u2ScalarLength + 4}, {nu1ABase, u2ModLength + 4},
             {nu1Workspace, <WorkspaceLength>} and {nu1HashBase, u2ScalarLength + 4}
43.3.7.9.7 Status Returned Values
          Table 43-109. GF2NEcDsaGenerate Fast Service Return Codes

          Returned Status                        Importance Meaning
          PUKCL_OK                               –             The computation passed without problem.
          PUKCL_WRONG_SELECTNUMBER Warning                     The given value for nu1ScalarNumber is not good
                                                               to perform this signature generation.

43.3.7.10 Verifying an ECDSA Signature (Compliant with FIPS 186-2)
43.3.7.10.1 Purpose
          This service is used to verify an ECDSA signature following the FIPS 186-2. It performs the second step
          of the Signature Verification.
          A hash value (HashVal) must be provided as input, it has to be previously computed from the message to
          be signed using a secure hash algorithm.
          As second significant input, the Signature is provided to be checked. This service checks the signature
          and fills the status accordingly.
43.3.7.10.2 How to Use the Service

43.3.7.10.3 Description
          The operation performed is:




         © 2019 Microchip Technology Inc.                    Datasheet                         DS60001507E-page 1563
                                                              SAM D5x/E5x Family Data Sheet
                                                            Public Key Cryptography Controller (PUKCC)

         Verify = EcDsaVerifySignature(PtA, HashVal, Signature, CurveParameters, PublicKey)
         The points used for this operation are represented in different coordinate systems. In this computation,
         the following parameters need to be provided:
           • A the input point is filled with the affine values (X,Y) and Z = 1 (pointed by{nu1PointABase,
             3*u2ModLength + 12})
           • Cns the working space for the Fast Modular Constant not initialized (pointed by
             {nu1CnsBase,u2ScalarLength + 8})
           • P the modulus filled (pointed by {nu1ModBase,u2ModLength +4})
           • The workspace not initialized (pointed by {nu1WorkSpace, 8*u2ModLength +44} The a and b
             parameters relative to the elliptic curve (pointed by {nu1ABase,2*u2ModLength + 8})
           • The order of the Point A on the elliptic curve (pointed by {nu1OrderPointBase,u2ScalarLength +4})
           • HashVal the hash value beforehand generated and filled (pointed by {nu1HashBase,u2ScalarLength
             +4})
           • The Public Key point is filled in “mixed” coordinates (X,Y) with the affine values and Z = 1 (pointed by
             {nu1PointPublicKeyGen, 3*u2ModLength + 12})
           • The input signature (R,S), even if it is not a Point, is represented in memory like a point in affine
             coordinates (X,Y) (pointed by {nu1PointSignature, 2*u2ScalarLength + 8})


                             Important: For the ECDSA signature verification be sure to follow the directives given for
                             the RNG on the chip you use (particularly initialization, seeding) and compulsorily start the
                             RNG.


           • The operation consists in obtaining a V value with all these input parameter and check that V equals
             the provided R. If all is correct and the signature is the good one, the status is set to PUKCL_OK. If
             all is correct and the signature is wrong, the status is set to PUKCL_WRONG_SIGNATURE. If an
             error occurs, the status is set to the corresponding error value (see Status Returned Values below).
         The service name for this operation is GF2NEcDsaVerifyFast. This service uses Fast mode and Fast
         Modular Reduction for computation.
43.3.7.10.4 Parameters Definition
         Table 43-110. GF2NEcDsaVerifyFast Service Parameters

          Parameter                     Type Direction Location      Data Length          Before          After
                                                                                          Executing       Executing
                                                                                          the Service     the Service
          nu1ModBase                    nu1   I         Crypto       u2ModLength + 4      Base of         Base of
                                                        RAM                               modulus P       modulus P
          nu1CnsBase                    nu1   I         Crypto       u2ScalarLength       Base of Cns     Base of Cns
                                                        RAM          +8
          u2ModLength                   u2    I         –            –                    Length of       Length of
                                                                                          modulus P       modulus P
          nu1OrderPointBase             nu1   I         Crypto       u2ScalarLength       Order of the Unchanged
                                                        RAM          +4                   Point A in the
                                                                                          elliptic curve




         © 2019 Microchip Technology Inc.                        Datasheet                        DS60001507E-page 1564
                                                          SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

         ...........continued
          Parameter                    Type Direction Location     Data Length        Before           After
                                                                                      Executing        Executing
                                                                                      the Service      the Service
          nu1PointSignature            nu1   I        Crypto       2*u2ScalarLength   Signature(r,     Corrupted
                                                      RAM          +8                 s)
          nu1HashBase (see             nu1   I        Crypto       u2ScalarLength     Base of the    Corrupted
          Note 1)                                     RAM          +4                 hash value
                                                                                      resulting from
                                                                                      the previous
                                                                                      SHA
          u2ScalarLength               u2    I        –            –                  Length of        Length of
                                                                                      scalar           scalar
          nu1PointABase                nu1   I/O      Crypto       3*u2ModLength      Generator        Corrupted
                                                      RAM          + 12               point
          nu1PointPublicKeyGen nu1           I/O      Crypto       3*u2ModLength      Public point     Corrupted
                                                      RAM          + 12
          nu1ABase                     nu1   I        Crypto       2*u2ModLength      Parameter a      Unchanged
                                                      RAM          +8                 and b of the
                                                                                      elliptic curve
          nu1Workspace                 nu1   I        Crypto       8*u2ModLength      –                Corrupted
                                                      RAM          + 44                                workspace

         Note:
          1. Whatever the chosen SHA, the resulting hash value may have a length inferior or equal to the
               modulo length and be padded with zeros until its total length is u2ModLength + 4.
43.3.7.10.5 Code Example
          PUKCL_PARAM PUKCLParam;
          PPUKCL_PARAM pvPUKCLParam = &PUKCLParam;

          // ! The Random Number Generator must be initialized and started
          // ! following the directives given for the RNG on the chip

          PUKCL (u2Option) = 0;

          // Depending on the option specified, not all fields should be filled PUKCL
          _GF2NEcDsaVerify(nu1ModBase) = <Base of the ram location of P>;
          PUKCL _GF2NEcDsaVerify(u2ModLength) = <Byte length of P>;
          PUKCL _GF2NEcDsaVerify(nu1CnsBase) = <Base of the ram location of Cns>;
          PUKCL _GF2NEcDsaVerify(nu1PointABase) = <Base of the A point>;
          PUKCL _GF2NEcDsaVerify(nu1PrivateKey) = <Base of the Private Key>;
          PUKCL _GF2NEcDsaVerify(nu1ScalarNumber) = <Base of the ScalarNumber>;
          PUKCL _GF2NEcDsaVerify(nu1OrderPointBase) = <Base of the order of A point>;
          PUKCL _GF2NEcDsaVerify(nu1ABase) = <Base of the a parameter of the curve>; PUKCL
          _GF2NEcDsaVerify(nu1Workspace) = <Base of the workspace>;
          PUKCL _GF2NEcDsaVerify(nu1HashBase) = <Base of the SHA resulting hash>;
          ...

          // vPUKCL_Process() is a macro command, which populates the service name
          // and then calls the library...
          vPUKCL_Process(GF2NEcDsaVerifyFast, &PUKCLParam);
          if (PUKCL (u2Status) == PUKCL_OK)
                      {
                      ...




        © 2019 Microchip Technology Inc.                       Datasheet                      DS60001507E-page 1565
                                                            SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

                          }
           else
                       if(PUKCL(u2Status) == PUKCL_WRONG_SIGNATURE)
                       {
                       ...
                       }
           else // Manage the error


43.3.7.10.6 Constraints
          No overlapping between either input and output are allowed. The following conditions must be avoided to
          ensure the service works correctly:
           • nu1ModBase, nu1CnsBase, nu1PointABase, nu1PointPublicKeyGen, nu1PointSignature,
             nu1OrderPointBase,nu1ABBase, nu1Workspace or nu1HashBase are not aligned on 32-bit
             boundaries
           • {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength + 8}, {nu1PointABase,
             3*u2ModLength + 12}, {nu1PointPublicKeyGen, 3*u2ModLength + 12}, {nu1PointSignature,
             2*u2ScalarLength + 8}, {nu1OrderPointBase, u2ScalarLength + 4}, {nu1ABBase, 2*u2ModLength
             + 8}, {nu1Workspace, <WorkspaceLength>} or {nu1HashBase, u2ScalarLength + 4} are not in Crypto
             RAM
           • u2ModLength is either: < 12, > 0xffc or not a 32-bit length
           • All overlapping between {nu1ModBase, u2ModLength + 4}, {nu1CnsBase, u2ModLength +8},
             {nu1PointABase, 3*u2ModLength + 12}, {nu1PointPublicKeyGen, 3*u2ModLength + 12},
             {nu1PointSignature, 2*u2ScalarLength + 8}, {nu1OrderPointBase, u2ScalarLength + 4},
             {nu1ABBase, 2*u2ModLength + 8}, {nu1Workspace, <WorkspaceLength>} and {nu1HashBase,
             u2ScalarLength + 4}
43.3.7.10.7 Status Returned Values
          Table 43-111. GF2NEcDsaVerifyFast Service Return Codes

          Returned Status                   Importance Meaning
          PUKCL_OK                          –             The computation passed without errors. The signature is
                                                          correct.
          PUKCL_WRONG_SIGNATURE Warning                   The signature is incorrect.

43.3.8    PUKCL Requirements and Performance

43.3.8.1 Services Stack Usage
          This library is using the main core to execute its computations, and therefore is also sharing some
          resources with the application.
          It may be important for the application to know RAM usage by the library functions and to be aware that
          the library does not use any global variables.
          The following table provides the minimum number of bytes used by the library that have to be available
          on the stacks to ensure that the functionality can be executed correctly. In some cases, the library may
          use less bytes than the specified number for some options. This table contains estimated values.
          Table 43-112. Services Stack Usage

          PUKCL Service                                                           STACK Usage (Bytes)
          SelfTest                                                                          112
          ClearFlags                                                                         0




         © 2019 Microchip Technology Inc.                    Datasheet                           DS60001507E-page 1566
                                   SAM D5x/E5x Family Data Sheet
                                   Public Key Cryptography Controller (PUKCC)

...........continued
 PUKCL Service                                     STACK Usage (Bytes)
 Swap                                                      8
 Fill                                                      8
 CondCopy                                                  24
 FastCopy                                                  16
 Smult                                                     16
 Smult (with reduction)                                    88
 Comp                                                      8
 Fmult                                                     24
 Fmult (with reduction)                                    96
 Square                                                    16
 Square (with reduction)                                   88
 Div                                                      144
 GCD                                                      136
 RedMod (Setup)                                           160
 RedMod (using fast reduction)                             80
 RedMod (randomize)                                        80
 RedMod (Normalize)                                        80
 RedMod (Using Division)                                  184
 ExpMod                                                   200
 PrimeGen                                                 416
 CRT                                                      304
 ZpEccAddFast                                             104
 ZpEccAddSubFast                                           92
 ZpEcConvProjToAffine                                     280
 ZpEcConvAffineToProjective                                64
 ZpEccDblFast                                              96
 ZpEccMulFast                                             168
 ZpEccQuickDualMulFast                                    216
 ZpEcDsaGenerateFast                                      392
 ZpEcDsaVerifyFast                                        456
 ZpEcDsaQuickVerify                                       368




© 2019 Microchip Technology Inc.     Datasheet                  DS60001507E-page 1567
                                                                   SAM D5x/E5x Family Data Sheet
                                                                Public Key Cryptography Controller (PUKCC)

         ...........continued
          PUKCL Service                                                                STACK Usage (Bytes)
          ZpEcRandomiseCoordinate                                                              56
          GF2NEccAddFast                                                                       128
          GF2NEcConvProjToAffine                                                               264
          GF2NEcConvAffineToProjective                                                         56
          GF2NEccDblFast                                                                       136
          GF2NEccMulFast                                                                       208
          GF2NEcDsaGenerateFast                                                                376
          GF2NEcDsaVerifyFast                                                                  440
          GF2NEcRandomiseCoordinate                                                            56

43.3.8.2 Parameter Size Limits for Different Services
         The following table lists parameter size limits for different services.
         For the services ModExp, PrimeGen, and CRT, additional details are available in the service description.
         Table 43-113. Parameter Size Limits

          API                              Min/Max Sizes                           Comments
          SelfTest                         –                                       –
          ClearFlags                       –                                       –
          Swap                             4 bytes to 2044 bytes                   Per block to be swapped
          Fill                             4 bytes to 4088 bytes                   –
          Fast Copy/Clear                  4 bytes to 2044 bytes                   Supposing Length(R) = Length(X)
          Conditional Copy/Clear           4 bytes to 2044 bytes                   Supposing Length(R) = Length(X)
          Smult                            4 bytes to 2040 bytes                   Supposing Length(R) = Length(X)
                                                                                   + 4 Bytes, No Z Parameter, No
                                                                                   Reduction
          Compare                          4 bytes to 2044 bytes                   Supposing Length(X) = Length(Y)
          FMult                            Input: 4 bytes to 1020 bytes Output:    Supposing Length(Y) = Length(X),
                                           4bytes to 2040 bytes                    No Z Parameter, No Reduction
          Square                           Input: 4 bytes to 1020 bytes            Supposing No Z Parameter, No
                                                                                   Reduction
                                           Output: 4 bytes to 2040 bytes

          Euclidean Division               Divider: 8 to 1016 bytes                Supposing Length(Num) =
                                                                                   2*Length(Divider)
                                           Num.: 8 to 2032 bytes

          Mod. inv. / GCD                  8 to 1012 bytes                         –




        © 2019 Microchip Technology Inc.                              Datasheet                     DS60001507E-page 1568
                                                         SAM D5x/E5x Family Data Sheet
                                                        Public Key Cryptography Controller (PUKCC)

...........continued
 API                               Min/Max Sizes                            Comments
 ModRed                            Modulus: 12 to 1016 bytes                Supposing RBase = XBase
                                   Input: 24 to 2032 bytes

 Fast ModExp Exp in                12 to 576 bytes                          Supposing Length(Exponent) =
 Crypto RAM                                                                 Length(Modulus), Window Size = 1
                                   (96 to 4608 bits)
                                                                            With the Exponent in Crypto RAM

 Fast ModExp                       12 to 672 bytes                          Supposing Length(Exponent) =
                                                                            Length(Modulus), Window Size = 1
 Exp not in Crypto RAM             (96 to 5376 bits)
                                                                            With the Exponent not in Crypto
                                                                            RAM

 Prime Gen.                        Prime Number: 12 to 448 bytes            Supposing Window Size = 1
                                   (96 to 3584 bits)

 CRT                               Modulus = Two Primes:                    Supposing Length(Exponent) =
                                                                            Length(Modulus), Window Size = 1
                                   Size of one prime from 24 to 448 bytes
                                   Modulus = from 48 to 896 bytes
                                   (384 to 7168 bits)

 ECC Addition qnd                  Modulus: 12 to 308 bytes                 –
 Subtraction GF(p)
 ECC Doubling GF(p)                Modulus: 12 to 400 bytes                 –

 ECC Multiplication                Modulus: 12 to 264 bytes                 Supposing Length(Scalar) =
 GF(p)                                                                      Length(Modulus)

 ECC Quick Dual                    Modulus: 12 to 152 bytes                 –
 Multiplication GF(p)
 ECDSA Generate GF(p) Modulus: 12 to 220 bytes                              Supposing Length(Scalar) =
                                                                            Length(Modulus)
                                   (up to 521 bits for common curves)

 ECDSA Verify GF(p)                Modulus: 12 to 188 bytes                 Supposing Length(Scalar) =
                                                                            Length(Modulus)
                                   (up to 521 bits for common curves)

 ECC Addition GF(2n)               Modulus: 12 to 248 bytes                 –

 ECC Doubling GF(2n)               Modulus: 12 to 364 bytes                 –

 ECC Multiplication                Modulus: 12 to 250bytes                  Supposing Length(Scalar) =
 GF(2n)                                                                     Length(Modulus)

 ECDSA Generate                    Modulus: 12 to 208 bytes                 Supposing Length(Scalar) =
 GF(2n)                                                                     Length(Modulus)
                                   (up to 571 bits for common curves)




© 2019 Microchip Technology Inc.                             Datasheet                     DS60001507E-page 1569
                                                                  SAM D5x/E5x Family Data Sheet
                                                                Public Key Cryptography Controller (PUKCC)

         ...........continued
          API                               Min/Max Sizes                        Comments
          ECDSA Verify GF(2n)               Modulus: 12 to 180 bytes             Supposing Length(Scalar) =
                                                                                 Length(Modulus)
                                            (up to 571 bits for common curves)

          ECDSA Quick Verify                Modulus: 12 to 140 bytes             Supposing Length(Scalar) =
          GF(2n)                                                                 Length(Modulus)
                                            (up to 571 bits for common curves)

43.3.8.3 Service Timing
         The values in the following tables are estimated performances for CPU clock of 120 MHz. The CPU and
         PUKCC are operated at the same frequency. Due to possible change in the parameters values, the
         measurements show approximated values.
         Other test conditions:
           • PUKCL library data in Crypto RAM
           • Test code and test data in SRAM
           • ICache and DCache are disabled
43.3.8.3.1 Service Timing for RSA
         RSA uses the ExpMod service for encryption and decryption. Following tables show service timing, where
         ‘W’ indicates window size.
         Table 43-114. RSA1024

          Operation                                                                Clock Cycles Timing one block
          RSA 1024 decryption / signature generation. No CRT, Regular              3.05 MCycles 25.42 ms
          implementation, W=4
          RSA 1024 decryption / signature generation.                              1.04 MCycles 8.67 ms
          With CRT, Regular implementation, W=4

          RSA 1024 encryption / signature verification.                            0.07 MCycles 0.58 ms
          No CRT, Fast implementation, W=1 Exponent=3

          RSA 1024 encryption / signature verification.                            0.07 MCycles 0.58 ms
          No CRT, Fast implementation, W=1 Exponent=0x10001

         Table 43-115. RSA2048

          Operation                                                               Clock Cycles Timing One block
          RSA 2048 decryption / signature generation.                             21.9 MCycles 182 ms
          No CRT, Regular implementation, W=4

          RSA 2048 decryption / signature generation. With CRT, Regular           6.19 MCycles 51.6 ms
          implementation, W=4




         © 2019 Microchip Technology Inc.                          Datasheet                    DS60001507E-page 1570
                                                          SAM D5x/E5x Family Data Sheet
                                                          Public Key Cryptography Controller (PUKCC)

         ...........continued
          Operation                                                           Clock Cycles Timing One block
          RSA 2048 encryption / signature verification.                       0.24 MCycles 2 ms
          No CRT, Fast implementation, W=1 Exponent=3

          RSA 2048 encryption / signature verification.                       0.24 MCycles 2 ms
          No CRT, Fast implementation, W=1 Exponent=0x10001

         Table 43-116. RSA4096

          Operation                                                           Clock Cycles Timing One block
          RSA 4096 Decryption / signature generation. No CRT, Regular         208 MCycles    1.73s
          implementation, W=1
          RSA 4096 Decryption / signature generation. With CRT, Regular       45.5 MCycles 379 ms
          implementation, W=3
          RSA 4096 encryption / signature verification.                       0.92 MCycles 7.67 ms
          No CRT, Fast implementation, W=1 Exponent=3

          RSA 4096 encryption / signature verification.                       0.92 MCycles 7.67 ms
          No CRT, Fast implementation, W=1 Exponent=0x10001

43.3.8.3.2 Service Timing for Prime Generation
         Prime generation uses the PrimeGen service.
         Table 43-117. Prime Generation

          Operation                                                      Clock Cycles         Timing One
                                                                                              Block
          Regular Generation of two primes, Prime_Length=512 bits,       Mean = 47.4          Mean = 0.40s
          W=4, Rabin Miller Iterations Number = 3, (average of 200       MCycles
          samples)
          Regular Generation of two primes, Prime_Length=512 bits,       Std Dev = 30.3       Std Dev = 0.25s
          W=4, Rabin Miller Iterations Number = 3, (Standard Deviation   Mcycles
          for 200 samples)
          Regular Generation of two primes, Prime_Length=1024 bits,      Mean = 448           Mean = 3.73s
          W=4, Rabin Miller Iterations Number = 3, (average of 200       MCycles
          samples)
          Regular Generation of two primes, Prime_Length=1024 bits,      Std Dev = 294        Std Dev = 2.45s
          W=4, Rabin Miller Iterations Number = 3, (Standard Deviation   Mcycles
          for 200 samples)
          Regular Generation of two primes, Prime_Length=2048 bits,      Mean = 4.78          Mean = 39.8s
          W=4, Rabin Miller Iterations Number = 3, (average of 200       GCycles
          samples)




         © 2019 Microchip Technology Inc.                   Datasheet                       DS60001507E-page 1571
                                                         SAM D5x/E5x Family Data Sheet
                                                        Public Key Cryptography Controller (PUKCC)

         ...........continued
          Operation                                                      Clock Cycles          Timing One
                                                                                               Block
          Regular Generation of two primes, Prime_Length=2048 bits,      Std Dev = 3,05        Std Dev = 25.4s
          W=4, Rabin Miller Iterations Number = 3, (Standard Deviation   GCycles
          for 200 samples)

43.3.8.3.3 Service Timing for ECDSA on Prime Field
         In the following table, ECDSA signature generation uses the ZpEcDsaGenerateFast service and
         signature verification uses ZpEcDsaQuickVerify
         Table 43-118. ECDSA GF(p)

          Operation                                              Clock Cycles        Timing One block
          ECDSA GF(p) 256 Generate Fast                          2.72 MCycles        22.7 ms
          ECDSA GF(p) 256 Verify Quick W=(6,6)                   1.78 MCycles        14.8 ms
          Scalar in Classical RAM

          ECDSA GF(p) 256 Verify Quick W=(4,4)                   1.83 MCycles        15.2 ms
          Scalar in PUKCC RAM

          ECDSA GF(p) 384 Generate Fast                          6.28 MCycles        52.3 ms
          ECDSA GF(p) 384 Verify Quick W=(5,5)                   3.93 MCycles        32.8 ms
          Scalar in Classical RAM

          ECDSA GF(p) 384 Verify Quick W=(4,4)                   4.09 MCycles        34.1 ms
          Scalar in PUKCC RAM

          ECDSA GF(p) 521 Generate Fast                          13.4 MCycles        112 ms
          ECDSA GF(p) 521 Verify Quick W=(4,5)                   8.4 MCycles         70.3 ms
          Scalar in Classical RAM

          ECDSA GF(p) 521 Verify Quick W=(4,4)                   8.6 MCycles         72ms
          Scalar in PUKCC RAM

43.3.8.3.4 Service Timing for ECDSA on Binary Field
         In the following table, ECDSA signature generation uses the GF2NEcDsaGenerateFast service and
         signature verification uses GF2NEcDsaVerifyFast
         Table 43-119. ECDSA GF(2n)

          Operation                                            CPU Cycles           Timing One block
          ECDSA GF(2n) B283 Generate Fast                      3.21 MCycles         26.8 ms
          ECDSA GF(2n) B283 Verify                             6.44 MCycles         53.5 ms
          ECDSA GF(2n) B409 Generate Fast                      6.93 Mcycles         57.8 ms




         © 2019 Microchip Technology Inc.                 Datasheet                         DS60001507E-page 1572
                                   SAM D5x/E5x Family Data Sheet
                                   Public Key Cryptography Controller (PUKCC)

...........continued
 Operation                              CPU Cycles     Timing One block
 ECDSA GF(2n) B409 Verify               13.8 Mcycles   115 ms
 ECDSA GF(2n) B571 Generate Fast        15.1 Mcycles   125 ms
 ECDSA GF(2n) B571 Verify               30.1 MCycles   251 ms




© 2019 Microchip Technology Inc.     Datasheet                  DS60001507E-page 1573
