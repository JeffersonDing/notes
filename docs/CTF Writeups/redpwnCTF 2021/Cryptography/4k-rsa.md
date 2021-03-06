# 4k RSA

This is a classic RSA question where we were given `n` `e` and `c`. In this case to decipher `c` we need to find `d` which is the modular inverse of the totient and `e`.

## Finding the Totient

To find the `Eulers Totient` we need to find the factors of n. Then we could put it in this equation since we know that all of n's factors are prime

```
phi = (p0-1)(p1-1)...(pn-1)
```

To factor a large number like n we could of course use the `Python Crypto` module but we can search for the number on [factordb](http://www.factordb.com).

### Prime Factorization

We input `n` into factordb and indeed it is already FF(fully factored)

```python
primes=[9353689450544968301,9431486459129385713,9563871376496945939,9734621099746950389,9736426554597289187,10035211751896066517,10040518276351167659,10181432127731860643,10207091564737615283,10435329529687076341,10498390163702844413,10795203922067072869,11172074163972443279,11177660664692929397,11485099149552071347,11616532426455948319,11964233629849590781,11992188644420662609,12084363952563914161,12264277362666379411,12284357139600907033,12726850839407946047,13115347801685269351,13330028326583914849,13447718068162387333,13554661643603143669,13558122110214876367,13579057804448354623,13716062103239551021,13789440402687036193,13856162412093479449,13857614679626144761,14296909550165083981,14302754311314161101,14636284106789671351,14764546515788021591,14893589315557698913,15067220807972526163,15241351646164982941,15407706505172751449,15524931816063806341,15525253577632484267,15549005882626828981,15687871802768704433,15720375559558820789,15734713257994215871,15742065469952258753,15861836139507191959,16136191597900016651,16154675571631982029,16175693991682950929,16418126406213832189,16568399117655835211,16618761350345493811,16663643217910267123,16750888032920189263,16796967566363355967,16842398522466619901,17472599467110501143,17616950931512191043,17825248785173311981,18268960885156297373,18311624754015021467,18415126952549973977]
```

This is the prime factorization of `n`

## Script

To find the totient phi, and find the final plaintext, I wrote a small python script to automate the process. I skiped the RSA values as they take up to much space. They could be sound in the provided txt file.

```python
from Crypto.Util.number import inverse
n= #n from provided txt file
e=65537
c= #c from provided txt file
primes= #the primes listed above. Don't want to showcase twice as there is quite a lot of them.
phi=1
for x in primes:
    phi=phi*(x-1)
d = inverse(e,phi)
m=pow(c,d,n)
print(hex(m))
```

Essentially, we set phi to one and multiply it to the next prime factor of `n` minus one. Then we get `d` by doing the moduler inverse of the public exponent and phi. To solve the plaintext, we just need to raise `c` to the power of `d` mod `n`.
