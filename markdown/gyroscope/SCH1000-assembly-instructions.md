# assembly-instructions-for-sch1000

*Source: `assembly-instructions-for-sch1000.pdf` (23 pages) — converted from PDF*


<!-- page 1 -->

1 (23)




ASSEMBLY INSTRUCTIONS FOR SCH1000 SERIES

       Technical Note




       Murata Electronics Oy   SCH1000     Doc.No. 10871
            www.murata.com                 Rev. 4

<!-- page 2 -->

2 (23)



Table of Contents

1     Objective .....................................................................................................................................4
2     Small Outline Integrated Circuit (SOIC) package ......................................................................4
3     SOIC-24 package outline and dimensions ................................................................................5
4     Tape and reel specifications ......................................................................................................6
5     Printed Circuit Board (PCB) design and assembly guidelines ................................................8
    5.1     PCB terminal pad design .......................................................................................................8
    5.2     Passive component placement under component legs ..........................................................8
    5.3     Temperature effects .............................................................................................................10
      5.3.1      General...........................................................................................................................10
      5.3.2      Thermal conductor ..........................................................................................................10
      5.3.3      External heating ..............................................................................................................10
    5.4     De-paneling .........................................................................................................................11
    5.5     Vibration reduction on PCB level..........................................................................................11
      5.5.1      Vibration mechanical range in application and in assembly process ...............................11
      5.5.2      Application and assembly process induced frequencies .................................................11
      5.5.3      Vibration reduction by PCB Design .................................................................................13
      5.5.4      Conformal coating...........................................................................................................17
      5.5.5      Gluing .............................................................................................................................17
    5.6     Solder paste ........................................................................................................................18
    5.7     Stencil and paste printing .....................................................................................................18
    5.8     Paste printing .......................................................................................................................18
    5.9     Component picking and placement ......................................................................................18
    5.10    Reflow soldering ..................................................................................................................19
    5.11    Moisture sensitivity level (MSL) classification .......................................................................20
    5.12    Inspection ............................................................................................................................21
    5.13    Precautions..........................................................................................................................21
      5.13.1         Mechanical shocks and vibration during handling and assembly.................................21
      5.13.2         Chemicals ...................................................................................................................21
      5.13.3         Coatings and nano-coating .........................................................................................22
      5.13.4         Vacuum level ..............................................................................................................22
      5.13.5         ESD ............................................................................................................................22
      5.13.6         Moisture ......................................................................................................................22
      5.13.7         Mechanical stress .......................................................................................................23
      5.13.8         Cleaning .....................................................................................................................23
      5.13.9         Magnetic field..............................................................................................................23

                  Murata Electronics Oy                               SCH1000                               Doc.No. 10871
                       www.murata.com                                                                       Rev. 4

<!-- page 3 -->

3 (23)



6   Rework Guidelines....................................................................................................................23
7   Environmental Aspects ............................................................................................................23
8   References ................................................................................................................................23




                Murata Electronics Oy                              SCH1000                             Doc.No. 10871
                     www.murata.com                                                                    Rev. 4

<!-- page 4 -->

4 (23)



1   Objective
    This document provides required and recommended items and guidelines for Printed
    Circuit Board (PCB) design and assembly of Murata's SCH1000 family components. It
    should be emphasized that this document serves only as a design guideline to help to
    develop the optimal assembly conditions. It is essential that users also use their own
    manufacturing practices and experience to be able to fulfill the needs of varying end-use
    applications.

    Required items must be fulfilled by the user to ensure component operation in
    application. Regarding recommended items, not following the recommendations might
    result in deviations from the specified performance. Required items are marked with
    label (Requirement) and it refers to the previous sentence when it is followed by a
    period. When the label (Requirement) is after a period mark, it refers to the whole
    section. Same notation applies to Recommended items with the label
    (Recommendation). User is responsible to evaluate and qualify implemented application
    design options in the final product.

    This document can be continuously updated in future. Please refer to the latest document.


