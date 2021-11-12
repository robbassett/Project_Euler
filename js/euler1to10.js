const performance = require('perf_hooks').performance;

utils = require('./utils.js')
data = require('./data.js')

function euler1(mx){
    var t0 = performance.now()
    var nums = []
    for (let i = 1; i < mx; i++){
        if (i%3 == 0 || i%5 == 0) {nums.push(i)}
    }
    var ans = nums.reduce((a,b) => a+b, 0)
    var t1 = performance.now()
    console.log('Euler #1: ' + ans + '  (' + (t1-t0) + ' ms)')
}

function euler2(mx){
    var t0 = performance.now()
    var fnums = [1,2]
    var efnums = [2]
    do {
        fnums.push(fnums.slice(-2)[0]+fnums.slice(-1)[0])
        if (fnums.slice(-1)[0]%2 == 0) {efnums.push(fnums.slice(-1)[0])}
    } while (fnums.slice(-1)[0] < mx)
    if (fnums.slice(-1)[0]%2 == 0) {efnums.pop()}
    var ans = efnums.reduce((a,b) => a+b, 0)
    var t1 = performance.now()
    console.log('Euler #2: ' + ans + '  (' + (t1-t0) + ' ms)')
}

function euler3(val){
    var t0 = performance.now()
    mx = parseInt(Math.sqrt(val))
    primes = utils.erasthenes(mx)
    var fl = 1
    do {
        tm = primes.pop()
        if (val%tm == 0){fl = 0}
    } while (fl == 1)
    var t1 = performance.now()
    console.log('Euler #3: ' + tm + '  (' + (t1-t0) + ' ms)')
}

function euler4(n){
    var t0 = performance.now()
    var st = 10**n - 1
    var cv = 0
    var fl = 1
    do {
        for (let i = 0; i < st; i++){
            tm = String(st*(st-i))
            if (tm == tm.split("").reverse().join("")) {
                tv = st*(st-i)
                i = st
            }
        }
        if (tv > cv){cv = tv}
        st -= 1
        if (st*st < cv) {fl = 0}
    } while (fl == 1)
    var t1 = performance.now()
    console.log('Euler #4: ' + cv + '  (' + (t1-t0) + ' ms)')
}

function euler5(n){
    var t0 = performance.now()
    var st = 1
    var fl = 1
    do{
        var tm  = n*st
        for (let i = n-1; i > 0; i--){
            x = i
            if (tm%x != 0) {break; }
        }
        st += 1
        if (x == 1) {fl = 0}
    } while (fl == 1);
    ans = (st-1)*n
    var t1 = performance.now()
    console.log('Euler #5: ' + ans + '  (' + (t1-t0) + ' ms)')
}

function euler6(n){
    var t0 = performance.now()
    var s1 = 0
    var s2 = 0
    for (let i = 1; i <= n; i++){
        s1 += i*i
        s2 += i
    }
    ans = s2*s2 - s1
    var t1 = performance.now()
    console.log('Euler #6: ' + ans + '  (' + (t1-t0) + ' ms)')
}

function euler7(n){
    var t0 = performance.now()
    ans = utils.n_primes(n).pop()
    var t1 = performance.now()
    console.log('Euler #7: ' + ans + '  (' + (t1-t0) + ' ms)')
}

function euler8(n){
    var t0 = performance.now()
    var str = data.euler8
    var ans = 0
    for (i = 0; i < str.length - n; i++) {
        var tp = parseInt(str[i])
        for (j = i+1; j < i+n; j++) {tp *= str[j]}
        if (tp > ans) {ans = tp}
    }
    var t1 = performance.now()
    console.log('Euler #8: ' + ans + ' (' + (t1-t0) + ' ms)')
}

euler1(1000)
euler2(4000000)
euler3(600851475143)
euler4(3)
euler5(20)
euler6(100)
euler7(10001)
euler8(13)