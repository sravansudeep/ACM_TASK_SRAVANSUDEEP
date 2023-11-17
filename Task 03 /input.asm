//computes RAM[1]=1+...RAM[0]
	@i
	M=1 //  i =1
	@sum
	M=0   //sum = 0

(LOOP)
	@i    // if i>RAM[0] goto STOP
	D=M
	@R0
	D=D-M
	@STOP
	D;JGT   //sum += i
	@i
	D=M
	@sum
	M=D+M  //  i++
	@i
	M=M+1
	@loop  //  goto LOOP
	0;JMP
