// visuales por Rafita Correa

a.setBins(8)

osc(10, 0.2, 0)
	.add(noise(()=>a.fft[4]*50))
	//.modulateRotate(osc(10))
	.color(1, 0, 1)
	.colorama([ 0.3])
	.saturate(10)
	.mask(shape(50).scale(()=>a.fft[3]*25).rotate(1, 0.3))
	//.modulateRotate(osc(10))
	.blend(o0, [0.8])
	.modulateHue(o0, 50)
	//.modulateRotate(osc(5))
	//.kaleid(4)
	//.modulateScale(osc(()=>a.fft[3]*4))
	.out(o0)
