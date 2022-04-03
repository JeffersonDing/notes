# Vectors

A vector is a mathematical way to describe a "journey" with two components: a **magnitude** and a **direction**. As opposed to a scaler value which only has a magnitude.

A vector can be represented using directed line segments where the length shows the magnitude and the arrow indicates the direction.

Two vectors are the same only when they have the same magnitude **and** direction. A negative of a vector is a vector parallel, same length but opposite in direction denoted as $-\vec{a}$  
![](src/vectors20220403132746.png)

#### Vector Addition

Vector addition is _Head-to-Tail_ where one vector is place at the end of another. The resultant vector starts from the start of the first vector and ends at the end of the second vector.

#### Vector Subtraction

Vector subtraction can be considered _Tail-to-Tail_ but you can also find the negated value of the second vector and do [vector addition](#vector-addition).

#### Scalar Multiplication

Scalar multiplication is multiplying a scalar value to a vector. It multiplies the magnitude of the vector of the scalar amount and changes the direction if the scalar is negative.

![](src/vectors20220403133031.png)

### Representing Vectors in a Plane

#### Notation

**Unit vector**: A normalized vector of magnitude 1  
**Position Vector**: The position vector of point P is a vector originating from the origin and ending at point P(x,y).  
**Displacement Vector**: The displacement vector of B relative to A $\vec{AB}$ is a vector that originates from A and terminates at B.  
![](src/vectors20220403132514.png)

Vectors are often denoted using a lower case letter with a hat like such $\vec{a}$ or the two points the vector originates and ends at like $\vec{AB}$

Vectors on a plane can also be represented as the two components like such:

$$
\begin{bmatrix}
x \\
y \\
\end{bmatrix} = xi+yj
$$

Where $i$ is the x unit vector $\begin{bmatrix} 1 \\ 0 \\  \end{bmatrix}$ and $j$ is the y unit vector $\begin{bmatrix} 0 \\ 1 \\  \end{bmatrix}$.

Generally we can represent a vector as $\begin{bmatrix} x \\ y \\  \end{bmatrix}$ where $x$ is the horizontal component and $y$ is the vertical component of the vector.

The magnitude or length of that vector is written as $|\vec{AB}|$ or $|\vec{a}|$. It's found using formula:

$$
\sqrt{{a_1}^2+{a_2}^2+...+{a_n}^2}
$$

where $a_n$ is each component of the vector.

#### Operations

If $a=\left(\begin{array}{l}a_{1} \\ a_{2}\end{array}\right)$ and $\mathbf{b}=\left(\begin{array}{l}b_{1} \\ b_{2}\end{array}\right)$ then $\mathbf{a}+\mathbf{b}=\left(\begin{array}{l}a_{1}+b_{1} \\ a_{2}+b_{2}\end{array}\right)$

If $\mathbf{a}=\left(\begin{array}{l}a_{1} \\ a_{2}\end{array}\right)$ and $\mathbf{b}=\left(\begin{array}{l}b_{1} \\ b_{2}\end{array}\right)$, then $\mathbf{a}-\mathbf{b}=\left(\begin{array}{l}a_{1}-b_{1} \\ a_{2}-b_{2}\end{array}\right)$

If $k$ is any scalar and $\mathbf{v}=\left(\begin{array}{l}v_{1} \\ v_{2}\end{array}\right)$, then $k \mathbf{v}=\left(\begin{array}{l}k v_{1} \\ k v_{2}\end{array}\right)$

## Scalar Product & Angle Between Two Vectors

The scalar product of two vectors is also knows as the dot product or inner product. It's found by multiplying each of a vectors compoments and summing them up like such:

$$
\left(\begin{array}{l}
a_{1} \\
a_{2} \\
a_{3}
\end{array}\right) \cdot\left(\begin{array}{l}
b_{1} \\
b_{2} \\
b_{3}
\end{array}\right)=a_{1} b_{1}+a_{2} b_{2}+a_{3} b_{3}
$$

The angle between two vectors $\theta$ is the angle between two vectors, we can find the angle using the cosine rule:
![](src/vectors20220403134618.png)

$$
|b-a|^2 = |a|^2 + |b|^2 + 2 |a||b|\cos{\theta} \\
\cos{\theta} = \frac{a\cdot b}{|a||b|}
$$

> Note: Vectors must be converging or diverging from the same point to have an angle between them

### Implications

The implications of the dot product indicates how close the two vectors are. In this case:

$$
\begin{aligned}
\vec{a}\cdot \vec{b}=0,\ \cos \theta =0,\ \theta =90^{\circ }\\
\vec{a}\cdot \vec{b}=\left| a\right| \left| b\right| ,\ \cos \theta =1,\ \theta =0\\
\vec{a}\cdot \vec{b} >0, \cos \theta  >0\\
\vec{a}\cdot \vec{b} <0, cos\theta  <0,
\end{aligned}
$$

As shown, if the dot product of the two vectors equal to 0, they are perpendicular to each other. If the dot product is equal to the two magnitudes of the vectors, they are parallel. If the product is greater than 0, the angle os acute and if they are less than 0, they angle between them is obtuse.

## Vector Product

## Vector Lines in 2D and 3D

## Intersection of 2 Vector Lines

## Equation of a Plane

## Intersection of a Line & Plane