2   Small Outline Integrated Circuit (SOIC) package
    Figure 1 shows SCH1000 family SOIC-24 package. The package is lead-free, pick-and-
    place mountable, and meets industry standard lead-free soldering processes.




    Figure 1 SOIC-24 package




    Murata Electronics Oy              SCH1000                    Doc.No. 10871
         www.murata.com                                           Rev. 4

<!-- page 5 -->

5 (23)



3   SOIC-24 package outline and dimensions
    The outline and dimensions for the SOIC package are shown in Figure 2.




    Figure 2 Outline of SOIC package. All dimensions are in millimeters. All angles are in
    degrees. Tolerances unless otherwise specified according to ISO2768-f. A sample part
    number for reference only. A 3D model of the component is available upon request.




    Murata Electronics Oy             SCH1000                  Doc.No. 10871
         www.murata.com                                        Rev. 4

<!-- page 6 -->

6 (23)




4   Tape and reel specifications

    Packing tape dimensions are presented in Figure 3. The reel dimensions, unreeling
    direction and component polarity on tape are presented in Figure 5 and
    Table 1 below.




    Figure 3 Packing tape specification. Dimensions are in millimeters [mm]
              Direction of unreeling




                   Pin 1
    Figure 4 Component position in carrier tape




    Murata Electronics Oy              SCH1000                 Doc.No. 10871
         www.murata.com                                        Rev. 4

<!-- page 7 -->

7 (23)




Figure 5 General figure of packing reel

Table 1. Packing reel dimensions [mm]
 A          N            W1                    W2max   M
 330             1001   32.4 (-0/+2.0)        38.4     13 (-0.2/+0.5)




Murata Electronics Oy                SCH1000               Doc.No. 10871
     www.murata.com                                        Rev. 4

<!-- page 8 -->

8 (23)



5     Printed Circuit Board (PCB) design and assembly guidelines

5.1   PCB terminal pad design

      PCB terminal pads should be wider than package lead to improve solder joint quality
      and reliability. A reference PCB terminal layout is presented in Figure 6. Note that pad
      design can be customized to suit PCB requirements. (Recommendation).




      Figure 6 Reference pad layout

      Pad metallization must be solder wettable to assure good quality solder joints.
      Recommended circuit board finishes for SMD soldering are NiAu, OSP, electroless-Ag
      and electroless-Sn.

5.2   Passive component placement under component legs
      Due to the SCH1000 component design, space is left between the component legs and
      PCB. If it is considered feasible for the PCB design and assembly line, this space may
      be utilized for passive components. Murata has verified concept with simulations and
      test PCBs but does not take responsibility of assembly or operation failures related to
      placement of passive components under component. Effect of component gluing and/or
      coating and using thermal pads with passives underneath component legs must also be
      evaluated separately.




      Murata Electronics Oy             SCH1000                  Doc.No. 10871
           www.murata.com                                        Rev. 4

<!-- page 9 -->

9 (23)




Figure 7 Schematic of passive component placement concept




Figure 8 Area available for passive components. All measurements are in millimeters
[mm]

If passive components are soldered under the SCH1000 component it must be done
prior to soldering of the component. The passive components must be also considered
in pick and place process as per chapter 5.9 (Requirement).

Placing passive components under the SCH1000 may affect the ability to make solder
quality control. Using X-ray to inspect solder quality may be necessary
(Recommendation).




Murata Electronics Oy            SCH1000                  Doc.No. 10871
     www.murata.com                                       Rev. 4

<!-- page 10 -->

10 (23)



5.3     Temperature effects
5.3.1   General
        Arrangement of mounted parts on front and back surfaces and their coefficients of
        thermal expansion (CTE) should be considered to reduce PCB warpage. Conductor
        occupancy for front and back side of the PCB should be similar to minimize PCB
        warping. Heat resistant board types should be used to reduce warpage. Prevention
        mechanisms, such as PCB fixture tools can be used to reduce PCB warping during
        reflow. (Recommendation).

        Heating effect of other components shall be considered when designing the PCB. It is
        not recommended to expose the SCH1000 component to uneven heating. When using
        multiple SCH1000 components, it is recommended that all components would
        experience a similar heat load to retain the greatest accuracy. This is especially
        important if the data from multiple components is used in comparison with each other.
        (Recommendation).

