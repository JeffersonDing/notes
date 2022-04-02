# Unit 4: Waves

## Oscillations, Vibrations and Waves

When an object vibrates back and forth or up and down with a regular repeating motion we describe it as oscillations. A pendulum, a mass attacked to a spring are examples of oscillation.  
![](src/waves20220331184624.png)

### Properties of oscillation

-    **Displacement (x)**: The distance from the equilibrium position at an instant in time measured in metres, m.
-    **Amplitude (A)**: The amplitude of an oscillator is the maximum displacement of the particles from the equilibrium position measured in metres, m.
-    **Period (T)**: The (Time) period is the time it takes for one complete oscillation to happen often measured as the time it takes to oscillates from one point back to the same point in the next cycle. Period is in seconds, s.
-    **Frequency (f)**: Frequency is a measure of how often something happens, in this case how many complete oscillations occurs in one second. It's liked to period of the wave by the following equation: $T=\frac{1}{f}$ or $f=\frac{1}{T}$ Frequency is measure in Hertz, Hz
-    **Phase Difference**: The measure of how "in step" different particles are. If they are moving together they are said to be in phase. If not they are said to be out of phase. Phase difference is measured in radians, rad.

## Simple Harmonic Motion

In each of the simple harmonic motion oscillators shown above, the object is oscillating back and forth or up and down with a **constant** time period.

### SMH Characteristics

The equilibrium point is where the object comes to rest. If we displace the object by $x$ metres there will be a force that brings the object back to the equilibrium point. We can represent this as

$$
F\ \alpha-x
$$

Since $F=ma$ and the mass of the object is constant, we can also write

$$
a\ \alpha-x
$$

Thus we can see that for an object to be moving in SMH:

1. The acceleration is proportional to the displacement
2. The acceleration is always towards the equilibrium (opposite to the displacement)

This means if we graph the acceleration $a$ against displacement $x$ we will get the following graph  
![](src/waves20220331201158.png)

### Equations for SMH

The following equations are for all SHM systems but consider a simple pendulum and a mass on a spring hanging from the ceiling.

#### Period

The period of a SHM depends on the type of SHM system but in the case of a pendulum the equation for the period is

$$
T=2\pi\sqrt{\frac{l}{g}}
$$

where $l$ is the length of the string attacked to the mass and $g$ the gravitational constant.  
However, the period in a SHM where a mass is attached to a string, the period is calculated as

$$
T=2\pi\sqrt{\frac{m}{k}}
$$

where $m$ is the mass and $k$ is the spring constant.
Looking at a mass attached to a spring, we can also use `Hooks Law` to see that the acceleration is in fact proportional and opposite to displacement

$$
\begin{align*}
F&=-kx\\
F&=ma\\
a &= -\frac{k}{m}x
\end{align*}
$$

#### Displacement

The displacement of the mass on the pendulum or the spring $x$ is given by the equation

$$
x = A\cos{2\pi ft}
$$

and since frequency $f=\frac{1}{T}$, the equation can also become

$$
x = A\cos{2\pi\frac{t}{T}}
$$

Where $t$ is the time into the cycle and $T$ is the period for one complete cycle and $A$ is the amplitude of the wave.

#### Velocity

The velocity of the mass at displacement $x$ can be calculated by

$$
v = \pm2\pi f\sqrt{A^2-x^2}
$$

Maximum velocity occurs when the pendulum is at equilibrium (lowest point) or the mass on the spring is at equilibrium (middle) where displacement is 0.

#### Acceleration

The acceleration of the mass at displacement $x$ is given by

$$
a = -(2\pi f)^2x
$$

We can see that acceleration is always the opposite direction of displacement. Maximum acceleration occurs at the end of the swings in a pendulum and at the highest and lowest point of the mass on a spring when displacement is equal to the Amplitude.

### SHM Graphs

When released from A the bob accelerates and moves to the centre point. When it reached B it has reached a maximum velocity in the positive direction and then begins to slow down. At C it has stopped completely so the velocity is zero, it is at a maximum displacement in the positive and accelerates in the negative direction. At D it is back to the centre point and moves at maximum velocity in the negative direction. By E the velocity has dropped to zero, maximum negative displacement and a massive acceleration as it changes direction. This repeats as the pendulum swings through F, G, H and back to I.  
![](src/waves20220331203138.png)  
Below are the graphs of displacement, velocity and acceleration:  
![](src/waves20220331203211.png)

#### Gradients of the Graph

