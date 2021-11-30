const performance = require('perf_hooks').performance;

utils = require('./utils.js')
data = require('./data.js')

const euler11 = function() {
    var t0 = performance.now()
    var mx = 0
    var d = data.euler11
    for (let i = 0; i < 20; i++) {
        for (let j = 0; j < 20; j++) {
            var s1 = []
            var s2 = []
            var s3 = []
            var s4 = []
            for (let k = 0; k < 4; k++) {
                if (j < 17) {
                    s1.push(d[i][j+k])
                } else {s1.push(0)}
                if (i < 17) {
                    s2.push(d[i+k][j])
                } else {s2.push(0)}
                if (i < 17 && j < 17) {
                    s3.push(d[i+k][j+k])
                } else {s3.push(0)}
                if (i > 3 && j < 17) {
                    s4.push(d[i-k][j+k])
                }
            }
            p1 = s1.reduce((psum,a) => psum * a, 1)
            p2 = s2.reduce((psum,a) => psum * a, 1)
            p3 = s3.reduce((psum,a) => psum * a, 1)
            p4 = s4.reduce((psum,a) => psum * a, 1)
            tmx = Math.max.apply(Math,[p1,p2,p3,p4])
            if (tmx > mx){
                mx = tmx
            }
        }
    }
    var t1 = performance.now()
    console.log('Euler #11: ' + mx + ' (' + (t1-t0) + ' ms)')
}

const euler12 = function(n) {
    const t0 = performance.now()
    var val = 1
    var cn = 1
    var facts = []
    do {
        cn ++
        val += cn
        facts = utils.get_factors(val)
    } while (facts.length < n);
    const t1 = performance.now()
    console.log('Euler #12: ' + val + ' (' + (t1-t0) + ' ms)')
}

euler11()
euler12(500)