5.3.2   Thermal conductor
        A thermal pad may be applied underneath the component to improve heat flux. A
        thermal pad may also reduce housing resonance accelerations and shift housing
        resonances to higher frequencies.
            • Thermal pad material
                  o The pad material shall not be conductive to avoid risk for short circuit
                      between component legs.
                  o The pad should not contain prohibited contaminants.
                  o Murata does not provide recommendations for thermal pad material.

             •   Pad geometry
                    o The pad must be applied before soldering process. The pad height
                       should be chosen so that the paste will not spread into contact with legs,
                       but still provides adequate and even contact area on the bottom lid.
                    o The thermal pad should be axially symmetrical and have an even height.

             •   Pad effect on component performance
                    o User is responsible to validate functionality and performance of sensor if
                        a thermal pad is used (Requirement)
                    o See also chapter Precautions

        Customer must confirm reliability of their thermal pad applying process by adequate
        reliability testing (thermal pad may be subjectable to lifetime effects). Care must be
        taken that system resonance frequencies are not shifted to prohibited frequency bands.
        For further instructions about vibration reduction, please refer to chapter 5.5.

5.3.3   External heating
        If external heating and/or cooling is applied to the component, all temperature effects
        mentioned previously in this chapter must be considered. The effect of external
        heating/cooling to component must be assessed separately.




        Murata Electronics Oy              SCH1000                  Doc.No. 10871
             www.murata.com                                         Rev. 4

<!-- page 11 -->

11 (23)



5.4     De-paneling
        PCB de-paneling is a source of mechanical or vibrational stress to the SCH1000
        component. PCB panel breakout tabs should be designed with minimum width and
        SCH1000 components should not be placed near the tabs. Holes on breakout tabs are
        not recommended when cutter, saw, or router is used for de-paneling, because the
        holes can increase the number of vibrational spikes. (Recommendation).

5.5     Vibration reduction on PCB level
        Performance might be inferior if the application PCB induces high resonance gain to the
        sensor component. Therefore, properly designed PCB attachment points together with
        PCB layout is of utmost important for applications that are intended to be used at
        vibrating environment.

5.5.1   Vibration mechanical range in application and in assembly process
        It is recommended that user measures the resonance gain over frequency from the
        vicinity of the SCH1000 component at the application and in assembly process. In order
        to maintain proper operation of the sensor, the g-values at the application use
        environment must not exceed the specified mechanical range of the sensor component
        (refer to the component datasheet and chapters "Vibration reduction on PCB level" and
        "Precautions" of this document) (Requirement).

        For example, PCB resonance modes can amplify external harmonic vibrations that can
        cause excessive vibration input to sensor component that exceeds the specified
        mechanical range. Murata cannot guarantee operation in conditions where the
        mechanical range of SCH1000 component is exceeded and takes no responsibility if
        sensor operation failure occurs in such cases.

5.5.2   Application and assembly process induced frequencies
        Sensor component can have adverse performance if the application or assembly
        process induces vibration peaks at critical frequency bands of the sensor component. It
        is advised that application and assembly process induced vibrational peak frequencies
        at the vicinity of the SCH1000 component should not overlap with Table 2 frequencies.
        Such vibration peaks can be caused by e.g., natural modal resonances of the use
        application's structures (PCB, lid, casing, mechanical fixtures) or other components at
        the use environment.

        Table 2 Murata recommends to design PCB and system so that they don’t have
        resonance frequencies in these frequency bands (Recommendation). Vibration at these
        frequency bands may be visible in component output.

         Frequency bands to avoid by component linear excitation direction
                     X                         Y                            Z
              9.5 kHz ± 1 kHz           8.6 kHz ± 1 kHz              12.2 kHz ± 1 kHz
                                       23.6 kHz ± 1.5 kHz
             27.8 kHz ± 1 kHz                  -                            -
                                        37 kHz ± 2 kHz




        Murata Electronics Oy             SCH1000                  Doc.No. 10871
             www.murata.com                                        Rev. 4

<!-- page 12 -->

12 (23)