-    Since $v=\frac{\Delta x}{\Delta t}$, the gradient of the displacement time graph gives us the velocity. The velocity graph is the derivative of the displacement graph. As shown, the gradient at point A,C,E,G,I are all 0 thus velocity is also 0.
-    Since $a=\frac{\Delta v}{\Delta t}$, the gradient of the velocity time graph gives us the acceleration. The acceleration graph is the derivative of the velocity time graph. As shown, at points B,D,F,H the gradient of velocity graph is 0 thus acceleration is 0.

#### Energy in SHM

When talking about Energy and Waves:

1. All waves require a medium to travel except Electromagnetic Waves
2. The speed of a wave is the speed which energy is transferred. It only depends on the medium.
3. Traveling waves transmit energy.

In all simple harmonic motion systems,there is a conversion between kinetic energy and potential energy. The total energy of the system remains **constant**. (This is only true for isolated systems) For a simple pendulum there is a transformation between kinetic energy and gravitational potential energy.

At its lowest point it has minimum gravitational and maximum kinetic, at its highest point (when displacement is a maximum) it has no kinetic but a maximum gravitational. This is shown in the graph.

For a mass on a spring there is a transformation between kinetic energy, gravitational potential energy and the energy stored in the spring (elastic potential). At the top there is maximum elastic and gravitational but minimum kinetic. In the middle there is maximum kinetic, minimum elastic but it still has some gravitational. At its lowest point it has no kinetic, minimum gravitational but maximum elastic.  
![](src/waves20220331203920.png)

Below is a graph of the energy of the mass graphed with displacement over time:
![](src/waves20220331210125.png)

As shown, the energy of the system is proportional to the amplitude squared $E\ \alpha A^2$ and **NOT** the frequency counter to popular belief.

## Traveling Waves

Traveling waves transport energy from one area of space to another, whereas standing waves do not transport energy. Traveling waves are not confined to a given space along the medium like an ocean wave.

### Longitudinal Waves

Here is a longitudinal wave; the oscillations are parallel to the direction of propagation (travel). Think about a slinky or sound waves.

Where the particles are close together, we call a **compression** and where they are spread, we call a **rarefaction**. The wavelength is the distance from one compression or rarefaction to the next. The amplitude is the maximum distance the particle moves from its equilibrium position to the right of left.  
An example of this would be sound waves. A sound wave approximately travels at $343.2\ ms^{-1}$ at $20\degree C$.  
![](src/waves20220331210918.png)

### Transverse Waves

Here is a transverse wave; the oscillations are perpendicular to the direction of propagation. Think about a string. Where the particles are displaced above the equilibrium position, we call a **crest** and below we call a **trough**. The wavelength, $\lambda$, is the distance from one peak or trough to the next. The amplitude is the maximum distance the particle moves from its equilibrium position up or down.
An example would be water waves or EM waves.
![](src/waves20220331211027.png)

### Electromagnetic Spectrum

Electromagnetic waves are transverse waves produced by oscillating and magnetically fields. It doesn't need a medium to transfer energy. The image below shows the EM spectrum from low frequency, low energy, long wavelength to high frequency, high energy and short wavelength.
![](src/waves20220331211649.png)
EM waves have two components, a vertical and horizontal component. The vertical component is often the Electric component and horizontal the Magnetic component. All EM waves travel at the speed of light $3.8 \times 10^8\ ms^{-1}$.
![](src/waves20220331211918.png)

### The Universal Wave Equation

The wave speed of a wave $v$, it’s frequency $f$ and it’s wavelength $\lambda$, are related by the equation:

$$
V=f\lambda
$$

Where $V$ is the speed of the wave in $ms^{-1}$, frequency in $Hz$ and wavelength in $m$.

### Wave Characteristics

#### Wavefronts and Rays

-    **Wavefronts**: are lines joining points which vibrate in phase with each other. Wavefronts can be straight lines or curves and the distance between successive wavefronts is the wavelength of the wave.
-    **Rays**: are lines that indicate the direction of a wave propagation. They are always perpendicular to wavefronts.

![](src/waves20220331223852.png)

#### Amplitude and Intensity

The intensity is defined as the power per unit area $\frac{P}{A}$ and is measured in $wm^{-2}$.  
The amplitude and intensity of the wave is corelate to the energy the wave has. The intensity of the wave is proportional to the square of it's amplitude thus $I\alpha A^2$. This is the inverse square law.  
![](src/waves20220331224715.png)

#### Polarization

> Only transverse waves can be polarized.

Polarization restricts the oscillations of a transverse wave to one plane. In the diagrams, the light is initially oscillating in all directions perpendicular to the wave direction. A piece of Polaroid only allows light transmission in one plane, filtering out oscillations in other oscillations.
![](src/waves20220331212817.png)

