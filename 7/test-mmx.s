	.file	"test-mmx.c"
	.section	.rodata
.LC0:
	.string	" %3d"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$80, %rsp
	movl	%edi, -68(%rbp)
	movq	%rsi, -80(%rbp)
	movw	$1, -48(%rbp)
	movw	$2, -46(%rbp)
	movw	$3, -44(%rbp)
	movw	$4, -42(%rbp)
	movw	$-4, -32(%rbp)
	movw	$-3, -30(%rbp)
	movw	$-2, -28(%rbp)
	movw	$-1, -26(%rbp)
#APP
# 16 "test-mmx.c" 1
	movq -48(%rbp),%mm0
# 0 "" 2
# 17 "test-mmx.c" 1
	movq -32(%rbp),%mm1
# 0 "" 2
# 18 "test-mmx.c" 1
	pmaddwd %mm1,%mm0
# 0 "" 2
# 19 "test-mmx.c" 1
	movq %mm0,-16(%rbp)
# 0 "" 2
# 20 "test-mmx.c" 1
	emms
# 0 "" 2
#NO_APP
	movl	$0, -52(%rbp)
	jmp	.L2
.L3:
	movl	-52(%rbp), %eax
	cltq
	movzwl	-48(%rbp,%rax,2), %eax
	cwtl
	movl	%eax, %esi
	movl	$.LC0, %edi
	movl	$0, %eax
	call	printf
	addl	$1, -52(%rbp)
.L2:
	cmpl	$3, -52(%rbp)
	jle	.L3
	movl	$10, %edi
	call	putchar
	movl	$0, -52(%rbp)
	jmp	.L4
.L5:
	movl	-52(%rbp), %eax
	cltq
	movzwl	-32(%rbp,%rax,2), %eax
	cwtl
	movl	%eax, %esi
	movl	$.LC0, %edi
	movl	$0, %eax
	call	printf
	addl	$1, -52(%rbp)
.L4:
	cmpl	$3, -52(%rbp)
	jle	.L5
	movl	$10, %edi
	call	putchar
	movl	$0, -52(%rbp)
	jmp	.L6
.L7:
	movl	-52(%rbp), %eax
	cltq
	movl	-16(%rbp,%rax,4), %eax
	movl	%eax, %esi
	movl	$.LC0, %edi
	movl	$0, %eax
	call	printf
	addl	$1, -52(%rbp)
.L6:
	cmpl	$1, -52(%rbp)
	jle	.L7
	movl	$10, %edi
	call	putchar
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.8.2-19ubuntu1) 4.8.2"
	.section	.note.GNU-stack,"",@progbits