Figure 9 Preferred maximum linear acceleration during production process based on
simulations and verified with practical tests. Prolonged vibration exceeding this curve
may cause damage to sensor (Murata has verified that 10 g @ 5 kHz-50 kHz vibration
with 2000 Hz/min sweep doesn’t damage the sensor). This curve contains safety
margin, but Murata recommends operating under the accelerations specified in this
graph. (Recommendation).




Murata Electronics Oy              SCH1000                  Doc.No. 10871
     www.murata.com                                         Rev. 4

<!-- page 13 -->

13 (23)



5.5.3   Vibration reduction by PCB Design
        PCB design has a major impact on system level performance for applications that are
        intended to be used at vibrating environment.

        PCB properties
          • Symmetricity
                 o Murata recommends using symmetrically shaped PCB to minimize the
                      potential number of vibrational modes on system level.




        Figure 10 PCB symmetry

        PCB attachment
          • The distance from attachment points to the component (e.g. free span) affects
              stiffness, fundamental frequency and damping properties of the PCB that the
              component experiences. In general, the center part of the PCB is more exposed
              to Z-directional acceleration than PCB edges, therefore recommendation is to
              prefer PCB edge areas for inertial sensor location than center area.




        Figure 11 PCB attachment point distance effect



        Murata Electronics Oy            SCH1000                Doc.No. 10871
             www.murata.com                                     Rev. 4

<!-- page 14 -->

14 (23)



     •   Attachment method and the amount and location of attachment points have a
         major effect on the PCB behavior.
             o Increased amount of attachment points in preferably symmetric locations
                stiffens the PCB and has potential for improving vibration behavior.
             o It is recommended to minimize free span over inertial sensor component
                by adding extra fastening points around sensor component.
             o Secure and tight fastening of PCB to system minimizes the movement of
                PCB and excitation of vibration modes.
             o Always use high stiffness attachment method like thick screws or similar,
                to attach the PCB to next level system. Using of loose attachment
                method, e.g., press fit contacts, for mechanical mounting of PCB will
                increase risk of high amplitude PCB vibration modes that can cause
                sensor operation failure.




Figure 12 PCB attachment point location effect




Figure 13 PCB attachment point type effect




Murata Electronics Oy              SCH1000                  Doc.No. 10871
     www.murata.com                                         Rev. 4

<!-- page 15 -->

15 (23)



PCB size and thickness (cross-sectional area)
  • Cross-sectional area affects stiffness, fundamental frequency, and damping
      properties of the PCB. In general
          o Smaller PCB size will have lower Z-directional amplitude and higher
              vibrational frequencies.
          o Thicker PCB will increase vibrational frequencies.
          o Number of copper layers stiffens PCB and increases vibrational
              frequencies.
  • PCB size and thickness should be chosen so that the PCB resonances will not
      overlap with Table 2 frequencies.




Figure 14 PCB size and thickness

PCB material
  • Elastic modulus affects stiffness, fundamental frequency, and damping
     properties of the PCB. In general, high modulus material will
         o increase PCB stiffness.
         o increase vibrational frequencies.
         o decrease damping properties of PCB.
         o If the PCB is too flexible, it can be artificially stiffened using PCB
             stiffening ribs.




         Figure 15 PCB material property effect to vibration performance


Murata Electronics Oy              SCH1000                  Doc.No. 10871
     www.murata.com                                         Rev. 4

<!-- page 16 -->

16 (23)



PCB attachment
  • Rubber dampers/vibration mounts at the attachments can reduce high frequency
      vibrations.
          o It is possible to use rubber dampers at module level also.
          o Good shock isolator is not always a good vibration isolator due to
              dynamic strain properties of elastomers.
  • If PCB is attached using screws, the screw material and screw length has an
      effect on the vibration behavior.
  • PCB edge guides have a slight effect on the vibration behavior.

Effect of other components
    • To avoid dynamic coupling, the resonances of other components near SCH1000
        components should be at least one octave away from the resonance bands
        defined in Table 2
            o If it is not possible to avoid these components or resonances cannot be
                tuned, the components should be laid out as far away from each other as
                possible.
    • High mass components should be laid out on the PCB symmetrically.




