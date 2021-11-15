function erasthenes(n){
    var sieve = Array.from({length:Math.floor(n/2)},i => i = 1)
    for (let i = 3; i < parseInt(Math.sqrt(n))+1; i += 2) {
        if (sieve[Math.floor(i/2)] == 1) {
            for (let j = Math.floor(i*i/2); j < sieve.length; j += i) {
                sieve[j] = 0
            }
        }
    }
    var out = [2]
    for (let i = 1; i < sieve.length; i++){
        if (sieve[i] == 1){
            out.push(2*i+1)
        }
    }
    return out
}

function n_primes(n){
    var p = [2]
    var c = 2
    do {
        var j = 0
        c += 1
        do {
            if (c % p[j] == 0) {break;}
            if (j == p.length- 1) {p.push(c);}
            j += 1
        } while (j < p.length);
    } while (p.length < n);
    return p
}

module.exports = {erasthenes, n_primes}