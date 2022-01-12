.global scheme_entry
scheme_entry:
    movq $8, %rax
    movq $3, %rcx
    subq %rcx, %rax
    ret