This is proof that the waves of the EM spectrum are transverse waves. If they were longitudinal waves the forwards and backwards motion would not be stopped by crossed pieces of Polaroid; the bottom set up would emit light.

##### Malu's Law

Malu's law states that the intensity of plane-polarized light that passes through an analyzer varies as the square of the cosine of the angle between the plane of the polarizer and the transmission axes of the analyzer defined by

$$
I = I_0 \cos^2{\theta}
$$

![](src/waves20220331213042.png)

##### Usages of Polarization

Polarization can be used to analyze optically active substances which rotates the plane of polarization such as sugar. The sweetness of the sugar is reflected by the intensity that passes through.
![](src/waves20220331213340.png)

Another use case is LCD or Liquid Crystal Displays. The liquid crystal will change is polarization when electricity is applied and thus being able to be seen through another polarizing film.
![](src/waves20220331213408.png)

#### Superposition

Superposition is the process by which two waves combine into a single wave form when they overlap. If we add these waves together the resultant depends on where the peaks of the waves are compared to each other. The principal of superposition states that when two waves meet the resultant displacement is the sum of the individual displacements.

![](src/waves20220331214000.png)

Here are three examples of what the resultant could be: a wave with an **amplitude of 1.5**, **no resultant wave at all** and a wave with an **amplitude of 2.0**  
![](src/waves20220331214101.png)

**Path Difference**: If two waves from the same source arrive at a point having taken a different path (Eg one of them reflected), they may have traveled different distances from the source. This difference in journey is called the path difference.

The path difference directly impacts how the wave superpositions itself with the other wave. If the path difference is equal to a whole number of wavelengths ($PD=λ, 2λ, 3λ, 4λ…$), the two waves will be in phase at this point and constructive interference will be observed (addition of amplitudes). If the path difference is a multiple of half a wavelength ($PD=0.5λ, 1.5λ, 2.5λ,3.5λ…$), the two waves will be in anti-phase at that point ("out of phase") and destructive interference will be observed (reduction of amplitude/cancellation).
![](src/waves20220331214637.png)

### Wave Behaviors

#### Refraction

Refraction is the change in direction of a wave when it transmits from one medium to another. An example would be a light ray refracting when entering water.

##### Refractive Index

The refractive index of a material is a measure of how easy it is for light to travel through it. The refractive index of material s can be calculated using:

$$
n = \frac{c}{c_s}
$$

Where $n$ is the refractive index, $c$ is the speed of light in a vacuum and $c_s$ is the speed of light in the material. Note that the higher the refractive index, the slower light can travel through it. The higher the refractive index, the denser is the material.

If the ray of light is incident at 90° to the material then there is no change in direction, only speed.

![](src/waves20220401200330.png)

When light passes from one material to another it is not only the speed of the light that changes, the direction often changes too.

![](src/waves20220401193743.png)

The angle of incidence, $\theta_1$, and the angle of refraction, $\theta_2$, is given by **Snell's Law**:

$$
\frac{n_1}{n_2} = \frac{\sin{\theta_1}}{\sin{\theta_2}}
$$

In this case, $n_1$ always the faster medium and $n_2$ having a larger index of refraction.  
When a wave travels from fast-to-slow: the wave bends towards normal; slow-to-fast: away from normal.

![](src/waves20220401194215.png)

A good way of thinking it is using wavefronts.

![](src/waves20220401195433.png)