Figure 16 Effect of other components



Murata Electronics Oy             SCH1000                 Doc.No. 10871
     www.murata.com                                       Rev. 4

<!-- page 17 -->

17 (23)



5.5.4   Conformal coating
        Conformal coating reduces housing resonance accelerations and shifts housing
        resonances to higher frequencies. If conformal coating is used for vibration reduction,
        several effects should be considered:

             •   Coating thickness
                    o A thick coating usually reduces vibrations better than a thin coating.

             •   Coating material
                    o Polyurethane and silicone based conformal coatings are known to be
                        good materials for vibration reduction.
                    o When choosing a coating material, the most important properties in
                        vibration point of view are coating's ability to form a thick layer and elastic
                        modulus of the coating.
                    o Coating material should not contain prohibited contaminants.

             •   Symmetricity and area of the coating
                    o There is a major difference if the whole component is coated vs body
                      only/legs only.
                    o Coating should be axially symmetrical i.e., spraying process should be
                      well controlled.

             •   Coating effect on component performance
                    o User is responsible to validate functionality and performance of sensor if
                        conformal coating is used (Requirement)
                    o See also chapter Precautions

        Customer must confirm reliability of their conformal coating by adequate reliability
        testing. Customer should avoid shifting system resonance frequencies to the critical
        frequency bands shown in Table 2. (Recommendation).

5.5.5   Gluing
        Due to the component design, gluing component body to the PCB is not recommended.
        The metal lid on the bottom of the component may experience stress from the glue,
        especially if exposed to a temperature gradient. This may in worst case lead to
        detachment of lid, component, or glued interface. Component legs can be glued after
        the SMT solder process by dispensing a large amount of glue on the legs.

        If gluing is used for vibration reduction despite the recommendation, several effects
        should be considered:

             •   Glue material
                    o Softer materials usually reduce vibration more than rigid materials
                       (difference in elastic modulus)
                    o All glues do not have adequate adhesion to component body or PCB.
                    o The glue should not contain prohibited contaminants.

             •   Glue geometry
                    o If glue is dispensed before soldering process, the glue dot height should
                        be chosen so that the glue will not spread into contact with legs (but still
                        providing adequate contact area on the component body)
        Murata Electronics Oy                SCH1000                    Doc.No. 10871
             www.murata.com                                             Rev. 4

<!-- page 18 -->

18 (23)



                    o    Murata does not recommend using only one large glue drop under
                         component.
                    o    Gluing should be axially symmetrical. If multiple glue dots are used, the
                         dot height and dot positioning should be even.
                    o    Underfill type of hard full bottom area attachment is not recommended.

           •   Gluing effect on component performance
                  o User is responsible to validate functionality and performance of sensor if
                      component gluing is used (Requirement)
                  o See also chapter Precautions

      Customer must confirm reliability of their gluing process by adequate reliability testing
      (gluing may brake over lifetime). Care must be taken that system resonance frequencies
      are not shifted to prohibited frequency bands.

5.6   Solder paste
      Recommended solder paste for the SOIC package is near eutectic lead-free SAC (tin-
      silver-copper) solder with melting point between 217–221ºC.

      A no-clean solder paste is required as washing the component is not allowed.

      Ultrasonic agitation is strictly prohibited for Murata's MEMS components since it can
      destroy the MEMS structures (Requirement).

5.7   Stencil and paste printing
      It is recommended to apply solder paste onto the PCB using stencil printing. Minimum
      stencil thickness that can be applied is 0.125 mm (Recommendation). Customer should
      validate system level reliability and vibration performance with their method of solder
      paste printing.

5.8   Paste printing
      The paste printing speed should be adjusted according to the solder paste
      specifications. It is recommended that proper care of printing speed is taken during the
      paste printing to ensure correct paste amount, shape, position, and other printing
      characteristics. Neglecting any of these can cause open solder joints, bridging, solder
      balling, or other unwanted soldering results.

