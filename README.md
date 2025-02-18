# reg-alloc
Implementation of Chaitin's register allocation algorithm using Python and llvmlite.


## Usage
```sh
$ pip install -r requirements.txt
$ 
```

## About 
Chaitin’s algorithm is a  graph-coloring-based approach to register allocation in compilers. 

By modeling variables and their live ranges as nodes and edges in an interference graph, the algorithm assigns a minimal number of registers to variables without conflicts.

Efficient register allocation is crucial for generating optimized machine code as it reduces the number of memory accesses and improves the overall performance of programs.

This implementation serves as an educational tool for understanding the principles of register allocation.

## References
[Register Allocation and Spilling via Graph Coloring](https://dl.acm.org/doi/pdf/10.1145/989393.989403)  
[Compilers Principles, Techniques, and Tools](https://www.amazon.in/Compilers-2e-Aho/dp/9332518661/ref=sr_1_1?crid=102BX5D3670H2&dib=eyJ2IjoiMSJ9.sZDFB1B_6Fylm6ggOLMgeQ.kPJtxpRyr7W0IIaa4tEUHgAa2MJPrf35HMjO2Ald03I&dib_tag=se&keywords=compileres&qid=1735748598&sprefix=compil%2Caps%2C737&sr=8-1)  
[llvmlite](https://llvmlite.readthedocs.io/en/latest/)  