In addition, the refractive indices are also related as following using the [Universal Wave Equation](#the-universal-wave-equation):

$$
\frac{\sin \theta_{1}}{\sin \theta_{2}}=\frac{n_{2}}{n_{1}}=\frac{\lambda_{1}}{\lambda_{2}}=\frac{v_{1}}{v_{2}}
$$

![](src/waves20220401194613.gif)

As shown when a wave travels through an intersection the frequency never changes but the wavelength and speed changes.

#### Reflection

Reflection happens when an incoming incident wave hits a reflecting surface.

![](src/waves20220401191739.gif)

As shown in the image above, the angle of incidence is always equal to the angle of reflection. The normal is the arbitrary perpendicular line to the reflecting surface.  
The reflection of waves if one end is tied is inverted as shown:  
![](src/waves20220401192513.gif)  
reflection of waves from a free end is not inverted:  
![](src/waves20220401192537.gif)

##### Critical Angle

When light travels from one medium to another the majority of light refracts but some of the light also reflects off of the junction and stays in the original material.

When an incident ray strikes the boundary of two mediums at an angle less than the critical angle, the light refracts into the second medium. If the ray strikes equal to the critical angle, the light is right along the junction. When the incident ray is greater than the critical angle, all the light is reflected into the original medium.  
![](src/waves20220401192909.png)

The critical angle can be found using the relationship between the refractive index of the two materials. Derived from [Snell's Law](#refraction) by substituting $\theta_2=90\degree$

$$
\sin{\theta_{c}}=\frac{1}{n_1}
$$

##### Total Internal Reflection

Total internal reflection only occurs when the light ray propagates from a optically denser medium to an optically less dense medium (always from the slower medium). An important usage is optical fibres, which is thin piece of flexible glass.
![](src/waves20220401195033.png)

#### Diffraction

Diffraction is when a wave bends as it passes through an obstacle or through an opening. The amount of diffraction depends on the wavelength compared to the gap as shown. When the wavelength is roughly equal to the slit width, maximum diffraction occurs.

![](src/waves20220401201144.png)

Waves can also ben about any obstacle, for example a wall or corner.

![](src/waves20220401202837.png)

> **Huygen's Principal**: Every wavefront is made of series of circular wavesources. The new position of the wavefront is formed by connecting the circular wavefronts from the previous wavefront.

#### Superposition & Interference

Superposition is explained previously [here](#superposition).

Interference is a special case of superposition where the waves that combine are coherent. The waves overlap and form a repeating interference pattern of maxima and minima areas. If the waves weren’t coherent the interference pattern would change rapidly and continuously.

Constructive interference occurs when two pulses displaced in the same direction cause an overlap. The resultant displacement is the sum of both displacements.

Destructive interference occurs when two pulses displaced in opposite directions cause an overlap. The resultant displacement is the difference of both displacements.

![](src/waves20220401212003.png)

## Standing Waves

When two similar waves travel in opposite directions, they can superpose to form a standing (or stationary) wave. Here is the experimental set up of how we can form a standing wave on a string. The vibration generator sends waves down the string at a certain frequency, they reach the end of the string and reflect back at the same frequency. On their way back the two waves traveling in opposite direction superpose to form a standing wave made up of nodes and antinode.

-    **Nodes**: Positions on a standing wave which do not vibrate. The waves combine to give zero displacement
-    **Anti-nodes**: Positions on a standing wave where there is a maximum displacement.

### Traveling vs Standing Waves

|            | Standing Waves                                 | Traveling Waves                                 |
| ---------- | ---------------------------------------------- | ----------------------------------------------- |
| Amplitude  | Maximum at antinode and zero at nodes          | The same for all parts of the wave              |
| Frequency  | All parts of the wave have the same frequency  | All parts of the wave have the same frequency   |
| Wavelength | Twice the distance between adjacent nodes      | The distance between two adjacent peaks         |
| Phase      | All points between two adjacent nodes in phase | Points one wavelength apart in phase            |
| Energy     | No energy translation                          | Energy translation in the direction of the wave |
| Waveform   | Does not move forward                          | Moves forwards                                  |

### Harmonics

As we increase the frequency of the vibration generator, we can see standing waves being set up. The first will occur when the generator is vibrating at the fundamental frequency, f0, of the string.
![](src/waves20220401230017.png)

-    First Harmonic
     -    $f = f_0 \lambda = 2 L$
     -    2 nodes and 1 antinode
-    Second Harmonic
     -    $f = 2f_0 \lambda = L$
     -    3 nodes and 2 antinodes
-    Third Harmonic
     -    $f = 3f_0 \lambda = \frac{2}{3} L$
     -    4 nodes and 3 antinodes
-    Fourth Harmonic
     -    $f = 4f_0 \lambda = \frac{1}{2} L$
     -    5 nodes and 4 antinodes

A string with a free end will produce an anti-node at the end point, compared to a node if the end is fixed. Similarly, standing waves in open ended pipes produce anti-nodes at the ends, whereas closed pipes produce nodes at the end points.

### Aircolumns

![](src/waves20220401230201.png)

#### Eliminating "End Effect"

The end effect refers to the small section (denoted as $\Delta x$) where the wave doesn't quite know if it's free to travel in air yet and thus result in inaccurate measurements.  
To combat this, we can move the air column in water down until we hear the first time the sound is loud, this is when the aircolumn is at it's first harmonic with wavelength $\frac{\lambda}{4}$. We can move it further down when the sound becomes loud once again at the 3rd harmonic which has a wavelength of $\frac{3\lambda}{4}$. With simple math, we can accurately calculate the wavelength. And since the end effect is present on both harmonics, when subtracting, it's eliminated.

![](src/waves20220401232957.png)