5.9   Component picking and placement
      Typically, SOIC package is picked from the carrier tape using vacuum assist type pick
      heads. It is recommended to test different pick-up nozzles to ensure accurate placement
      of the component.

      Placement should be done with modern automatic component pick & place machinery
      using vision systems. Recognition of the packages automatically by a vision system
      enables correct centering and orientation of packages.

      Force during placement of the component must be adjusted to not cause damage to the
      component. Additionally, if passive components are placed under the component
      according to proposition in chapter 5.2, the trajectory of the pick and place nozzle and
      placement force and accuracy must be optimized to not damage these components.
      Murata Electronics Oy                 SCH1000                  Doc.No. 10871
           www.murata.com                                            Rev. 4

<!-- page 19 -->

19 (23)




5.10   Reflow soldering
       A forced convection reflow oven is recommended to be used for soldering SOIC
       components. IR-based reflow ovens are not generally suitable for lead-free soldering.
       Figure 7 presents a general forced convection reflow solder profile and it also shows the
       typical phases of a reflow process. The reflow profile used for soldering the SOIC
       package should always follow the solder paste manufacturer's specifications and
       recommended profile. Note that washing of the component is not allowed
       (Requirement).

       Too high a reflow peak temperature can have an adverse effect on the sensor
       performance. The peak reflow temperature measured from the top of the package body
       should not exceed 250°C and the time at the package peak temperature of 250 +0/-5°C
       should not exceed 30 seconds (Recommendation). The absolute maximum package
       peak temperature of SCH1000 component is 260°C and time within the temperature of
       260 +0/-5°C must not exceed 30 seconds (Requirement). Murata cannot guarantee
       operation in the case when the package peak temperature specification is exceeded and
       takes no responsibility if sensor operation failure occurs in such a case.

       Maximum number of reflow cycles for SCH1000 components is three (Requirement).

       Reflow soldering with vacuum condition is not guaranteed by Murata. If reflow soldering
       with vacuum conditions is used, customer should confirm reliability of the reflow process
       by adequate reliability testing. (Recommendation).




       Figure 17 Typical convection reflow soldering phases and profile

       PCB boards can have a large temperature variance over the board area during reflow
       due to uneven thermal mass distribution and oven properties. User should measure
       package peak temperature (peak reflow temperature) and solder joint temperature
       profiles at various locations on the board to ensure correct conditions for package
       integrity, solder joint formation, and component self-alignment.


       Murata Electronics Oy              SCH1000                  Doc.No. 10871
            www.murata.com                                         Rev. 4

<!-- page 20 -->

20 (23)



       Reflow profile measurements should be made with thermocouples following the
       guidelines described in JEDEC JEP140: Beaded Thermocouple Temperature
       Measurement of Semiconductor Packages. Package peak temperature is measured
       from the center top surface of the component and solder joint temperature is measured
       directly from the solder joint contact. Fixing of a thermocouple should be made with
       minimum amount of thermally conductive attachment medium. Large measurement error
       may result if the thermocouple is fixed with media having low thermal conductivity, such
       as polyimide tape. Temperature profiles should be adjusted across the whole PCB to
       minimize temperature gradient across the circuit board and to provide proper soldering
       temperature profile of all solder joints. Extreme caution must be used if the circuit board
       contains components with highly different thermal masses. (Recommendation).


5.11   Moisture sensitivity level (MSL) classification
       The Moisture Sensitivity Level of the SOIC component is Level 3 according to the
       IPC/JEDEC J-STD-020E. The parts are delivered in a dry pack.

       Following instruction shall be followed:

       1. Calculated shelf life in sealed bag: 12 months at < 40 °C and < 90% relative humidity
          (RH) (Requirement).

       2. Maximum package peak temperature for the package is 260°C, maximum package
           peak temperature time is 30sec within 260 +0/-5°C, measured from the package top
           surface (Requirement).

       3. After bag is opened, devices that will be subjected to reflow solder or other high
           temperature process must be

           a) Stored at <10%RH
           or
           b) Mounted within 168 hours of factor conditions ≤30 °C/60%RH. (Requirement)

           Note: Do not re-store devices that have exposed >10% RH conditions.

       4. Devices require bake, before mounting, if:

           a) Humidity Indicator Card is > 10% when read at 23 ± 5 °C
           b) 3a or 3b not met. (Requirement)

       5. If baking is required, minimum baking time is 96 hours at 85°C ≤5%RH
          (Requirement).

           Note: Also Tape&Reel materials are applicable for baking at 85°C.

       6. Long-term storage of components shall always be within sealed dry bag
          (Requirement).

       7. To guarantee lifetime targets following storage conditions for sealed vacuum dry
          packed components shall be applied: +15°C to 40°C, humidity ≤ 60% RH
          (Requirement).

       Murata Electronics Oy               SCH1000                  Doc.No. 10871
            www.murata.com                                          Rev. 4

<!-- page 21 -->

21 (23)



         8. The buildup of impureness on soldering pins from atmosphere can affect
            solderability. The storage time without vacuum package should be minimized. The
            maximum storage time without vacuum package must not exceed 6 months
            (Requirement).

         9. Maximum storage time before soldering: 1 year (Recommendation), 2 years
            (Requirement).

         Note: Packing materials and procedures according to IPC/JEDEC J-STD-033D
         Note: Level and body temperature defined by IPC/JEDEC J-STD-020E

5.12     Inspection
         Optical and visual inspection of solder joints can be done easily, because the solder
         joints are clearly seen. A visual inspection of the solder joints with conventional AOI
         (automatic optical inspection) system can be used. Also X-ray inspection can be used.

         Cross-sectional analysis is also an approved method to inspect how well solder has
         wetted the pads of component. Cross-sectional analysis is not used for production
         inspection, but if required, it can be used to establish and optimize the component
         assembly process parameters.

5.13     Precautions
         MEMS sensors are mechanically and electrically sensitive components. Following
         sections describe precautions for sensor component. Exceeding any of these limits or
         neglecting these guidelines may lead to immediate malfunction of the sensor component
         or malfunction that occurs after a period. Murata does not take any responsibility if there
         has been any violation against these precautions.

         The reliability requirements for the devices are applied and validated according to AEC-
         Q100 Rev. H.

5.13.1   Mechanical shocks and vibration during handling and assembly
         Shocks may cause mechanical damage to the internal structures of MEMS sensor,
         causing malfunction of sensor, therefore mechanical shocks should be avoided. The
         level depends heavily on the pulse width and shape and should be evaluated case by
         case. As a general guideline, the lighter assembly or part, the higher shock levels will be
         generated on sensor component.

         Any dropped component shall not be used and shall be scrapped (Requirement).

         Sensor components are mechanical devices and especially sensitive to repetitive
         vibrations and shocks, therefore vibration of the device should be avoided both prior to
         and during assembly. Many assembly processes can induce vibration, typical ones
         being PCB singulation, dropping or knocking parts on hard surfaces, transportation,
         friction welding, ultra-sonic cleaning, and usage of pneumatic wrenches.

5.13.2   Chemicals
         Sensor components shall not be exposed to (Requirement):
         • Chemicals which are known to react with silicones, such as solvents. These are for
            example used in various cleaning processes.
         Murata Electronics Oy              SCH1000                   Doc.No. 10871
              www.murata.com                                          Rev. 4

<!-- page 22 -->

22 (23)



         •    Chemicals with high impurity levels, such as Cl-, Na+, NO3-, SO4-, NH4+
         •    Pressurized low molecular gas such as He or H2, used for example in leak test for
              hermetical sealing.
         •    Materials with high amount of volatile content, like solvents.

         Materials containing halogens (F, Br, I or Cl), halides, their compounds or phosphorus
         containing materials (such as in flame retardants, thermal stabilizers in plastics, Bromine
         in PCB material or halogens/halides in soldering paste) shall be avoided in close vicinity
         of sensor component. (Requirement).

         If heat stabilized polymers are used in application, user should check that iodine, or
         other halogen, containing additives are not used. Halogen free solder paste classified by
         IEC61249-2-21 may have Iodine additive instead of limited Cl and Br in the IEC
         standard (Br<900ppm, Cl<900ppm and Br + Cl <1500ppm). Iodide compounds are
         known to cause corrosion issues with gold aluminum interconnects. User should also
         check that excessive amount of I, Br or other halogen containing additive are not used
         (Requirement: zero iodine, no intentional use in user application). Quantitative value is
         depending on number of factors, including the total volume of such halogen material,
         stability of halogen within material, hermeticity level of application and temperature,
         among others. (Requirement).

         Life-time reliability tests should always be performed at application level to validate the
         end product against life-time requirements/mission profile, as corrosion effects heavily
         depend on the final construction of application, temperature, time and other application
         specific factors.

5.13.3   Coatings and nano-coating
         User has the responsibility to validate use of any material or structure that modifies
         mechanical connection between the sensor and the PCB, e.g., coating, lacquering, or
         gluing to PCB. (Requirement). However, Murata has verified that a nano-coating type
         coating does not affect the component over temperature or lifetime performance.

5.13.4   Vacuum level
         Performance of SCH1000 components at high vacuum conditions is not guaranteed by
         Murata. User is responsible to validate functionality and performance of sensor if it is
         exposed to or used under high vacuum levels. (Requirement).

5.13.5   ESD
         Sensor components are electrical devices. Sensor components should be handled
         under good ESD practices and ESD discharges should be avoided. The following
         numbers are absolute maximum ratings:

         •    ±500 V charged device model, ±750 V for corner pins device model (Requirement).
         •    ±2 kV human body model (Requirement).

5.13.6   Moisture
         Sensor components are moisture sensitive devices, classified as MSL3 level. Guidelines
         defined by PC/JEDEC J-STD-033 shall be followed (Requirement).


         Murata Electronics Oy               SCH1000                   Doc.No. 10871
              www.murata.com                                           Rev. 4

<!-- page 23 -->

23 (23)



5.13.7   Mechanical stress
         Mechanical stress due to PCB bending, molding, coating, and potting may affect the
         sensor performance. Excessive stress due to PCB bending shall be avoided
         (Recommendation). User is responsible to validate functionality and performance of
         sensor if molding or potting material is used (Requirement).

         PCB bending over the sensor area should be limited to 1.0% (Recommendation). User
         is responsible to validate functionality and performance of sensor due to PCB bending
         (Requirement).

5.13.8   Cleaning
         Ultrasonic cleaning is strictly prohibited (Requirement).
         Items listed in “Precautions” section are applicable for cleaning. In addition to ultrasonic
         cleaning other types of cleaning might have negative effects on the component
         performance or functionality. Murata recommends validating following cleaning
         procedures (Recommendation):
         - Wet cleaning with solvent
         - High velocity or pressure air blowing
         - Plasma cleaning with vacuum

5.13.9   Magnetic field
         Avoid operation the sensor in a strong magnetic field (Recommendation).

6        Rework Guidelines
         If it becomes necessary to detach a SCH1000 component from a PCB, the preferred
         way to remove the component is by hot air. The part together with the PCB must be
         dried in an oven at 95°C +/- 5°C for 48 hours +5/-0 hours and detachment must be
         made within 168 hours after the drying is completed (Recommendation).

         A detached component cannot be re-used and must be scrapped (Requirement).

7        Environmental Aspects
         Murata Electronics Oy respects environmental values and thus, its SOIC packages are
         lead-free, Halogen free and RoHS and China RoHS compatible. Murata Electronics’
         sensors should be soldered with lead-free solders to guarantee full RoHS compatibility
         (Recommendation).

8        References
         JEDEC / Electronic Industries Alliance, Inc. Moisture/Reflow Sensitivity Classification for
         Non-Hermetic Solid State Surface Mount Devices (J-STD-020E).

         Handling, Packing, Shipping and Use of Moisture/Reflow Sensitive Surface Mount
         Devices (IPC/JEDEC J-STD-033).

         JEDEC Solid State Technology Association. Beaded Thermocouple Temperature
         Measurement of Semiconductor Packages (JEDEC JEP140).

         Murata Electronics Oy reserves all rights to modify this document without prior notice.

         Murata Electronics Oy              SCH1000                    Doc.No. 10871
              www.murata.com                                           Rev. 4